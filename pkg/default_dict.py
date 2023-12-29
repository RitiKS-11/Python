from collections import defaultdict

def protein_fruit_source(data):
    # returns portein and fruits sources
    result = defaultdict(list)
    for type, source in data:
        result[type].append(source)
    return result['fruit'] + result['protein']


def group_by_age(name_and_ages):
    result = defaultdict(list)
    for name, age in name_and_ages:
        result[age].append(name)

    return dict(result)


    

