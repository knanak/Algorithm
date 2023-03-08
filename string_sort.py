import string
s=input()
s=s.replace(' ', '')
print(s)

ch=''
result=0

for i in s:
  if i.isalpha():
    ch+=i
    new_ch = sorted(ch)

  else:
    i=int(i)
    
    result+=i



new=''
for i in new_ch:
  new+=i
  
print(new, result, sep='')
