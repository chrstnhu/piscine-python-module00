# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)

# Print the numbers
print(f"module_00, ex_04 : {kata[2]:.2f}, {kata[3]:.2e}, {kata[4]:.2e}")

# Expected output:
# python3 kata04.py
# module_00, ex_04 : 132.42, 1.00e+04, 1.23e+04

# python3 kata04.py | cut -c 10,18
# ,: