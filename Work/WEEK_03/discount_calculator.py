while True:
    ori=float(input("Enter Price: "))
    if ori < 10000:
        disc=0
        print("Discount amt = 0")
        res= ori - disc
        print(f"Payable amt = NGN{res:,.2f}")
    elif ori >=10000 and ori <50000:
        disc=((5/100)*ori)
        print(f"Discount amt (5%)= NGN{disc:,.2f}")
        res= ori - disc
        print(f"Payable amt= NGN{res:,.2f}")
    elif ori >= 50000:
        disc=((10/100)*ori)
        print(f"Discount amt (10%)= NGN{disc:,.2f}")
        res= ori - disc
        print(f"Payable amt= NGN{res:,.2f}")
    
    
    
    
    
