print("BCA-III QUIZ")

play = input("Do You Want play tha game? ").upper()
print()

if play != "YES":
    print("Don't worry play again!")
    quit()
else:
    print("Let's Goooooooooo...")

print("🎉"*30)
print()

score = 0

d1 = int(input("5+2 = "))
if d1 == 7:
    print("Correct✅")
    score += 1
else:
    print("Worng❎")
    score -= 1

d2 = int(input("5*2 = "))
if d2 == 10:
    print("Correct✅")
    score += 1
else:
    print("Worng❎")
    score -= 1

d3 = int(input("7*3 = "))
if d3 == 21:
    print("Correct✅")
    score += 1
else:
    print("Worng❎")
    score -= 1

d4 = int(input("8/2 = "))
if d4 == 4:
    print("Correct✅")
    score += 1
else:
    print("Worng❎")
    score -= 1

d5 = int(input("13%2 = "))
if d5 == 1:
    print("Correct✅")
    score += 1
else:
    print("Worng❎")
    score -= 1

print("Your Score Is: ",score)