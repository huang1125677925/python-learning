# def divide(e, f):
#     breakpoint()
#     return f / e
#
# a, b = 0, 1
# print(divide(a, b))



from dataclasses import dataclass, field

@dataclass(order=True)
class Country:
    name: str
    population: int
    area: float = field(repr=True, compare=False)
    coastline: float = 0

    def beach_per_person(self):
        """Meters of coastline per person"""
        return (self.coastline * 1000) / self.population
    
    

norway = Country("Norway", 5320045, 323802, 58133)
print(norway)


print(norway.area)


usa = Country("United States", 326625791, 9833517, 19924)
nepal = Country("Nepal", 29384297, 147181)
print(nepal)


print(usa.beach_per_person())


print(norway.beach_per_person())
    
    
