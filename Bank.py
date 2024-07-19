def Check_Details(acc_no) :
    temp = ""
    for account in customer :
        account = account.split(",")
        if acc_no == account[1] :
            #print(acc no already existed)
            temp= 1
                
    if temp == "":
        return 0
        
    elif temp == 1:
        return 1
        
        
def add_balance(acc_no,balance):
    i=0
    for account in customer:
        account = account.split(",")
        if acc_no == int(account[1]):
            account[2] = int(account[2]) + balance
            customer[i] = account[0] + "," + str(account[1]) + "," + str(account[2])
            
        i = i+1
     
    print(customer)

def remove_balance(acc_no,balance):

    i=0
    for account in customer:
        account = account.split(",")
        if acc_no == int(account[1]):
            account[2] = int(account[2]) - balance
            customer[i] = account[0] + "," + str(account[1]) + "," + str(account[2])
            
        i = i+1
    print(customer)
    
customer=[]
customer=["Aishwarya,2,2000"]
customer.append("kalyani,3,1000")
customer.append("neha,4,900")

while True:

    choice=int(input("Press 1 for add account:\n Press 2 for add balance:\n Press 3 for remove balance:\n"))
    
    if choice == 1:
        name=input("Enter name of the customer:")
        
        while True:
            acc_no=input("Enter account no of the customer:")
            re = Check_Details(acc_no)
            if re == 1:
                print("Account no is already assined!")
                continue
            elif re == 0:
                break
                
        balance = input("Enter the balance of the customer:")
        
        customer.append(name + "," + acc_no + "," + balance)
        print(customer)
        
        
    elif choice == 2:
        acc_no= int(input("Enter the account no of customer:"))
        balance=int(input("Enter amount to add:"))
        add_balance(acc_no,balance)
        
        
    elif choice == 3:
        acc_no= int(input("Enter the account no of customer:"))
        balance=int(input("Enter amount to remove:"))
        remove_balance(acc_no,balance)
        
    else:
        print("Invalid input")