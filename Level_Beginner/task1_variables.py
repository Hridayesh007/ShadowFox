# 1.1 Create pi and check type
pi = 22/7
print(f"Value of pi: {pi}")
print(f"Data type of pi: {type(pi)}")
# 1.2 Reserved Keywords
# try:
#     for = 4
# except SyntaxError as e:
#     print(f"Error: {e}")
# Reason: 'for' is a reserved keyword used for loops. It cannot be used as a variable name.
# 1.3 Simple Interest Calculation
principal = 1000
rate = 5
time = 3
simple_interest = (principal * rate * time) / 100
print(f"Simple Interest for {time} years: {simple_interest}")