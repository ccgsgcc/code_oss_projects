class Toyota:
    
    def __init__(self):
        self.color = "blue"
        self.price = "1 000 000 000"
        self.max_velocity = "200 км.ч"
        self.engine_rpm = 0
        
    def start(self):
        print("поехали")
        self.engine_rpm = 900
        
    def go(self):
        print("go,go,go")
        self.engine_rpm = 2000
        self.current_velocity = "20 км в час"

my_car = Toyota()

print('color', my_car.color)
print('velocity', my_car.max_velocity)
print('price', my_car.price)
print('engine rpm', my_car.engine_rpm)

my_car.start()
print("Машина завелась")
print('rpm', my_car.engine_rpm)
my_car.go()
print('Current_velocity', my_car.current_velocity)

#класс как лекало для производства объектов

# produced, plan = 0
# stock = []
# while produced < plan:
#     new_car = Toyota()
#     stock.append(new_car)
#     produced += 1

class Robot():
    
    def __init__(self):
        self.name = 'R2D2'
        
    def hello(self):
        print('Привет!, меня зовут -', self.name)
    
robot = Robot()
robot.hello()

some_var = robot
robot.hello()

some_robot = some_var
some_robot.hello()

some_robot.name = 'CPPP'
some_robot.hello()

robot.hello()
#значение(имя) изначальное робота изменится
