import sqlite3
import mysql.connector
import base64

# connection = mysql.connector.connect(user='root', password='root',
#                                      host='127.0.0.1',
#                                      database='python_base')
# cursor = connection.cursor()

con = sqlite3.connect(r'/Users/nikitazaytsev/Desktop/my_data.db')
cursor = con.cursor()

cursor.execute('''
SELECT * FROM employees;
''')
print(cursor.fetchall())

cursor.execute('''
SELECT *
  FROM employees
 WHERE first_name = 'David';

''')
print(cursor.fetchall())

cursor.execute('''
SELECT *
  FROM employees
 WHERE job_id = 1;

''')
print(cursor.fetchall())

cursor.execute('''
SELECT *
  FROM employees
 WHERE department_id = 50 AND salary > 4000;

''')
print(cursor.fetchall())

cursor.execute('''
SELECT *
  FROM employees
 WHERE department_id = 20 OR department_id = 30;

''')
print(cursor.fetchall())

cursor.execute('''
SELECT *
  FROM employees
 WHERE first_name LIKE '%a';

''')
print(cursor.fetchall())

cursor.execute('''
SELECT *
  FROM employees
 WHERE     (department_id = 50 OR department_id = 80)
       AND commission_pct IS NOT NULL;

''')
print(cursor.fetchall())

cursor.execute('''
SELECT *
  FROM employees
 WHERE first_name LIKE '%n%n%';

''')
print(cursor.fetchall())

cursor.execute('''
SELECT *
  FROM employees
 WHERE first_name LIKE '%_____%';

''')
print(cursor.fetchall())

cursor.execute('''
SELECT *
  FROM employees
 WHERE salary BETWEEN 8000 AND 9000;

''')
print(cursor.fetchall())

cursor.execute('''
SELECT *
  FROM employees
 WHERE first_name LIKE '%\%%' ESCAPE '\\';

''')
print(cursor.fetchall())

cursor.execute('''
SELECT DISTINCT manager_id
  FROM employees
 WHERE manager_id IS NOT NULL;

''')
print(cursor.fetchall())

cursor.execute('''
SELECT first_name || '(' || LOWER (job_id) || ')' employee FROM employees;
''')
print(cursor.fetchall())
