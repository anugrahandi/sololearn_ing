import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

heights_arr = np.array(heights)
print('heights_arr = {}'.format(heights_arr))
print('\n1. Assign at Pos. 3')
print('-'*30)
print('heights_arr[3] = 165')
heights_arr[3] = 165
print('heights_arr = {}'.format(heights_arr))