from itertools import combinations

transactions = [
    {'milk', 'bread', 'butter'},
    {'bread', 'butter'},
    {'milk', 'bread'},
    {'milk', 'butter'},
    {'bread', 'butter'}
]

min_support = 2

pair_counts = {}

for transaction in transactions:
    pairs = combinations(transaction, 2)
    for pair in pairs:
        pair = tuple(sorted(pair))
        pair_counts[pair] = pair_counts.get(pair, 0) + 1

print("Frequent 2-itemsets:")
for pair, count in pair_counts.items():
    if count >= min_support:
        print(pair, ":", count)