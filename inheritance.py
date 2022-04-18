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
  fares.append(int(stationfare["fare"]))
print(stations)
print(fares)

class Comments:
  title               = "#### %s 승차권 판매기입니다. ####"
  product_description = "%s:%s(%s원)"
  insert_fare         = "\n요금을 넣어 주세요. : "
  insufficient_fare   = "%s 요금이 부족합니다. 거스름돈은 %s원 입니다."
  select_station      = "원하시는 역 번호를 선택하세요. : "
  select_error        = "잘못 입력하셨습니다."
  finish_sale         = "선택하신 역은 %s 입니다. 거스름돈은 %s 원 입니다. \n감사합니다."
  terminate_sale      = "승차권 판매를 종료합니다."

class Products:
  productNames = []
  productValues = []

class SubwayTicket(Products):
  _data = stationfares
  _name = "지하철"
  _status = True
  
  def __init__(self):
      print(Comments.title %self._name)
  
  def set_products(self):
    Products.productNames = []
    Products.productValues = []
    for stationfare in self._data:
      Products.productNames.append(stationfare['station'])
      Products.productValues.append(stationfare['fare'])

  def run(self):
    self.set_products()
    while self._status:
      try:
        inputMoney = int(input(Comments.insert_fare))
      except ValueError:
          print(Comments.select_error)
      else:
        self.selectStation(inputMoney)

  def selectStation(self, money):
    print(Comments.select_station)
    for idx, name in enumerate(Products.productNames):
      fare = Products.productValues[idx]
      print(Comments.product_description %(str(idx), name, fare))
    inputStation = int(input(Comments.select_station))
    self.payment(money, inputStation)

  def payment(self, money, idx):
    name = Products.productNames[idx]
    fare = Products.productValues[idx]
    if money >= int(fare):
      balance = money - int(fare)
      print(Comments.finish_sale %(name, str(balance)))
    else:
      print(Comments.insufficient_fare %(name, str(money)))
      
tm = SubwayTicket()
try:
  tm.run()
except KeyboardInterrupt:
  tm._status = False
  print(Comments.terminate_sale)
  
#3. Inheritance
railstationfares = [
                    {"station": "천안", "fare": 15000},
                    {"station": "대전", "fare": 20000},
                    {"station": "동대구", "fare": 37000},
                    {"station": "부산", "fare": 53000}
]

class RailTicket(SubwayTicket):
  _data = railstationfares
  _name = "고속철도"

tm = RailTicket()
try:
  tm.run()
except KeyboardInterrupt:
  tm._status = False
  print(Comments.terminate_sale)