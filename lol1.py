
def  GCF (a,b):
     t = min ([a,b])
     alist = list()
     for i in range(1,t+1):
          if (a % i == 0  and b % i == 0):
              alist. append (i)
     return max(alist)
def find_GCF(a, b):
    if b == 0: return a
    return find_GCF(b,a%b)

          
dt = 0.01
t = 0
h1 = 1
h2 = 0
g = 9.8
s = 0.2
s0 = 0.001 * 5
m = 1
def solve (s0,m,dt,h1 = 1,h2 = 0):
    t = 0
    g = 9.8
    s1 = 0.2
    s2 = 0.2
    xlist = list()
    ylist = list()
    while h1 >= h2:
        xlist.append(h1)
        ylist.append(t)
        Q = s0 * m * (2*g*(h1-h2)) ** 0.5
        dh1 = (-Q/s1) * dt
        h1 = h1 + dh1
        dh2 = (-s1/s2)* dh1
        h2 = h2 + dh2
        t += dt
    return xlist,ylist


def solve2 (s0,m,dt,h1 = 1,h2 = 0):
    t = 0
    g = 9.8
    s1 = 0.2
    s2 = 0.2
    xlist = list()
    ylist = list()
    while h1 >= h2:
        xlist.append(h1)
        ylist.append(t)
        Q = s0 * m * (2*g*(h1-h2)) ** 0.5
        dh1 = (-Q/s1) * dt
        h1 = h1 + dh1
        dh2 = (-s1/s2)* dh1
        h2 = h2 + dh2
        t += dt
    return t


def solve1 (s0,m,dt,h1 = 1,h2 = 0):
    t = 0
    g = 9.8
    s1 = 0.2
    s2 = 0.2
    xlist = list()
    ylist = list()
    while h1 >= h2:
        xlist.append(h2)
        ylist.append(t)
        Q = s0 * m * (2*g*(h1-h2)) ** 0.5
        dh1 = (-Q/s1) * dt
        h1 = h1 + dh1
        dh2 = (-s1/s2)* dh1
        h2 = h2 + dh2
        t += dt
    return xlist,ylist

#import matplotlib.pyplot as plt

#fig = plt.figure()
# Добавление на рисунок прямоугольной (по умолчанию) области рисования
#scatter1 = plt.scatter(0.0, 0.0)
t = 100000
#print('Scatter: ', type(scatter1))

"""xlist , ylist = solve(0.00000000001,0.85,t)
print(ylist)
xlist1 , ylist1 = solve1(0.00000000001,0.85,t)
print(ylist1)"""
"""print(1)
plt.xlabel('Time, sec ')
plt.ylabel('Water level, m')
xlist2 , ylist2 = solve(0.0000001,0.85,t)
xlist3 , ylist3 = solve1(0.000001,0.85,t)
print(2)
xlist4 , ylist4 = solve(0.0001,0.85,t)
xlist5 , ylist5 = solve1(0.0001,0.85,t)
print(3)
myhex = '#0000FF'
graph1 = plt.plot(ylist,xlist,color=myhex)
graph2 = plt.plot (ylist1,xlist1,color=myhex)

my = '#7FFFD4'
graph3 = plt.plot(ylist2,xlist2,color=my)
graph4 = plt.plot (ylist3,xlist3,color=my)

m = '#FF0000'
graph5 = plt.plot(ylist4,xlist4,color=m)
graph6 = plt.plot (ylist5,xlist5,color=m)



print('Plot: ', len(graph1), graph1)

text1 = plt.text(0.5, 0.5, '')
text2 = ''
text3 = ''
print('Text: ', type(text1))

grid1 = plt.grid(True)   # линии вспомогательной сетки



plt.show()


"""

    
