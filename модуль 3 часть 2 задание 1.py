
glist=[1, 2, 3, "one", 5, 6, 1, 2, "one"]
x=set(glist)
dup=[]
for c in x:
    if(glist.count(c)>1):
        dup.append(c)
print(dup)