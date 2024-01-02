import sell_weapons
def buy(shop, budget, item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary, bought_items, main_weapon_list, secondary_weapon_list):
    print (main_weapon)
    print (secondary_weapon)
    if budget >= shop[item]:
        if item not in bought_items:
            if item in main_weapon_list and main_weapon:
                budget, last_bought_main = sell_weapons.sell(shop, budget, last_bought_main, bought_items)
                budget -= shop[item]
                bought_items.append(item)
                last_bought_main = item
            elif item in secondary_weapon_list and secondary_weapon:
                budget, last_bought_secondary = sell_weapons.sell(shop, budget, last_bought_secondary, bought_items)
                budget -= shop[item]
                bought_items.append(item)
                last_bought_secondary = item
            else:
                budget-= shop[item]
                bought_items.append(item)

                if item in main_weapon_list:
                    last_bought_main = item
                    main_weapon = True
                else:
                    last_bought_secondary = item
                    secondary_weapon = True
            

    return (budget, item, main_weapon, secondary_weapon, last_bought_main, last_bought_secondary)