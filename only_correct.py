print("\nBCA-III QUIZ")
print("🎉" * 40)

play = input("Do You Play The Game (YES/NO): ").upper()

if play != "YES":
    print("Sad to see you go! 🤦‍♂️")
    quit()

print("Let's Gooooooo....")

score = 0

q1 = int(input("2 + 7 = "))
if q1 == 9:
    print("Correct ✅")
    score += 1

q2 = int(input("6 * 9 = "))
if q2 == 54:
    print("Correct ✅")
    score += 1

q3 = int(input("2 - 7 = "))
if q3 == -5:
    print("Correct ✅")
    score += 1

q4 = int(input("2 + 7 = "))
if q4 == 9:
    print("Correct ✅")
    score += 1

q5 = int(input("7 / 7 = "))
if q5 == 1:
    print("Correct ✅")
    score += 1

print("Your score is =", score)