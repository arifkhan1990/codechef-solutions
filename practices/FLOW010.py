T = int(input())

classM = {'b': 'BattleShip', 'c': 'Cruiser', 'd': 'Destroyer', 'f': 'Frigate'}

for _ in range(T):
  c = str(input())
  print(classM[c.lower()])