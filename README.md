# **Object Oriented Programming in Python**

## **Contents**

1.   [Classes and Instances](#01-classes-and-instances)
2.   [Class Variables](#02-class-variables)
3.   [Classmethods and Staticmethods](#03-class-and-static-methods)
4.   [Creating Subclasses](#04-inheritance-creating-subclasses)
5.   [Special (Magic/Dunder) Methods](#05-special-magicdunder-methods)
6.   [Property Decorators-Getters, Setters and Deleters](#06-property-decorators--getters-setters-and-deleters)



# **NOTES**


---


## **01. Classes and Instances**

* ###  **Classes**
  Classes are the building blocks in Object Oriented Programming. Classes allow us to logically group our data and functions in a way that is easy to reuse and also easy to build upon if need be.



* ### **Instances**
  An Instance is a concrete occurrence of any object. Classes can be seen as blueprints from which you create your Instances.

---


## **02. Class Variables**

Attributes or methods specific to a class are called Class attributes

For example :

```
 class Employee:
    num_of_emps = 0                 
    raise_amount = 1.04            
    def __init__(self,fname,lname,salary):                             
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.num_of_emps += 1
```

Here ``` no_of_emps ``` and ```raise_amount ``` are class attributes. These are used when certain values need to be set outside a function.



---

## **03. Class and Static Methods**

* ###  **Class Methods**
  Class methods:takes the first argument as the class, these are created using decoraters @classmethod.
  Creating class method using decorater
 
  ``` 
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount 
   ```

* ###  **Static Methods**
  A static method can't access or modify the class state. Static methods does not automatically passes the first argument as  self these act as regular functions ,we add them to the class as they have logical connection with the class in order to create the static method the decorater @staticmethod is used.


---

## **04. Inheritance-Creating Subclasses**

* ###  **Inheritance**
  Inheritance allows us to inherit attributes and methods from the parent class
this is used to create sub classes and get the functionality of our parent class without writing the same thing more than once withhout affecting parent class in any way.

* ###  **Creating-Subclasses**
  Syntax for creating subclass  --> class classname(inherited from)
  
  **For example:**
  
  ```
  class Developer(Employee): #subclass Developer inherited from class Employee
        raise_amount = 1.05
        def __init__(self,fname,lname,salary,prog_lang):
            super().__init__(fname,lname,salary)
            self.prog_lang = prog_lang
  ```
---
## **05. Special (Magic/Dunder) Methods**
Special methods also known as magic methods these methods allow us to emulate some built-in within python and it's also how we implement operator overloading

For example: 

> ```print(4+6)``` and ```print('a'+'b')``` ,these two statements will have different result still using same operator but getting different results this is known as operator overloading.

 Special methods use double underscore ```__init__``` also known as dunder
two more common dunder special methods are 
dunder :
* ```repr()``` : is met to be an unambiguous representation of the object and should be used for thing like logging and debugging etc....
* ```str()``` : is a more of a readable representation of an object and is meant to be used as a display to the end user.

---
## **06. Property Decorators -Getters, Setters and Deleters**
 Property Decoraters allow us to define a method but allow us to access it as a attribute.
* ###  **Getters**
  A Getter is a method that gets the value of a property.
* ###  **Setters**
  A Setter is a method that sets the value of a property

  > Setting ```fname``` and ```lname``` using Setter from a string.

  ``` 
   @fullname.setter 
    def fullname(self,name):
        fname,lname = name.split(" ")
        self.fname = fname
        self.lname = lname
   ```

* ###  **Deleters**
  A Deleter is a method that deletes the value of a property.<br><br>
  > Deleter for ```fullname```
   ```
    @fullname.deleter
    def fullname(self): 
        print('Name Deleted!')
        self.fname = None
        self.lname = None
   ```
---

## **CREDITS**

Thanks to Mr. Corey Schafer for his amazing playlist: [Python OOP Tutorials - Working with Classes](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)


