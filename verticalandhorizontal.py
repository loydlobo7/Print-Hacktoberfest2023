# Python3 program to find if a matrix is symmetric.
MAX = 1000

def checkHV(arr, N, M):
	
	# Initializing as both horizontal and vertical
	# symmetric.
	horizontal = True
	vertical = True
	
	# Checking for Horizontal Symmetry. We compare
	# first row with last row, second row with second
	# last row and so on.
	i = 0
	k = N - 1
	while(i < N // 2):
		
		# Checking each cell of a column.
		for j in range(M):
			
			# check if every cell is identical
			if (arr[i][j] != arr[k][j]):
				horizontal = False
				break
		i += 1
		k -= 1
		
	# Checking for Vertical Symmetry. We compare
	# first column with last column, second column
	# with second last column and so on.
	i = 0
	k = M - 1
	while(i < M // 2):
		
		# Checking each cell of a row.
		for j in range(N):
			
			# check if every cell is identical
			if (arr[i][j] != arr[k][j]):
				vertical = False
				break
		i += 1
		k -= 1
		
	if (not horizontal and not vertical):
		print("NO")
	elif (horizontal and not vertical):
		print("HORIZONTAL")
	elif (vertical and not horizontal):
		print("VERTICAL")
	else:
		print("BOTH")
		
# Driver code
mat = [[1, 0, 1],[ 0, 0, 0],[1, 0, 1]]

checkHV(mat, 3, 3)

# This code is contributed by shubhamsingh10
