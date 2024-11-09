x='this is computer'
y=['a','e','i','o','u','A','E','I','O','U']
consonantcount=0
vowelcount=0
for i in x:
    if i in y:
        vowelcount=vowelcount+1
print('vowelcount',vowelcount)
for k in x:
    if k not in y and k!=' ':
        consonantcount=consonantcount+1
print('consonantcount',consonantcount)
    
    

