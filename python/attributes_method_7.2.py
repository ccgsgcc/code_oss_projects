class Robot():
    
    def __init__(self):
        self.name = 'R2D2'
        
    def hello(self):
        print('Привет!, меня зовут -', self.name)
    
    def go(self, x, y):
        print('Иду в точку ', x, y)
        
robot = Robot()
robot.go(x=100, y=200)
# robot.temperature = 1

# while robot.temperature < 10:
#     robot.temperature += 2
# print(robot.temperature)   
# # del robot.temperature
# # print(robot.temperature)  
# # можно удалять объекты

# robot_2 = Robot()
# robot_2.name = 'ВАЛЛИ'

# print(robot.name, robot_2.name)
# print(robot, robot_2)
# #если не писать атрибут переменной ,
# #то будет выведено адрес памяти переменной

# print(robot_2 == robot, robot is robot_2)
#проверка является ли правдой имя 1 робота вторым 1 
# robot = Robot()
# robot.hello()

# some_var = robot
# robot.hello()

# some_robot = some_var
# some_robot.hello()

# some_robot.name = 'CPPP'
# some_robot.hello()

# robot.hello()
# #значение(имя) изначальное робота изменится

attr_name = 'model'
if hasattr(robot, attr_name):
    print(robot.model)
    #hasattr(object, name) - проверка существования 
else:
    setattr(robot, attr_name, 'android')
    #setattr(object,name,value) - установка

print(getattr(robot, attr_name)) #после присвоении 
#через setattr , мы получаем через getattr значении
#
# удалить атрибут attr_name из robot
print(robot.model)
# delattr(robot, attr_name) #удаление 
for attr_name in ('weight', 'height', ):
    setattr(robot, attr_name, 42)
print(hasattr(robot, 'weight'))
print(getattr(robot, 'weight'))


