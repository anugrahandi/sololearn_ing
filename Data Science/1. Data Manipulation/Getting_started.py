import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

print(len([i for i in heights if i>188 ]))

heights_arr = np.array(heights)
print("(heights_arr > 188).sum() = {}".format((heights_arr > 188).sum()))
print("heights_arr.size = {}".format(heights_arr.size))
print("heights_arr.shape = {}".format(heights_arr.shape))

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]
heights_and_ages = heights + ages
# convert a list to a numpy array
heights_and_ages_arr = np.array(heights_and_ages)
print("heights_and_ages_arr.shape = {}".format(heights_and_ages_arr.shape))
heights_and_ages_arr = heights_and_ages_arr.reshape((2,45))
'''
Numpy can calculate the shape (dimension) for us if we indicate the unknown dimension as -1. 
For example, given a 2darray `arr` of shape (3,4), arr.reshape(-1) would output a 1darray 
of shape (12,), while arr.reshape((-1,2)) would generate a 2darray of shape (6,2).
'''
# print(heights_and_ages_arr)
print("heights_and_ages_arr.shape = {}".format(heights_and_ages_arr.shape))
print("heights_arr.dtype = {}".format(heights_arr.dtype))

heights_float = [189.0, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

heights_float_arr = np.array(heights_float)
print('heights_float_arr.dtype = {}'.format(heights_float_arr.dtype))
print('heights_float_arr = {}'.format(heights_float_arr))