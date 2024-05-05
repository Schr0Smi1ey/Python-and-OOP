from Bank import *
from User import *
from Admin import *

janata = Bank('Janata Bank Limited','JanataBank@gmail.com','Dhaka')
admin = Admin('Sarafat','KarimSarafat@gmail.com','test','Khulna')

jabbar = admin.createAccount('Jabbar','jabbar@email.com','dkfa','Dhaka','Savings')
Karim = admin.createAccount('Karim','karim@gmail.com','fhfa','Dhaka','Savings')
Rahim = admin.createAccount('Rahim','Rahim@proton.mail','fff','Khulna','Current')
Tanvir = admin.createAccount('Tanvir','Tanvir@yahoo.com','ffff','Jasshore','Savings')
Rian = admin.createAccount('Rian','Rian@yahoo.com','aerf','Jamalpur','Current')
Nayeem =  admin.createAccount('Nayeem','Nayeem@yahoo.com','hfhaf','Shoriyatpur','Savings')