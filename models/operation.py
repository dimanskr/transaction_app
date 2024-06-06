from datetime import datetime


class Operation:
    def __init__(self, data):
        self.id = data["id"]
        self.state = data["state"]
        self.date = datetime.fromisoformat(data["date"])
        self.amount = float(data["operationAmount"]["amount"])
        self.currency_name = data["operationAmount"]["currency"]["name"]
        self.currency_code = data["operationAmount"]["currency"]["code"]
        self.description = data["description"]
        self.from_account = data.get("from", None)
        self.to_account = data["to"]

    def formated_date(self):
        """
        Дата в формате DD.MM.YYYY
        """
        return self.date.strftime("%d.%m.%Y")

    def __str__(self):
        return (f"{self.state} transfer {self.description} {self.formated_date()}"
                f"from {self.from_account} to {self.to_account} in the amount {self.amount} {self.currency_name}")

    def __repr__(self):
        return (f"{self.__class__.__name__}(id={self.id}, state='{self.state}', date='{self.date}', "
                f"amount={self.amount}, currency_name='{self.currency_name}', "
                f"currency_code='{self.currency_code}', description='{self.description}', "
                f"from_account='{self.from_account}', to_account='{self.to_account}')")
