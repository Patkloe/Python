print("test","voir", sep = "-")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["type"] = "Vw Passat"
nouv = thisdict.popitem()
print(nouv)
print(type(nouv))
