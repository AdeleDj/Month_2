class Distance:
    conversion_to_meters = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    def __init__(self, value, unit):
        if unit not in self.conversion_to_meters:
            raise ValueError(f"Unknown unit: {unit}")
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def to_meters(self):
        return self.value * self.conversion_to_meters[self.unit]

    @classmethod
    def from_meters(cls, meters, target_unit):
        value = meters / cls.conversion_to_meters[target_unit]
        return cls(value, target_unit)

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        total_meters = self.to_meters() + other.to_meters()
        return Distance.from_meters(total_meters, self.unit)

    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented

        result_meters = self.to_meters() - other.to_meters()
        if result_meters < 0:
            raise ValueError("The distance can't be negative!")

        return Distance.from_meters(result_meters, self.unit)


d1 = Distance(10, "m")
d2 = Distance(2, "km")
d3 = Distance(50, "cm")

print(d1)
print(d2)

result1 = d1 + d2
print(result1)

result2 = d1 + d3
print(result2)

result3 = d2 + d1
print((result3))

print(d2 - d1)

print(d1 - d2)

