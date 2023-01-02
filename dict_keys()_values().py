car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()
z = car.keys()
y=car.items()  #returning keys ans values
print(x)
print(z)
#y = list(x) convertir en list
#print(y)
# u = list(z) convertir en list

tr={1:2,4:5,3:2}
print(min(sorted(tr.items()),key=lambda a:a[1]))  # we use lambda to tell the function how to return those values, items() we get two values
print(min(sorted(tr.keys())))  # here we get just a value   for each item in the dictionary
print(min(sorted(tr.values()))) # here we get just a value  for each item in the dictionary
print(sorted(tr.items(),reverse=True)) #sorted reverse
