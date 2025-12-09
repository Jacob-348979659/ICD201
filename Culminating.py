MENU_ITEMS = {
    1: ("Classic Burger", 5.99), 2: ("Cheese Burger", 6.99), 3: ("Bacon Burger", 7.99), 4: ("Veggie Burger", 6.49),
    5: ("Caesar Salad", 4.99), 6: ("Garden Salad", 4.49), 7: ("Greek Salad", 5.49), 8: ("Cobb Salad", 6.49),
    9: ("Small Fries", 1.99), 10: ("Medium Fries", 2.49), 11: ("Large Fries", 2.99), 12: ("Sweet Potato Fries", 3.49),
    13: ("Soda", 1.49), 14: ("Iced Tea", 1.99), 15: ("Lemonade", 1.99), 16: ("Water", 0.99)
}

CATEGORIES = [("--- BURGERS ---", range(1, 5)), ("--- SALADS ---", range(5, 9)), ("--- FRIES ---", range(9, 13)), ("--- DRINKS ---", range(13, 17))]

def border(c="=", w=60): return c * w

def display_menu():
    print(f"\n{border()}\n{'ITEM #':<8} {'DESCRIPTION':<30} {'PRICE':<10}\n{border()}")
    for cat, rng in CATEGORIES:
        print(f"\n{cat}")
        for i in rng: n, p = MENU_ITEMS[i]; print(f"{i:<8} {n:<30} ${p:<9.2f}")
    print(f"\n{border()}")

def add_item(order, num, menu=MENU_ITEMS):
    if num not in menu: return print(f"Invalid: {num}. Select 1-16.") or False
    name, price = menu[num]
    for item in order:
        if item["item"] == name: item["quantity"] += 1; return print(f"Added '{name}' (${price:.2f}). Qty: {item['quantity']}") or True
    order.append({"item": name, "price": price, "quantity": 1}); print(f"Added '{name}' (${price:.2f})"); return True

def remove_item(order, idx):
    if not (0 <= idx < len(order)): return print(f"Invalid index: {idx}.") or False
    r = order.pop(idx); print(f"Removed '{r['item']}' (${r['price']:.2f})"); return True

def update_item_qty(order, idx, qty):
    if not (0 <= idx < len(order)): return print(f"Invalid index.") or False
    if not isinstance(qty, int) or qty <= 0: return print(f"Qty must be positive.") or False
    o = order[idx]; old = o["quantity"]; o["quantity"] = qty; print(f"Updated '{o['item']}': {old} → {qty}"); return True

def display_receipt(order):
    if not order: return print("\nEmpty order.")
    print(f"\n{border()}\n{'ORDER RECEIPT':^60}\n{border()}\n{'#':<3} {'ITEM':<32} {'QTY':<5} {'PRICE':<10}\n{border('-')}")
    total = sum(i["price"] * i["quantity"] for i in order)
    for i, item in enumerate(order, 1): print(f"{i:<3} {item['item']:<32} {item['quantity']:<5} ${item['price']*item['quantity']:<9.2f}")
    print(f"{border('-')}\n{'TOTAL':<40} ${total:<9.2f}\n{border()}\n"); return total

def calculate_totals(order): s = sum(i["price"] * i["quantity"] for i in order); return s, s*0.13, s*1.13

def get_card_type(card): return ["Visa", "Mastercard", "American Express", "Discover", "Unknown"][{4:0, 5:1, 3:2, 6:3}.get(int(card[0]), 4)]

def validate_card(card):
    d = [int(x) for x in card if x.isdigit()]
    if not (13 <= len(d) <= 19): return False
    total = sum(((d[i]*2-9 if d[i]*2 > 9 else d[i]*2) if j%2 else d[i]) for j, i in enumerate(reversed(range(len(d)))))
    return total % 10 == 0

def get_tip(sub):
    while True:
        t10, t15, t18 = sub*0.1, sub*0.15, sub*0.18
        print(f"\nTip options:\n  [1] 10% (${t10:.2f})\n  [2] 15% (${t15:.2f})\n  [3] 18% (${t18:.2f})\n  [4] Custom\n  [5] None")
        c = input("Select: ").strip()
        if c in ['1','2','3']: return [t10, t15, t18][int(c)-1]
        if c == '4':
            try: t = float(input("Amount: ")); return t if t >= 0 else (print("Must be positive") or None)
            except: print("Invalid amount.")
        elif c == '5': return 0
        else: print("Invalid choice.")

def print_summary(sub, hst, tip, total):
    print(f"\n{border()}\nSubtotal:{' '*31} ${sub:>7.2f}\nHST (13%):{' '*30} ${hst:>7.2f}")
    if tip > 0: print(f"Tip:{' '*36} ${tip:>7.2f}")
    print(f"Total:{' '*35} ${total:>7.2f}\n{border()}\n")

def process_cash(total):
    while True:
        try:
            c = float(input(f"Enter amount: "))
            if c < total: print(f"Need ${total-c:.2f} more.")
            else: print(f"\n{border()}\nChange: ${c-total:.2f}\n{border()}\nThank you!\n"); return True
        except: print("Invalid amount.")

def process_credit(total):
    while True:
        card = input("Card number: ").replace(" ", "").replace("-", "")
        if not card.isdigit(): print("Digits only."); continue
        if not validate_card(card): print("Invalid card."); continue
        ct, masked = get_card_type(card), "*"*(len(card)-4)+card[-4:]
        print(f"Type: {ct}\nCard: {masked}")
        while True:
            p = input("PIN (4 digits): ")
            if len(p) == 4 and p.isdigit(): print(f"\n{border()}\nApproved!\nCharged: ${total:.2f}\nCard: {masked}\n{border()}\n"); return True
            print("Invalid PIN.")

def process_payment(order):
    if not order: return print("Empty order.") or False
    sub, hst, total = calculate_totals(order)
    print(f"\n{border()}\n{'PAYMENT':^60}\n{border()}"); print_summary(sub, hst, 0, total)
    while True:
        pt = input("Pay [CA]sh or [CR]edit? ").strip().upper()
        if pt in ['CA', 'CR']:
            add_tip = input("Add tip? [Y/N]: ").strip().upper() == 'Y'
            if add_tip:
                tip = get_tip(sub)
                if tip is None: continue
            else:
                tip = 0 if pt == 'CA' else (get_tip(sub) if input("Reconsider? [Y/N]: ").strip().upper() == 'Y' else 0)
            if tip is None: continue
            if tip > 0: print_summary(sub, hst, tip, total+tip)
            return (process_cash if pt == 'CA' else process_credit)(total+tip)
        print("Invalid. Enter CA or CR.")

def main():
    order = []
    display_menu()
    while True:
        print("\nOptions: [A]dd, [U]pdate, [R]emove, [V]iew, [P]ay, [Q]uit")
        c = input("Select: ").strip().upper()
        try:
            if c == 'A':
                while (i := input("Item (1-16) or [B]ack: ").strip().upper()) != 'B':
                    try: add_item(order, int(i))
                    except: print("Valid number.")
            elif c == 'U':
                if order:
                    display_receipt(order)
                    while (a := input("Position or [B]ack: ").strip().upper()) != 'B':
                        if (q := input("Qty or [B]ack: ").strip().upper()) != 'B':
                            try: update_item_qty(order, int(a)-1, int(q))
                            except: print("Valid numbers.")
                            display_receipt(order)
                else: print("Empty order.")
            elif c == 'R':
                if order:
                    display_receipt(order)
                    while (a := input("Position or [B]ack: ").strip().upper()) != 'B':
                        try: remove_item(order, int(a)-1); display_receipt(order)
                        except: print("Valid number.")
                else: print("Empty order.")
            elif c == 'V': display_receipt(order)
            elif c == 'P': order = [] if process_payment(order) else order; print("New order..." if not order else "")
            elif c == 'Q': (print("Thanks!") or exit()) if not order or input("Sure? [Y/N]: ").upper() == 'Y' else None
            else: print("Invalid option.")
        except: print("Error. Try again.")

if __name__ == "__main__": main()
