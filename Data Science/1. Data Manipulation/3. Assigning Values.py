import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

heights_arr = np.array(heights)
print('heights_arr = {}'.format(heights_arr))
print('\n1. Assign at Pos. 3')
print('-'*30)
print('heights_arr[3] = 165')
heights_arr[3] = 165
print('heights_arr = {}'.format(heights_arr))

print('\n2. Assign in 2darray: use indexing for single element.')
print('This example reset the heights array to default and add ages array.')
print('-'*30)
heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_and_ages = heights + ages 
heights_and_ages_arr = np.array(heights_and_ages)
heights_and_ages_arr = heights_and_ages_arr.reshape((2,45))
print('heights_and_ages_arr = {}\n'.format(heights_and_ages_arr))
print('heights_and_ages_arr[0, 3] = 165 <-- first row, 4th column')
heights_and_ages_arr[0, 3] = 165
print('heights_and_ages_arr = {}'.format(heights_and_ages_arr))

print('\n3. Assign using Slicing')
print('-'*30)
heights_and_ages_arr[0,:] = 180
print('heights_and_ages_arr[0,:] = 180 <-- 1st row, all columns')
print('heights_and_ages_arr = {}'.format(heights_and_ages_arr))

print('\n4. Assign with combine Slicing to change any subset of array.')
print('-'*30)
heights_and_ages_arr[:2, :2] = 0
print('heights_and_ages_arr[:2, :2] = 0 <-- All 2 members for row 1 and 2.')
print('heights_and_ages_arr = {}'.format(heights_and_ages_arr))

print('\n5. Assign with List.')
print('-'*30)
heights_and_ages_arr[:, 0] = [190, 58]
print('heights_and_ages_arr[:, 0] = [190, 58] <-- All rows first column')
print('heights_and_ages_arr = {}'.format(heights_and_ages_arr))

print('\n6. Assign with Numpy Array. Shape must match.')
print('-'*30)
new_record = np.array([[180, 183, 190], [54, 50, 69]])
heights_and_ages_arr[:, 42:] = new_record
print('''
new_record = np.array([[180, 183, 190], [54, 50, 69]])
heights_and_ages_arr[:, 42:] = new_record <-- all rows, 43rd to rest columns. 
Each column replaces with each
''')
print('heights_and_ages_arr = {}'.format(heights_and_ages_arr))

print('\n7.A Menggabungkan Array : Seringkali kita buat array dari 1 array baru digabungkan.')
print('Perhatikan bahwa shape() nya (45,) tidak ada 1-baris nya.')
print('-'*30)
ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]
ages_arr = np.array(ages)
print('ages_arr = {}'.format(ages_arr))

print('''
print(ages_arr.shape)
print(ages_arr[:3,])
''')
print(ages_arr.shape)
print(ages_arr[:3,])

print('\n7.B Combining Array : reshape heights_arr to (45,1).')
print('Then we can stack them horizontally (by column) to get a 2darray using "hstack":')
print('-'*30)
heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]
ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_arr = np.array(heights)
ages_arr = np.array(ages)

heights_arr = heights_arr.reshape((45,1))
ages_arr = ages_arr.reshape((45,1))

height_age_arr = np.hstack((heights_arr, ages_arr))

print('''
heights_arr = np.array(heights)
ages_arr = np.array(ages)

heights_arr = heights_arr.reshape((45,1))            <-- IMPORTANT
ages_arr = ages_arr.reshape((45,1))                  <-- IMPORTANT
height_age_arr = np.hstack((heights_arr, ages_arr))  <-- MAIN

print(height_age_arr.shape)
print(height_age_arr[:3,])
'''
)
print(height_age_arr.shape)
print(height_age_arr[:3,])
# print(height_age_arr)

print('''
7.C Now height_age_arr has both heights and ages for the presidents, each column corresponds to the height and age of one president.
Similarly, if we want to combine the arrays vertically (by row), we can use 'vstack'.
To combine more than two arrays horizontally, simply add the additional arrays into the tuple.
''',end='')
print('-'*30)
heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]
ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

print('''
heights_arr = np.array(heights)
ages_arr = np.array(ages)

heights_arr = heights_arr.reshape((1,45))
ages_arr = ages_arr.reshape((1,45))

height_age_arr = np.vstack((heights_arr, ages_arr))
print(height_age_arr.shape)
print(height_age_arr[:,:3])
''')
heights_arr = np.array(heights)
ages_arr = np.array(ages)

heights_arr = heights_arr.reshape((1,45))
ages_arr = ages_arr.reshape((1,45))

height_age_arr = np.vstack((heights_arr, ages_arr))
print(height_age_arr.shape)
print(height_age_arr[:,:3])
# print(height_age_arr)

print('''
8. Concatenate
More generally, we can use the function numpy.concatenate. 
If we want to concatenate, link together, two arrays along rows, then pass 'axis = 1' to achieve the same result as using numpy.hstack; 
and pass 'axis = 0' if you want to combine arrays vertically.
In the example from the previous part, we were using hstack to combine two arrays horizontally, instead:
''',end='')
print('-'*30)

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]
ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_arr = np.array(heights)
ages_arr = np.array(ages)

heights_arr = heights_arr.reshape((45,1))
ages_arr = ages_arr.reshape((45,1))

# height_age_arr = np.hstack((heights_arr, ages_arr))
height_age_arr = np.concatenate((heights_arr, ages_arr), axis=1)

print(height_age_arr.shape)
print(height_age_arr[:3,:])

print('''
8.B Also you can get the same result as using vstack:

You can use np.hstack to concatenate arrays ONLY if they have the same number of rows.
''',end='')
print('-'*30)

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]
ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_arr = np.array(heights)
ages_arr = np.array(ages)

heights_arr = heights_arr.reshape((1,45))
ages_arr = ages_arr.reshape((1,45))

#height_age_arr = np.vstack((heights_arr, ages_arr))
height_age_arr = np.concatenate((heights_arr, ages_arr), axis=0)

print(height_age_arr.shape)
print(height_age_arr[:,:3])