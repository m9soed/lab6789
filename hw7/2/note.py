from datetime import date

class Note():
    _date: date
    _data: str

    def __init__(self, data: str) -> None:
        self._date = date.today()
        self._data = data

    @property
    def date(self): 
        return self._date

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data: str): 
        self._data = data

    def __str__(self) -> str:
        return f"date: {self._date} data: {self._data}"

    def __repr__(self) -> str:
        return f"date: {self._date} data: {self._data}"

