numbers = [1, 2, 3, 4, 5]
product = 1
number_list = []

for number in numbers:
    product *= number
for i in range(2):
    number_list.append(product)

print(number_list)  # Output: 120