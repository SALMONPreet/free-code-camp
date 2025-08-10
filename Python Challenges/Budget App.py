class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item['description'][:23].ljust(23)
            amt = f"{item['amount']:.2f}"[:7].rjust(7)
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    title = "Percentage spent by category\n"

    
    spends = []
    for category in categories:
        total = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        spends.append(total)
    total_spent = sum(spends)
    percentages = [(int((spend / total_spent) * 10) * 10) for spend in spends]

    
    chart_lines = ""
    for i in range(100, -1, -10):
        line = f"{str(i).rjust(3)}|"
        for percent in percentages:
            line += " o " if percent >= i else "   "
        chart_lines += line + " \n"

    
    separator = "    " + "-" * (len(categories) * 3 + 1) + "\n"

    
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)
    name_lines = ""
    for i in range(max_len):
        line = "    "
        for name in names:
            if i < len(name):
                line += f" {name[i]} "
            else:
                line += "   "
        line += " "  
        name_lines += line + "\n"

    return title + chart_lines + separator + name_lines.rstrip("\n")
