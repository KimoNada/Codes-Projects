import numpy as np

np.random.seed(123)
#Intialize all_walks(don't change this line)
all_walks = []

#Simulate random walk 10 times
for i in range(500):  #Simulate 10 times when display all_walks then 250 times when implementing clumsiness and 500 times when plot the distribution in Histogram

    #Initializing
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step -1 )
        elif dice <= 5:
            step = step + 1
        else:
            step = step +np.random.randint(1,7)
        #Implement clumsiness
        if np.random.rand() <= 0.001:
            step = 0
        random_walk.append(step)

    all_walks.append(random_walk)

#Convert all_walks to Numpy array
np_aw = np.array(all_walks)

#Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
#plot random_walk
#plt.plot(np_aw)
#show the plot
#plt.show()

#clear the figure
#plt.clf()

#Transpose np_aw 
np_aw_t = np.transpose(np_aw)

#plot np_aw_t and show
#plt.plot(np_aw_t)
#plt.show()
#Select last row from np_aw_t
ends = np_aw_t[-1 , :]
#plot Histogram of ends , display plot
plt.hist(ends)
plt.show()