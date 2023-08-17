from typing import Dict, Optional, List

#from ..enums.item_type_enum import ItemTypeEnum
from ..entities.account import BankAccount
from .bank_repository_interface import IBank
#from .item_repository_interface import IItemRepository


class IBankMock(IBank):
    __accounts: Dict[tuple,BankAccount]

    def __init__(self):
        self.__accounts = {}

    def create_account(self,name:str,agency:str,account:str,initialBalance:float):
        newAccount = BankAccount(name,agency,account)
        self.__accounts[(agency,account)] = newAccount

    def get_account(self, agency:str, account:str) -> Optional[BankAccount]:
        return self.__accounts.get((agency,account),None)

    def deposit(self, agency:str, account:str, ammount:float):
        acc = self.get_account(agency,account)
        if acc is None: return
        return acc.Deposit(ammount)

    def withdraw(self, agency:str, account:str, ammount:float):
        acc = self.get_account(agency,account)
        if acc is None: return
        return acc.Withdraw(ammount)

    def get_history(self, agency:str, account:str):
        acc = self.get_account(agency,account)
        if acc is None: return
        return acc.history

#class ItemRepositoryMock(IItemRepository):
#    items: Dict[int, Item]
#    
#    def __init__(self):
#        self.items = {
#            1: Item(name="Barbie", price=48.90, item_type=ItemTypeEnum.TOY, admin_permission=False),
#            2: Item(name="Hamburguer", price=38.00, item_type=ItemTypeEnum.FOOD, admin_permission=False),
#            3: Item(name="T-shirt", price=22.95, item_type=ItemTypeEnum.CLOTHES, admin_permission=False),
#            4: Item(name="Super Mario Bros", price=55.00, item_type=ItemTypeEnum.GAMES, admin_permission=True)
#        }
#        
#    def get_all_items(self) -> List[Item]:
#        return self.items.values()
#    
#    def get_item(self, item_id: int) -> Optional[Item]:
#        return self.items.get(item_id, None)
#    
#    def create_item(self, item: Item, item_id: int) -> Item:
#        
#        self.items[item_id] = item
#        return item
#    
#    def delete_item(self, item_id: int) -> Item:
#        item = self.items.pop(item_id, None)
#        return item
#        
#        
#    def update_item(self, item_id:int, name:str=None, price:float=None, item_type:ItemTypeEnum=None, admin_permission:bool=None) -> Item:
#        item = self.items.get(item_id, None)
#        if item is None:
#            return None
#        
#        if name is not None:
#            item.name = name
#        if price is not None:
#            item.price = price
#        if item_type is not None:
#            item.item_type = item_type
#        if admin_permission is not None:
#            item.admin_permission = admin_permission
#        self.items[item_id] = item
#        
#        return item
#        
#    
#    
