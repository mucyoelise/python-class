length = int(input('Enter the number of strings to put in a list: '))
def func_list(length):
    string = [input(f'Enter string {index + 1}: ') for index in range(length)]
    return({string[index] : len(string[index]) for index in range(length)})
print(func_list(length))