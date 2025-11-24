import sqlite3

con = sqlite3.connect('Institute.db')
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Students(
    id INT, 
    name TEXT,
    surname TEXT, 
    age INT, 
    city TEXT)""")
cur.execute("""CREATE TABLE IF NOT EXISTS Courses(
    id INT,
    name TEXT,
    time_start TEXT,
    time_end TEXT)""")
cur.execute("""CREATE TABLE IF NOT EXISTS Student_courses(
    student_id INT,
    course_id INT)""")
cur.executemany("""INSERT INTO Students  VALUES (?,?,?,?,?)""",
   [ (1, 'Max', 'Brooks', 24, 'Spb'),
    (2, 'John', 'Stones', 15, 'Spb'),
    (3, 'Andy', 'Wings', 45, 'Manhester'),
    (4, 'Kate', 'Brooks', 34, 'Spb')])
cur.executemany("""INSERT INTO Courses (id,name,time_start,time_end)VALUES (?,?,?,?)""", [
    (1, 'python', '2021-07-21', '2021-08-21'),
    (2, 'java', '2021-07-13', '2021-08-16')])
cur.executemany("""INSERT INTO Student_courses VALUES (?,?)""",
[(1, 1),
                (2, 1),
                (3, 1),
                (4, 2)])
cur.execute("SELECT * FROM Students WHERE age > 30")
print(cur.fetchall())
cur.execute("SELECT * FROM Student_courses WHERE course_id = 1")
print(cur.fetchall())
cur.execute("SELECT * FROM Students WHERE id <= 2")
print(cur.fetchall())
con.commit()
con.close()
