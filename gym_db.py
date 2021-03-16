#Imports
import mysql.connector
from mysql.connector import errorcode
import csv

#Connection details
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Ambition2020",
    #database = "björkman"
)

DB_NAME = "gym_db"

cursor = mydb.cursor()

#Create a database that does not exist
def create_database(cursor, DB_NAME):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

#Creat table to the new db
def create_table(cursor):
    customer = "CREATE TABLE `customer` ("\
            "   `user_id` mediumint(10) unsigned NOT NULL auto_increment,"\
            "    `name` varchar(255) default NULL,"\
            "    `person_number` varchar(13) default NULL,"\
            "    `age` varchar(10) default NULL,"\
            "    `email` varchar(255) default NULL,"\
            "    `phone` varchar(100) default NULL,"\
            "    `membership` varchar(255) default NULL,"\
            "    `pt` varchar(255) default NULL,"\
            "    PRIMARY KEY (`user_id`)"\
            "    ) ENGINE=InnoDB"

    employee = "CREATE TABLE `employee` ("\
            "   `employee_id` mediumint(10) unsigned NOT NULL auto_increment,"\
            "    `name` varchar(255) default NULL,"\
            "    `age` varchar(13) default NULL,"\
            "    `address` varchar(25) default NULL,"\
            "    `phone` varchar(100) default NULL,"\
            "    `title` varchar(100) default NULL,"\
            "    `coaching` varchar(100) default NULL,"\
            "    `pt` varchar(100) default NULL,"\
            "    PRIMARY KEY (`employee_id`)"\
            "    ) ENGINE=InnoDB"

    workout_class = "CREATE TABLE `workout_class` ("\
            "   `id_number` mediumint(10) unsigned NOT NULL auto_increment,"\
            "    `name` varchar(25) default NULL,"\
            "    `place` varchar(20) default NULL,"\
            "    `description` varchar(100) default NULL,"\
            "    `time` varchar(50) default NULL,"\
            "    `pt` varchar(25) default NULL,"\
            "    PRIMARY KEY (`id_number`)"\
            "    ) ENGINE=InnoDB"

    membership = "CREATE TABLE `membership` ("\
            "   `membership_id` mediumint(10) unsigned NOT NULL auto_increment,"\
            "    `membership_type` varchar(25) default NULL,"\
            "    `membership_period` varchar(25) default NULL,"\
            "    `signup_fee` varchar(25),"\
            "    `membership_amount` varchar(50) default NULL,"\
            "    PRIMARY KEY (`membership_id`)"\
            "    ) ENGINE=InnoDB"        

    #gym = "CREATE VIEW 'gym' AS("\
            

    try:
        print("Creating table: ")
        cursor.execute(customer)
        cursor.execute(employee)
        cursor.execute(workout_class)
        cursor.execute(membership)
        #cursor.execute(gym)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

#Insert files to the table
def insert_into_table(cursor):
    insert_sql = ["INSERT INTO customer (user_id, name, person_number, age, email, phone, membership, pt)"
    "VALUES (1246,'Fiona Baker','19450120-0768','76','molestie.Sed@turpisnec.net','04 68 00 15 37', 'Senior','Janife Allstar');",
    "INSERT INTO customer (user_id, name, person_number, age, email, phone, membership, pt)"
    "VALUES (3456,'Kasimir Horn','19760604-1700','45','non.quam@venenatis.com','07 72 08 27 40','Activ','Clark Kent');",
    "INSERT INTO customer (user_id, name, person_number, age, email, phone, membership, pt)"
    "VALUES (1637,'James Holland','19930517-2745','28','sem@molestieorcitincidunt.ca','06 77 12 89 88','Student','null');",
    "INSERT INTO customer (user_id, name, person_number, age, email, phone, membership, pt)"
    "VALUES (3526,'Gray Bowman','19860814-3691','35','justo.Praesent@risus.edu','03 04 35 97 70','Activ','null');",
    "INSERT INTO customer (user_id, name, person_number, age, email, phone, membership, pt)"
    "VALUES (2564,'Tarik Durham','19561128-2817','65','Curabitur.egestas@mi.com','06 11 79 46 81','Semi-Activ','null');",
    "INSERT INTO customer (user_id, name, person_number, age, email, phone, membership, pt)"
    "VALUES (5363,'Ariana Richardson','19500523-2257','71','Morbi.sapien@lorbiacumsan.co.uk','08 47 40 40 85','Senior','Clark Kent');",]

    for query in insert_sql:
        try:
            print("SQL query {}: ".format(query), end='')
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            # Make sure data is committed to the database
            mydb.commit()
            print("OK")

    insert_sql = ["INSERT INTO employee (employee_id, name, age, address, phone, title, coaching, pt)"
    "VALUES (12396,'Clark Kent','33','whatstraat 24','05 66 50 14 37', 'coach','body pump','pt');",
    "INSERT INTO employee (employee_id, name, age, address, phone, title, coaching, pt)"
    "VALUES (37534,'Karin Blek','40','villastreet 53','05 74 45 23 70','receptionist','null','null');",
    "INSERT INTO employee (employee_id, name, age, address, phone, title, coaching, pt)"
    "VALUES (76430,'Charl Grenland','54','dhushevag 67','08 99 15 89 48','janitor','null','null');",
    "INSERT INTO employee (employee_id, name, age, address, phone, title, coaching, pt)"
    "VALUES (46384,'Janife Allstar','23','straatgata 322','06 45 35 67 97','coach','yoga','pt');",
    "INSERT INTO employee (employee_id, name, age, address, phone, title, coaching, pt)"
    "VALUES (12149,'Carla Gonsales','37','gatugatavag 98','34 11 79 46 81','manager','null','null');",
    "INSERT INTO employee (employee_id, name, age, address, phone, title, coaching, pt)"
    "VALUES (74628,'Ruth Gran','28','bhaastreet 63','05 82 44 23 90','coach','pilates','pt');",
    "INSERT INTO employee (employee_id, name, age, address, phone, title, coaching, pt)"
    "VALUES (25639,'Frans Hupp','45','allstreet 12','06 95 45 24 80','coach','spinning','pt');",]

    for query in insert_sql:
        try:
            print("SQL query {}: ".format(query), end='')
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            # Make sure data is committed to the database
            mydb.commit()
            print("OK")

    insert_sql = ["INSERT INTO workout_class (id_number, name, place, description, time, pt)"
    "VALUES (102,'body pump','group room','strength training in group form, with barbell','tuesdays at 10:00 a.m', 'Clark Kent');",
    "INSERT INTO workout_class (id_number, name, place, description, time, pt)"
    "VALUES (210,'spinning','bicycle room','exercise that are performed on an exercise bike','wednesdays at 4:30 p.m', 'Frans Hupp');",
    "INSERT INTO workout_class (id_number, name, place, description, time, pt)"
    "VALUES (250,'yoga','yoga room','yoga class with customized physical yoga exercises','fridays at 8:00 a.m','Janife Allstar');",
    "INSERT INTO workout_class (id_number, name, place, description, time, pt)"
    "VALUES (520,'pilates','group room','provides body control, improved posture, focus and inner peace','saturdays at 10:00 a.m','Ruth Gran');",]

    for query in insert_sql:
        try:
            print("SQL query {}: ".format(query), end='')
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            # Make sure data is committed to the database
            mydb.commit()
            print("OK")

    insert_sql = ["INSERT INTO membership (membership_id, membership_type, membership_period, signup_fee, membership_amount)"
    "VALUES (1,'activ','6 months','500:-','249');",
    "INSERT INTO membership (membership_id, membership_type, membership_period, signup_fee, membership_amount)"
    "VALUES (2,'semi activ','3 months','300:-','199');",
    "INSERT INTO membership (membership_id, membership_type, membership_period, signup_fee, membership_amount)"
    "VALUES (3,'student','1 year','250:-','149');",
    "INSERT INTO membership (membership_id, membership_type, membership_period, signup_fee, membership_amount)"
    "VALUES (4,'senior','1 month','null','99');",]

    for query in insert_sql:
        try:
            print("SQL query {}: ".format(query), end='')
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            # Make sure data is committed to the database
            mydb.commit()
            print("OK")



#Menu for choices
def menu():
    while True:
        print("\n>Menu<\n1. Name and age of all customers. \n"
        "2. Show the name and ID of the customers who have activ membership. \n"
        "3. Choose a customer and find out what membership they have. \n"
        "4. Create a VIEW Gym and get to see what is important for the customer to know when they want to sign a membership. \n"
        "5. Show the name and phonenumber of the customers who have a specific coach. \n"
        "6. Find out the average age for each membership type \n"
        "7. Id-number for the workout class, place and instructor name \n"
        "\n")
        user_inp = (input("Please choose one option: "))

        #Name and age of all customers
        if (user_inp == "1"):
            query_1 = "SELECT name, age FROM customer;"
            cursor.execute(query_1)
            print("\n  >>> Name and age of customers <<<\n")
            for (name, age) in cursor:
                #for a in name:
                    print("Name: {:<20} Age: {:<20}".format(name, age))
            print("-----------------------------------")

        # Show the name and user_id of the customers who have 'Activ' membership_type
        elif (user_inp == "2"):
            query_2 = "SELECT customer.name, user_id, membership_type FROM customer, membership WHERE membership_type = membership AND membership='Activ'"
            cursor.execute(query_2)
            for (name, user_id, membership_id) in cursor:
                print("Name: {:<20} \nUser ID: {:<20}\nMembership type: {:<20}\n".format(name,user_id, membership_id))
            print("-----------------------------------")

        #JOIN Choose a customer and find out what membership they have
        elif (user_inp == "3"):
            query3 = "SELECT name FROM customer"
            cursor.execute(query3)
            print("\nCustomers name ")
            for (name) in cursor:
                for a in name:
                    print("-> {}".format(a))
            customers_name = input("\nWrite the name of one of the customers: ")
            query_3_1 = f"SELECT membership_type FROM membership JOIN customer ON customer.name = '{customers_name}' and customer.membership = membership.membership_type;"
            cursor.execute(query_3_1)
            for a in customers_name:
                for (membership_type) in cursor:
                    for b in membership_type:
                        print("\nMembership type: {}".format(b))
            print("-----------------------------------")

        #Create a VIEW
        elif (user_inp == "4"):
            query4 = "CREATE VIEW `gym` AS\n SELECT membership_type, membership_period, membership_amount FROM membership;"
            cursor.execute(query4)
            #Use a View
            query4_1 = "SELECT membership_type, membership_period, membership_amount FROM gym;"
            cursor.execute(query4_1)
            for (membership_type, membership_period, membership_amount) in cursor:
                print("Membership type: {:<15} Membership period: {:<10} Membership amount: {:<10}".format(membership_type, membership_period, membership_amount))
            print("-----------------------------------")
     
        #Show the name and phonenumber of the customers who have a specific coach
        elif (user_inp == "5"):
            query5 = "SELECT name, phone, pt FROM customer WHERE customer.pt='Clark Kent';"
            cursor.execute(query5)
            for (name, phone, pt) in cursor:
                print("Name: {:<20} Phone: {:<15} Personal trainer: {}".format(name, phone, pt))
            print("-----------------------------------")
            
        #Find out the average age of our members and employees
        elif (user_inp == "6"):
            query6 = "SELECT membership, AVG(customer.age) FROM customer GROUP BY membership;"
            cursor.execute(query6)
            for (membership, average) in cursor:
                print("Membership: {:<15} Average: {}".format(membership, average))
            print("-----------------------------------")

        #Id number for the workout_class, place and instructor name
        elif (user_inp == "7"):
            query7 = "SELECT workout_class.id_number, place, employee.name FROM workout_class JOIN employee ON employee.name = workout_class.pt;"
            cursor.execute(query7)
            for (id_number, place, name) in cursor:
                print("Workclass id-number: {:<8} Place: {:<15} PT name: {:<15}".format(id_number, place, name))
            print("-----------------------------------")
    

#Show the error if database does not exist
try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor, DB_NAME)
        print("Database {} created successfully.".format(DB_NAME))
        mydb.database = DB_NAME

        #Tables
        create_table(cursor)
        insert_into_table(cursor)

    else:
        print(err)

menu()

cursor.close()
mydb.close()