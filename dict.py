car ={
    'brand':'Toyota',
    'model':'spider',
    'year':2020,
    'color':['white','red','black']
}
print(car)
print(car['brand'])
print(car.get('color'))
print(car.keys())
car['year']=2023
print(car)
print(car.values())
print(car.items())

if 'color' in car:
    print(True)

car.update({'engines':'V6'})
print(car)
# car.pop('color')
# print(car)
# car.popitem()
# print(car)
# car.clear()
# print(car)
# del car
# print(car)

for x in car:
    print(x)

for x in car:
    print(car[x])

carr = {'brand':'lexus'}
carr = car.copy()
print(car)

cars = dict(carr)
print(cars)

python_class = {
    'student1':{
        'name':'john',
        'age': 8,
        'course': 'Ethical hacking',
        'complexion': 'caramel',
    },
    'student2':{
        'name': 'Mummy Happy',
        'age': 40,
        'course': 'Data science',
        'complexion': 'dark', 
    },
    'student3':{
        'name': 'justina',
        'age': 12,
        'course': 'AI',
        'complexion': 'fair', 
    },
    'student4':{
        'name': 'ifeanyi',
        'age': 11,
        'course': 'Cyber Security',
        'complexion': 'white', 
    },
    'student5':{
        'name': 'Re Re',
        'age': 14,
        'course': 'Cyber Security',
        'complexion': 'dark', 
    },
    'student6':{
        'name': 'Chigaemezu',
        'age': 6,
        'course': 'Marketing',
        'complexion': 'caramel', 
    },
    'student7':{
        'name': 'Eyong',
        'age': 22,
        'course': 'Money',
        'complexion': 'caramel', 
    },
    'student8':{
        'name': 'Eyong',
        'age': 22,
        'course': 'Money',
        'complexion': 'caramel', 
    }

}

# print(python_class)
# print(python_class['student7'])
# print(python_class['student7']['name'])
print(python_class.items())
for x in python_class.items():
    print(x)