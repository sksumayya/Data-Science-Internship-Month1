n = int(input("Enter number of temperature values: "))

temps = []

for i in range(n):
    temp = float(input(f"Enter temperature {i+1}: "))
    temps.append(temp)

avg = sum(temps) / len(temps)

print("Average Temperature:", avg)