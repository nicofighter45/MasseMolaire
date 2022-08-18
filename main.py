atomic = {
    'H': 1.008, 'He': 4.002602, 'Li': 6.94, 'Be': 9.0121831, 'B': 10.81, 'C': 12.011, 'N': 14.007,
    'O': 15.999, 'F': 18.998403163, 'Ne': 20.1797, 'Na': 22.98976928, 'Mg': 24.305, 'Al': 26.9815385,
    'Si': 28.085, 'P': 30.973761998, 'S': 32.06, 'Cl': 35.45, 'Ar': 39.948, 'K': 39.0983, 'Ca': 40.078,
    'Sc': 44.955908, 'Ti': 47.867, 'V': 50.9415, 'Cr': 51.9961, 'Mn': 54.938044, 'Fe': 55.845, 'Co': 58.933194,
    'Ni': 58.6934, 'Cu': 63.546, 'Zn': 65.38, 'Ga': 69.723, 'Ge': 72.630, 'As': 74.921595, 'Se': 78.971,
    'Br': 79.904, 'Kr': 83.798, 'Rb': 85.4678, 'St': 87.62, 'Y': 88.90584, 'Zr': 91.224, 'Nb': 92.90637,
    'Mo': 95.95, 'Tc': 97, 'Ru': 101.07, 'Rh': 102.90550, 'Pd': 106.42
}

molecule = input("Composants :\n")


def isNumber(value: int) -> bool:
    string = molecule[value]
    return string == "0" or string == "1" or string == "2" or string == "3" or string == "4" or string == "5"\
           or string == "6" or string == "7" or string == "8" or string == "9"


def getAtomic(*values: int) -> float:
    name = ""
    for value in values:
        name += molecule[value]
    print(name)
    output = atomic.get(name)
    if output is None:
        raise Exception("Je ne reconnais pas cet atome :" + name)
    else:
        return output


mass = 0
atom_mass = 0
check_last = True
i = 0
while i < len(molecule) - 1:
    if isNumber(i):
        if isNumber(i + 1):
            mass += atom_mass * int(molecule[i] + molecule[i + 1])
            i += 1
        else:
            mass += atom_mass * int(molecule[i])
    else:
        if not isNumber(i + 1):
            atom_mass = getAtomic(i, i + 1)
            i += 1
            if i == len(molecule):
                check_last = False
        else:
            atom_mass = getAtomic(i)
    i += 1

if check_last and isNumber(len(molecule) - 1):
    mass += atom_mass * int(molecule[len(molecule) - 1])

print(mass)
