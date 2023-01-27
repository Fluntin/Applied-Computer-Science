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
        else:
            # newvalue is already in the tree
            return (root) 
    #------------------------------------------------- OK  
