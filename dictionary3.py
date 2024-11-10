def dict_tuplist():
    tup_list = [(input('Enter the name: '), int(input('Enter the age: '))) for i in range(int(input('Enter the size of tuple list you want: ')))]
    return({age : name for name, age in tup_list})
print(f'\nThe dictionary of key: age and value: name is the following: \n{dict_tuplist()}')