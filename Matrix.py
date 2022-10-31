# Python 3 program to find unique
# element in matrix
def unique(mat, n, m):

	maximum = 0; flag = 0
	
	for i in range(0, n):
		for j in range(0, m):
			
			# Find maximum element in
			# a matrix
			if(maximum < mat[i][j]):
				maximum = mat[i][j];

	uniqueElementDict = [0] * (maximum + 1)

	# loops to traverse through the matrix
	for i in range(0, n):
		for j in range(0, m):
				uniqueElementDict[mat[i][j]] += 1

	# Print all those keys whose count is 1
	for key in range(maximum + 1):
		if uniqueElementDict[key] == 1:
			print (key, end = " ")
			flag = 1
	
	if(flag == 0):
		print("No unique element in the matrix")

# Driver Code
mat = [[1, 2, 3, 20],
	[5, 6, 20, 25],
	[1, 3, 5, 6],
	[6, 7, 8, 15]]
n = 4
m = 4
unique(mat, n, m)
