from numpy import random 	##untuk menggunakan fungsi random pada modul numpy

##membuat class yang berisi atribut robot
class Robot: 	
  def __init__(self, MAXDAMAGE, HP): 	##inisialisasi variabel atribut
    self.MAXDAMAGE = MAXDAMAGE
    self.HP = HP

##membuat data robot
UNOBOT = Robot(200, 1500)
MADBOT = Robot(100, 3000)
MEGABOT = Robot(150, 2000)

##membuat class untuk menjalankan perang antar robot
class Battle:	
  def Start_Battle(): 
    print("Battle Start!")
    a = 0

##membuat perulangan untuk battle
    while 1>a:

##dmg robot random sesuai max dmg

      rob1.Damage = random.randint(rob1.MAXDAMAGE)
      rob2.Damage = random.randint(rob2.MAXDAMAGE)
      print(rob1_name,"Attacks", rob2_name, "for", random.randint(rob1.MAXDAMAGE), "Damage!!")
      print(rob2_name,"Attacks", rob1_name, "for",  random.randint(rob2.MAXDAMAGE), "Damage!!")

##healt point robot berkurang sesuai dmg yang diterima
      rob1.HP = rob1.HP - rob2.Damage
      if rob1.HP <= 0:
        a = 1	##saat HP salah satu robot = 0, ubah parameter perulangan untuk menghentikan battle
        print(rob2_name,"DEFEATED!!")
        print(rob1_name,"WIN THE GAME!!")
      rob2.HP = rob2.HP - rob1.Damage
      if rob2.HP <= 0:
        a = 1
        print(rob1_name,"DEFEATED!!")
        print(rob2_name,"WIN THE GAME!!")

#buat tampilan daftar Robot
print("="*41) 
print("="*5,"Choose robots for the battle:","="*5)
print("="*41) 
print("1. UNOBOT")
print("2. MADBOT")
print("3. MEGABOT")
print("="*41) 

##input dua robot yang dipilih untuk battle
First = int(input("Select First Robot :"))
Second = int(input("Select Second Robot :"))

##bagi kasus tiap pilihan 
print("="*41) 
if First == 1:
  print("First Robot is UNOBOT")
  rob1 = UNOBOT
  rob1_name = "UNOBOT"
elif First == 2:
  print("First Robot is MADBOT")
  rob1 = MADBOT
  rob1_name = "MADBOT"
elif First == 3:
  print("First Robot is MEGABOT")
  rob1 = MEGABOT
  rob1_name = "MEGABOT"
else:
  print("EROR")
if Second == 1:
  print("Second Robot is UNOBOT")
  rob2 = UNOBOT
  rob2_name = "UNOBOT"
elif Second == 2:
  print("Second Robot is MADBOT")
  rob2 = MADBOT
  rob2_name = "MADBOT"
elif Second == 3:
  print("Second Robot is MEGABOT")
  rob2 = MEGABOT
  rob2_name = "MEGABOT"
else:
  print("EROR")

##Display HP awal robot yang dipilih
print("="*41) 
print(rob1_name,"Max HP",rob1.HP)      
print(rob2_name,"Max HP",rob2.HP)

##Display MAX DAMAGE robot yang dipilih
print("="*41) 
print(rob1_name,"Max DAMAGE",rob1.MAXDAMAGE)      
print(rob2_name,"Max DAMAGE",rob2.MAXDAMAGE)
print("="*41) 

##jalanan Fungsi Battle untuk melakukan battle antar Robot
Battle.Start_Battle()

##SELESAI