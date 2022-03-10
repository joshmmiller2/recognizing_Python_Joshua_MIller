num1 = 42 #variable declaration
num2 = 2.3
boolean = True #data type
string = 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #string declared
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))  #print function
print(pizza_toppings[1]) #print function
pizza_toppings.append('Mushrooms') #append function add mushroom to list
print(person['name']) #print function
person['name'] = 'George' #change first name to george
person['eye_color'] = 'blue' #change eye color to blue
print(fruit[2]) #print function to show banana

if num1 > 45: # if statement
    print("It's greater")
else:
    print("It's lower") # else statement

if len(string) < 5:
    print("It's a short word!") #if statement print function
elif len(string) > 15:
    print("It's a long word!") #elif statement print function
else:
    print("Just right!") #else statement print function

for x in range(5):
    print(x) #print function
for x in range(2,5):
    print(x) #print function
for x in range(2,10,3):
    print(x) #print function
x = 0
while(x < 5):
    print(x) #print function
    x += 1

pizza_toppings.pop() #remove element
pizza_toppings.pop(1) #remove element

print(person) #print function
person.pop('eye_color')
print(person) #print function 

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement') #print function
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello') #print function

print_hello_ten_times() #print function

def print_hello_x_times(x):
    for num in range(x):
        print('Hello') #print function

print_hello_x_times(4) #print function

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello') #print function

print_hello_x_or_ten_times() #print function
print_hello_x_or_ten_times(4) #print function