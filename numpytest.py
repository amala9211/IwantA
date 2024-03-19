import numpy as np

print('my numpy versiom', np.__version__)

randomlist = []
for i in range(1000000) :
    n = np.random.randint(1, 20) 
    randomlist.append(n) 
#
    print("randomlist:", randomlist)