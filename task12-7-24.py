#1) GLOBAL AND LOCAL VARIABLES: 
ac='CENTRALIZED AC'
def livingroom():
    global ac
    print('The living room has a ',ac)
def bedroom():
    ac='2 ton ac'
    print(' The bedroom has a ',ac)
def kitchen():
    fan_no=2
    print('No of fans:',2)

livingroom()
bedroom()
kitchen()

#2)BANKING :
total=10000
def deposit():
    cash=int(input('Enter the amount to be deposited in your account:'))
    print('DEPOSITED Amount = ',cash)
    final=total+cash
    print('Total amount:',final)
    
def withdrawal():
    transactionamt=int(input('ENTER THE AMOUNT TO BE WITHDRAWED:'))
    if transactionamt>total:
        print('Sorry, the transaction has failed due to insufficient balance amount')
    else:
        c=total - transactionamt
        print('amount withdrawed:' , transactionamt)
        print('net balance:',c)
def show_balance():
    print('The net balance is: ',total)
def exit():
    print('THANK U')

print('WELCOME TO THE BANK!!')
op= input('what would you like to do: 1) DEPOSIT , 2) WITHDRAW ,3) CHECK BALANCE ,4)EXIT : ')
if op=='DEPOSIT':
    deposit()
elif op=='WITHDRAW':
    withdrawal()
elif op=='CHECK BALANCE':
    show_balance()
elif op=='EXIT':
    exit()
            
    

    
