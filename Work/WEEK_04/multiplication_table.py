# Display a multiplication table from 1 to 12.

number = int(input("Enter a whole number: "))
st_m= int(input("Enter Starting Multiplier: "))
ed_m= int(input("Enter Ending Multiplier: "))

print()
print(f"MULTIPLICATION TABLE FOR {number}")
print("==============================")

if st_m > ed_m:
    print("INVALID INPUT")
else:
    for multiplier in range(st_m, ed_m + 1):

        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")
