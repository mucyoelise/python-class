def calculator(numbers):
    even_tot = sum(num for num in numbers if num % 2 == 0)
    odd_tot = sum(num for num in numbers if num % 2 != 0)
    return (even_tot, odd_tot)
numbers = [int(input('Enter a number: ')) for _ in range(5)]
print(calculator(numbers))