#FARENHEIT AND CELSIUS CONVERTOR

temperature = float(input("Temperature: "))
tempUnit = input("You want to convert to (F)arenheit or (C)elsius: ")

if tempUnit.upper() == "F":
    converted = str((9 / 5 * temperature) + 32)
    print("The temperature in Fahrenheit Grades is: " + converted)

elif tempUnit.upper() == "C":
    converted = str(5 /9 * (temperature - 32))
    print("The temperature in Celsius grades is: " + converted  )

else:
    print("You didn't select a correct Temperature Unit")

