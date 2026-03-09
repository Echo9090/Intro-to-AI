from itertools import combinations

transactions = [
    {'milk', 'bread', 'butter'},
    {'bread', 'butter'},
    {'milk', 'bread'},
    {'milk', 'butter'},
    {'bread', 'butter'}
]

min_support = 2

item_counts = {}

# Count single items
for transaction in transactions:
    for item in transaction:
        item_counts[item] = item_counts.get(item, 0) + 1

print("Frequent 1-itemsets:")
for item, count in item_counts.items():
    if count >= min_support:
        print(item, ":", count)