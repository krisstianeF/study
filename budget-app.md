# Budget App

```python
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount, 
                'description': f'Transfer to {other.name}'
                })
            other.ledger.append({
                'amount': amount, 
                'description': f'Transfer from {self.name}'
                })
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        lines = [13*'*' + self.name + 13*'*']
        
        for item in self.ledger:
            description = item["description"][:23]
            amount = item["amount"]
            lines.append(f'{description:<23}{amount:>7.2f}')
        lines.append(f'Total: {self.get_balance()}')
        return "\n".join(lines)


def create_spend_chart(categories):
    category_withdrawals = {}

    # Calculate withdrawals for each category
    for category in categories:
        withdrawals = 0
        for transaction in category.ledger:
            amount = transaction['amount']
            if amount < 0:
                withdrawals += -amount  # Add the amount spent (negative for withdrawals)
        category_withdrawals[category.name] = withdrawals

    # Calculate total withdrawals across all categories
    total_withdrawals = sum(category_withdrawals.values())

    # Calculate percentages spent for each category based on withdrawals
    category_percentages = {}
    for name, withdrawals in category_withdrawals.items():
        category_percentages[name] = (withdrawals / total_withdrawals) * 100 if total_withdrawals > 0 else 0

    # Generate the chart body
    chart_list = ["Percentage spent by category"]
    for i in range(100, -1, -10):
        line = f"{i:3}| "
        for name in category_percentages:
            percent = category_percentages[name]
            if percent >= i:
                line += "o  "
            else:
                line += "   "
        chart_list.append(line)

    # Print the horizontal line at the bottom of the chart
    chart_list.append("    " + "-" * (len(category_percentages) * 3 + 1))

    # Print category names vertically
    max_name_length = max(len(name) for name in category_percentages)
    for i in range(max_name_length):
        line = "     "
        for name in category_percentages:
            if i < len(name):
                line += name[i] + "  "
            else:
                line += "   "
        chart_list.append(line)

    return "\n".join(chart_list)
    

food = Category('Food')
clothing = Category("Clothing")
auto = Category('Auto')

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
food.transfer(50, clothing)

clothing.withdraw(25.55, "shirt")
auto.deposit(500, "initial")
auto.withdraw(100, "gas")

print(food)
print(create_spend_chart([food, clothing, auto]))


```
