import random, os, time

def rolldice(side):
  result=random.randint(1,side)
  return result

def health():
  healthstat=(rolldice(6)*rolldice(12))/2+10
  return healthstat
def strength():
  strengthstat=(rolldice(6)*rolldice(8))/2+12
  return strengthstat
while True:
  print("Character Builder")
  print()
  name=input("name your Legend")
  type=input("Type: human,elf,ogre,warlock,priest:")
  print()
  print(name)
  print("health:",health())
  print("stregnth:",strength())
  print()
  print("Go down in history legendary warrior.")
  print()
  again=input("Create another?")
  if again=="no" or again=="no":
    break
time.sleep(1)
os.system("clear")

  
  