cities = [
    "Budapest, Rome, Istanbul, Sydney, Kyiv, Hong Kong",
    "Kyiv, Hong Kong",
    "Budapest"
]

for cities_str in cities:
    cities_list = cities_str.split(', ')

    if len(cities_list) == 0:
        result = ""
    elif len(cities_list) == 1:
        result = cities_list[0]
    else:
        cities_except_last = ", ".join(cities_list[:-1])
        result = f"{cities_except_last} and {cities_list[-1]}"

    print(result)
