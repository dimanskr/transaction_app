from datetime import datetime


class Operation:
    def __init__(self, data):
        self.id = data.get("id")
        self.state = data.get("state")
        self.date = datetime.strptime(data.get("date"), "%Y-%m-%dT%H:%M:%S.%f")
        self.amount = float(data["operationAmount"]["amount"])
        self.currency_name = data["operationAmount"]["currency"]["name"]
        self.currency_code = data["operationAmount"]["currency"]["code"]
        self.description = data.get("description")
        self.from_account = data.get("from", None)
        self.to_account = data.get("to")

    def formated_date(self):
        """
        date in format DD.MM.YYYY
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
