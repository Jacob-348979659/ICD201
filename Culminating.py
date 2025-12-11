from typing import List, Dict, Tuple, Optional, Any # Import necessary types from typing module

RESTAURANT_NAME = "BURGER BISTRO" # Restaurant name

MENU_ITEMS: Dict[int, Tuple[str, float]] = { # Initialize menu items
    1: ("Classic Burger", 5.99), 2: ("Cheese Burger", 6.99), 3: ("Bacon Burger", 7.99), 4: ("Veggie Burger", 6.49), # Burgers
    5: ("Caesar Salad", 4.99), 6: ("Garden Salad", 4.49), 7: ("Greek Salad", 5.49), 8: ("Cobb Salad", 6.49), # Salads
    9: ("Small Fries", 1.99), 10: ("Medium Fries", 2.49), 11: ("Large Fries", 2.99), 12: ("Sweet Potato Fries", 3.49), # Fries
    13: ("Soda", 1.49), 14: ("Iced Tea", 1.99), 15: ("Lemonade", 1.99), 16: ("Water", 0.99) # Drinks
}

CATEGORIES: List[Tuple[str, range]] = [ # Menu categories
    ("--- BURGERS " + "-" * 48, range(1, 5)),
    ("--- SALADS " + "-" * 49, range(5, 9)),
    ("--- FRIES " + "-" * 50, range(9, 13)),
    ("--- DRINKS " + "-" * 49, range(13, 17)),
]

def border(c: str = "=", w: int = 60) -> str: # Create a border line of a given character and width
    return c * w

def display_menu() -> None: # Go through the MENU_ITEMS and print them while formatting
    print(f"\n{border()}\n{RESTAURANT_NAME:^60}\n\n{'#':<8} {'ITEM NAME':<30} {'PRICE':<10}\n{border()}") # Print menu header
    for cat, rng in CATEGORIES: # Loop through each category and its range of items
        print("\n" + cat)
        for i in rng:
            n, p = MENU_ITEMS[i]
            print(f"{i:<8} {n:<30} ${p:<9.2f}") # Print each menu item with its number, name, and price
    print("\n" + border())

def add_item(order: List[Dict[str, Any]], num: int, menu: Dict[int, Tuple[str, float]] = MENU_ITEMS) -> bool: # Function to add an item to the order
    if type(num) is not int: # Check if the item number is an integer
        print("Item number must be an integer.")
        return False
    if num not in menu: # Check if the item number is valid
        print(f"Invalid item {num}; select 1-16.")
        return False
    name, price = menu[num]
    for item in order: # Check if the item is already in the order
        if item["item"] == name:
            item["quantity"] += 1
            print(f"Added '{name}' (${price:.2f}); qty {item['quantity']}")
            return True
    order.append({"item": name, "price": price, "quantity": 1}) # Add new item to the order
    print(f"Added '{name}' (${price:.2f})")
    return True

def remove_item(order: List[Dict[str, Any]], idx: int) -> bool: # Function to remove an item from the order by index
    if type(idx) is not int: # Check if the index is an integer
        print("Index must be an integer.")
        return False
    if not (0 <= idx < len(order)): # Check if the index is valid
        print(f"Invalid index: {idx}.")
        return False
    r = order.pop(idx) # Remove the item from the order
    print(f"Removed '{r['item']}' (${r['price']:.2f})")
    return True

def update_item_qty(order: List[Dict[str, Any]], idx: int, qty: int) -> bool: # Function to update the quantity of an item in the order
    if type(idx) is not int: # Check if the index is an integer
        print("Index must be an integer.")
        return False
    if not (0 <= idx < len(order)): # Check if the index is valid
        print("Invalid index.")
        return False
    if type(qty) is not int: # Check if the quantity is an integer
        print("Quantity must be an integer.")
        return False
    if qty <= 0: # Check if the quantity is positive
        print("Qty must be positive.")
        return False
    o = order[idx]
    old = o["quantity"]
    o["quantity"] = qty
    print(f"Updated '{o['item']}': {old} → {qty}")
    return True

def display_receipt(order: List[Dict[str, Any]]) -> Optional[float]: # Function to display the receipt of the current order
    if not order: # Check if the order is empty
        print("\nEmpty order.")
        return None
    print(f"\n{border()}\n{'ORDER RECEIPT':^60}\n{border()}\n{'#':<3} {'ITEM':<26} {'QTY':<5} {'UNIT':<10} {'PRICE':<10}\n{border('-')}")
    total = sum(i["price"] * i["quantity"] for i in order) # Calculate total price
    for i, item in enumerate(order, 1): # Print each item in the order
        unit = item['price']
        subtotal = unit * item['quantity']
        print(f"{i:<3} {item['item']:<26} {item['quantity']:<5} ${unit:<9.2f} ${subtotal:<9.2f}")
    print(f"{border('-')}\n{'TOTAL:':<47} ${total:<9.2f}\n{border()}\n")
    return total

def calculate_totals(order: List[Dict[str, Any]]) -> Tuple[float, float, float]: # Function to calculate subtotal, tax, and total
    s = sum(i["price"] * i["quantity"] for i in order); return s, s * 0.13, s * 1.13 # Return subtotal, HST, and total

def parse_positive_int(s: str) -> Optional[int]: # Function to parse a positive integer from a string
    if not isinstance(s, str): # Check if input is a string
        return None
    s = s.strip()
    if s.isdigit(): # Check if the string represents a digit
        v = int(s)
        return v if v > 0 else None
    return None

def prompt_positive_int(prompt: str, min_v: int = 1, max_v: Optional[int] = None, allow_back: bool = True) -> Optional[int]: # Function to prompt user for a positive integer input
    while True:
        s = input(prompt).strip()
        if allow_back and s.upper() in ('B', 'BACK'): # Check for back option
            return None
        if s.isdigit():
            v = int(s)
            if v < min_v or (max_v is not None and v > max_v): # Validate range
                if max_v is None:
                    print(f"Enter >= {min_v}.")
                else:
                    print(f"Enter {min_v}-{max_v}.")
                continue
            return v
        print("Invalid.")

def prompt_positive_float(prompt: str, allow_back: bool = True) -> Optional[float]: # Function to prompt user for a positive float input
    while True:
        s = input(prompt).strip()
        if allow_back and s.upper() in ('B', 'BACK'): # Check for back option
            return None
        try: # Try to convert input to float
            v = float(s)
        except ValueError: # Handle invalid float conversion
            print("Invalid.")
            continue
        if v < 0: # Validate positive value
            print("Must be >= 0.")
            continue
        return v

def prompt_choice(prompt: str, choices: Tuple[str, ...], allow_back: bool = True) -> Optional[str]: # Function to prompt user for a choice from given options
    cset = {c.upper() for c in choices}
    while True:
        s = input(prompt).strip()
        if allow_back and s.upper() in ('B', 'BACK'): # Check for back option
            return None
        if s.upper() in cset: # Validate choice
            return s.upper()
        print("Invalid.")

def prompt_card_number(prompt: str) -> Optional[str]: # Function to prompt user for a credit card number
    while True:
        s = input(prompt).strip()
        if s.upper() in ('B', 'BACK'): # Check for back option
            return None
        card = s.replace(' ', '').replace('-', '')
        if not card.isdigit(): # Validate digits only
            print("Digits only.")
            continue
        return card

def get_card_type(card: str) -> str: # Function to determine the type of credit card based on its number
    return ({'4': 'Visa', '5': 'Mastercard', '3': 'American Express', '6': 'Discover'}.get(card[0]) if card else 'Unknown') or 'Unknown' # Return card type based on first digit

def validate_card(card: str) -> bool: # Function to validate a credit card number using the Luhn algorithm
    d = [int(x) for x in card if x.isdigit()]
    if not (13 <= len(d) <= 19): # Check length of card number
        return False
    total = 0
    for i, digit in enumerate(reversed(d)): # Apply Luhn algorithm
        if i % 2 == 1: # Double every second digit
            digit *= 2
            if digit > 9: # Subtract 9 if greater than 9
                digit -= 9
        total += digit
    return total % 10 == 0

def get_tip(sub: float) -> Optional[float]: # Function to get tip amount from user
    t10, t15, t18 = sub * 0.1, sub * 0.15, sub * 0.18
    print(f"\n{border()}\nTip:\n [1]10%(${t10:.2f})\n [2]15%(${t15:.2f})\n [3]18%(${t18:.2f})\n [4]Custom\n [5]None\n [B]Back\n")
    ch = prompt_choice("Select: ", ('1', '2', '3', '4', '5'))
    if ch is None: # Check for back option
        return None
    if ch in ('1', '2', '3'): # Return predefined tip amounts
        return (t10, t15, t18)[int(ch) - 1]
    if ch == '4': # Prompt for custom tip amount
        v = prompt_positive_float("Amount: ")
        return v
    return 0.0

def print_summary(sub: float, hst: float, tip: float, total: float) -> None: # Function to print the payment summary
    print(f"\n{border()}\nSubtotal:{' ' * 31} ${sub:>7.2f}\nHST (13%):{' ' * 30} ${hst:>7.2f}"); (print(f"Tip:{' ' * 36} ${tip:>7.2f}") if tip > 0 else None); print(f"TOTAL:{' ' * 34} ${total:>7.2f}\n{border()}\n")

def process_cash(total: float) -> bool: # Function to process cash payment
    v = prompt_positive_float(f"Enter amount (total ${total:.2f}) or [B]ack: ")
    if v is None: # Check for back option
        print('Cancelled.')
        return False
    if v < total: # Check if the amount is sufficient
        print(f"Short ${total-v:.2f}.")
        return False
    print(f"\n{border()}\nChange: ${v-total:.2f}\n{border()}\nThanks!\n")
    return True

def process_credit(total: float) -> bool: # Function to process credit card payment
    card = prompt_card_number("Card number or [B]ack: ")
    if card is None: # Check for back option
        print('Cancelled.')
        return False
    if not validate_card(card): # Validate the credit card number
        print('Bad card.')
        return False
    ct = get_card_type(card)
    masked = '*' * (len(card) - 4) + card[-4:] # Mask the card number except for the last 4 digits
    print(f"Type:{ct} Card:{masked}")
    pin = prompt_positive_int("PIN(4 digits): ", min_v=0)
    if pin is None: # Check for back option
        print('Cancelled.')
        return False
    s_pin = str(pin)
    if len(s_pin) == 4: # Validate PIN length
        print(f"\n{border()}\nApproved\nCharged:${total:.2f}\n{border()}\n")
        return True
    print('Bad PIN.')
    return False

def process_payment(order: List[Dict[str, Any]]) -> bool: # Function to process the payment for the order
    if not order: # Check if the order is empty
        print("Empty order.")
        return False
    sub, hst, total = calculate_totals(order)
    print(f"\n{border()}\n{'PAYMENT':^60}\n{border()}")
    print_summary(sub, hst, 0.0, total) # Print payment summary without tip
    ch = prompt_choice("Pay [CA]/[CR] or [B]ack: ", ('CA', 'CR'))
    if ch is None: # Check for back option
        print('Cancelled.')
        return False
    add_tip = prompt_choice("Add tip? [Y/N]: ", ('Y', 'N')) == 'Y'
    tip = 0.0
    if add_tip: # Get tip amount if user chooses to add tip
        t = get_tip(sub)
        if t is None:
            print('Cancelled.')
            return False
        tip = t
    if tip > 0: # Print final summary with tip
        print_summary(sub, hst, tip, total + tip)
    processor = process_cash if ch == 'CA' else process_credit
    return processor(total + tip)

class POS: # Point of Sale class to manage the order flow
    def __init__(self) -> None: # Initialize the POS system with an empty order
        self.order: List[Dict[str, Any]] = []

    def add_flow(self) -> None: # Flow to add items to the order
        while True:
            v = prompt_positive_int("Item (1-16) or [B]ack: ", min_v=1, max_v=16) # Prompt for item number
            if v is None:
                break
            add_item(self.order, v)

    def update_flow(self) -> None: # Flow to update item quantities in the order
        if not self.order: # Check if the order is empty
            print("Empty order.")
            return
        display_receipt(self.order)
        while True:
            pos = prompt_positive_int("Position or [B]ack: ", min_v=1, max_v=len(self.order))
            if pos is None: # Check for back option
                break
            qty = prompt_positive_int("Qty or [B]ack: ")
            if qty is None: # Check for back option
                break
            update_item_qty(self.order, pos - 1, qty)
            display_receipt(self.order)

    def remove_flow(self) -> None: # Flow to remove items from the order
        if not self.order: # Check if the order is empty
            print("Empty order.")
            return
        display_receipt(self.order)
        while True:
            pos = prompt_positive_int("Position or [B]ack: ", min_v=1, max_v=len(self.order))
            if pos is None: # Check for back option
                break
            remove_item(self.order, pos - 1)
            display_receipt(self.order)

    def view_flow(self) -> None: # Flow to view the current order
        display_receipt(self.order)

    def pay_flow(self) -> None: # Flow to process payment for the order
        if not self.order: # Check if the order is empty
            print("Your order is empty.")
            return
        if process_payment(self.order): # Process payment
            self.order.clear()
            print("New order...")

def main() -> None: # Main function to run the POS system
    pos = POS() # Create a POS instance
    display_menu() # Display the menu
    while True:
        print("\nOptions: [A]dd, [U]pdate, [R]emove, [V]iew, [P]ay, [Q]uit")
        c = input("Select: ").strip().upper()
        if c == 'A': # Add item flow
            pos.add_flow()
        elif c == 'U': # Update item quantity flow
            pos.update_flow()
        elif c == 'R': # Remove item flow
            pos.remove_flow()
        elif c == 'V': # View order flow
            pos.view_flow()
        elif c == 'P': # Payment flow
            pos.pay_flow()
        elif c == 'Q': # Quit the program
            if pos.order and input("Are you sure? [Y/N]: ").upper() != 'Y': # Check for unsaved order
                continue
            print("Thanks!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__": main() # Run the main function
