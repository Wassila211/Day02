date = input("Taper une date pour savoir si elle est bissextile:\n")
date = int(date)

if(date%4==0 and date%100!=0 or date%400==0):
  print("c'est une année bissextile")
else:
  print("ce n'est pas une année bissextile")


