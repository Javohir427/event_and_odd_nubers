#A four-digit integer is given. Find the sum of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".
var_int = 4368


x1=var_int%10
var_int//=10

x2=var_int%10
var_int//=10

x3=var_int%10
var_int//=10

x4=var_int%10
var_int//=10
a = ((x1+1)%2)*x1
b = ((x2+1)%2)*x2
c = ((x3+1)%2)*x3
d = ((x4+1)%2)*x4

sum_even = a+b+c+d
print (sum_even)


