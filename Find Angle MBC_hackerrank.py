import math

ab = int(input())
bc = int(input())

angle_rad = math.atan2(ab, bc)
angle_deg = round(math.degrees(angle_rad))

print(f"{angle_deg}{chr(176)}")
