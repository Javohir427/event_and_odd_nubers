#A four-digit integer is given. Find the sum of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".
var_int = 4353
sum_even = 0
a = var_int%10
b = var_int%100//10
c = var_int//100%10
d = var_int//1000
a_1 = (a+1)%2
b_1 = (b+1)%2
c_1 = (c+1)%2
d_1 = (d+1)%2
sum_even = a_1+b_1+c_1+d_1
print(sum_even)