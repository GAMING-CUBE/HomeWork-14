a = [1952, 10.45, 2+3j, False, 'pythonguide.pp.ua', (1, -6), [3, 15], {'Class C': ['Volkswagen Golf', 'Ford Focus'],
                                                                              'Class F': ['Audi A8', 'Bentley', 'Maybach'], 'E': ['Toyota Camry']}, None]
b = {type(i).__name__: i for i in a}

for i, o in b.items():
    print("<class '" + i + "'>", o)
