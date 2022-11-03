#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".
var_int = 4653
a = var_int%10
b = var_int%100//10
c = var_int//100%10
d = var_int//1000

a_1 = (a+1)%2
b_1 = (b+1)%2
c_1 = (c+1)%2
d_1 = (d+1)%2
print(a_1+b_1+c_1+d_1)  