# Variables
varString = ""
varNumber = 2
varName = "Alexis"
print(varName + str(varNumber))

# If else statements
age = 21
if age < 30:
  print("You're young")
elif age > 30:
  print("You're still young")
else:
  print("I don't know how you got there")

# Lists
colors = ["Red", "Green", "Blue"]
print(colors)
colors.append("Yellow")
print(colors)
colors.remove("Red")
print(colors)
print(colors[2])

# For each
for color in colors:
  print(color)

# Dictionaries
me = {
  "firstName": varName,
  "lastName":"Peñuñuri",
  "age": age,
}
print(me)
print(me["firstName"])
me["age"] = 99
me["favColor"] = "Blue"
print(me)

# Functions
def sayHello():
  print("Hello")

def sayGoodbye(name, age):
  print("Goodbye, " + name + " " + str(age))

sayHello()
sayGoodbye(varName, age)

def printMenu():
  print("--- Calculator ---")
  print("1) Sum")
  print("2) Substraction")
  print("3) Multiplication")
  print("4) Division")

printMenu()
opt = int(input("Choose an option: "))
num1 = float(input("Type the first number: "))
num2 = float(input("Type the second number: "))

if opt == 1:
  total = num1 + num2
  print("The sum of", num1, "and", num2, "equals to", total)
elif opt == 2:
  total = num1 - num2
  print("The substraction of", num1, "and", num2, "equals to", total)
elif opt == 3:
  total = num1 * num2
  print("The multiplication of", num1, "and", num2, "equals to", total)
elif opt == 4:
  if num2 == 0:
    print("Error: Cannot divide by zero")
  else:
    total = num1 / num2
    print("The division of", num1, "and", num2, "equals to", total)