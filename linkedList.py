# LinkedList implemetation

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def add( self, data ):
		node = Node ( data )
		if self.head == None :
			self.head = node
		else :
			node.next = self.head
			node.next.prev = node
			self.head = node

    def remove( self, element ):
		tmp = element.prev
		element.prev.next = element.next
		element.prev = tmp

    def search( self, data ) :
		element = self.head
		if element != None :
			while element.next != None :
				if ( element.data == data ) :
					return element
				element = element.next
			if ( element.data == data ) :
				return element
		return None

    def __str__( self ) :
		s = ""
		element = self.head
		if element != None :
			while element.next != None :
				s += element.data
				element = element.next
			s += element.data
		return s


l = LinkedList()

l.add( 'a' )
l.add( 'b' )
l.add( 'c' )
print l
l.remove(l.search('b'))
print l
