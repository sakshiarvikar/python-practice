#List is a collection which is ordered and changeable. Allows duplicate members.
l1 = [3, 5, 234, 5, 3]
l2 = ["sonu", "divya"]
l3 = [True , False]
l4 = [3, 4, "abc", True]

print(type(l1))
print(l1)
print(l2)
print(l3)
print(l4)
#l1.sort()
#print(l1)
#l2.sort()
#print(l2)
print(l1[2:])

if "sakshi" in l2:
    print("yess its sakshi")
else:
    print("no")

l1.extend(l2)
print(l1)
l4.append(2)
print(l4)











