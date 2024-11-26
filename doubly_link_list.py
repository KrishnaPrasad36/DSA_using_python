class node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start=None):
        self.start=None

    def is_empty(self):
        return self.start==None    

    def insert_at_start(self,data):
        
        n=node(None,data,self.start)
        if not self.is_empty():
            self.start=n
        else:

            self.start=node(None,data,None)    

    def insert_at_last(self,data):
        

        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=node(temp,data,None)
        else:
            self.start=node(None,data,None)
    def search_at(self,data):
        temp=self.start
        while temp.next is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        
            return None
            
    def insert_after(self,temp,data):
        if temp is not None:
            n=node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev=n
            temp.next=n 
       

          
    def delete_first(self):
        temp=self.start
        if temp.prev==None:
            temp.item=None
            temp=temp.next
            temp.prev=None
        else:
            return None

    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next       
                     
list=DLL()
list.insert_at_start(20)
list.insert_at_start(10)
list.insert_after(list.search_at(30),50)
list.insert_at_last(30)
list.insert_at_last(40)
list.print_list()




       
    

        


       

