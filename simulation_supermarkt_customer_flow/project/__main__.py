
from Customer import Customer
from Supermarket import Supermarket

'''
get class from Customer and Supermarket try to simulate the customer. 
The for loop is not yet working, it works only once. 
'''

if __name__ == '__main__':
    
    Rewe = Supermarket()

    while Rewe.open:
        Rewe.get_time()
        Rewe.next_minute()
        Rewe.add_new_customer(10)
        Rewe.moving_around()
        Rewe.remove_ex_customer()
        Rewe.customer
        print(Rewe)

        