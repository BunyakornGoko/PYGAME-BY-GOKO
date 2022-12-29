### สร้างโปรแกรมให้มีคน5คน ซึ่งรับค่า INPUT เป็นตัวเลข เลข 0 - 100 และเอาตัวเลขทั้ง5คนนั้นมาหาค่าเฉลี่ยแล้ว คูณด้วย 0.8 และเอาค่าที่ได้ ไปเทียบกับPlayer ว่า ใครใกล้เคียงที่สุด


import os

os.system('cls')

while True:
    
    my_list = []
    duplicates = []
    
    for i in range(5):
        print("Player" , i+1)
        my_list.append(int(input('your number: ')))
        if my_list[i] >=0 and my_list[i] <=100:
            pass
        else:
            raise Exception("Please choose your number between 0-100")
        print("---------------------------------")

    # ! This is duplicate checking function
    for value in my_list:
        if my_list.count(value) > 1:
            if value not in duplicates:
                duplicates.append(value)
    
    if len(duplicates) == 0:
        break
    else:
        os.system('cls')
        print(my_list)
        print("There are players with duplicate values.",duplicates,"This game void!!\nPlease choose your new number.")

print(my_list)

average = sum(my_list)/len(my_list)
game = average * 0.8;

for i in range(5):
    my_list[i] = abs(game - my_list[i])

min = min(my_list)
winner = my_list.index(min) + 1;

print("ค่าเฉลี่ย : %.2f\nGame : (Average * 0.8)= %.2f\nWinner is Player %d" % (average, game, winner))

print("---------------------------------")