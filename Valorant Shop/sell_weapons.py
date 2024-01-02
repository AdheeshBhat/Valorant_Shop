def sell(shop, budget, item, bought_items):
    if item in bought_items:
        budget += shop[item]
        bought_items.remove(item)
    return budget, item