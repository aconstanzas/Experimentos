#make a script that asks the capacity in milliamps and the years of use of a battery to tell you the range of battery life from 1 to 100 and that does all this using this formula mAh ÷ mA * 0.7 = estimated hours of life of the battery
input_capacity = int(input("Enter the capacity in milliamps: "))
input_years = int(input("Enter the years of use: "))
print("The range of battery life is: ", input_capacity / input_years * 0.7)
#end of program