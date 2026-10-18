import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3
import requests
import csv
from pathlib import Path
from datetime import datetime
from PIL import Image

from Product_Pricing import create_database, save_product, get_product
from Cost_Calculation import number, calculate_cost
from Live_Silver_Price_API import live_silver_price, get_exchange_rate
from AI_image_analysis import analyse_image
from semi.semi_auto_labor_rules import get_labor_costs
from File_Handling import save_csv, load_csv, save_pdf

DATABASE = Path(__file__).with_name("jewellery_products.db")



def read_quote():
    product_ID = fields["product_id"].get().strip()
    category = fields["category"].get().strip()
    product_size = fields["size"].get().strip()

    input_choice = fields["mode"].get().lower().strip()
    craft_type = fields["craft_type"].get().lower().strip()
    plating_color = fields["plating_color"].get().lower().strip()
    e_coating = fields["e_coating"].get().lower().strip()

    product_image = fields["image_link"].get().strip()
    ai_notes = fields["ai_notes"].get().strip()

    if product_ID == "":
        raise ValueError("Enter a Product ID.")

    if len(product_ID) > 30:
        raise ValueError("Product ID must be 30 characters or fewer.")

    for character in product_ID:
        if not character.isalnum() and character not in "-_":
            raise ValueError("Product ID can use letters, numbers, - and _ only.")

    if category == "" or product_size == "":
        raise ValueError("Enter a category and size.")

    if craft_type not in ["handmade", "casted"]:
        raise ValueError("Choose handmade or casted.")

    if plating_color not in ["s", "rh", "g", "rg"]:
        raise ValueError("Choose s, rh, g or rg.")

    if e_coating not in ["yes", "no"]:
        raise ValueError("Choose yes or no for E-coating.")

    silver_weight_g = number(fields["silver_weight_g"].get(), "Silver weight")
    silver_price_oz = number(fields["silver_price_oz"].get(), "Silver price")
    exchange_rate = number(fields["exchange_rate"].get(), "Exchange rate")
    wastage_percent = number(fields["wastage_percent"].get(), "Wastage")
    stone_cost = number(fields["stone_cost"].get(), "Stone cost")
    Qty = number(fields["quantity"].get(), "Quantity")
    Tax = number(fields["Tax"].get(), "Tax")
    shipping_fees = number(fields["shipping_fees"].get(), "Shipping fees")

    if silver_weight_g <= 0:
        raise ValueError("Silver weight must be greater than 0.")

    elif silver_price_oz <= 0:
        raise ValueError("Silver price must be greater than 0.")

    elif exchange_rate <= 0:
        raise ValueError("Exchange rate must be greater than 0.")

    elif Qty <= 0 or Qty != int(Qty):
        raise ValueError("Quantity must be a positive whole number.")

    elif wastage_percent > 100 or Tax > 100:
        raise ValueError("Wastage and tax must be between 0 and 100.")

    Qty = int(Qty)

    if input_choice == "manual":
        making_labor = number(fields["making_labor"].get(), "Making labour")
        sanding_labor = number(fields["sanding_labor"].get(), "Sanding labour")
        polishing_labor = number(fields["polishing_labor"].get(), "Polishing labour")
        plating_labor = number(fields["plating_labor"].get(), "Plating labour")
        e_coating_labor = number(fields["e_coating_labor"].get(), "E-coating labour")
        mark_up = number(fields["mark_up"].get(), "Markup")

    elif input_choice == "semi" or input_choice == "auto":
        if input_choice == "auto" and ai_notes == "":
            raise ValueError("Click Auto fill first or choose Semi.")

        labor = get_labor_costs(silver_weight_g, craft_type, plating_color, e_coating)

        making_labor = labor[0]
        sanding_labor = labor[1]
        polishing_labor = labor[2]
        plating_labor = labor[3]
        e_coating_labor = labor[4]
        mark_up = labor[5]

        fields["making_labor"].set(making_labor)
        fields["sanding_labor"].set(sanding_labor)
        fields["polishing_labor"].set(polishing_labor)
        fields["plating_labor"].set(plating_labor)
        fields["e_coating_labor"].set(e_coating_labor)
        fields["mark_up"].set(mark_up)

    else:
        raise ValueError("Choose manual, semi or auto.")

    T_Labor_Cost = (
        making_labor + sanding_labor + polishing_labor
        + plating_labor + e_coating_labor
    )

    result = calculate_cost(
        silver_weight_g, silver_price_oz, wastage_percent,
        T_Labor_Cost, stone_cost, Qty, mark_up,
        exchange_rate, Tax, shipping_fees
    )


    data = {
        "product_id": product_ID,
        "category": category,
        "size": product_size,
        "mode": input_choice,
        "craft_type": craft_type,
        "plating_color": plating_color,
        "e_coating": e_coating,
        "image_link": product_image,
        "ai_notes": ai_notes,
        "silver_weight_g": silver_weight_g,
        "silver_price_oz": silver_price_oz,
        "exchange_rate": exchange_rate,
        "wastage_percent": wastage_percent,
        "making_labor": making_labor,
        "sanding_labor": sanding_labor,
        "polishing_labor": polishing_labor,
        "plating_labor": plating_labor,
        "e_coating_labor": e_coating_labor,
        "stone_cost": stone_cost,
        "quantity": Qty,
        "mark_up": mark_up,
        "Tax": Tax,
        "shipping_fees": shipping_fees
    }

    data.update(result)
    data["date_calculated"] = datetime.now().isoformat(timespec="seconds")

    return data



def quotation_text(data):
    text = "Product ID: " + data["product_id"] + "\n"
    text += "Quantity: " + str(data["quantity"]) + "\n"
    text += "All prices in THB\n\n"
    text += "Silver cost per piece: " + str(data["Silver_Cost"]) + "\n"
    text += "Wastage per piece: " + str(data["Wastage_Cost"]) + "\n"
    text += "Labour per piece: " + str(data["T_Labor_Cost"]) + "\n"
    text += "Stones per piece: " + str(data["stone_cost"]) + "\n"
    text += "Cost per piece: " + str(data["T_Cost"]) + "\n"
    text += "Wholesale per piece: " + str(data["Wholesale_price"]) + "\n"
    text += "Order subtotal: " + str(data["Raw_Quotation"]) + "\n"
    text += "Tax: " + str(data["Tax_Cost"]) + "\n"
    text += "Shipping: " + str(data["shipping_fees"]) + "\n"
    text += "Final quotation: " + str(data["Final_Quotation"])
    return text


def show_quote(data):
    output.delete("1.0", tk.END)
    output.insert(tk.END, quotation_text(data))


def calculate():
    try:
        data = read_quote()
        show_quote(data)
        status.set("Calculated. Click Save product to store it.")

    except ValueError as error:
        messagebox.showerror("Check your inputs", str(error))



def save_estimate():
    try:
        data = read_quote()
        save_product(connection, data)
        show_quote(data)
        status.set("Product " + data["product_id"] + " saved.")

    except (ValueError, sqlite3.Error) as error:
        messagebox.showerror("Could not save", str(error))


def fill_form(data):
    for name in fields:
        if name in data:
            fields[name].set(data[name])

    output.delete("1.0", tk.END)


def load_product():
    try:
        product_ID = fields["product_id"].get().strip()
        data = get_product(connection, product_ID)
        fill_form(data)
        show_quote(data)
        status.set("Product loaded. Calculate again after editing.")

    except (ValueError, sqlite3.Error) as error:
        messagebox.showerror("Could not load", str(error))



def export_csv():
    try:
        data = read_quote()
        filename = filedialog.asksaveasfilename(defaultextension=".csv")

        if filename:
            save_csv(filename, data)
            show_quote(data)
            status.set("CSV exported.")

    except (ValueError, OSError, csv.Error) as error:
        messagebox.showerror("Could not export CSV", str(error))


def import_csv():
    filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    if not filename:
        return

    try:
        data = load_csv(filename, fields)
        fill_form(data)
        status.set("CSV loaded. Check inputs, Calculate, then Save product.")

    except (ValueError, OSError, csv.Error) as error:
        messagebox.showerror("Could not import CSV", str(error))


def export_pdf():
    try:
        data = read_quote()
        filename = filedialog.asksaveasfilename(defaultextension=".pdf")

        if filename:
            save_pdf(filename, quotation_text(data))
            show_quote(data)
            status.set("PDF exported.")

    except (ValueError, OSError) as error:
        messagebox.showerror("Could not export PDF", str(error))



def fetch_prices():
    price = live_silver_price(goldapi_key.get())
    rate, rate_date = get_exchange_rate()

    fields["silver_price_oz"].set(price)
    fields["exchange_rate"].set(rate)

    return rate_date


def get_prices():
    status.set("Getting prices. Please wait...")
    window.update_idletasks()

    try:
        rate_date = fetch_prices()
        status.set("Prices filled. Exchange-rate date: " + rate_date)

    except (requests.RequestException, ValueError, KeyError, TypeError) as error:
        status.set("Request failed. You can enter prices manually.")
        messagebox.showerror("Price error", str(error))



def choose_photo():
    filename = filedialog.askopenfilename(filetypes=[("Photos", "*.jpg *.jpeg *.png")])

    if filename:
        fields["image_link"].set(filename)
        fields["ai_notes"].set("")
        status.set("Photo selected. Auto fill sends this photo to Claude.")


def automatic_input():
    if fields["image_link"].get().strip() == "":
        choose_photo()

    if fields["image_link"].get().strip() == "":
        return

    status.set("Getting prices and sending the photo to Claude...")
    window.update_idletasks()

    try:
        rate_date = fetch_prices()
        result = analyse_image(fields["image_link"].get().strip(), claude_key.get())

        fields["category"].set(result["category"])
        fields["ai_notes"].set(result["notes"])
        fields["mode"].set("auto")

        status.set("Auto fill complete. Check details. FX date: " + rate_date)

        messagebox.showinfo(
            "Check AI suggestions",
            result["notes"] + "\n\nCheck the category. Enter measured weight "
            "and manufacturing details, then click Calculate."
        )

    except (requests.RequestException, ValueError, KeyError, TypeError,
            OSError, Image.DecompressionBombError) as error:
        status.set("Auto fill failed. You can use Manual or Semi.")
        messagebox.showerror("Auto fill error", str(error))



def add_field(parent, row, name, label, value="", choices=None):
    tk.Label(parent, text=label).grid(row=row, column=0, sticky="w", padx=5, pady=2)

    fields[name] = tk.StringVar(value=str(value))

    if choices is None:
        box = tk.Entry(parent, textvariable=fields[name], width=24)

    else:
        box = tk.OptionMenu(parent, fields[name], *choices)

    box.grid(row=row, column=1, sticky="ew", padx=5)



window = tk.Tk()
window.title("Jewellery Pricing")

fields = {}
status = tk.StringVar(value="Example values only. Enter your product details.")
goldapi_key = tk.StringVar()
claude_key = tk.StringVar()

left = tk.LabelFrame(window, text="Product and prices")
left.grid(row=0, column=0, padx=10, pady=5, sticky="n")

right = tk.LabelFrame(window, text="Costs - THB per piece")
right.grid(row=0, column=1, padx=10, pady=5, sticky="n")

add_field(left, 0, "mode", "Input mode", "semi", ["manual", "semi", "auto"])
add_field(left, 1, "product_id", "Product ID", "R001")
add_field(left, 2, "category", "Category", "ring")
add_field(left, 3, "size", "Product size", "S")
add_field(left, 4, "silver_weight_g", "Billable silver weight (g)", 4)
add_field(left, 5, "craft_type", "Craft type", "casted", ["handmade", "casted"])
add_field(left, 6, "plating_color", "Plating", "s", ["s", "rh", "g", "rg"])
add_field(left, 7, "e_coating", "E-coating", "no", ["yes", "no"])
add_field(left, 8, "silver_price_oz", "Silver price (USD/troy oz)", 30)
add_field(left, 9, "exchange_rate", "THB for 1 USD", 35)
add_field(left, 10, "quantity", "Quantity", 10)
add_field(left, 11, "image_link", "Photo path")
add_field(left, 12, "ai_notes", "AI notes")

add_field(right, 0, "wastage_percent", "Wastage %", 5)
add_field(right, 1, "making_labor", "Making labour", 10)
add_field(right, 2, "sanding_labor", "Sanding labour", 5)
add_field(right, 3, "polishing_labor", "Polishing labour", 5)
add_field(right, 4, "plating_labor", "Plating labour", 12)
add_field(right, 5, "e_coating_labor", "E-coating labour", 0)
add_field(right, 6, "stone_cost", "Total stone cost per piece", 10)
add_field(right, 7, "mark_up", "Markup %", 16)
add_field(right, 8, "Tax", "Tax %", 7)
add_field(right, 9, "shipping_fees", "Shipping for whole order", 100)

tk.Label(right, text="GoldAPI key").grid(row=10, column=0, sticky="w")
tk.Entry(right, textvariable=goldapi_key, show="*", width=24).grid(row=10, column=1)

tk.Label(right, text="Claude API key").grid(row=11, column=0, sticky="w")
tk.Entry(right, textvariable=claude_key, show="*", width=24).grid(row=11, column=1)

buttons = tk.Frame(window)
buttons.grid(row=1, column=0, columnspan=2)

tk.Button(buttons, text="Choose photo", command=choose_photo).grid(row=0, column=0)
tk.Button(buttons, text="Get prices", command=get_prices).grid(row=0, column=1)
tk.Button(buttons, text="Auto fill", command=automatic_input).grid(row=0, column=2)
tk.Button(buttons, text="Calculate", command=calculate).grid(row=0, column=3)
tk.Button(buttons, text="Save product", command=save_estimate).grid(row=0, column=4)

tk.Button(buttons, text="Load product", command=load_product).grid(row=1, column=0)
tk.Button(buttons, text="Import CSV", command=import_csv).grid(row=1, column=1)
tk.Button(buttons, text="Export CSV", command=export_csv).grid(row=1, column=2)
tk.Button(buttons, text="Export PDF", command=export_pdf).grid(row=1, column=3)

tk.Label(window, textvariable=status, wraplength=750).grid(row=2, column=0, columnspan=2)

output = tk.Text(window, width=90, height=15)
output.grid(row=3, column=0, columnspan=2, padx=10, pady=5)



connection = sqlite3.connect(DATABASE)
create_database(connection)

if __name__ == "__main__":
    try:
        window.mainloop()
    finally:
        connection.close()
