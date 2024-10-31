counter = int(input('Enter the number of elements to put in a list: '))
dictionary = {}
def dict_funct():
    for _ in range(counter):
        element = input('Enter a string: ')
        dictionary.update({element : len(element)})
dict_funct()
print(f'\n{dictionary}')
