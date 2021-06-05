def planet_mass(gravity, radius):
    mass = (gravity * radius**2 * 10**11) / (6.67)
    return mass

def planet_vol(radius):
    volume = (4 * 3.1415 * radius**3) / 3
    return volume
