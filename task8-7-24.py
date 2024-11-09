#1)21 multiplication table
num=21
for i in range (1,21,1):
    print(num ,'X', i,'= ', num*i)

#2)number as input to print right angled trangle pattern
num=int(input())
for i in range(1,num+1):
    for j in range(0,i):
        print(i ,end=' ')
    print()
    
#3) list to dict
l = ["a", "b", "c", "d", "e"]
pairs = []

for i in range(0, len(l) - 1):
    pairs.append((l[i], l[i + 1]))

result_dict = dict(pairs)
print(result_dict)

print('''4)iter() is a built in function that makes entities such as list,set etc into an iterzator
# iterator is a counter variable that is used for traversing through a particular range of values''')

