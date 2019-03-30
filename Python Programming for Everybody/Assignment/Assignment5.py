score = float(input("Enter Score: "))
if(score<=1 and score>=0.9):
    grade = "A"
elif(score<0.9 and score>=0.8):
    grade = "B"
elif(score<0.8 and score>=0.7):
    grade = "C"
elif(score<0.7 and score>=0.6):
    grade = "D"
elif(score<0.6 and score>=0):
    grade = "F"
else:
    grade = "an error"
print(grade)
