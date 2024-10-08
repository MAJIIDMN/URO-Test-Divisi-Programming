from numpy import random

class Robot:
  def __init__(self, MAXDAMAGE, HP):
    self.MAXDAMAGE = MAXDAMAGE
    self.HP = HP
UNOBOT = Robot(200, 1500)
MADBOT = Robot(100, 3000)
MEGABOT = Robot(150, 2000)
class Game:
class Battle:
  def Start_Battle():
    print("Battle Start!")
    a = 0
    while 1>a:
      rob1.Damage = random.randint(rob1.MAXDAMAGE)
      rob2.Damage = random.randint(rob2.MAXDAMAGE)
      print(rob1_name,"Attacks", rob2_name, "for", random.randint(rob1.MAXDAMAGE), "Damage!!")
      print(rob2_name,"Attacks", rob1_name, "for",  random.randint(rob2.MAXDAMAGE), "Damage!!")
      rob1.HP = rob1.HP - rob2.Damage
      if rob1.HP <= 0:
        a = 1
        print(rob2_name,"DEFEATED!!")
        print(rob1_name,"WIN THE GAME!!")
      rob2.HP = rob2.HP - rob1.Damage
      if rob2.HP <= 0:
        a = 1
        print(rob1_name,"DEFEATED!!")
        print(rob2_name,"WIN THE GAME!!")
print("="*41) 
print("="*5,"Choose robots for the battle:","="*5)
print("="*41) 
print("1. UNOBOT")
print("2. MADBOT")
print("3. MEGABOT")
print("="*41) 
First = int(input("Select First Robot :"))
Second = int(input("Select Second Robot :"))
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
print("="*41) 
print(rob1_name,"Max HP",rob1.HP)      
print(rob2_name,"Max HP",rob2.HP)
print("="*41) 
print(rob1_name,"Max DAMAGE",rob1.MAXDAMAGE)      
print(rob2_name,"Max DAMAGE",rob2.MAXDAMAGE)
print("="*41) 
Battle.Start_Battle()
