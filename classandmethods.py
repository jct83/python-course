class Planet: 

    shape = "round"

    def __init__(self, name, radius, gravity, system): # Instance atribute
        self.name = name
        self.radius = radius
        self.gravity  = gravity
        self.system = system
    
    def orbit(self): # Instance Method
        return f'{self.name} is orbiting in the {self.system}'

    @classmethod #Same for each Planet
    def commons(cls): #Access to class level atributes
        return (f'All planets are {cls.shape} because of gravity')

    @staticmethod # Doesnt have access to self and class, only to the parameter which define its (speed)
    def spin(speed = "2000 miles per hour"): 
        return(f"The planet spins and spins t {speed}")


hoth = Planet('Hoth', 20000, 5.5, 'Hoth System')
print(f'Name is {hoth.name}')
print(hoth.orbit()) # yang def orbit(self)

naboo = Planet('Naboo', 300, 5.2, 'Naboo system')
print(f'Name is {naboo.name}')
print(naboo.orbit())

print(Planet.shape) #Instance atr - apply individual instance (hoth)
print(Planet.commons())
print(Planet.spin("a very high speed"))