#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
t1 = ("sakshi", "divya", "renuka")
t2 = (1, 2, 3, 4, 2)
t3 = ("brandy", 5, True)

print(t1)
print(t2)
print(t3)

if "sakshi" in t1:
    print("yes its sakshi")
else:
    print("no")

print(t1[2])
print(t2[1:2])

#this two method are tuple method
print(t1.count("sakshi"))
print(t2.count(2))
print(t3.index(0))

#Convert the tuple into a list to be able to change it:
#we convert tuple to list then all list method is use
t5 = list(t1)
t5[1] = "mina"
t1 = tuple(t5)
print(t1)

