def calculate_due_amount(total_bill, amount_paid):
    if amount_paid < total_bill:
        return total_bill - amount_paid
    else:
        pass  
    print("No due amount, perfectly paid")

total_bill = int(input("Enter total bill amount: "))
amount_paid = int(input("Enter amount paid: "))

due = calculate_due_amount(total_bill, amount_paid)
if due > 0:
    print(f"Due amount is:",due)
