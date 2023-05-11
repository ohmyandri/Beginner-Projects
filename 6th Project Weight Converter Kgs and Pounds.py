#WEIGHT CONVERTER PROGRAM:
weight = float(input("Weight: "))
weightUnit = input("(K)g or (L)bs: ")

if weightUnit.upper() == "K":
    converted = str(weight * 2.20462)
    print("Weight in Lbs: " + converted)

elif weightUnit.upper() == "L":
    converted = str(weight / 2.20462)
    print("Weight in Kg: " + converted)

else:
    print("You didn't select a correct Weight Measurement")