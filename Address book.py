
def my_func(run):
  option=raw_input("Do you want to continue Y/N:")
  if option == "y" or option == "Y" :
   return 6
  else:
    exit()

run = True
while run:
 print "ADDRESS BOOK"
 print "\n\t\t1.Create address book"
 print "\n\t\t2.Append address book"
 print "\n\t\t3.View address book"
 print "\n\t\t4.Quit"
 choice=input("\n\tEnter a choice:")
 while choice<5:
        #get file choice from user
        if choice == 1:
            #create file
            a_name=raw_input("Enter the Address_book name:")
            f= open(a_name + ".txt","w+")
            name=raw_input("Enter the name:")
            address=raw_input("Enter the address:")
            phone=input("Enter the Phone number:")
            mail=raw_input("Enter the Mail id:")
            f.write("\tName:%s" % name)
            f.write("\n\tAddress:%s" % address)
            f.write("\n\tPhone number:%d" % phone)
            f.write("\n\tMail id:%s" % mail)
            f.close() 
            my_func(run)
        elif choice == 2:
            #append file
            a_name=raw_input("Enter the Address_book name to append:")
            f= open(a_name + ".txt","a+")
            name=raw_input("Enter the name:")
            address=raw_input("Enter the address:")
            phone=input("Enter the Phone number:") 
            mail= raw_input("Enter the Mail id:")
            f.write("\n\n\tName:%s" % name)
            f.write("\n\tAddress:%s" % address)
            f.write("\n\tPhone number:%d" % phone)
            f.write("\n\tMail id:%s" % mail)
            f.close()
            my_func(run)
        elif choice == 3:
            #View file
            a_name=raw_input("Enter the Address_book name to view:")
            f= open(a_name + ".txt","r+")
            print f.read()
            f.close()
            choice = my_func(run)
        elif choice == 4:
            #exit
            exit()
