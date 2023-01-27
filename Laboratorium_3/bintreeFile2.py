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

def putta (root, newvalue):
    # If no root node -> create root node
    if root == None:
        print("Root created")
        return(Node(newvalue))
    #------------------------------------------------- OK
    # Else there exists a root node -> return is always root! -> no changes
    else:
        pointer=root
        if (newvalue < pointer.value):
            
            if pointer.left == None:
                pointer.left=Node(newvalue)
                print("Left node created")
                #Done!
                return (root)
            else:
                # Call recursive -> left
                putta (pointer.left, newvalue)
    
        elif (newvalue > pointer.value):
            
            if pointer.right == None:
                pointer.right=Node(newvalue)
                print("Right nodecreated")
                #Done!
                return (root)
            else:
                # Call recursive -> right
                putta (pointer.right, newvalue)
    #------------------------------------------------- OK   
    
    return (root) 
    #------------------------------------------------- OK  
  

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