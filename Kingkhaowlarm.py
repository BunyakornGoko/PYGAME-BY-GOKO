# สร้างโปรแกรมให้มีคน5คน ซึ่งรับค่า INPUT เป็นตัวเลข เลข 0 - 100 และเอาตัวเลขทั้ง5คนนั้นมาหาค่าเฉลี่ยแล้ว คูณด้วย 0.8 และเอาค่าที่ได้ ไปเทียบกับPlayer ว่า ใครใกล้เคียงที่สุด

# Player1 = int(input("Player1 :"))
# Player2 = int(input("Player2 :"))
# Player3 = int(input("Player3 :"))
# Player4 = int(input("Player4 :"))
# Player5 = int(input("Player5 :"))

# List_NumPlayer.append(Player1)
# List_NumPlayer.append(Player2)
# List_NumPlayer.append(Player3)
# List_NumPlayer.append(Player4)
# List_NumPlayer.append(Player5)
# print("-----------------------------------")
# print(List_NumPlayer)
# Sum = (Player1 + Player2 + Player3 + Player4 + Player5)/5
# print("ค่าเฉลี่ย" , Sum)
import os
os.system('cls')

scoreplayer1 = 0
scoreplayer2 = 0
scoreplayer3 = 0
scoreplayer4 = 0
scoreplayer5 = 0

# ! Loop ทั้งเกม (จะมีทั้งหมด 10 รอบ)
for i in range(3):
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


        for value in my_list:
            if my_list.count(value) > 1:
                if value not in duplicates:
                    duplicates.append(value)

        if len(duplicates) == 0:
            break
        else:
            os.system('cls')
            print (my_list)
            print("There are players with duplicate values.",duplicates,"This game void!!\nPlease choose your new number.")

    print(my_list)
                        
    average = sum(my_list)/len(my_list)
    game = average * 0.8;

    for i in range(5):
        my_list[i] = abs(game - my_list[i])


    # print("Calculated range:", my_list)

    min_value = min(my_list)
    winner = my_list.index(min_value) + 1;

    print("Average :",average,"\nGame :(Average * 0.8) = ",game)
    print("Winner is Player",winner)

    if winner == 1:
        scoreplayer2 -=1
        scoreplayer3 -=1
        scoreplayer4 -=1
        scoreplayer5 -=1
    elif winner == 2:
        scoreplayer1 -=1
        scoreplayer3 -=1
        scoreplayer4 -=1
        scoreplayer5 -=1
    elif winner == 3:
        scoreplayer1 -=1
        scoreplayer2 -=1
        scoreplayer4 -=1
        scoreplayer5 -=1
    elif winner == 4:
        scoreplayer1 -=1
        scoreplayer2 -=1
        scoreplayer3 -=1
        scoreplayer5 -=1
    elif winner == 5:
        scoreplayer1 -=1
        scoreplayer2 -=1
        scoreplayer3 -=1
        scoreplayer4 -=1

    print("---------------------------------")
    print("Score Player1 :" , scoreplayer1)
    print("Score Player2 :" , scoreplayer2)
    print("Score Player3 :" , scoreplayer3)
    print("Score Player4 :" , scoreplayer4)
    print("Score Player5 :" , scoreplayer5)
    print("---------------------------------")

winner_Chicken = min(winner)
print("Player ",winner," winner winner chicken dinner")

