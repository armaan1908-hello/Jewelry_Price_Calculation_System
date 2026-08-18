input_choice = input('Select Input Type ("Manual", "Auto"matic OR "Semi"-Automatic): ') 
input_choice = input_choice.lower().strip()
print(input_choice)
if input_choice == "manual":
    product_ID = input("Enter Product ID: "))
    product_ID = product_ID.strip()
    product_image = 
    craft_type = input('Select "Hand Made" OR "Casted": ')
    craft_type = craft_type.lower().strip()
    silver_weight_g = float(input("Enter Silver Weight (grams): "))
    product_size = input('Enter Product Size (Small-"S", Medium-"M", Large-"L"): ')
    product_size = product_size.lower().strip()
    plating_color = input('Enter plating (Silver-"S", Rhodium-"RH", Gold-"G", RoseGold-"RG": ') 
    plating_color = plating_color.lower().strip()
    mark_up = input(int('Enter the mark-up percentage(%) eg."15": '))
    mark_up = (mark_up)/100
    if craft_type == "handmade":
        making_labor = float(input("Enter hand-made labor: "))
    elif craft_type == "casted":
        making_labor = float(input("Enter casting labor: "))
        sanding_labor = float(input("Enter sanding labor: "))
        polishing_labor = float(input("Enter polishing labor: "))
    if plating_color == "s":
        plating_labor = 
    elif plating_color == "rh":
        plating_labor =
    elif plating_color == "g":
        plating_labor =
    elif plating_color == "rs":
        plating_labor =
    e_coating = input('E-Coating, "YES or "NO" ?: ')
    e_coating = e_coating.lower().strip()
    if e_coating == "yes":
        e_coating_labor = float(input("Enter coating labor: "))
    elif e_coating == "yes":
        e_coating_labor = 0
    

 elif input_choice == "semi" 
    product_ID = input("Enter Product ID: "))
    product_ID = product_ID.strip()
    product_image = 
    craft_type = input('Select "Hand Made" OR "Casted": ')
    craft_type = craft_type.lower().strip()
    silver_weight_g = float(input("Enter Silver Weight (grams): "))
    product_size = input('Enter Product Size (Small-"S", Medium-"M", Large-"L"): ')
    product_size = product_size.lower().strip()
    plating_color = input('Enter plating (Silver-"S", Rhodium-"RH", Gold-"G", RoseGold-"RG": ') 
    plating_color = plating_color.lower().strip()
    e_coating = input('E-Coating, "YES or "NO" ?: ')
    e_coating = e_coating.lower().strip()
    if craft_type == "handmade" and product_size == "s":
        making_labor = S_handmade_labor
    elif craft_type == "handmade" and product_size == "m":
        making_labor = M_handmade_labor
    elif craft_type == "handmade" and product_size == "l":
        making_labor = L_handmade_labor
    elif craft_type == "casted" and product_size == "s":
        making_labor = S_making_labor
        sanding_labor = S_sanding_labor
        polishing_labor = S_polishing_labor
    elif craft_type == "casted" and product_size == "m":
        making_labor = M_making_labor
        sanding_labor = M_sanding_labor
        polishing_labor = M_polishing_labor
    elif craft_type == "casted" and product_size == "m":
        making_labor = M_making_labor
        sanding_labor = M_sanding_labor
        polishing_labor = M_polishing_labor
    elif craft_type == "casted" and product_size == "l":
        making_labor = L_making_labor
        sanding_labor = L_sanding_labor
        polishing_labor = L_polishing_labor
    if plating_color == "s" and product_size == "s":
        plating_labor = s_S_plating_labor
    elif plating_color == "s" and product_size == "m":
        plating_labor = s_M_plating_labor
    elif plating_color == "s" and product_size == "l":
        plating_labor = s_L_plating_labor
    elif plating_color == "rh" and product_size == "s":
        plating_labor = rh_S_plating_labor
    elif plating_color == "rh" and product_size == "m":
        plating_labor = rh_M_plating_labor
    elif plating_color == "rh" and product_size == "l":
        plating_labor = rh_L_plating_labor
    elif plating_color == "g" and product_size == "s":
        plating_labor = g_S_plating_labor
    elif plating_color == "g" and product_size == "m":
        plating_labor = g_M_plating_labor
    elif plating_color == "g" and product_size == "L":
        plating_labor = g_L_plating_labor
    elif plating_color == "rs" and product_size == "s":
        plating_labor = rs_S_plating_labor
    elif plating_color == "rs" and product_size == "m":
        plating_labor = rs_M_plating_labor
    elif plating_color == "rs" and product_size == "l":
        plating_labor = rs_L_plating_labor
    if e_coating = "yes" and product_size == "s":
        e_coating_labor = S_e_coating_labor
    elif e_coating = "yes" and product_size == "m":
        e_coating_labor = M_e_coating_labor
    elif e_coating = "yes" and product_size == "l":
        e_coating_labor = L_e_coating_labor
    elif e_coating = "no"
        e_coating_labor = 0
    if product_size == "s":
        mark_up = S_mark_up
    elif product_size == "m":
        mark_up = M_mark_up
    elif product_size == "l":
        mark_up = L_mark_up
    
elif input_choice == "auto"
    product_ID = input("Enter Product ID: "))
    product_ID = product_ID.strip()
    product_image = 
    
    (AUTOFILL)


Silver_Cost = (silver_weight_g)*(silver_price_g)
T_Labor_Cost = (making_labor+sanding_labor+polishing_labor+plating_labor+e_coating_labor)
T_Cost = Silver_Cost+T_Labor_Cost

Wholesale_price = (T_Cost)*(1+mark_up)
Raw_Quotation = (Wholesale_price)*(Qty)
Final_Quotation = ((Raw_Quotation)*(1+(Tax/100)))+(shipping_fees)

X
