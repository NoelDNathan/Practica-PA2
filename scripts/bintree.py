from collections import deque

class BinTree:

    def __init__(self,v=None,left=None,right=None):
        """
        Warning, an empty tree is NOT None
        An empty tree is a BinTree with self.__node equal to None
        The object created by a call to BinTree() is an empty tree
        Requirement: If the value v is None, so must be the two children.
        """
        assert (v is None and left is None and right is None) or v is not None
        if v is None:
            self.__node = None
        else:
            left  = left  if left  is not None else BinTree()
            right = right if right is not None else BinTree()
            self.__node = {"v": v, "fesq": left, "fdre": right}
            
    # Getters
    def get_root(self):
        """
        Pre: It is assumed that the BinTree is NOT empty
        returns the value at the root of the BinTree
        """
        return self.__node["v"]
    
    def get_left(self):
        """
        Pre: It is assumed that the BinTree is NOT empty
        returns the left child of the BinTree
        """
        return self.__node["fesq"]
    
    def get_right(self):
        """
        Pre: It is assumed that the BinTree is NOT empty
        returns the right child of the BinTree
        """
        return self.__node["fdre"]

    # Setters
    def set_root(self,v):
        """
        changes the value at the root of the BinTree
        """
        assert(v is not None)
        if not self.empty():
            self.__node["v"] = v
        else:
            self.__node =  {"v": v, "fesq": BinTree(), "fdre": BinTree()}
        
    def set_left(self,left):
        """
        Pre: left is a BinTree and the BinTree is not empty
        changes the left child of the BinTree
        """
        self.__node["fesq"] = left
        
    def set_right(self,right):
        """
        Pre: right is a BinTree and the BinTree is not empty
        changes the right child of the BinTree
        """
        self.__node["fdre"] = right
        
    # Other operations
    def empty(self):
        """
        returns True if the BinTree is empty, False in other case
        """
        return self.__node == None
        
    def leaf(self):
        """
        returns True if the BinTree is a leaf, False if not.
        """
        return self.get_left().empty() and self.get_right().empty()

    # Traversals 
    def preorder(self):
        """
        returns a list with the elements of the BinTree, ordered 
        as is specified in the definition of the pre-order traversal.
        """
        if self.empty():
            return []
        else:
            return [self.get_root()] + self.get_left().preorder() + self.get_right().preorder()

    def postorder(self):
        """
        returns a list with the elements of the BinTree, ordered 
        as is specified in the definition of the post-order traversal.
        """
        if self.empty():
            return []
        else:
            return self.get_left().postorder() + self.get_right().postorder() + [self.get_root()]
        
    def inorder(self):
        """
        returns a list with the elements of the BinTree, ordered 
        as is specified in the definition of the in-order traversal.
        """
        if self.empty():
            return []
        else:
            return self.get_left().inorder() + [self.get_root()] + self.get_right().inorder()

    def levelorder(self):
        """
        returns a list with the elements of the BinTree, ordered 
        as is specified in the definition of the levels-order traversal.
        """
        if self.empty():
            return []
        else:
            resultat = []
            q = deque()
            q.append(self)
            while len(q) > 0:
                tt = q.popleft()
                resultat.append(tt.get_root())
                if not tt.get_left().empty():
                    q.append(tt.get_left())
                if not tt.get_right().empty():
                    q.append(tt.get_right())
            return resultat

