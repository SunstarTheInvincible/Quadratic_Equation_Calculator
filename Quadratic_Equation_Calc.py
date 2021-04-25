"""Hello peeps 

this is a 

quadratic equation calculator.

Although i've published

 a quadratic eqution calculator earlier also
 
 but that was written in C++ and 
 
 this is written in Python.
 
 Feel Free to do any changes.

"""

# Please do an upvote if you 👍 😂😂😂

a = float(input("Please enter the coefficient of x²: "))

print("The coefficient of x² entered is " + str(a))

b = float(input("Please input the coefficient of x: "))

print("The coefficient of x entered is " + str(b))

c = float(input("Please enter the constant(k/c): "))

print("The constant(k/c) entered is " + str(c))

d = float(b*b + (-4)*a*c)

x1 = ((-b) + (d)**(1/2))/(2*a)

print('The 1st root is:')

print(x1)

x2 = ((-b) - (d)**(1/2))/(2*a)

print('The 2nd root is:')

print(x2)

if d == 0:

 print("The roots are real and repeated!")

elif d > 0:

 print("The roots are real and distinct!")

elif d < 0:

 print("The roots are imaginary!")