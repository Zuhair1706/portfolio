seta={0,1}
lista=[2,3,4,5]
seta.update(lista)
print(seta)

#2)
setb={0,2,4,6,8,10}
setc={2,3,5,6,8,9,11}
d=setb.intersection(setc)
print(d)

#3)
universal={0,1,2,3,4,5,6,7,8,9}
sete={2,3,4,5,6,7}
f=universal-sete
print(f)

#4)
set1 = {10, 20, 30}
set2 = {30, 4, 50}
set1.update(set2)
print(set1)

#5)
set1.clear()
print(set1)

#6)

setu = {10, 20, 30}
setv = {30, 4, 50}
result = setu.symmetric_difference(setv)
print(result)
#7)
print(setu.intersection(setv))

#8)
set4={1,2,3,4,5}
set5={3,4,5,6,7,8}
set4.update(set5)
print(set4)
set6 = set4.intersection(set5)
print(set4-set6)



