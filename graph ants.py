import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d 
import random

fig = plt.figure()
axl = fig.add_subplot(111, projection='3d')

#ants (allied)
x = [random.randint(1,30),random.randint(1,30),random.randint(1,30),
     random.randint(1,30),random.randint(1,30),random.randint(1,30),
     random.randint(1,30),random.randint(1,30),random.randint(1,30),
     random.randint(1,30),random.randint(1,30),random.randint(1,30)]
y = [random.randint(1,30),random.randint(1,30),random.randint(1,30),
     random.randint(1,30),random.randint(1,30),random.randint(1,30),
     random.randint(1,30),random.randint(1,30),random.randint(1,30),
     random.randint(1,30),random.randint(1,30),random.randint(1,30)]
z = [random.randint(1,30),random.randint(1,30),random.randint(1,30),
     random.randint(1,30),random.randint(1,30),random.randint(1,30),
     random.randint(1,30),random.randint(1,30),random.randint(1,30),
     random.randint(1,30),random.randint(1,30),random.randint(1,30)]

#Food
x2 = [random.randint(10,20)]
y2 = [random.randint(10,20)]
z2 = [random.randint(10,20)]

#Enemy
x3 = [random.randint(5,25)]
y3 = [random.randint(5,25)]
z3 = [random.randint(5,25)]

axl.scatter(x, y, z, c='b', marker='o', label='Ants (Allied)')
axl.scatter(x2, y2, z2, c='g', marker='o', label='Food')
axl.scatter(x3, y3, z3, c='r', marker='o', label='Enemy')

axl.set_xlabel('x axis')
axl.set_ylabel('y axis')
axl.set_zlabel('z axis')
plt.legend()

plt.show()
