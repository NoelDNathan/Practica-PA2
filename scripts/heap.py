from operator import lt, gt

class Heap:

    def __init__(self, items=[], cmp=lt): # per defecte tenim un min-heap
        assert cmp == lt or cmp == gt  # només acceptem aquestes funcions
        self.__cmp = cmp
        # __heapify crea i inicialitza la variable d'instància __lst
        self.__heapify(items)

    # Operacions del heap

    def show(self):
        return self.__lst
    
    def inserir(self, x):
        (self.__lst).append(x)
        self.__surar(len(self.__lst)-1)
        
    def obtenir(self):
        # Pre: lst no pot ser buida
        assert not self.buit()
        primer = self.__lst[1]
        darrer = (self.__lst).pop()
        if len(self.__lst) > 1:
            self.__lst[1] = darrer
            self.__enfonsar(1)
        return primer  
            
    def buit(self):
        return len(self.__lst) == 1 and self.__lst[0] == None

    # Operacions *privades*
        
    def __heapify(self,ll = []):
        self.__lst = [None]  # element a ignorar en la posició 0
        for e in ll:
            (self.__lst).append(e)
        darrer_index = len(self.__lst)-1
        for i in range(darrer_index//2, 0, -1):
            self.__enfonsar(i)

    def __surar(self,i):
        # Pre: self.__lst no és buida
        #      1 <= i < len(lst)
        if i > 1 and self.__cmp(self.__lst[i],self.__lst[i//2]):
            self.__lst[i], self.__lst[i // 2] = self.__lst[i // 2], self.__lst[i]  
            self.__surar(i // 2)                         
            
    def __enfonsar(self,i):
        # Pre: self.__lst no és buida
        #      1 <= i < len(self.__lst)
        n = len(self.__lst)-1      
        c = 2*i             
        if c <= n:          
            if c+1 <= n and self.__cmp(self.__lst[c+1],self.__lst[c]):
                c += 1                        
            if self.__cmp(self.__lst[c],self.__lst[i]):
                self.__lst[i],self.__lst[c] = self.__lst[c],self.__lst[i] 
                self.__enfonsar(c)              

