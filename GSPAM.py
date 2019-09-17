import smtplib
import getpass
import time


ENDC = '\033[m'
TCYAN =  '\033[36m'
TYELL = '\033[33m'
TRED = '\033[31m'
print(TCYAN + "[*] Welcome To SheZco's Gspammer", ENDC)
print(TRED + "[*] Please Use For Educational Purposes only")

print('''             . . .
              \|/
            `--+--'
              /|/
             ' | '
               |
               |
           ,--'#`--.
           |#######|
        _.-'#######`-._
     ,-'###############`-.
   ,'#####################`,
  /#########################/
 |###########################|
|#############################|
|#############################|
|#############################|
|#############################|
 |###########################|
  \#########################/
   `.#####################,'
     `._###############_,'
        `--..#####..--'

------------------------------------------------
 ''')

user = input("[!] Enter your gmail: ")
passwd = getpass.getpass("[!] Enter your pass: ")


counter = 1
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, passwd)
    print("Successfully Logged In as " + user)

except:
    print("Wrong Password Or Gmail... password was " + passwd)

target = input("[!] Enter Target gmail: ")
subj = input("[?] Subject: ")
msg = input("[?] Message: ")

while True:
    try:
        counter += 1
        server.sendmail(user, target, msg, subj)
        print(TYELL + "Succesfully sent %s " % counter)
    except:
        print("Cant send")
        quit()
