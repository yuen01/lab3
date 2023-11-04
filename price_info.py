
price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}


def total_cost_shopping():
    total_cost = 0
    for fruit, quantity in quantity_list.items():
        if fruit in price_list:
            cost = price_list[fruit] * quantity
            total_cost += cost
    print("Total cost =", total_cost)
    return total_cost


def cost_of_fruits(fruit, quantity):
    for fruit, quantity in quantity_list.items():
        if fruit in price_list:
            cost = price_list[fruit] * quantity
            print("Cost of", quantity, fruit, "=", cost)
            return cost


def main():

    cost_of_fruits('apple', 10)
    total_cost_shopping()


if __name__ == "__main__":
    main()