#testing stdout
print 'Hello World'
#testing stderr
#print ' 

import numpy as np
from matplotlib import pyplot as plt
size=255
testPng=np.zeros((size,size,3))

for i in range(size):
    for j in range(size):
        testPng[i,j]=(i,(2*size-i-j)/2,j)

plt.imsave('test123.png',testPng)
