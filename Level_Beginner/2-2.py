# 2.2 Pond Area & Water Volume
radius = 84
pi_val = 3.14
area = pi_val * (radius ** 2)
water_per_sm = 1.4
total_water = area * water_per_sm
print(f"Total water in pond: {int(total_water)} liters") # int() removes decimals