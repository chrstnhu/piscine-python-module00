# Put this at the top of your kata03.py file
kata = "The right format"

# Calculate the right format
print(("-" * (40 - len(kata))) + kata + "%")

# Expected output:
# python3 kata03.py
# -------------------------------The right format%

# python3 kata03.py | wc -c
# 42