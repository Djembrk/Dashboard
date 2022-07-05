import telnetlib
import time

tel = telnetlib.Telnet("localhost",  23, timeout = 2) #Creation de l'objet 
tel.open("localhost" , 23)

tel.read_until(b"Username:") #lire jusqu'a Username
tel.write(("1234").encode('ascii') + b"\n") #ecrit l'Username

tel.read_until(b"Password:") #lire jusqu'a Password
tel.write(("1234").encode('ascii') + b"\n") #ecrit le password 

time.sleep(5)
tel.read_until(b">")
tel.write(("dir").encode('ascii') + b"\n")

print(tel.read_eager().decode('ascii'))

tel.close()