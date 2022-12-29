# เกม XO
table = ["0","1","2",
         "3","4","5",
         "6","7","8"]

def displaytable():
    print(table[0]+ " / " + table[1] + " / " + table[2])
    print("----------")
    print(table[3]+ " / " + table[4] + " / " + table[5])
    print("----------")
    print(table[6]+ " / " + table[7] + " / " + table[8])
    print("----------")



def playgame():
    player = "x"
    print("ยินดีต้อนรับเข้าสู่เกม XO")
    for x in range(9):
        

        displaytable()
        # checkwin()
        if table[0] == table[1] == table[2] or\
            table[3] == table[4] == table[5] or\
            table[6] == table[7] == table[8] or\
            table[0] == table[3] == table[6] or\
            table[1] == table[4] == table[7] or\
            table[2] == table[5] == table[8] or\
            table[0] == table[4] == table[8] or\
            table[6] == table[4] == table[2] :
            if player == "x":
                player = "o"
            if player == "o":
                player = "x"
            print(player +"win")
            break
             

        # insert.xo
        
        while True:
            try:
                print("It's" + player + "turn")
                pos = int(input("ใส่เลขที่ผู้เล่นต้องการ: "))     #บรรทัดนี้คือการเช็คว่าเป็นตัวเลข ถ้าไม่ใช่ตัวเลขจะแปลงเป็นintไม่ได้แล้วจะโดนไปดู except
                if pos in range(0,9) and table[pos] == str(pos):            #บรรทัดนี้จะอยู่ใน range 0-8 ถ้าไม่ใช่จะใส่ค่าไม่ได้ และจะเช็คว่ามีใครใส่หรือยัง   #"x" == "0"  
                    table[pos] = player
                    if player == "x":
                        player = "o"
                    elif player == "o":
                        player = "x"
                
                    break
                else:print("กรุณาป้อนเลข 0-8")
            except:
                print("กรุณาป้อนเป็นตัวเลข")

if __name__ == "__main__":
    playgame()





