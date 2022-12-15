print("Helloo Suman")
print("Cash available in your account is 25000")
def atm(BALANCE):
    
    a=int(input(
    '''    PRESS 1 TO WITHDRAW CASH
    PRESS 2 TO DEPOSIT  CASH
    PRESS 3 TO KNOW YOUR CURRENT BALANCE
    PRESS 4 TO EXIT
    ENTER: '''))
    

    if a==1:
        W_AMOUNT=int(input("ENTER THE AMOUNT TO WITHRAW IN MULTIPLE OF 500: "))
        if BALANCE >=W_AMOUNT:
            if W_AMOUNT%500==0:
                print(W_AMOUNT, "HAS BEEN WITHDRAWN SUCCESSFULLY")
                BALANCE -=W_AMOUNT
                print("CURRENT BALANCE IS ",BALANCE)
                
            else:
                print("INAPPOROPIRATE ENTRY")
        else:
            print("INSUFFICENT BALANCE")
    elif a==2:
        D_AMOUNT=int(input("ENTER THE AMOUNT TO DEPOSIT: "))
        BALANCE+=D_AMOUNT
        print("CURRENT BALANCE IS ",BALANCE)
    elif a==3:
        print("CURRENT BALANCE IS ",BALANCE)
        if BALANCE<5000:
            print("LOW BALANCE")
    elif a==4:
        
        print('''THANKS FOR USING ATM
        ---- SUCCESSFULLY EXITED ----''')
    if a!=4:
        atm(BALANCE)    
atm(25000)  