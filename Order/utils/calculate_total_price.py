def calculate_total_price(order) :
    total_price = 0
    for item in order.items.all() :
        total_price += item.quantity * item.menu_item.price
    order.total_price = total_price
    order.save()
    
    return total_price