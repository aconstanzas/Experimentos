#create a script that converts temperature from fahrenheit to celsius and viceversa 
celsius = float(input("Enter the temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("The temperature in fahrenheit is: ", fahrenheit)
fahrenheit = float(input("Enter the temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("The temperature in celsius is: ", celsius)
#end of script