n = int(input("Enter N : "))
k = int(input("Enter K : "))
Array = []
for i in range(1,n+1):
    Array.append(i)
print(Array)
result = list(filter(lambda n:(n % k == 0), Array))
print("ตัวเลขที่รับมาจากตัวแปร n และหาร k ลงตัว =" , result)

        