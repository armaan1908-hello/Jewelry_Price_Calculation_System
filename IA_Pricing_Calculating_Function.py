def calculate_cost(silver_weight_g, silver_price_oz, wastage_percent, labor_cost, stone_cost, quantity, wholesale_markup):
    silver_price_g = silver_price_oz/30
    raw_silver_price_g = silver_price_g * silver_weight_g
    
    if silver_weight <= 0:
        raise ValueError("Silver weight must be greater than 0.")
    elif silver_price_oz <= 0:
        raise ValueError('Silver price must be realistic "greater than 0".')
    elif quantity <= 0:
        raise ValueError("Item quantity must be greater than 0.")
    
    silver_price_g = silver_price_oz/30
    raw_silver_price_g = silver_price_g * silver_weight_g

    if silver_weight_g <= 5:
      casting_labor_cost = ...
      casting_wasted_percentage =
      handmade_labor_cost =
      handmade_wastage_percentage = 
      finishing_touch_cost = 
      polishing_cost =
    elif silver_weight_g > 5 and silver_weight_g <= 10:
      casting_labor_cost = ...
      casting_wasted_percentage =
      handmade_labor_cost =
      handmade_wastage_percentage = 
      finishing_touch_cost = 
      polishing_cost =
    elif silver_weight_g > 10:
      casting_labor_cost = ...
      casting_wasted_percentage =
      handmade_labor_cost =
      handmade_wastage_percentage = 
      finishing_touch_cost = 
      polishing_cost =
    
    
    
  
    # flash_silver_plate_cost =
    # flash_G/RG_plate_cost =
    # 1m_G/RG_plate_cost =
    # E-coating_cost = 

    #markup(could be differ depending on both quantity and silver_weight of Item) = 