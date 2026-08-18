def calculate_cost(silver_weight_g, silver_price_oz, wastage_percent, labor_cost, stone_cost, quantity, wholesale_markup):
    silver_price_g = silver_price_oz/30
    raw_silver_price_g = silver_price_g * silver_weight_g
    
    if silver_weight <= 0:
        raise ValueError("Silver weight must be greater than 0.")
    elif silver_price_oz <= 0:
        raise ValueError('Silver price must be realistic "greater than 0".')
    elif quantity <= 0:
        raise ValueError("Item quantity must be greater than 0.")
    
 
 # Data (values) for semi and auto:   

    if silver_weight_g <= 4:
        S_handmade_labor = 12
        S_making_labor = 10
        S_sanding_labor = 5
        S_polishing_labor = 5
        s_S_plating_labor = 12
        rh_S_plating_labor = 22 
        g_S_plating_labor = 25
        rs_S_plating_labor = 25
        S_e_coating_labor = 2
        S_mark_up = 16
    
    elif silver_weight_g > 4 and silver_weight_g <= 8:
        M_handmade_labor = 15
        M_making_labor = 12
        M_sanding_labor = 8
        M_polishing_labor = 8
        s_M_plating_labor = 15
        rh_M_plating_labor = 32
        g_M_plating_labor = 35
        rs_M_plating_labor = 35
        M_e_coating_labor = 3
        M_mark_up =14
      
    elif silver_weight_g > 8:
        L_handmade_labor = 20
        L_making_labor = 15
        L_sanding_labor = 10
        L_polishing_labor = 10
        s_L_plating_labor = 18
        rh_L_plating_labor = 45
        g_L_plating_labor = 50
        rs_L_plating_labor = 48
        L_e_coating_labor = 4
        L_mark_up = 12
    
    
  
    # flash_silver_plate_cost =
    # flash_G/RG_plate_cost =
    # 1m_G/RG_plate_cost =
    # E-coating_cost = 

    #markup(could be differ depending on both quantity and silver_weight of Item) = 
