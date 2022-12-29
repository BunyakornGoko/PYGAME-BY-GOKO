def myRandom():
    Name = input("Name :")
    List_Average = []
    print("-------------------------")
    for i in range(1,6):
        import random               
        x = random.randrange(1,10)
        print("Round :" , i) 
        print(x)
        print("-------------------------")    
        List_Average.append(x)      
        average = sum(List_Average)/len(List_Average)
    print("Average random numbers :" , average)      
                        
    if i <= 10:
        print("True")

    else :
        print("False")

def Average():
    number = [10,10,10,10,10]
    print(number)
    average = sum(number)/len(number)
    print(average)




myRandom()
Average()

