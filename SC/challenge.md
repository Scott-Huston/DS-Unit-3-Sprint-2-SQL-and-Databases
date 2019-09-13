import sqlite3

conn = sqlite3.connect(
    '/Users/scotthuston/Desktop/LS_3.1/SC/northwind_small.sqlite3'
    )

curs = conn.cursor()

find_most_expensive = '''
SELECT ProductName FROM Product ORDER BY UnitPrice DESC LIMIT 10;
'''
curs.execute(find_most_expensive).fetchall()

# Result:
# [('Côte de Blaye',),
#  ('Thüringer Rostbratwurst',),
#  ('Mishi Kobe Niku',),
#  ("Sir Rodney's Marmalade",),
#  ('Carnarvon Tigers',),
#  ('Raclette Courdavault',),
#  ('Manjimup Dried Apples',),
#  ('Tarte au sucre',),
#  ('Ipoh Coffee',),
#  ('Rössle Sauerkraut',)]

avg_hire_age = 'SELECT AVG(HireDate - BirthDate) FROM Employee'
curs.execute(avg_hire_age).fetchall()

# Result:
# [(37.22222222222222,)]

most_expensive_with_supplier = '''
SELECT Product.ProductName, Supplier.CompanyName
FROM Product
LEFT JOIN Supplier
ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC LIMIT 10;
'''
curs.execute(most_expensive_with_supplier).fetchall()

# Result:
# [('Côte de Blaye', 'Aux joyeux ecclésiastiques'),
#  ('Thüringer Rostbratwurst', 'Plutzer Lebensmittelgroßmärkte AG'),
#  ('Mishi Kobe Niku', 'Tokyo Traders'),
#  ("Sir Rodney's Marmalade", 'Specialty Biscuits, Ltd.'),
#  ('Carnarvon Tigers', 'Pavlova, Ltd.'),
#  ('Raclette Courdavault', 'Gai pâturage'),
#  ('Manjimup Dried Apples', "G'day, Mate"),
#  ('Tarte au sucre', "Forêts d'érables"),
#  ('Ipoh Coffee', 'Leka Trading'),
#  ('Rössle Sauerkraut', 'Plutzer Lebensmittelgroßmärkte AG')]

largest_category = '''
SELECT Category.CategoryName
FROM Product
LEFT JOIN Category
ON Product.CategoryId = Category.Id
GROUP BY Category.CategoryName
ORDER BY COUNT(*) DESC LIMIT 1;
'''
curs.execute(largest_category).fetchall()

# Result:
# [('Confections',)]

emp_most_territories = '''
SELECT Employee.FirstName, Employee.LastName
FROM EmployeeTerritory
LEFT JOIN Employee
ON EmployeeTerritory.EmployeeId = Employee.Id
GROUP BY EmployeeId
ORDER BY COUNT(*) DESC LIMIT 1;
'''
curs.execute(emp_most_territories).fetchall()

# Result:
# [('Robert', 'King')]

curs.close()
