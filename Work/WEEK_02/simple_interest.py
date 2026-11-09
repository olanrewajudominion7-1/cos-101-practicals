principal=float(input("Enter initial principal: "))
rate=float(input("Enter current rate(%): "))
time=float(input("Enter timeline: "))
interest= (principal*rate*time)/100
print(f"Current Interest Earned= NGN {interest:,.2f}")
