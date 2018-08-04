#import NumPy as np
import numpy as np

#Create an array of 10 zeros
arr = np.arange(10)
arr[:] = 0
print(arr)
#or
arro = np.zeros(10)
print(arro)

#Create an array of 10 ones
arr2 = np.arange(10)
arr2[:] = 1
print (arr2)
#or
arro2 = np.ones(10)
print(arro2)


#Create an array of 10 fives
arr3 = np.arange(10)
arr3[:] = 5
print(arr3)
#or
arro3 = np.ones(10) * 5
print(arro3)


#Create an array of the integers from 10 to 50
arr4 = np.arange(10,51)
print(arr4)


#Create an array of all the even integers from 10 to 50
arr5 = np.arange(10,51,2)
print(arr5)


#Create a 3x3 matrix with values ranging from 0 to 8
arr6_2d = np.array([[0,1,2],[3,4,5],[6,7,8]])
print(arr6_2d)
#or
arr6 = np.arange(9).reshape(3,3)
print(arr6)


#Create a 3x3 identity matrix
Imat = np.eye(3)
print(Imat)


#Use numpy to generate a random number between 0 and 1
random = np.random.rand(1)
print(random)


#Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
stand = np.random.randn(25)
print(stand)


new_array = np.arange(1,101).reshape(10,10)/100
print(new_array)
#or
new_array2 = np.linspace(0.01,1,100).reshape(10,10)
print(new_array2)

arr7 = np.linspace(0,1,20)
print(arr7)


mat = np.arange(1,26).reshape(5,5)
print(mat)
print(mat[2:,1:])
print(mat[3,4])
print(mat[:3,1:2])
print(mat[4])
print(mat[3:])

#Get the sum of all the values in mat
print(np.sum(mat))

#Get the standard deviation of the values in mat
print(np.std(mat))

#Get the sum of all the columns in mat
print(mat.sum(axis=0))








































