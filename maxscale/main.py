#Matt Bennett
#6/11/2023 CNE370
#Script to query a sharded database
#Big thanks to Celine who did the queries.
#Used the tabulate website heavily. https://www.askpython.com/python-modules/tabulate-tables-in-python 

import mysql.connector
from tabulate import tabulate

db = mysql.connector.connect(host="172.23.0.4", port="4000", user="maxuser", password="maxpwd")
cursor = db.cursor()


print('The largest zipcode in zipcodes_one:')
cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 1;")
result = cursor.fetchone()
print(result[0])


print('All zipcodes where state = KY:')
cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one WHERE State = 'KY';")
results = cursor.fetchall()
list1 = [result[0] for result in results if result[0] != ""]
cursor.execute("SELECT Zipcode FROM zipcodes_two.zipcodes_two WHERE State = 'KY';")
results = cursor.fetchall()
list1 += [result[0] for result in results if result[0] != ""]
list1split = [list1[i:i+10] for i in range(0, len(list1), 10)]
print(tabulate(list1split, tablefmt='grid'))


print('All zipcodes between 40000 and 41000:')
cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one WHERE zipcode BETWEEN 40000 AND 41000;")
results = cursor.fetchall()
list2 = [result[0] for result in results if result[0] != ""]
cursor.execute("SELECT Zipcode FROM zipcodes_two.zipcodes_two WHERE zipcode BETWEEN 40000 AND 41000;")
results = cursor.fetchall()
list2 += [result[0] for result in results if result[0] != ""]
list2split = [list2[i:i+10] for i in range(0, len(list2), 10)]
print(tabulate(list2split, tablefmt='grid'))


print('The TotalWages column where state = PA:')
cursor.execute("SELECT TotalWages FROM zipcodes_one.zipcodes_one WHERE state = 'PA';")
results = cursor.fetchall()
list3 = [result[0] for result in results if result[0] != ""]
cursor.execute("SELECT ALL TotalWages FROM zipcodes_two.zipcodes_two WHERE state = 'PA';")
results = cursor.fetchall()
list3 += [result[0] for result in results if result[0] != ""]
list3split = [list3[i:i+10] for i in range(0, len(list3), 10)]
print(tabulate(list3split, tablefmt='grid'))
