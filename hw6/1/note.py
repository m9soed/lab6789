class Note():
    _id: int
    _data: str

    def __init__(self, id: int, data: str) -> None:
        self._id = id
        self._data = data

    @property
    def id(self): 
        return self._id

    @id.setter
    def id(self, id: int): 
        self._id = id

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data: str): 
        self._data = data

    def __str__(self) -> str:
        return f"id: {self._id} data: {self._data}"
