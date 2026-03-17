import numpy as np

n = int(input("Enter number of elements: "))

data = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    data.append(num)

arr = np.array(data)

print("Array:", arr)
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))