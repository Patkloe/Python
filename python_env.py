test={'a':5, 'b':6, 'c':7, 'd':8}
print(test)
i=0
while i<=9:
 print(i)
 i+=1
test={}
print(test)
env=locals()
print(env)
print(env['test'])
