# 2.1 Formatting
num = 145
# 'o' stands for Octal representation
result = format(num, 'o')
print(f"The octal representation of 145 is: {result}")

# 2.2 Pond Area & Water Volume
radius = 84
pi_val = 3.14
area = pi_val * (radius ** 2)
water_per_sm = 1.4
total_water = area * water_per_sm
print(f"Total water in pond: {int(total_water)} liters") # int() removes decimals

# 2.3 Speed Calculation
distance = 490 # meters
time_min = 7
time_sec = time_min * 60
speed = distance / time_sec
print(f"Speed: {int(speed)} m/s")