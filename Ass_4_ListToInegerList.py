
l = ["log", "hari", "pranes", "money", "lu", "lee", "health", "meditation"]

def findlen(l):
    k =[]
    # count = 0
    for i in l:
        # for k in i:
        #     count += 1
        k.append(len(i))
    return k

m = findlen(l)
print(m)