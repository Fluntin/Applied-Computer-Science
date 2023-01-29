class Node:
    
    def __init__(self, value, left=None, right=None):
        self.left=left
        self.right=right
        self.value=value

class Bintree:
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root,newvalue)

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")
        
# Help functions----------------------------------------------------------------

def putta(root, newvalue):
    if root is None:
        return Node(newvalue)
    
    
    if newvalue > root.value:
        root.right = putta(root.right, newvalue)
    else:
        root.left = putta(root.left, newvalue)
        
    return root
  

#---------------------------------------------------------------------------------------------
def finns (pointer, value):
    
    if pointer==None:
        #No more options 
        return False            
    
    elif value == pointer.value:
        # Found it!
        return (True)
    
    elif value < pointer.value:
        # Call recursive -> left
        return (finns(pointer.left,value))
    
    elif value > pointer.value:
        # Call recursive -> right
        return (finns(pointer.right,value))
#---------------------------------------------------------------------------------------------       
 
 # input:
 #      40
 #     /\
 #    20   50
 #   / \    \
 #  10  30   60
 # /   /  \
 # 5  67  78
 #
 # output: 5 10 20 30 40 50 60 67 78
 # https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python

def skriv (pointer):
    if pointer != None:
        # Call recursive -> left
        skriv(pointer.left)
        print(pointer.value, end=' ')
        # Call recursive -> right
        skriv(pointer.right)
        
        
    
            
                
            
        
 