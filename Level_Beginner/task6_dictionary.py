# 6.1 List of Tuples
friends = ["Aditya", "Beatrix", "Charlie", "Danielle", "Emerson"]
friend_lengths = [(name, len(name)) for name in friends]
print(f"Friend Name Lengths: {friend_lengths}")

# 6.2 Expense Tracker
your_expenses = {"Hotel": 1200, "Food": 800, "Transportation": 500, "Attractions": 300, "Misc": 200}
partner_expenses = {"Hotel": 1000, "Food": 900, "Transportation": 600, "Attractions": 400, "Misc": 150}

your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print(f"Your Total: {your_total}, Partner Total: {partner_total}")

if your_total > partner_total:
    print("You spent more.")
else:
    print("Your partner spent more.")

# Significant difference
for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > 100: # Assuming > 100 is "significant"
        print(f"Significant difference in {category}: {diff}")