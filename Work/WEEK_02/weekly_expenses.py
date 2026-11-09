input("Enter student name:")
DTC = float(input("Enter Daily transport cost"))
DFC = float(input("Enter daily feeding cost"))
DOC = int(input("Enter number of days on campus"))
OWE = float(input("Enter amount of other weekly expenses"))
Transport_total = DTC*DOC
Feeding_total = DFC*DOC
weekly_total = Transport_total + Feeding_total + OWE

print(f"Transport total={Transport_total:.2f}")
print(f"Feeding total={Feeding_total:.2f}")
print(f"Other weekly expenses ={OWE:.2f}")
print(f"Weekly total={weekly_total:.2f}")

