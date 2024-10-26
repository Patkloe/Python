def compare(s):
 lg=len(s)
 first=s[0]
 lst=s[lg-1]
 if lg>=2 and first==lst:
  return True
 else:
  return False
  
txt="reveni"
print(compare(txt))

tab=["revenir","sens","gg","mkl","opo"]
num=0
for x in tab:
 if compare(x):
  num+=1
print(num)
