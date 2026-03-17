def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total

n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

result = sum_of_squares(numbers)

print("Sum of squares:", result)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even_numbers)