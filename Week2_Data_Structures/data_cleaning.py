n = int(input("Enter number of elements: "))

data = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    data.append(num)

unique_data = list(set(data))

print("Data after removing duplicates:", unique_data)

filtered_data = []

for num in unique_data:
    if num > 10:
        filtered_data.append(num)

print("Filtered data (greater than 10):", filtered_data)