#Python Object Oriented Programming
#why classes?
#They logically allow us to group our data and functions as they are easy to use and easy to build if need in

#functions used in classes are known as methods

#simple class

class Employee:
    #CLass variables are those who are shared among the all instances of the same class,holds the same value for each instances
    num_of_emps = 0                 #class variable for number of employee
    raise_amount = 1.04             #class variable which can be accessed by all the instances of the class 
    def __init__(self,fname,lname,salary):                             #constructor or the initializer ,recieve the first parameter as instance of the class
    # pass                                         # in order to left emoty a class or function for the time being
        self.fname = fname
        self.lname = lname
        self.salary = salary
        #for each employee we create through the init method we increment our num_of_emps count by 1
        #since the init method runs everytime we create the new employee
        Employee.num_of_emps += 1
        #here we use Employee.num_of_emps instead of self cuz,there is no such case where the total number of employee will be different for each instances
    
    #here only instance is used to create the fullname method
    @property # fullname() can be used as a attribute w/o braces
    def fullname(self):                                             #Each method in the class will take the instance as the first paramter 
        return f"{self.fname} {self.lname}"                          #here we will use the self so that we can use this method with every instance of the class
    
    #setter decorator for fullname
    @fullname.setter  #setting fname and lname using setter from a string
    def fullname(self,name):
        fname,lname = name.split(" ")
        self.fname = fname
        self.lname = lname

    #deleter for fullname
    @fullname.deleter
    def fullname(self): 
        print('Name Deleted!')
        self.fname = None
        self.lname = None

    @property
    def email(self):   #property decorater for email to access it as a attribute
        return f"{self.fname}.{self.lname}@company.com"                                             
    def apply_raise(self): #method for class for annual raise of emoloyee using class variable instead of instance variable since raise will be same for each emoloyee
        # also the class variable can only be accessed'by instances of that class or the class itself
        self.salary = int(self.salary * self.raise_amount) 
        #self here in the gives us the ability to change the single instance if we wanted to,also it will allow any sub class to overwite the constant if we wanted to
    
    #special dunder repr() and str() methods
    def __repr__(self):
        return f"Employee({self.fname} ,{self.lname} ,{self.salary})" #returning the string reprensenting our dunder init method
    
    def __str__(self):
        return f"{self.fullname()}, {self.email})" #more readable for end user
    
    def __add__(self,other):  #special dunder add method
        return self.salary + other.salary
    
    def __len__(self):
        return len(self.fullname())
  
    #creating class method using decorater
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        fname,lname,salary = emp_str.split('-')
        return cls(fname,lname,salary) #--> using cls inside our class method instead of Employee (it is exact same thing)
    
    @staticmethod
    def is_workday(day): #making use of datetime module to grab week days
        if day.weekday() == 5 or day.weekday() == 6:  #if it is weekend return false
            return False
        return True  

class Developer(Employee): #subclass Developer inherited from class Employee
        raise_amount = 1.05
        def __init__(self,fname,lname,salary,prog_lang):
            #Emoloyee.__init__(fname,lname,salary) -->this can also be used but becomes more specific but un usable with multiple inheritance
            super().__init__(fname,lname,salary) #this will pass the fname,lname,salary to parent class init method and let that class handel thoses argument
            self.prog_lang = prog_lang

class Manager(Employee):#manager subclass who supervises employees
    def __init__(self,fname,lname,salary,employees=None): #employess -->list of employees manager supervises,not passing directly the empty list (mutable object) as default argument
        super().__init__(fname,lname,salary)
        if employees is None:
            self.employess = []
        else:
            self.employees = employees

    def add_emp(self,emp): #adding new employees for supervision
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp): #removing employees who were no more supervised
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self): #get all employees a manager supervises
        for emp in self.employees:
            print('*',emp.fullname())

#class:- A blue print for creating instances

# emp_1 = Employee()                                #creating instances of a class 
# emp_2 = Employee()          

# print(emp_1,emp_2)                                #both will have unique memory locations

#Instance variables contain data that is unique to each instance.

#manually creating instance variables

# emp_1.fname = 'John'
# emp_1.lname = 'Smith'
# emp_1.email = 'john.smith@company.com'
# emp_1.salary = 50000

# emp_2.fname = 'Jeff'
# emp_2.lname = 'Christ'
# emp_2.email = 'jeff.christ@company.com'
# emp_2.salary = 60000

# print(emp_2.email)
# print(emp_1.email)

emp_1 = Employee('John','Smith',50000)                     #instance is automatically passed as we call our init method
emp_2 = Employee('Jeff','Christ',60000)  

# print(Employee.num_of_emps)         #it will run for each instances we create through init method

# print(emp_2.email)
# print(emp_1.email)

#two types to print the full names of the employess
# print("{} {}".format(emp_1.fname,emp_1.lname))
# print("{} {}".format(emp_2.fname,emp_2.lname))

# print(f"{emp_1.fname}{emp_1.lname}")
# print(f"{emp_2.fname}{emp_2.lname}")

#self in method fullname is important to pass as emp_1 will be passed as instance of this class to the method fullname() ,so self describe the instance of the class
# print(emp_1.fullname())
# print(emp_2.fullname())



#when we call the method with instance of class like emp_1.fullname() need not to pass self to the method it does it on its own
#But when we call an instance to the class itself like Emplpyee.fullname() we need to pass the self as it doesn't know about 
# what instance we need to run our method with so we do have to pass the instance

# emp_1.fullname()
# print(Employee.fullname(emp_1))

#applying the apply_raise method using instances
# print(emp_1.salary)
# print(emp_2.salary)
# emp_1.apply_raise()
# emp_2.apply_raise()
# print(emp_2.salary)

#accessing the class variable through class itself
# print(Employee.raise_amount)

#on accessing an class attribute on an instance it will check if that instance contains that attribute
#or if the instance doesn't contains the variable than it checks within the class or any other class it inherits from contains the attribute

#printing the name space for the emp instance to check which attributes are associated with it
# print(emp_1.__dict__)
#accessing the class variable thorugh instances
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

#printing the namespace for the class
# print(Employee.__dict__)

#chaning the class variable raise_amount using the class
# Employee.raise_amount = 1.05
# print(emp_1.raise_amount)

#changing the class variable for the particular instance of class
# emp_1.raise_amount = 1.06
# now this will add the raise_amount to the instance as the variable 
# print(emp_1.__dict__)
#here emp_1.raise_amount will return the raise_amount variable from its own namespace before searching in the class namespace
# print(emp_1.raise_amount)



#static methods,regular methods and class methods

#regular methods: automatically takes instance as the first argument in order to take class as the first argument we use class methods
#class methods:takes the first argument as the class, class methods are created using decoraters @classmethod

# using the class method to manipulate the raise of employee
# Employee.set_raise_amt(1.05)  # -->automatically recieves the class

# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

#class methods can also be used by instances for eg:-

# emp_1.set_raise_amt(1.05) #not used
# This is change the value of raise_amount for both the class and instances
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

#class methods as alternative constructors
#passing employee details as string seperated by hyphen and splitting them using split function and passing into Employee
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-90000'
emp_str_3 = 'Loren-Makael-85000'

# fname,lname,salary = emp_str_1.split('-')
# new_emp_1 = Employee(fname,lname,salary)

# print(new_emp_1.email)
# print(new_emp_1.salary)

#doing the same with alternative 
new_emp_1 = Employee.from_string(emp_str_1) #creating new emp  using alternative constructor from_string
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

# print(new_emp_1.email)
# print(new_emp_1.salary)
# print(new_emp_2.email)
# print(new_emp_2.salary)
# print(new_emp_3.email)
# print(new_emp_3.salary)


#static methods does not automatically passes the first argument as clas or the self
#these act as regular functions ,we add them to the class as they have logical connection with the class
#in order to create the static method the decorater is used --> @staticmethod
#for a method to be a static method which doesn't access 'class or a instance in the function

#using a static method
# import datetime
# my_date = datetime.date(2016,7,15)

# print(Employee.is_workday(my_date))

# Subclasses and Inheritance
#inheritance allows us to inherit attributes and methods from the parent class
#this is used to create sub classes and get the functionality of our parent class without writing the same thing more than once withhout affecting parent class in any way
#syntax for creating subclass  --> class classname(inherited from)

dev_1 = Developer('John','Smith',50000,'Python')                     #instance is automatically passed as we call our init method
dev_2 = Developer('Jeff','Christ',60000,'Java')

# print(dev_1.salary)
# dev_1.apply_raise()  #applying change to the developer class will have no effect upon parent class Employee
# print(dev_1.salary)

#when instansiated our developer it first looked for the init method in the developer class since it was empty that time, then python will continue this chain of inheritance until it find for what its looking for
#this chain is called the method resolution order 

# print(help(Developer)) #gives method resoultion order

# print(dev_1.email)
# print(dev_1.prog_lang)


mgr_1 =Manager('Miachel','Clinton',90000,[dev_1])
mgr_2 =Manager('Jordan','Phillips',95000,[])

# print(mgr_1.email)

# mgr_1.add_emp(dev_2)
# # mgr_1.print_emps()
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()
# mgr_2.print_emps()


#python has 2 builtin functions:
#isinstance --> will tell us if a object is a instance of class
# print(isinstance(mgr_1,Manager))
#issubclass --> will tell us if a class is subclass of another 
# print(issubclass(Developer,Employee))

#Special methods also known as magic methods these methods allow us to emulate some built-in within python and it's also how we implement operator overloading
# for eg: print(4+6) and print('a'+'b') ,these two statements will have different result still using same operator but getting different results this is known as operator overloading
#special methods use double underscore __init__ also known as dunder
#two more common dunder special methods are 
# dunder repr() : --> is met to be an unambiguous representation of the object and should be used for thing like logging and debugging etc....
# dunder str() : --> is a more of a readable representation of an object and is meant to be used as a display to the end user
 
#we should have an repr() method as min coz if we have an repr() method without str() then calling str() on an object will just use repr() as a fall back
#repr() : thumb rule in creating this method is to display somthing that u can copy and paste in the python code that would recreate that smaje object

# print(repr(emp_1))
# print(str(emp_1))
# print(emp_1)
#running funtions above are directly calling those special mtehods mentioned down below
# print(emp_1.__str__())
# print(emp_1.__repr__())

#some special methods for arthimetic
#print(1+7) --> #this uses the special dunder add method mentioned below
#print(int.__add__(1,7)) 

#print(str.__add__('a','b')) #special dunder method for string concatenation 

#above mentioned example is best suited for operator overloading

#a dunder add method for adding two employee salary
# print(emp_1+emp_2)

# dunder lenght method
# print(len('eight')) #uses special dunder method used below
# print('eight'.__len__())

#print(len(emp_1))

#NotImplemented is returned whenever an object doesn't know how to handle the operation it will passes to another object but if none of them know how to handle it will eventually throw a error


#Property Decoraters ,Getters and Setters and Deleters
#lets' say one need to change the emp_1 
emp_1.fname ='Jennifer'

# print(emp_1.fname)
# print(emp_1.email) #it will remain unaffected
# print(emp_1.fullname()) #fullname will be updated since it grabes the current last name and first name from the init method

#property Decoraters allow us to define a method but allow us to access it as a attribute
# using email as a attribute with property decoreter

# print(emp_1.fname)
# print(emp_1.email) 
# print(emp_1.fullname())

#setter 
# for eg: by setting an fullname we want to change the first name ,last name ,and email by using setter

emp_1.fullname = 'Peter Jhonson'


print(emp_1.fname)
print(emp_1.email) 
print(emp_1.fullname)
