""" please go through the docs before running this scripts """

from twilio.rest import Client

print("\n" + " *****        WELCOME TO AUTOMATED PYTHON MESSAGING SCRIPT       ***** ")
print(" *****  PLEASE CREATE A TWILIO ACCOUNT BEFORE USING THE SCRIPT ***** ")
print(" *****      TO CREATE TWILIO ACCOUNT GO TO WWW.TWILIO.COM      ***** ")
print(" *****            TYPE 'YES/yes'  IF YOU WANT TO PROCEED       ***** "+'\n')
i = input()
print("\n")


if (i == "YES" or i == "yes"):
    account_sid = input(" ENTER YOUR TWILIO ACCOUNT-SID ")
    auth_token  = input(" ENTER YOUR TWILIO AUTH-TOKEN  ")
    
    client = Client(account_sid,auth_token)
     
    print("**** press 1 for single phone number    *****")
    print("**** press 2 for multiple phone numbers *****")
    i = int(input())

    if (i == 1):
        print(" ***** PLEASE ENTER RECIEVER's NUMBER **note mention your country code followed by '+' *****")       
        number = int(input())
        print(" ***** PLEASE ENTER YOUR SID *****")
        my_sid = input()
        print(" ENTER YOUR MESSAGE ")
        msg = input()
        """ client.message.create will be responsible for the sending the message
            also here messaging_service id is the id that you got from twilio     
            
            'to' attribute specifies whom you want to send the message
            'body' attribute specifies what message you want to send
        """
        message = client.messages.create(  
                              messaging_service_sid=my_sid, 
                              body=msg,      
                              to=number
        ) 
        print(" msg sent ")
    
    if (i == 2):
        print(" ***** PLEASE ENTER RECIEVER's NUMBER **note mention your country code followed by '+' *****")       
        number = list(int (i) for i in input().strip().split(' '))
        print(" ***** PLEASE ENTER YOUR SID *****")
        my_sid = input()
        print(" ENTER YOUR MESSAGE ")
        msg = input()
        """ client.message.create will be responsible for the sending the message
            also here messaging_service id is the id that you got from twilio     
            
            'to' attribute specifies whom you want to send the message
            'body' attribute specifies what message you want to send
        """
        for i in number:
            message = client.messages.create(  
                              messaging_service_sid=my_sid, 
                              body=msg,      
                              to=number
            ) 
            print(" call success to the number " + str(i))




    

   