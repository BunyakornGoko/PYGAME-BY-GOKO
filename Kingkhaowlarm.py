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

score_Player = [0,0,0,0,0]

# ! Loop ทั้งเกม (จะมีทั้งหมด 10 รอบ)
for i in range(2):
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

    for i in range(5):
        if i == (winner - 1):
            continue
        score_Player[i] -= 1

        

    print("---------------------------------")
    for i in range(5):
        print("Score Player%d : %d" % (i+1,score_Player[i]))
    print("---------------------------------")

final_winner = score_Player.index(max(score_Player)) + 1
print("Player " , final_winner ," winner winner chicken dinner")




