class Product():

    name: str
    num: int
    weight_per_unit: float

    def __init__(self, name: str, num: int, weight_per_unit: float) -> None:
        self.name = name
        self.num = num
        self.weight_per_unit = weight_per_unit
    
    @property
    def total_weight(self) -> float:
        return self.num * self.weight_per_unit
    
    def __str__(self) -> str:
        return f"{self.name} - {self.num} units - {self.weight_per_unit} kg"