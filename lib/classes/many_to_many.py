class Coffee:
    all = []
    
    def __init__(self, name):
        self.name = name
        Coffee.add_to_all(self)
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if not hasattr(self,'name'):
            if(isinstance(name,str) and len(name) >= 3):
                self._name = name
            else:
                raise ValueError("Coffee name must be string over 3 characters long")
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        customerList = []
        for order in self.orders():
            if order.customer not in customerList:
                customerList.append(order.customer)
        return customerList
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        prices = [order.price for order in self.orders()]
        return sum(prices) / self.num_orders()
    
    @classmethod
    def add_to_all(cls,coffee):
        cls.all.append(coffee)

class Customer:
    all = []
    
    def __init__(self, name):
        self.name = name
        Customer.add_to_all(self)
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if(isinstance(name,str) and 1 <= len(name) <= 15):
            self._name = name
        else:
            raise ValueError("customer name must be string between 1 and 15 characters long")
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        coffee_list = []
        for order in self.orders():
            if order.coffee not in coffee_list:
                coffee_list.append(order.coffee)
        return coffee_list
    
    def create_order(self, coffee, price):
        return Order(self,coffee,price)
    
    @classmethod
    def add_to_all(cls,customer):
        cls.all.append(customer)
        
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.add_to_all(self)
        
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,price):
        if hasattr(self, 'price'):
            raise Exception("Order prices cannot be changed")
        if(isinstance(price,float) and 1 <= price <= 10):
            self._price = price
        else:
            raise ValueError("Order price must be floating point number between 1 and 10 inclusive")
    
    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self,customer):
        if isinstance(customer,Customer):
            self._customer = customer
        else:
            raise ValueError("Customer must be an object of the Customer class")
        
    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee,Coffee):
            self._coffee = coffee
        else:
            raise ValueError("Coffee must be an object of the Coffee class")
        
    @classmethod
    def add_to_all(cls,order):
        cls.all.append(order)