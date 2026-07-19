game = input("Do you play the game? ").upper()

if(game != "YAS"):
    print("Ok! Do it letter")

else:
    score = 0

    q1 = int(input("Q1. 6+7 ="))

    if(q1 == 13):
        print("Correct✅")
        score = score+1
    else:
        print("Wrong❎")

    q2 = int(input("Q2. 8*7 ="))

    if(q2 == 56):
        print("Correct✅")
        score = score+1
    else:
        print("Wrong❎")

    q3 = int(input("Q3. 9*8 ="))

    if(q3 == 72):
        print("Correct✅")
        score = score+1
    else:
        print("Wrong❎")

    q4 = int(input("Q4. 48/6 ="))

    if(q4 == 8):
        print("Correct✅")
        score = score+1
    else:
        print("Wrong❎")
    
    q5 = int(input("Q5. 4-1 ="))

    if(q5 == 3):
        print("Correct✅")
        score = score+1
    else:
        print("Wrong❎")

    print("Score: ",score)

    print("The quiz is end")

    

    
    
    
