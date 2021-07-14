import numpy as np
import random
import pandas as pd

df = pd.read_csv('../execrise/customer_full')

def get_dict(df):
    location_dict={}
    for location, next_location in zip(df['location'],df['next_location']):
        if location in location_dict.keys():
            location_dict[location].append(next_location)
        else:
            location_dict[location] = [next_location]
    yield location_dict


class Customer:
    
    '''Customer that moves in a supermarket.
    parameters: 
    cust_id:custumer id
    cur_state: current location
    next_state : next location
    is_active : bool if cur state checkout, is active is False
    '''
    
    def __init__(self,cust_id,state='entrance'): # the start point is by default entrance
        self.cust_id = cust_id
        self.state = state
        self.is_active = True
  
    def __repr__(self): 
        return 'customerid is %d, current state is %s'%(self.cust_id,self.state)
        
    def next_state(self):
        
        '''1. changing self.cur_loc. We want to move the customer, keep updating the cur_loc is the way.
        2. update weight random choice with probilities and combination of all 5 locations'''
        all_status = list(df['location'])
        self.state = np.random.choice(all_status)
        step = 0
        for i in range(step):    
            self.state.append(np.random.choice(location_dict[state_init[i]]))
        #self.state = random.choice(['dairy','fruit_vagi','spices','drink','checkout'])
        print(self.cust_id,self.state)
    
    def check_active(self):
        
        if self.state == 'checkout':
            self.is_active = False
            
        else:
            self.is_active = True