from datetime import datetime


class Operation:
    def __init__(self, data):
        self.id = data.get("id", 0)
        self.state = data.get("state", None)
        self.date = datetime.strptime(data.get("date"), "%Y-%m-%dT%H:%M:%S.%f")
        self.amount = float(data.get("operationAmount", {}).get("amount", 0.0))
        self.currency_name = data.get("operationAmount", {}).get("currency", {}).get("name", None)
        self.currency_code = data.get("operationAmount", {}).get("currency", {}).get("code", None)
        self.description = data.get("description", None)
        self.from_account = data.get("from", None)
        self.to_account = data.get("to", None)

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
