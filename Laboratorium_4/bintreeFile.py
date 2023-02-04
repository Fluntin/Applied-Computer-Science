class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

class Bintree:
    def __init__(self):
        self.root = None

    def put(self, newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root, newvalue)

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")
        
def putta(p, value):
    if p != None and p.data != value:
        if p.data < value:
            if p.right != None:
                putta(p.right, value)
            else:
                p.right = Node(value)
                
        if p.data > value:
            if p.left != None:
                putta(p.left, value)
            else:
                p.left = Node(value)
    if p == None:
        p = Node(value)
        #print(p.data)
    return p
            
    #när ska man deklarera att value får plats

def skriv(p):
    if p != None:
        skriv(p.left)
        print(p.data)
        skriv(p.right)

def finns(p,value):
    if p == None: 
        return False
    if value == p.data:
        return True
    if value < p.data: 
        return finns(p.left, value)
    if value > p.data: 
        return finns(p.right, value)

def antal(root):
        if root == None: 
            return 0
        else:
            return 1 + antal(root.left) + antal(root.right)
        
if __name__ == '__main__':
    
    #Here ???
    #Låt filen bfs.py utgå från förra labben, som ju har två binärträd.
    # Nu kallar vi dom:
    # 1. -> svenska (ordlistan)
    # 2. -> gamla (dumbarnen)
    
    svenska = Bintree()
    gamla=Bintree()
    
    with open("word3.txt", "r", encoding = "utf-8") as swedishfile:
        for row in swedishfile:
            word = row.strip()                
            if word in svenska:
                gamla.put(word)
            else:
                svenska.put(word)

