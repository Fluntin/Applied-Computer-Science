class Node():
	def __init__(self, element, next=None):
		self.element = element
		self.next = next

class LinkedQ():

	def __init__(self):
		self.__first = None
		self.__last = None

	def enqueue(self, element):
		end_Node = Node(element)
		if self.__first == None:
			self.__first = end_Node
			self.__last = end_Node
		else:
			self.__last.next = end_Node
			self.__last = end_Node

	def dequeue(self):
		first_element = self.__first.element
		self.__first = self.__first.next 
		return first_element

	def isEmpty(self):
		if self.__first == None:
			return True
		else:
			return False

	def peek(self):
		if not self.isEmpty():
			return self.__first.element
		else:
			return None
