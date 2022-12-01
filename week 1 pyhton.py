print("hello world")
print('hello world')
print("hello 'hello' world")
print("I'm zaid")
print("hello \"world\" world")
print('I\'m zaid')
# \n is for new line
print("line A\nline B \n line C")
# \t is for tab
print("name\tZaid")
print("this is backslash \\")
# \\ is for backslash
print("this is backslash \\\\")
print("hell\blo")
# this is comment

# output: Line A \n Line B
print("Line A \\n Line B")
print("Line B \\t Line B")
print("this is double backslash \\\\\\\\")

# output: \" \'
print(" \\\" \\\' ")
#\' = '
# \\ = \
# \\\' = \'

#this is \\ double backslash
print("this is \\\\ double backslash")

# this is /\/\/\/\/\ mountain
print("this is /\\/\\/\\/\\/\\ mountain")

#he is    awesome
print("he is\tawesome")

# \" \n \t \'
print(" \\\" \\n \\t \\\' ")

# by putting r we can treat \n as normal.
print(r"line A \n line B")

#print emoji in python(replace + with 000 and add blackslash at starting)
print("\U0001F602")
print("\U0001F604")
print("\U0001F618")

#python as calculator
print(2+3*4)
print(2/4)
print(4/2) #floating point divison
print(4//2) #integer divison
print(2//4)
print(2**3) #power
print(2**0.5) #square root
print(round(2**0.5, 4)) #round off
print(2**3/2*6-4*(3-4/2))
print((2+3)*2) #2+3=5 then 5*2
print((2+3)*5/2%6) #5*5 /2 %6 = 25/2%6

#exponents
print(2**3**2) #2**9

#variables
number1 = 2
print(number1)
number1 = 4
print(number1)

# we can store string , number in variable
name="zaid"
print(name)
name=123
print(name)

#rule we can't start variable with number (1number=4).we can start with letter,_ ......first letter
_name="zaid"
print(name)
user_one_name="Rohit" #snake case writing
userOneName="Mohit" #camel case writing

#strings
first_name="zaid"
last_name="kazmi"
full_name=first_name+" "+last_name
print(full_name)
print(full_name+str(3)) #no error
#print(full_name+3) error
print(first_name*3)

#user input
#input function
name=input("type your name")
print("hello " + name)

#string
age=input("what is your age ?") #24, "24"
print("your age is " + age)

#int() function
number_one=int(input("enter first number"))
number_two=int(input("enter second number"))
total=number_one+number_two
print("total is "+ str(total))

#str 4-->"4"
#int 4-->4
#float "4"-->4.0
number1 = str(4)
number2 = float("44")
number3 = int("33")
print(number2 + number3)#final answer float

name, age="zaid", "19"
print("hello" + name +  "your age is" + age)

x=y=z=1
print(x+y+z)

#two or more inputs in one line in python
name, age = input("enter your name and age").split(",")
print(name)
print(age)

#string formatting
name="zaid"
age="19"
print("hello" + name +  "your age is" + str(age)) #ugly syntax

print("hello {} your age is {} ".format(name,age)) #python 3
print(f"hello {name} your age0 is {age}") #clean syntax python 3.6

#avg of three numbers
num1=input("enter first number: ")
num2=input("enter second number: ")
num3=input("enter third number: ")
#(int(num1)+int(num2)+int(num3))/3
print(f"average of three numbers : {(int(num1)+int(num2)+int(num3))/3}")

#string indexing
language="python"
#positions(index number)
#p=0,-6 y=1,-5 t=2,-4 h=3,-3 o=4,-2 n=5,-1
print(language[4])
print(language[-4])

#string slicing
lang="Python"
#syntax- [start argument : stop argument] increase a number in stop argument for example if you want to print Py it should contain 0:2
print(lang[0:2])
print(lang[-3:6])
print(lang[:])

#step argument
print("Zaid"[0:2])
print("zaid"[0::2])
print("zaid"[5::-1]) #reverse
print("zaid"[-1::-1]) #reverse
print("zaid kazmi"[::-1]) #reverse

#string methods
name="ZaId kAzMi"
#1. len() function
print(len(name)) #also counts spaces btw two words
#2. lower() method
print(name.lower())
#3. upper() method
print(name.upper())
#4. title() method
print(name.title()) #makes 1st alphabet capital
#5. count() method
print(name.count("a"))

#Question
#take two comma separated inputs from user
#1.) users name
#2) a single character
#output - 2 print lines 1) users name length 2)count the character that user inputed

#solution
name,char= input("enter comma separated name and character: ").split(",")
print(f"length of your name is {len(name)}")
print(f"character count : {name.count(char)}") #case sensitive
#ZAID-zaid
#H-h
#name.lower().count(char.lower())
print(f"character count : {name.lower().count(char.lower())}") #case insensitive

#strip method
name="   za   id  "
dots=".........."
#lstrip() method
print(name + dots)
print(name.lstrip() + dots) #to remove left side space we use lstrip
print(name.rstrip() + dots) #to remove right side space we use rstrip
print(name.replace(" ","") + dots) #to remove all the space

# Lecture 40 - Assignment operatiors
name = "harsh"
name = name + "it" #name  += "it"
print(name)
age=20 
age += 1
print(age)

# Lecture 42 and 43 and 44 - If statement , pass statement , if-else statement

age = int(input())
if age>=14:
    print("you are above 14")



# Lecture 43
x=18
if x>18:
    pass


# Lecture 44
age = int(input())
if age>=14:
    print("you are above 14")
else:
    print("not eligible")

# Lecture 45 - Chapter 3 Exercise 1 (NUMBER GUESSING GAME)
winning_number = 17
input_number = int(input("Enter a number: "))
if input_number==winning_number:
    print("YOU WIN!!!")
else:
    if input_number>winnig_number:
        print("Too High")
    else:
        print("Too Low")

# Lecture 47 - And or operator in python
name = 'abc'
age = 18
if name == 'abc' and age==18:
    print("condition true")
else:
    print("condition false")

# Or operatoer (if one is true then output is true)
if name == 'abc' or age==18:
    print("condition true")
else:
    print("condition false")

# Lecture 48 - Chapter 3 Exercise 2 
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if name[0]=='a' or name[0]=='A' and int(age)>10:
    print("you can watch coco movie")
else:
    print("sorry , you cannot watch coco")

# Lecture 50 and 51 and 52 - If ElifElse statement and keywords and empty or not
age = int(input("Please input your age: "))
if age==0:
    print("You cannot watch")

if 0<age<=3:
    print("Ticket price : Free")
elif 3<age<=10:
    print("Ticket Price; 150")
elif 10<age<=600:
    print("Ticket Price : 250")
else:
    print("Ticket Price : 200")

# Lecture 51
name = "Sandarbh"
if 'a' in name:
    print("a is present in name")
else:
    print("not present")

# Lecture 52
name = input("enter your name: ")
if name: 
    print(f"your name is {name}")
else:
    print("you did not type anything")


# LEcture 53 and 54 - While loop and sum of numbers
#print("hello world") #10 times
i=1
while i<=10:
    print("Hello world")
    i = i+1

# Lecture 54
total = 0
i = 1
while i<=10:
    total = total + i
    i = i+ 1
print(total)

# Lecture 55 - Chapter three exercise 3
n = int(input("enter a number: "))
sum = 0 
i = 1
while i<=n:
    sum += i
    i += 1
print(sum)

# Lecture 57 - Chapter 3 exercise 4 
num_1= input("Enter more than one digit number: ")
sum_of_digits = 0
i = 0
while i<len(num_1):
    sum_of_digits += int(num_1[i])
    i +=1
print(sum_of_digits)

# Lecture 58 - chapter 3 exercise 5
name = input("Enter your name: ")
temp = ""
i = 0 
while i<len(name):
    if name[i] not in temp:
        temp += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i +=1

# Lecture 61 and 62 : Infinite loop and For loop
i = 1
while i <=10:
    print("Hello world")
    i += 1

#Lecture 62 
for i in range(1,11):
    print(f"Hello world : {i}")
    print("this is line \n")











