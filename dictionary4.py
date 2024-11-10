def even_odd_dict():
    nbr_list = [int(input('Enter a number: ')) for _ in range(int(input('Enter the size of list you want: ')))]
    return(( sum([num for num in nbr_list if num % 2 == 0]), sum([num for num in nbr_list if num % 2 != 0])))
print(f'\nThe sum of even and odd numbers in tuple are the following respectively:\n{even_odd_dict()}')