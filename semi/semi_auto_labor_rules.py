def get_labor_costs(silver_weight_g, craft_type, plating_color, e_coating):

    if silver_weight_g <= 4:
        handmade_labor = 12
        making_labor = 10
        sanding_labor = 5
        polishing_labor = 5
        
        silver_plating = 12
        rhodium_plating = 22 
        gold_plating = 25
        rose_gold_plating = 25
        
        e_coating_labor = 2
        mark_up = 16
    
    elif silver_weight_g <= 8:
        handmade_labor = 15
        making_labor = 12
        sanding_labor = 8
        polishing_labor = 8
        
        silver_plating = 15
        rhodium_plating = 32 
        gold_plating = 35
        rose_gold_plating = 35
        
        e_coating_labor = 3
        mark_up = 14
      
    else:
        handmade_labor = 20
        making_labor = 15
        sanding_labor = 10
        polishing_labor = 10
        
        silver_plating = 18
        rhodium_plating = 45 
        gold_plating = 50
        rose_gold_plating = 48
        
        e_coating_labor = 4
        mark_up = 12
    
    
    if craft_type == "handmade":
        making_labor = handmade_labor
        sanding_labor = 0
        polishing_labor = 0
        
    elif craft_type == "casted":
        making_labor = casting_labor
        handmade_labor = 0

    else:
        raise ValueError("Choose handmade or casted.")

    if plating_color == "s":
        plating_labor = silver_plating

    elif plating_color == "rh":
        plating_labor = rhodium_plating

    elif plating_color == "g":
        plating_labor = gold_plating
    
    elif plating_color == "rg":
        plating_labor = rose_gold_plating

    else:
        raise ValueError("Choose s, rh, g, or rg.")

    if e_coating == "no":
        e_coating_labor = 0

    elif e_coating != "yes":
        raise ValueError("Choose yes or no for E-coating.")


    return (making_labor, sanding_labor, polishing_labor, plating_labor, e_coating_labor, mark_up)
