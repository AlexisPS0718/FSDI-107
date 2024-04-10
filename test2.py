user = {
  "name": "Alexis", 
  "lastName": "Peñuñuri", 
  "age": 21
}

print(user)
print("Type of 'user':", type(user))
print(user["name"] + " " + user["lastName"])

numbers = [
  73, 25, 49, 86, 12, 58, 37, 91, 64, 18, 5, 42, 70, 96, 21, 67, 30, 54, 83, 9, 46, 78, 15, 63, 88, 33, 61, 8, 72, 39, 3, 59, 93, 27, 65, 17, 51, 80, 11, 75, 23, 55, 97, 31, 76, 43, 6, 69, 34, 99, 29, 57, 2, 89, 45, 22, 60, 85, 14, 68, 4, 40, 77, 19, 82, 24, 52, 94, 28, 62, 10, 74, 32, 66, 1, 56, 20, 48, 81, 36, 90, 7, 41, 79, 13, 50, 87, 35, 71, 16, 53, 95, 38, 84, 26, 92, 47, 98, 44, 100
]

total = 0
n = 0
for number in numbers:
  print(number, end = ", ")
  total += number
  n += 1

print("\nSum of the elements:", total)
print("Number of elements:", n)