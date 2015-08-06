
class TreeNode:
	def __init__(self, key, left=None,right=None,parent = None):
		self.leftChild = left
		self.rightChild = right
		self.keyValue = key
		self.parent = parent

	def hasleftChild(self):
		return self.leftChild

	def hasRightChild(self):
		return self.rightChild

	def binary_insert(self,key):
		if self.keyValue:
			if key <= self.keyValue :
				if self.hasleftChild() :
					self.leftChild.binary_insert(key)
				else:
					self.leftChild = TreeNode(key)
			else:
				if self.hasRightChild():
					self.rightChild.binary_insert(key)
				else:
					self.rightChild = TreeNode(key)
		else:
			self = TreeNode(key)
	
	def InOrderTraversal(self):
		if 	self.hasleftChild():
			self.leftChild.InOrderTraversal()
		print self.keyValue
		if self.hasRightChild():
			self.rightChild.InOrderTraversal()

	def display_tree(self):
		if self.keyValue:
			print self.keyValue
			if self.hasleftChild():
				self.leftChild.display_tree()
			if self.hasRightChild():
				self.rightChild.display_tree()
		else:
			return None
	
	def delete(self,key):
		node, parent = self.search(key)
		if node.hasleftChild() and node.hasRightChild() :
			print "both"
			p = node
			successor = node.rightChild
			while successor.leftChild:
				p = successor
				successor = successor.leftChild
			node.keyValue = successor.keyValue
			if successor.hasRightChild():
				p.rightChild =  successor.rightChild
			successor.keyValue = None
		elif node.hasleftChild() or node.hasRightChild():
			if node.hasleftChild():
				child = node.leftChild
			else:
				child = node.rightChild
			if parent :
				if parent.leftChild == node:
					parent.leftChild = child
				else:
					parent.rightChild = child
			node.keyValue = None
		else:
			if parent.leftChild == node :
				parent.leftChild = None
			elif parent.rightChild == node :
				parent.rightChild = None
			node.keyValue = None

	def search(self, data, parent = None):
		if self.keyValue == data:
			print "Available"
			return self, parent
		else:
			if self.keyValue > data :
				if self.leftChild is None:
					return None,None
				else:
					return self.leftChild.search(data, self)
			else:
				if self.rightChild is None:
					return None, None
				else:
					return self.rightChild.search(data, self)



node = TreeNode(3)
node.binary_insert(4)
node.binary_insert(2)
node.binary_insert(6)
node.display_tree()
node.search(4)
#node.delete(6)
node.display_tree()
#node.binary_insert(6)
#node.delete(3)
#node.display_tree()
node.InOrderTraversal()



