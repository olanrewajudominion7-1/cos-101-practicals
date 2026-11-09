student_name = input("ENTER STUDENT NAME:")
student_ID = input("ENTER MATRIC NO:")
score = float(input("ENTER YOUR TEST SCORE:"))
if score <0 or score >100:
    print("INVALID INPUT, ENTER A SCORE FROM 0 TO 100")
else:
    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 40:
        grade = "D"
    elif score >= 30:
        grade = "E"
    else:
        grade = "F"
print()
print("STUDENT RESULT")
print("=================")
print(f"Name: {student_name}")
print(f"MATRIC NO.: {student_ID}")
print(f"Score: {score}")
print(f"Grade: {grade}")
print("==================")
print("Thank you")
