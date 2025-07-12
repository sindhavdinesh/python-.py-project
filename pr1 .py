print("welcome to introdaction")

name=input("please enter your name:")
age=int(input("please enter your age:"))
height=(float(input("please enter your height:")))
favorite_number=int(input("please enter your favorite number:"))
print("")
print("thank you for using the personal data collector.goodbye!")
print("")
print("name:",name,"type:",type(name),"memory address:",id(name))
print("age:",age,"type:",type(age),"memory address:",id(age))
print("height:",height,"type:",type(height),"memory address:",id(height))
print("favorite_number:",favorite_number,"type:",type(favorite_number),"memory address:",id(favorite_number))

import datetime

age=int(input("how old are you?"))
current_year=datetime.datetime.now().year
birth_year=current_year - age
print("you were born in",birth_year)



      
      
    '''  
      
      

        welcome to introdaction
please enter your name:dinesh
please enter your age:18
please enter your height:145
please enter your favorite number:145

thank you for using the personal data collector.goodbye!

name: dinesh type: <class 'str'> memory address: 2274411794800
age: 18 type: <class 'int'> memory address: 140718508230088
height: 145.0 type: <class 'float'> memory address: 2274372130032
favorite_number: 145 type: <class 'int'> memory address: 140718508234152
how old are you?18
you were born in 2007
'''            
