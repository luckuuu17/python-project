import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='user'
)
mycursor=mydb.cursor()

class TravelDocument:
    def _init_(self, name, city, address,phone_no, issue_date, expiry_date):
        self.name = name
        self.city = city
        self.address = address
        self.phone_no=phone_no
        self.issue_date = issue_date
        self.expiry_date = expiry_date

    def _str_(self):
        return f"{self.name },{self.city},{self.address},{self.phone_no},{self.issue_date},{self.expiry_date}"


class DocumentManager:
    def createDB():
        try:
             mycursor.execute("CREATE DATABASE LUCKY")
             print("DataBase ")
        except Exception:
            print('Already Created DB')

    def useDB():
        try:
            mycursor.execute("use Lucky")
            print('using DB')
        except Exception:
            print('issue')
    def createTravel():
        try:
            mycursor.execute('create table lucky1(name varchar(20),city varchar(10), address varchar(20),phone_no varchar(10), issue_date varchar(10), expiry_date varchar(10))')
            print("table created")
        except Exception:
            print('Already created table')

    def insertTravel():
        try:
            mycursor.execute("INSERT INTO lucky1 (name, city, address,phone_no, issue_date, expiry_date) VALUES ('Vijay', 'Bly','patel nagar',20.7.24,25.7.24)")
            mydb.commit()
            print('Inserted successfully')
        except Exception as e:
            print('Error occurred:', e)

    def updateTravel():
        try:
            mycursor.execute("UPDATE lucky1 set city='chennai' where name='bly'")
            mydb.commit()
            print('Updated successfully')
        except:
            print('Already Inserted Data into Table')
    def deleteTravel():
        try:
            mycursor.execute("delete from lucky1 where name='vijay'")
            mydb.commit()
            print('Deleted Successfully!')
        except Exception:
            print('Issue while Deleting')
            

td=DocumentManager
td.createDB()
td.useDB()
#td.createTravel()
#td.insertTravel()
#td.updateTravel()
td.deleteTravel()
