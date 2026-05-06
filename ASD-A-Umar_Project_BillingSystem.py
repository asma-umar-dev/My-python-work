# Project 3: Smart Grocery Billing System
# Student: Asma Umar | Institute: As-Sa’adah Institute

def get_item_details():
    name = input("Enter item name: ")
    price = float(input("Enter price per unit: "))
    qty = float(input("Enter quantity: "))
    return price * qty

def apply_discount(subtotal):
    if subtotal > 1000:
        return subtotal * 0.10, "10%"
    elif subtotal > 500:
        return subtotal * 0.05, "5%"
    else:
        return 0, "0%"

def generate_bill():
    grand_subtotal = 0
    while True:
        item_total = get_item_details()
        grand_subtotal += item_total
        print(f"Item Total: {item_total}")
        
        cont = input("\nAdd another item? (y/n): ")
        if cont.lower() != 'y':
            break
            
    discount_val, discount_perc = apply_discount(grand_subtotal)
    final_bill = grand_subtotal - discount_val
    
    print(f"\nSubtotal: {grand_subtotal}")
    print(f"Discount applied: {discount_perc}")
    print(f"Final Bill: {final_bill}")

# Run Project
generate_bill()
