# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:08:36 2020

@author: Amir_Ranjouriheravi(71313)
"""


class customers:
    
    def __init__(self, name, cash=0):
        self.name = name
        self.cash = cash   
    
    class stock:
        
        @classmethod
        def __init__(self, kind, price, Quan_1=0):
            self.kind = kind
            self.price = price
            self.quant = Quan_1
            
    class share:
        
        @classmethod
        def __init__(self, kind_1, Quan_2=0):
            self.kind = kind_1
            self.quant = Quan_2

    S = stock("HFM", 20)
    mf1 = share("BRT")                 
    mf2 = share("GHT")        
    
    
    def addCash(self, amount):
        self.cash = self.cash + amount
        return self.cash
    
    
    def withdrawCash(self, amount_2):
        self.cash = self.cash - amount_2
        return self.cash
    
    
    def buystock(self, quantity, kind_2):
        if  kind_2 == "HFM":
            self.stock.quant = quantity
            self.cash = self.cash - self.stock.price * quantity
        
    def buymutualfund(self, quantity_2, kind):
        self.cash = self.cash - 1 * quantity_2
        self.share.quant = quantity_2 
        if  kind == "BRT" :
            global quant_BRT
            quant_BRT =  quantity_2
            return quant_BRT
        if  kind == "GHT" :
            global quant_GHT
            quant_GHT = quantity_2
            return quant_GHT
    
    def check_balance(self):
        if self.cash < 0:
            print("Sorry! You can not go over to your budget constraint!")
        if self.cash >= 0:
            print(f"Do not worry!\nYour cash amount is positive: {self.cash}")
               
            
    def portfolio(self): 
        print(f"Dear {self.name},\n cash:{self.cash}\n stock:{self.stock.quant} HFM\n mutual funds:\n {quant_BRT_after_sell} BRT\n {quant_GHT_after_sell} GHT")

    def sellstock(self, quantity_3, kind_3):
        import random
        B = random.uniform(10, 30)
        if kind_3 == "HFM":
            self.stock.quant = self.stock.quant - quantity_3
            self.cash = self.cash + quantity_3 * B
        
    def sellmutualfund(self, quantity_4, kind_4):
        import random
        A = random.uniform(0.5, 1.5)
        self.cash = self.cash + A * quantity_4
        self.share.quant = self.share.quant - quantity_4 
        if  kind_4 == "BRT" :
            global quant_BRT_after_sell
            quant_BRT_after_sell = quant_BRT - quantity_4
            return quant_BRT_after_sell
        if  kind_4 == "GHT" :
            global quant_GHT_after_sell
            quant_GHT_after_sell = quant_GHT - quantity_4
            return quant_GHT_after_sell

    def check_portfolio(self):
        if quant_GHT_after_sell < 0 or quant_BRT_after_sell < 0 or self.stock.quant< 0 :
            print("It is not possible to sell more than you have! change your portfolio!!!")
            
        

#The following commands are written only for testing- (The numbers are different from example of assisgnment.)
            
        
customer_1 = customers('Mr.heravi')
customer_1.addCash(1000)
customer_1.withdrawCash(400)
customer_1.buystock(10, "HFM")
customer_1.buymutualfund(300, "BRT")
customer_1.buymutualfund(50, "GHT")
customer_1.sellstock(4, "HFM")
customer_1.sellmutualfund(280, "BRT")
customer_1.sellmutualfund(10, "GHT")
print(customer_1.check_balance())
print(customer_1.check_portfolio()) 
print(customer_1.portfolio())       
        
        