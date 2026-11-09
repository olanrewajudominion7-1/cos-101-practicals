input("Enter student name:")
DTC = float(input("Enter Daily transport cost:"))
DFC = float(input("Enter daily feeding cost:"))
DOC = int(input("Enter number of days on campus:"))
OWE = float(input("Enter amount of other weekly expenses:"))
if DTC <0:
    print("INVALID")
elif DFC <0:
    print("INVALID")
elif DOC <0:
    print("INVALID")
elif OWE <0:
    print("INVALID")
else:
    Transport_total = DTC*DOC
    Feeding_total = DFC*DOC
    weekly_total = Transport_total + Feeding_total + OWE

    print(f"Transport total={Transport_total:.2f}")
    print(f"Feeding total={Feeding_total:.2f}")
    print(f"Other weekly expenses ={OWE:.2f}")
    print(f"Weekly total={weekly_total:.2f}")
print("=========================") 

wk_b=int(input("Enter Weekly Budget: "))
if wk_b < weekly_total:
    print("Within Budget")
elif wk_b == weekly_total:
    print("Exactly on Budget")
else:
    res= wk_b - weekly_total
    print(f"Amount Exceeded by NGN{res:,.2f}")
