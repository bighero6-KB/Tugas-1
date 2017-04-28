import numpy
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

# Make data.
X = np.arange(-3, 3, 0.01)
Y = np.arange(-3, 3, 0.01)
X, Y = np.meshgrid(X, Y)
#https://en.wikipedia.org/wiki/Rosenbrock_function
Z = (1+((X+Y+1)**2)*(19-(14*X)+((3*X)**2))-(14*Y)+(6*X*Y)+((3*Y)**2))*(30+(((2*X)-(3*Y))**2)*(18-(32*X)+((12*X)**2)+(48*Y)-(36*X*Y)+((27*Y)**2)))

#Semut (Allied)
num_func_params = 2
num_semut = 5
position = -3 + 6 * np.random.rand(num_semut, num_func_params)
velocity = np.zeros([num_semut, num_func_params])
personal_best_position = np.copy(position)
personal_best_value = np.zeros(num_semut)

#Isi setting dari semut (Allied)
print ('Semut (Allied)')
print ('position = ')
print (position)
print ()

print ('Velocity = ')
print (velocity)
print ()

print ('Personal Best Position = ')
print (personal_best_position)
print ()

print ('Personal Best Value Awal= ')
print (personal_best_value)
print ()

#Semut (Enemy)++
num_semut_enemy = 2
m_position = -2 + 6 * np.random.rand(num_semut_enemy, num_func_params)
m_velocity = np.zeros([num_semut_enemy, num_func_params])
m_personal_best_position = np.copy(m_position)
m_personal_best_value = np.zeros(num_semut_enemy)

#Isi setting dari semut (Enemy)
print ('Semut (Enemy)')
print ('position = ')
print (m_position)
print ()

print ('Velocity = ')
print (m_velocity)
print ()

print ('Personal Best Position = ')
print (m_personal_best_position)
print ()

print ('Personal Best Value Awal= ')
print (m_personal_best_value)
print ()

#Posisi Semut (Allied) pada arange
for i in range(num_semut):
    #Z = (1-X)**2 + 1 *(Y-X**2)**2
    personal_best_value[i] = (1-position[i][0])**2 + 1 *(position[i][1]-position[i][0]**2)**2
    print ('Semut (Allied) dengan personal best ke ', end=' ')
    print (i, end=' ')
    print (' = ', end=' ')
    print (personal_best_value[i])
print ()

#Posisi Semut (Enemy) pada arange ++
for i in range(num_semut_enemy):
    #Z = (1-X)**2 + 1 *(Y-X**2)**2
    m_personal_best_value[i] = (1-m_position[i][0])**2 + 1 *(m_position[i][1]-m_position[i][0]**2)**2
    print ('Semut (Enemy) dengan personal best ke ', end=' ')
    print (i, end=' ')
    print (' = ', end=' ')
    print (m_personal_best_value[i])
print ()

#Beberapa Gambar yang akan dicetak
tmax = 300

#Kecepatan
c1 = 0.001
c2 = 0.002

levels = np.linspace(-1, 35, 5)

#++
food = 1
food_best_position = -2 + 6 * np.random.rand(food, num_func_params)
food_best = np.zeros(food)
food_best = (1-food_best_position[0][0])**2 + 1 *(food_best_position[0][1]-food_best_position[0][0]**2)**2


print ('levels = ')
print (levels)
print ()

print ('Food Best (Anggaplah Kalau ini Makanan)')
print ('Food Best = ')
print (food_best)
print ()

print ('Food Best Position = ')
print (food_best_position)
print ()

for t in range(tmax): #looping gambar
    print ()
    print ()
    print ('tmax ', end=' ')
    print (t, end=' ')
    print (' : ')
    for i in range(num_semut): #looping pada semut (Allied)
        error = (1-position[i][0])**2 + 1 *(position[i][1]-position[i][0]**2)**2
        print ('Error ', end=' ')
        print (i, end=' ')
        print (' = ', end=' ')
        print (error)

        #Personal best Value
        print ('Personal Best Value ', end=' ')
        print (i, end=' ')
        print (' = ', end=' ')
        print (personal_best_value[i])
        print ('Status Pengecekkan (personal_best_value > error):', end=' ')
        if personal_best_value[i] > error:
            print ('Right')
            print ('PBValue(', end='')
            print (personal_best_value[i], end='')
            print (') = Error(', end='')
            print (error, end='')
            print (')')
            personal_best_value[i] = error
            
            print ('PBPosition(', end='')
            print (personal_best_position[i], end='')
            print (') = Position(', end='')
            print (position[i], end='')
            print (')')
            personal_best_position[i] = position[i]
        else:
            print ('Wrong')
        print ()

    for i in range(num_semut_enemy): #looping pada semut (Enemy)++
        m_error = (1-m_position[i][0])**2 + 1 *(m_position[i][1]-m_position[i][0]**2)**2
        print ('m_Error ', end=' ')
        print (i, end=' ')
        print (' = ', end=' ')
        print (m_error)

        #Personal best Value
        print ('m_Personal Best Value ', end=' ')
        print (i, end=' ')
        print (' = ', end=' ')
        print (m_personal_best_value[i])
        print ('Status Pengecekkan (m_personal_best_value > m_error):', end=' ')
        if m_personal_best_value[i] > m_error:
            print ('Right')
            print ('PBValue(', end='')
            print (m_personal_best_value[i], end='')
            print (') = Error(', end='')
            print (m_error, end='')
            print (')')
            m_personal_best_value[i] = m_error
            
            print ('PBPosition(', end='')
            print (m_personal_best_position[i], end='')
            print (') = Position(', end='')
            print (m_position[i], end='')
            print (')')
            m_personal_best_position[i] = m_position[i]
        else:
            print ('Wrong')
        print ()

    #Percobaan ++
    for i in range(num_semut):
        print (round(position[i][0], 0))
        print ('Position', end=' ')
        print (i, end=' ')
        print ('= ', end='')
        print (position[i])
        print ('Food Best Position =', end=' ')
        print (food_best_position[0])
        print ('Status Pengecekkan (Food_best = best):', end=' ')
        if round(position[i][0], 0) == round(food_best_position[0][0], 0) and round(position[i][1], 0) == round(food_best_position[0][1], 0):
            print ('Right')
            food_best_position = -3 + 6 * np.random.rand(food, num_func_params)
            food_best = (1-food_best_position[0][0])**2 + 1 *(food_best_position[0][1]-food_best_position[0][0]**2)**2
        else:
            print ('Wrong')
        print ()

    #Velocity Semut (Allied)
    for i in range(num_semut):
        #update velocity
        velocity[i] += c1 * np.random.rand() * (personal_best_position[i]-position[i]) \
                    +  c2 * np.random.rand() * (food_best_position[0] - position[i])
        position[i] += velocity[i]
        print ('Velocity Semut (Allied)', end=' ')
        print (i, end=' ')
        print (':')
        print ('Velocity', end=' ')
        print ('=', end=' ')
        print (velocity[i])
        print ('Position', end=' ')
        print ('=', end=' ')
        print (position[i])

    #Velocity Semut (Enemy)++
    for i in range(num_semut_enemy):
        #update velocity
        m_velocity[i] += c1 * np.random.rand() * (m_personal_best_position[i]-m_position[i]) \
                    +  c2 * np.random.rand() * (food_best_position[0] - m_position[i])
        m_position[i] += m_velocity[i]
        print ('Velocity Semut (Enemy)', end=' ')
        print (i, end=' ')
        print (':')
        print ('Velocity', end=' ')
        print ('=', end=' ')
        print (m_velocity[i])
        print ('Position', end=' ')
        print ('=', end=' ')
        print (m_position[i])

    #Map
    fig = plt.figure()
    CS = plt.contour(X, Y, Z, levels =levels, cmap=cm.gist_stern)
    plt.gca().set_xlim([-5,5])
    plt.gca().set_ylim([-5,5])

    #Menampilkan Semut dan Makanan
    for i in range(num_semut):
        plt.plot(position[i][0], position[i][1], 'yo')

    for i in range(num_semut_enemy):
        plt.plot(m_position[i][0], m_position[i][1], 'ro')
    plt.plot(food_best_position[0][0], food_best_position[0][1], 'bo')
    
    plt.title('{0:03d}'.format(t))
    filename = 'img{0:03d}.png'.format(t)
    plt.savefig(filename, bbox_inches='tight')
    plt.close(fig)