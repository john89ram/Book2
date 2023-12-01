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
