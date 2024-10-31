# Note that tuple need to be initialised when you create it for it's unchangeable
people = [('Mucyo', 12), ('Elise', 13), ('Samuel', 14)]

def tup_list():
    return {age: person for person, age in people}

print(tup_list())   