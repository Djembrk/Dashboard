import telnetlib
import time

tel = telnetlib.Telnet("localhost",  23, timeout = 2) #Creation de l'objet tel
tel.open("localhost" , 23) # ouverture de la connexion en local sur le port 23

tel.read_until(b"Username:") #lire jusqu'a Username
tel.write(("Identifiant").encode('ascii') + b"\n") #ecrit l'Username

tel.read_until(b"Password:") #lire jusqu'a Password
tel.write(("Mot de passe ").encode('ascii') + b"\n") #ecrit le password 

time.sleep(5)
tel.read_until(b">") #Lire jusqu'au prompt 
tel.write(("dir").encode('ascii') + b"\n") # ecrit dir

print(tel.read_eager().decode('ascii')) # affiche le résultat de la commande "dir"

tel.close() # ferme la connexion 