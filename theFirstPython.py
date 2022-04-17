# Test
print(2+3)
print('Hello World')

#1. Variable
score = 0
print('score')
print(score)
score = 10
print(score)
score = 20
print(score)

#2. Data Type
## Int
level = 1
print(type(level))

## Float
angle = 35.45
print(angle)
print(type(angle))

## Str
name = 'Jonathan'
print(name)
print(type(name))

## Bool
sound = True
print(sound)
print(type(sound))

#3. List
names = []
name = input('Enter name:')
names.append(name)
print(names)

name = 'Tom'
names.append(name)
print(names)

name = 'Jane'
names.append(name)
print(names)

print(names[1])
print(names[0])
print(names[-1])
print(names[0:2])
print(names[1:])
print(len(names))
print(names.index('Jane'))
names[1] = 'Jimmy'
print(names)

scores = [100, 90, 70]
highscores = [names, scores]
print(highscores)
highscores[0][0]
highscores[1][0]

#4. Dictionary
stationfares = []
dic = {}
station = input('Enter station : ')
fare = int(input('Enter fare : '))
dic['station'] = station
dic['fare'] = fare
stationfares.append(dic)
print(dic)
print(stationfares)

dic = {}
station = '성북'
fare = 2000
dic['station'] = station
dic['fare'] = fare
stationfares.append(dic)
print(dic)
print(stationfares)

print(stationfares[0])
print(dic.keys())
print(dic.values())

#5. Condition
name = input('What is your name : ')

if name == 'bird':
      print("I could fly to you")
else:
  print("I could walk to you")

if name == 'bird':
      print("I could fly to you")
elif name == 'pig':
  print("I could walk to you")
else:
  print("I could stay to you ")
  
#6. Loop
num = int(input('Multiplication table of : '))

for i in range(1, 10):
  print(num, 'X', i, '=', num*i)
  
for i in range(2, 10):
      for j in range(1, 10):
        print('%2d X %2d = %5d' %(i, j, i*j))
print('-----------------')
  
num = int(input('Multiplication table of : '))
i = 1
while i < 10:
  print(num, 'X', i, '=', num*i)
  i += 1

i = 2
while i < 10:
  j = 1
  while j < 10:
   print("%2d X %2d = %5d" %(i, j, i*j))
   j += 1
  print('-----------------')
  i += 1

stationfares = [
                {"station": "청량리", "fare": "1500"},
                {"station": "성북", "fare": "1800"},
                {"station": "의정부", "fare": "2000"},
                {"station": "소요산", "fare": "2500"}
]

stations = []
fares = []
for stationfare in stationfares:
  stations.append(stationfare["station"])
  fares.append(stationfare["fare"])
print(stations)
print(fares)

#7. Function
print(len(stationfares))
print(max(fares))
print(min(fares))
print(sum(fares))

for idx, station in enumerate(stations):
  print(idx, station)

sum = lambda a, b : a+b
sum(2,3)

def getFare(station):
      for stationfare in stationfares:
        if stationfare['station'] == station:
            return stationfare['fare']
  
fare = getFare("청량리")
print(fare)

for station in stations:
  print(station, getFare(station))