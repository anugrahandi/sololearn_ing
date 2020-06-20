import numpy as np
print('1. Indexing 1darray')
print('-'*30)

# Height of president of USA
heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]
print(heights_arr[2])
print('Height of 3rd President = heights_arr[2] = {}'.format(heights_arr[2]))

print('\n2. Indexing 2darray')
print('-'*30)
a = '''In a 2darray, there are two axes, axis 0 and 1. 
Axis 0 runs downward down the rows whereas axis 1 runs horizontally across the columns.'''
print(a)

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_and_ages = heights + ages
heights_and_ages_arr = np.array(heights_and_ages)
heights_and_ages_arr = heights_and_ages_arr.reshape((2,45))
print('heights_and_ages_arr : \n{}'.format(heights_and_ages_arr))
print('Age of 3rd President = heights_and_ages_arr[1,2] = {}'.format(heights_and_ages_arr[1,2]))

print('\n3. Slicing')
print('-'*30)
print('heights_and_ages_arr[0, 0:3] = {}'.format(heights_and_ages_arr[0, 0:3]))
print('heights_and_ages_arr[0, :3] = {}'.format(heights_and_ages_arr[0, :3]))
print('heights_and_ages_arr[:, 3] = {}'.format(heights_and_ages_arr[:, 3]))
b = '''Numpy slicing syntax follows that of a python list: arr[start:stop:step]. 
When any of these are unspecified, they default to the values start=0, stop=size of dimension, step=1.'''
print(b)

print('\n4. Slicing')
print('-'*30)