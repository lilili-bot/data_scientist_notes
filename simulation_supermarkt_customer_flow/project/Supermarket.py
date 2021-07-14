import pandas as pd
import time
import datetime
from Customer import Customer
import numpy as np
import random

df_time = pd.read_csv('../execrise/df_time.csv')

class Supermarket:
    
    '''
    1. class Supermarket
    2. Add method, add customer, by applying number of customer into supermarket
    3. add method to move around the customer, compose method change_aisle from customer
    '''
    # starts at 7:00am, self.minutes is adding when the time passing. 
    def __init__(self):
        #self.num_customer = num_customer
        self.customer = []
        self.minutes = datetime.datetime.now()
        self.last_id = 0
        self.open = True 
    
    def __repr__(self):
        return 'There are still total %d customer left.'%(len(self.customer))
    
    def get_time(self):
        
        '''current time in HH:MM format'''
        
        self.minutes
        
        
        print(self.minutes)

    
    def print_customer(self):
        
        """print all customers with the current time and id in CSV format.
        """
        '''
        save all added customer in a df then save to csv.
        1. first create a empty table.
        2. append new data in it. 
        '''
        pass
    
    def next_minute(self):

        # self.minutes = self.minutes + datetime.timedelta(minutes = 60)
        #self.minutes += datetime.timedelta(minutes=10)

        if self.minutes < pd.to_datetime('20:40:00'):

            self.minutes += datetime.timedelta(minutes = 10)

        else:
            self.open = False

        print(self.minutes)

        return self.minutes, self.open

     

    def add_new_customer(self,number): 
        
        '''randomly creates new customers.'''
        
        customer_per_min = round(df_time['sum'].mean())
        minutes = 10
        lam = customer_per_min * minutes
        customer_number = np.random.poisson(lam, 10)
        customer_num = np.random.choice(customer_number)
        
        for n in range(1, customer_num+1):
            
            self.customer.append(Customer(n)) # composition
            
        return self.customer
                    
            
    def moving_around(self):
        for customer in self.customer:
            customer.next_state()
            
            '''need to change the location again, when the cur_loc is check_out, the customer is not any more in the s
            uper market.'''
    
    def remove_ex_customer(self):        
        
        rest_customers = []
        
        for customer in self.customer:
            '''
            running check_active attribution from Customer Class, return the status of the check_active
            '''
            customer.check_active()
            
            if customer.is_active:
                
                rest_customers.append(customer)
                
        self.customer = rest_customers
        print('The rest customer is %s'%(self.customer))

    def checkout_customer(self):

        if self.open == False:

            customer.next_state = 'checkout'

        print('All rest customer are checkedout.')


        
