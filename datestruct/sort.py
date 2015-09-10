class BTree:
	def __init__(self,value):
		self.left = None
		self.date = value
		self.right = None

	def insertLeft(self,value):
		self.left = BTree(value)
		return self.left

	def insertRight(self,value):
		self.right = BTree(value)
		return self.right

	def show(self):
		print self.data

	def inorder(node):
		if node.data:
			if node.left:
				inorder(node.left)	
			node.show()
			if node.right:
				inorder(node.right)

	def riorder(node):
		if node.data:
			if node.right:
				inorder(node.right)	
			node.show()
			if node.left:
				inorder(node.left)

	def insert(node,value):
		if value > node.data:
			if node.right:
				insert(node.right,value)
			else:
				node.insertRight(value)
		else:
			if node.left:
				insert(node.left,value)
			else:
				node.insertLeft(value)


	if __name__ == "__main__":
		l = [58,11,2,33,22,4,55,33,221,24]
		Root = BTree(l[0])
		node = Root
		for i in range(1,len(l)):		
			insert(Root,l[i])

		print "1---->10"
		inorder(Root)
		print "10---->1"
		riorder(Root)
