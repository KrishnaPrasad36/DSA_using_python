class node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start=None):
        self.start=None

    def is_empty(self):
        self.start=None    

    def insert_at_start(self,data):
        
        n=node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n    

    def insert_at_last(self,data):

        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            n=node(self,temp.prev,data,None)
        else:
            self.start=n
    def search(self,data):
        temp=self.start
        while temp.next!=None:
            if temp.item==data:
                return temp
            else:
                return None
    def insert_after(self,temp,data):
        if temp.next!=None:
            n=node(self,temp,data,temp.next)
            temp.next=n
        else:
            self.start.next=n   
    def delete_first(self):
        temp=self.start
        if temp.prev==None:
            temp.item=None
            temp=temp.next
            temp.prev=None
        else:
            return None

            
                     





       
    

        


       

