class Employee:
    def set_info(self,id,name,salary,position):
        self.id=id
        self.name=name
        self.salary=salary
        self.position=position

    def get_info(self):
        print("Id:",self.id)
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Position:",self.position)

s1= Employee()
s1.set_info(1,"Siddhesh",20000,"Software Testing")
s1.get_info()



# write python class innentory with attributes like item_id,item_name,stock_count,price & methods like add_item &check_item,delete_item use Dictionary to store item details where the key is item_id the value is dictonary containing the item_name,stock_count & price

class Innentory:
    def __init___(self,item_id,item_name,stock_count,price):
        self.item_id=item_id
        self.item_name=item_name
        self.stock_count=stock_count
        self.price=price

    