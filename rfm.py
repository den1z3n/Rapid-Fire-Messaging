#!/usr/bin/python3

print('''
##############################
#### Rapid Fire Messaging ####
##############################
''')

# Program Author: z3n



import sys, socket, getpass, smtplib





## Text Menu 1

def print_menu1():       ## Menu Design
    print(30 * "-" , "M A I N - M E N U" , 30 * "-")
    print("1. Start")
    print("2. Exit")
    print(79 * "-")





while True:
    print_menu1()    ## Displays Menu 1

    # Error Handling - print_menu1
    def is_number(s):
     while s.isdigit() == False:
        s = input("Choose From Menu Options [1-2]: ")
     return int(s)
    choice = is_number(input("Enter Your Choice [1-2]: "))





    if choice == 1:

     # Enter SMTP Relay E-Mail & Service Address
     while True:
         try:
            username = input("Enter E-Mail: ")
            password = getpass.getpass(prompt="Enter E-Mail Password: ")
            obj = smtplib.SMTP(input("Enter smtp.domain.tld:port#: "))

            obj.starttls()
            obj.login(username, password)
            break

         # Error Handling - Disconnected
         except smtplib.SMTPServerDisconnected:
          print("Disconnected.")

         # Error Handling - Authentication Error
         except smtplib.SMTPAuthenticationError:
          print("Authentication Error")

         # Error Handling - Name or Service Not Known
         except socket.gaierror:
          print("Name or Service Not Known.")

         # Error Handling - Connection Refused
         except socket.error:
          print("Connection Refused.")




     ## Text Menu 2

     def print_menu2():  # Menu Design
        print(25 * "-", "M E S S A G I N G - M E N U", 25 * "-")
        print("1. E-Mail")
        print("2. SMS")
        print("3. Exit")
        print(78 * "-")





     while True:
         print_menu2()  # Displays Menu 2

         # Error Handling - print_menu2
         def is_number(s):
          while s.isdigit() == False:
             s = input("Choose From Menu Options [1-3]: ")
          return int(s)
         choice = is_number(input("Enter Your Choice [1-3]: "))





         if choice == 1:

          ##E-Mail Rapid Fire Messaging##

          # Enter Target Email Address
          email = input("Enter Target E-Mail: ")
          message = input("Message: ")
          email_message = (" \r\n\r\n From: %s\r\n To: %s\r\n\r\n  %s"
          % (username, "".join(email), "".join(message)))





          while True:
              try:
                  obj.sendmail(username, email, email_message)
                  print("Message sent! Sending another...Press Ctrl+C to stop.")

                  continue

              # Error Handling - Connection Unexpectedly Closed
              except smtplib.SMTPServerDisconnected:
               print("Connection Unexpectedly Closed")

              # Error Handling - Failed Attempt
              except smtplib.SMTPRecipientsRefused:
               print("Failed Attempt")

              # Error Handling - CTRL+C
              except KeyboardInterrupt:
               print("Stopped.")
              break





         elif choice == 2:

          ##SMS Rapid Fire Messaging##

          carrier = 0

          # Enter SMS Target
          carrier = input("Enter @carrier: ")

          phone = input("Enter Phone Number: ") + str(carrier)
          message = input("Message: ")
          phone_message = ("From: %s\r\nTo: %s \r\n\r\n %s"
          % (username, "".join(phone), "".join(message)))





          while True:
              try:
                  obj.sendmail(username, phone, phone_message)
                  print("Message sent! Sending another...Press Ctrl+C to stop.")
                  continue

              # Error Handling - Connection Unexpectedly Closed
              except smtplib.SMTPServerDisconnected:
               print("Connection Unexpectedly Closed")

              # Error Handling - Failed Attempt
              except smtplib.SMTPRecipientsRefused:
               print("Failed Attempt")

              # Error Handling - CTRL+C
              except KeyboardInterrupt:
               print("Stopped.")

              # Error Handling - Try Again
              except smtplib.SMTPDataError:
               print("Try Again.")
              break





         elif choice == 3:
          print("Exiting")
          break

         else:
          print("Choose From Menu Options")





    elif choice == 2:

            ##Exit Rapid Fire Messaging##

            print("Exiting Rapid Fire Messaging")
            sys.exit()





    else:
     print("Choose From Menu Options")
