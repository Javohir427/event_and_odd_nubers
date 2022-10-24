#A four-digit integer is given. Find the sum of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the odd digits in the variable "var_int".
var_int = 4578
sum_even = 0
a = var_int%10
b = var_int%100//10
c = var_int%1000//100
d = var_int//1000

e = (a%2)*a
f = (b%2)*b
g = (c%2)*c
h = (d%2)*d
k = e+f+g+h
print(k)
