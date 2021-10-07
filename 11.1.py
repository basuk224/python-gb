from datetime import date


class Data:
    def __init__(self, data):
        self.data=data.split("/")

    @classmethod
    def extract(cls, data):
        day, month, year = [int(i) for i in data.split("/")]
        return f"{day}/{month}/{year}"

    @staticmethod
    def valid(data):
        try:
            day, month, year = data.split('/')
            date(int(year), int(month), int(day))
            return 'Верная дата'
        except ValueError:
            return 'Неверная дата'


print(Data.extract("10/11/2001"))
print(Data.valid("13/13/2001"))