# surface of volume and area of cylindar
pi=3.14
height=float(input("Enetr the height of cylinder:"))12

radian=float(input("Enter the radiant of cylinder:"))

volume=pi* radian*radian*height
sur_area=((2*pi*radian)*height)+((pi*radian**2)*2)

print("volume",volume)
print("surface",sur_area)