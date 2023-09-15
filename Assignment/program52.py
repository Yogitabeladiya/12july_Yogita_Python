# amountn

data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

# Create an empty dictionary to store the combined values
combined = {}

# Loop through the list of dictionaries
for d in data:
    # Get the item and amount from each dictionary
    item = d['item']
    amount = d['amount']
    # If the item is already in the combined dictionary, add the amount to the existing value
    if item in combined:
        combined[item] += amount
    # Otherwise, set the amount as the value for the item
    else:
        combined[item] = amount

# Print the combined dictionary
print(combined)