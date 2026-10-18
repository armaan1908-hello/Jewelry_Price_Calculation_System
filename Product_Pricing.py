import json

def create_database(connection):
    connection.execute("""
        CREATE TABLE IF NOT EXISTS Products 
        (product_id INTEGER PRIMARY KEY,
        category TEXT NOT NULL,
        size TEXT NOT NULL,
        image_link TEXT,
            
        cost_per_piece REAL NOT NULL,
        wholesale_price REAL NOT NULL,
        quantity INTEGER NOT NULL,
        final_quotation REAL NOT NULL,
        
        saved_inputs TEXT NOT NULL,
        date_calculated TEXT NOT NULL)
    """)
    connection.commit()


def save_product(connection, data):
    data = data.copy()
    data["saved_inputs"] = json.dumps(data)

    with connection:
        product = connection.execute(
            "SELECT product_id FROM Products WHERE product_id = ?",
            (data["product_id"],)
        ).fetchone()

        if product is None:
            connection.execute("""
            INSERT INTO Products (
            product_id, category, size, image_link,
            cost_per_piece, wholesale_price, quantity,
            final_quotation, saved_inputs, date_calculated)
            VALUES (
            :product_id, :category, :size, :image_link,
            :T_Cost, :Wholesale_price, :quantity,
            :Final_Quotation, :saved_inputs, :date_calculated)
            """, data)

        else:
            connection.execute("""
            UPDATE Products SET
            category = :category,
            size = :size,
            image_link = :image_link,
            cost_per_piece = :T_Cost,
            wholesale_price = :Wholesale_price,
            quantity = :quantity,
            final_quotation = :Final_Quotation,
            saved_inputs = :saved_inputs,
            date_calculated = :date_calculated
            WHERE product_id = :product_id
            """, data)


def get_product(connection, product_ID):
    product = connection.execute(
        "SELECT saved_inputs FROM Products WHERE product_id = ?",
        (product_ID,)).fetchone()

    if product is None:
        raise ValueError("Product not found.")

    return json.loads(product[0])
