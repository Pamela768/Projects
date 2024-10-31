import sys

name = input("What is your name: ")

eng = int(input("What was your english score: "))
math = int(input("What was your math's score: "))
sci = int(input("What was your science score: "))




if eng >100 or math >100 or sci>100:
	print ("Are you trying to cheat, your score was way greater than 100\nNice try")
	sys.exit()


# for english 
if eng >= 90:
	eng_score = "A"
elif eng >= 80:
	eng_score = "B"
elif eng >= 70:
	eng_score = "C"
elif eng >= 60:
	eng_score = "D"
elif eng >= 50:
	eng_score = "E"
elif eng >= 40:
	eng_score = "F"
else:
    print("Invalid Grade")


if math >= 90:
	math_score = "A"
elif math >= 80:
	math_score = "B"
elif math >= 70:
	math_score = "C"
elif math >= 60:
	 math_score = "D"
elif math >= 50:
	math_score = "E"
elif math >= 40:
	math_score = "F"
else:
    print("Invalid Grade")

if sci >= 90:
	sci_score = "A"
elif sci>= 80:
	sci_score = "B"
elif sci >= 70:
	sci_score = "C"
elif sci >= 60:
	 sci_score = "D"
elif sci >= 50:
	sci_score = "E"
elif sci >= 40:
	sci_score = "F"
else:
    print("Invalid Grade")


print(f"Your english grade: {eng_score}\nYour math's grade: {math_score}\nYour science grade: {sci_score}")

avg = round((eng+math+sci)/3,2)
print(f"{name}, Your average is {avg}")

if avg <= 40:
    print("You resuly wasn't the best, you can do much better")
if avg>= 50:
    print("You can still do better")
if avg >= 60:
    print("Great Job but you can still do better")
if avg >= 80:
    print("Congrats, You did very well. The sky is just the limit")
