from space.planet import Planet
from space.calc import planet_mass, planet_vol

naboo = Planet('Naboo', 300000, 8, 'Naboo System')

naboo_mass = planet_mass(naboo.gravity, naboo.radius)
naboo_vol = planet_vol(naboo.radius)

print(f"{naboo.name} has \na mass of {naboo_mass} \nand \na volume of {naboo_vol}")
