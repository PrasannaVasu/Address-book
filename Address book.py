run = True
while run:
 print "ADDRESS BOOK"
 print "\n\t\t1.Create address book"
 print "\n\t\t2.Append address book"
 print "\n\t\t3.Quit"
 choice=input("\n\tEnter a choice:")
 while choice<4:
        #get file choice from user
        if choice == 1:
            #create file
            f= open("Address book.txt","w+")
            name=raw_input("Enter the name:")
            address=raw_input("Enter the address:")
            phone=input("Enter the Phone number:")
            mail=raw_input("Enter the Mail id:")
            f.write("\tName:%s" % name)
            f.write("\n\tAddress:%s" % address)
            f.write("\n\tPhone number:%d" % phone)
            f.write("\n\tMail id:%s" % mail)
            f.close() 
            break
        elif choice == 2:
            #append file
            f= open("Address book.txt","a+")
            name=raw_input("Enter the name:")
            address=raw_input("Enter the address:")
            phone=input("Enter the Phone number:") 
            mail= raw_input("Enter the Mail id:")
            f.write("\n\n\tName:%s" % name)
            f.write("\n\tAddress:%s" % address)
            f.write("\n\tPhone number:%d" % phone)
            f.write("\n\tMail id:%s" % mail)
            f.close()
            break
        elif choice == 3:
            #exit
            exit()

 