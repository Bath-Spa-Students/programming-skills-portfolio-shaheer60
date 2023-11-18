sandwich_orders = ('chicken', 'beef', 'pastrami', 'pastrami', 'egg', 'chocolate', 'pastrami')
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")

# Removing 'pastrami' from the list of orders
while 'pastrami' in sandwich_orders:
    sandwich_orders = list(sandwich_orders)
    sandwich_orders.remove('pastrami')
    sandwich_orders = tuple(sandwich_orders)

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")
