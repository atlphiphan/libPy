import random

print("Player 1? ")
name1 = input("> ")
print("Player 2? ")
name2 = input("> ")
print("Player 3? ")
name3 = input("> ")
print("Player 4? ")
name4 = input("> ")

players = [name1,name2,name3,name4]
c1= 0
c2= 0
c3= 0
c4= 0
num_weeks = 1

while num_weeks < 11 and len(players) >= 2:
  chosen = random.sample(players, 2)
#  print("Week %s " % num_weeks + "players " + ', '.join(chosen))
  print("%s" % num_weeks + ": " + ', '.join(chosen))

  if name1 in chosen:
    c1 += 1
  if name2 in chosen:
    c2 += 1
  if name3 in chosen:
    c3 += 1
  if name4 in chosen:
    c4 += 1

  if c1 == 5 and name1 in chosen:
    players.remove(name1)
  if c2 == 5 and name2 in chosen:
    players.remove(name2)
  if c3 == 5 and name3 in chosen:
    players.remove(name3)
  if c4 == 5 and name4 in chosen:
    players.remove(name4)

  num_weeks +=1
  continue