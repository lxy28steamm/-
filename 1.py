import numpy as np
x=np.random.randint(-5,10,(20,5))
m=np.mean(x,axis=0)
std=np.std(x,axis=0)
std_data=(x-m)/std
floor=m-3*std
upper=m+3*std
floor = np.broadcast_to(floor, std_data.shape)
upper = np.broadcast_to(upper, std_data.shape)
std_data = np.where((std_data < floor) | (std_data > upper), m, std_data)
print(std_data)