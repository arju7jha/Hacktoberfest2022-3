# Python3 implementation to construct
# Binary Tree in level order fashion

# Structure of the Node of Binary tree
# with count of Children nodes in
# left sub-tree and right sub-tree.
class Node:
	
	def __init__(self, data):
		
		self.data = data
		self.rcount = 0
		self.lcount = 0
		self.left = None
		self.right = None

# Function to check whether the given
# Binary tree is a perfect binary tree
# using the no. of nodes in tree.
def isPBT(count: int) -> bool:

	count = count + 1

	# Loop to check the count is in
	# the form of 2^(n-1)
	while (count % 2 == 0):
		count = count / 2

	if (count == 1):
		return True
	else:
		return False

# Recursive function to insert
# elements in a binary tree
def insert(root: Node, data: int) -> Node:

	# Condition when root is NULL
	if (root is None):
		n = Node(data)
		return n

	# Condition when count of left sub-tree
	# nodes is equal to the count
	# of right sub-tree nodes
	if (root.rcount == root.lcount):
		root.left = insert(root.left, data)
		root.lcount += 1

	# Condition when count of left sub-tree
	# nodes is greater than
	# the right sub-tree nodes
	elif (root.rcount < root.lcount):

		# Condition when left Sub-tree is
		# Perfect Binary Tree then Insert
		# in right sub-tree.
		if (isPBT(root.lcount)):
			root.right = insert(root.right, data)
			root.rcount += 1

		# If Left Sub-tree is not Perfect
		# Binary Tree then Insert in left sub-tree
		else:
			root.left = insert(root.left, data)
			root.lcount += 1

	return root

# Function for inorder Traversal of tree.
def inorder(root: Node) -> None:

	if root != None:
		inorder(root.left)
		print(root.data, end = " ")
		inorder(root.right)

# Driver Code
if __name__ == "__main__":

	arr = [ 8, 6, 7, 12, 5, 1, 9 ]
	size = len(arr)
	root = None

	# Loop to insert nodes in
	# Binary Tree in level order
	for i in range(size):
		root = insert(root, arr[i])
		
	inorder(root)

# This code is contributed by sanjeev2552
