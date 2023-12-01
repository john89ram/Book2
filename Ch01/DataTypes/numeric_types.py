# Integers - an integer is a data type that represents whole numbers without any 
# fractional part. Integers can be positive, negative, or zero. In Python, you can define an integer by simply assigning a whole number to a variable.
integer = 15
print(integer)

# Floats - a float is a data type that represents real numbers, including both 
# integer and fractional parts. Floats are used to store numbers that may have a decimal point or an exponent (scientific notation).
float = 15.0
print(float)

# Math Operators from Highest to Lowest Precedence

# Operator      Operation           Example     Evaluates to...
# **            Exponent            2 ** 3      8
# %             Modulus/Remainder   22 % 8      6
# //            Integer Division    22 // 8     2
# /             Division            22 / 8      2.75
# *             Multiplication      3 * 5       15
# -             Subtraction         5 - 2       3
# +             Addition            2 + 3       4

print(2**3)
print(22%8)
print(22//8)
print(22/8)
print(3*5)
print(5-2)
print(2+2)

# () can be used to override these expressions. 
# From left to right we can follow the parentheses. 
# (5-1) * ((7+1)/(3-1))
#   ^        ^     ^
#   4   *   (8  /  2)
#               ^
#   4   *       4.0
#       ^
#       16.0 (Remember that the "/" will leave any decimal left)
print((5-1)*((7+1)/(3-1)))