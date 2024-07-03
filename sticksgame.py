sticks = 21
print(" there is total 21 sticks , we have to choose 1 - 4 sticks in a one chance ")
print(" if any take last stick then  loose the game ")
while True :
        print("sticks left: " , sticks)
        sticks_taken = int (input(" take sticks :"))
        if sticks == 1:
                print("you took the last stick , game loose ")
                break
        if sticks_taken >= 5 or sticks_taken <= 0 :
                print("wrong choice")
                continue
        print("computer took :" , ( 5 - sticks_taken ) , "\n")
        sticks -= 5
