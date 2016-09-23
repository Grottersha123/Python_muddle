n = int(input())
t = (input())[0:n+1]
print(type(t))
t = tuple([int(i)for i in t if i != ''])
print(hash(t))
