from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

class IBank(ABC):
    @abstractmethod
    def create_account(self,name:str,agency:str,account:str,initialBalance:float):
        # Creates an bank account
        pass

    @abstractmethod
    def get_account(self, agency:str, account:str):
        # Returns an bank account
        pass

    @abstractmethod
    def deposit(self, agency:str, account:str, ammount:float):
        # Makes a deposit to an account
        pass

    @abstractmethod
    def withdraw(self, agency:str, account:str, ammount:float):
        # Makes a withdraw to an account
        pass

    @abstractmethod
    def get_history(self,agency:str,account:str):
        # Returns account transaction history
        pass

#class IItemRepository(ABC):
#    
#    
#    @abstractmethod
#    def get_all_items(self) -> List[Item]:
#        '''
#        Returns all the itens in the database 
#        '''
#        pass
#    
#    @abstractmethod
#    def get_item(self, item_id: int) -> Optional[Item]:
#        '''
#        Returns the item with the given id.
#        If the item does not exist, returns None
#        '''
#        pass
#    
#    @abstractmethod
#    def create_item(self, item: Item, item_id: int) -> Item:
#        '''
#        Creates a new item in the database
#        '''
#        pass
#    
#    @abstractmethod
#    def delete_item(self, item_id: int) -> Item:
#        '''
#        Deletes the item with the given id.
#        If the item does not exist, returns None
#        '''
#        
#    @abstractmethod
#    def update_item(self, item_id:int, name:str=None, price:float=None, item_type:ItemTypeEnum=None, admin_permission:bool=None) -> Item:
#        '''
#        Updates the item with the given id.
#        If the item does not exist, returns None
#        '''
#        pass
#    
    
