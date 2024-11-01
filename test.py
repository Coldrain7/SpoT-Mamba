import numpy as np
sequence = np.load('./datasets/PEMS04/pemsd4.npz')["data"]
seq = np.load('./datasets/PEMS04/PEMS04.npz')["data"]
flow = sequence[:,:,0]
print(flow)
all_equal1 = np.all(sequence[:,:,0] == seq[:,:,0])
print(all_equal1)  # 输出: True
occupy = sequence[:,:,1] * 288
print(occupy)
all_equal1 = np.all(sequence[:,:,1] == seq[:,:,1])
print(all_equal1)
speed = sequence[:,:,2]
print(speed)
all_equal1 = np.all(sequence[:,:,2] == seq[:,:,2])
print(all_equal1)
