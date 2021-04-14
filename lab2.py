import re
import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database='mydatabase'
)

cur = mydb.cursor()
cur.execute('''create table employee(
            id int primary key not null,
            full_name varchar(50) not null,
            salary int not null,
            is_manager int
            );''')
mydb.commit()


class Person:
   def __init__(self, full_name, money,sleepmood,healthRate):
      self.full_name = full_name
      self.money = money
      self.sleepmood = sleepmood
      self.healthRate = healthRate

  
   def sethealthRate(self, healthRate):
       if healthRate>=0 and healthRate<=100:
          self.healthRate=healthRate
       else:
          print('out of range')

   def sleep(self,hours):
      if hours==7:
          self.sleepmood = 'happy'
          print('your sleepmood changed to happy')
      elif hours > 7:
          self.sleepmood = 'lazy'
          print('your sleepmood changed to lazy')
      elif hours < 7:
          self.sleepmood = 'tired'
          print('your sleepmood changed to tired')
      return self.sleepmood

   def eat(self,meals):
       if meals<=3 and meals>=1:
            if meals==3:
                self.healthRate = '100'
                print('your healthRate changed to 100')
            elif meals==2:
                self.healthRate = '75'
                print('your healthRate changed to 75')
            elif meals==1:
                self.healthRate = '50'
                print('your healthRate changed to 50')
            return self.healthRate
       else:
           print('out of range')

   def buy(self,items):
      if items==1:
          self.money-=10
          print('Your money decreased by 10')

# p1=Person('mariam',2000,'happy',75)
# print(p1.healthRate)
# p1.sleep(9)
# print(p1.sleepmood)
# print(p1.healthRate)
# p1.eat(3)
# print(p1.healthRate)
# print(p1.money)
# p1.buy(1)
# print(p1.money)
# p1.sethealthRate(1000)

class Employee(Person):

   def __init__(self,full_name, money,sleepmood,healthRate, id, email, workmood,salary,is_manager):
      Person. __init__(self, full_name, money,sleepmood,healthRate)

      self.id = id
      self.email = email
      self.workmood = workmood
      self.salary = salary
      self.is_manager = is_manager

      sql="INSERT INTO employee (id, full_name, salary,is_manager) Values " \
            "(%s,%s,%s,%s)"
      val = (self.id,self.full_name, self.salary, self.is_manager)
      cur.execute(sql, val)
      print("employee added")  
      mydb.commit()   

    
   def setsalary(self, salary):
       if(salary>=10000):
          self.salary = salary
       else:
          print('out of range')
    
   def getsalary(self):
       return self.salary

   def setemail(self, email):
      if(re.search('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', email)):
         self.email = email
      else:
         print("Invalid Email")



   def work(self,hours):
      if hours==8:
          self.workmood = 'happy'
          print('your workmood changed to happy')
      elif hours < 8:
          self.workmood = 'lazy'
          print('your workmood changed to lazy')
      elif hours > 8:
          self.workmood = 'tired'
          print('your workmood changed to tired')
      return self.workmood

   def sendemail(self,to,subject,sender):
      f=open('email.txt','w')
      f.write(f'This email is sent to : {to} \n')
      f.write(f'This email subject is :{subject} \n')
      f.write(f'This email sender is : {sender} \n')
      f.close()

# e1=Employee('mohamed',2000,'happy',75,2,'mariam@gmail.com','happy',90000,0)
# print(e1.get_employee('1'))
# print(e1.workmood)
# e1.work(10)
# print(e1.workmood)
# e1.setsalary(5000)
# print(e1.salary)
# e1.setemail('mariam')
# e1.sendemail('mariam','python','mohamed')


#association relationship , office=>whole
#Employee=>part
class Office:

   def __init__(self):
       pass
  
   def get_all_employees(self):
       cur.execute('select * from employee')
       rows = cur.fetchall()
       for row in rows:
            print(row)
       mydb.commit()
   
   def get_employee(self,num):
            cur.execute(f'select * from employee where id={num}')
            rows = cur.fetchall()
            for row in rows:
                print(row)
            mydb.commit()


   def hire(self,id,full_name,salary,is_manager):
      sql="INSERT INTO employee (id, full_name, salary,is_manager) Values " \
      "(%s,%s,%s,%s)"
      val = (id,full_name,salary,is_manager)
      cur.execute(sql, val)
      print("employee hired")  
      mydb.commit()  

   def fire(self,num):
      cur.execute(f'delete from employee where id={num}')
      print("employee fired")  
      mydb.commit()

# o=Office()
# print(o.get_all_employees())
# print(o.get_employee('1'))
# print(o.hire(3,'sherif',10000,1))
# # print(o.fire('3'))


ans=True
while ans:
    print ("""
    1.Add a Employees
    2.Get All Employees
    3.Exit/Quit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
       o=Office()
       id = input("Enter your id")
       name = input("Enter your name")
       salary = input("Enter your salary")
       is_manager = input("Enter your is_manager")
       o.hire(id,name,salary,is_manager)
    elif ans=="2": 
       o=Office()
       o.get_all_employees()
    elif ans=="3":
      print("\n Goodbye") 
      ans=False
    elif ans !="":
      print("\n Not Valid Choice Try again") 
      
      
      
mydb.close()
