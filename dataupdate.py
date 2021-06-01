fname=input('enter name file: ')

try:
    data=open(fname)
    for i in data:
        print(i)
except:
    print('can not open file')
    quit()

count=0
for line in data:
    if line.startswith('abdul'):
        count+=1
    print(line)
  
