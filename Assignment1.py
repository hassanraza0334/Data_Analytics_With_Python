# 1.Print Your Name with your Father name and Date of birth 
#  using suitable escape sequence charactor


print("My Name is Hassan Raza S/0 Muhammad Tufail\nMy Date of Birth is 03.09.2000")


# 2.Write your small bio using variables and print it using print function

Name="My Name is Hassan Raza"
Eduction="I am recently completed my bacholar in computer Science"
print(Name)
print(Eduction)

# 3.Write a program in which use all the operators we can use in Python
# (i).Arithmetic Operators
a=2
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# (ii). Relational Operators
a=50
b=20
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a>b)
print(a<b)

# (iii). Assignment Operators
Number=10
Number=Number+10
print(Number)

# (iv). Logical Operators
# Logical Operators Boolen value ka opper kam kertay han 
# e.g  
# (Not operators) ka kaam hota ha ka jo bi value aya osa Ulat ker dey----> Okay 
a=50
b=30
print(not(a>b))

# (And Operators) And operators True Taab deta ha jab Dono Value True ho
val1=True
val2=True
print(val1 and val2)

# (Or Operators) ma dono value ma sa ik bi true ho gi phir ans true hi aya ga--->Okay
val1=True
val2=False
print(val1 or val2)

# 4. Completes the following steps of small task:
#Mention Marks of English , Islamiat and Maths out of 100 in 3 different variables
#Mention Variable of Total Marks and assign 300 to it
#Calculate Percentage

English_marks=85
Islamiat_marks=90
Math_marks=78
Total_marks=300
obtained_marks=English_marks+Islamiat_marks+Math_marks
Percentage=(obtained_marks/ Total_marks)*100
print("Obtained_marks :",obtained_marks)
print("percentage :",Percentage)

# 5. Take the values of two variables a and b, then swap their values without 
# using a third variable and print the result before and after swapping
a=5
b=10
print("Before Swapping :",a,b)
a,b=b,a
print("After Swapping :",a,b)

# 6.Take the radius of a circle from a variable and calculate its Area and Circumference (use pi = 3.14159)
pi=3.14159
r=5
print("Area :",pi*r*r)
print("Circumference :",2*pi*r)

# 7.Take the price of an item and a discount percentage in variables, then calculate and print the 
# discount amount and the final price after discount
Price=1000
Disc=20
print("Discount Amount :",Price*Disc/100)
print("Final :", Price-(Price*Disc/100))