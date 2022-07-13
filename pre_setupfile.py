import dbconnection


def pre_setup_db():
    in_db = dbconnection.mysql_dbconnect()
    cursor = in_db.cursor()
    cursor.execute(f"Drop database if exists ineuron ")
    cursor.execute(f"create database if not exists ineuron")
    in_db.commit()


def pre_setup_student():
    in_db = dbconnection.mysql_dbconnect()
    cursor = in_db.cursor()
    cursor.execute(f"CREATE TABLE ineuron.student (FirstName varchar(20) DEFAULT NULL, LastName varchar(20) DEFAULT NULL, DoB date DEFAULT NULL, Enrollment_date datetime DEFAULT CURRENT_TIMESTAMP, Address varchar(100) DEFAULT NULL, email varchar(50) DEFAULT NULL, rollno int NOT NULL AUTO_INCREMENT, PRIMARY KEY (rollno))")
    cursor.execute(f"INSERT INTO ineuron.student (FirstName,LastName,DoB,Address,email) VALUES ('Gaurav', 'Sharma', '2000-01-03', 'India', 'gs1@gmail.com')")
    cursor.execute(f"INSERT INTO ineuron.student (FirstName,LastName,DoB,Address,email) VALUES ('Ajay', 'Yadav', '1990-01-01', 'Australia', 'ajydv@gmail.com')")
    in_db.commit()


def pre_setup_course():
    in_db = dbconnection.mysql_dbconnect()
    cursor = in_db.cursor()
    cursor.execute(f"create table ineuron.student_course_detail (courseid int, student_id int, primary key (courseid, student_id))")
    cursor.execute(f"insert into ineuron.student_course_detail (courseid, student_id) values (1, 1)")
    cursor.execute(f"insert into ineuron.student_course_detail (courseid, student_id) values (2, 2)")
    in_db.commit()


def pre_setup_course_detail():
    in_db = dbconnection.mysql_dbconnect()
    cursor = in_db.cursor()
    cursor.execute(f"create table ineuron.course (courseid int auto_increment,coursename varchar(50), fees decimal(8,2), start_date date, end_date date, primary key (courseid))")
    cursor.execute(f"insert into ineuron.course (coursename, fees, start_date, end_date) values('Full Stack Data Science', 17000, '2022-05-17', '2023-01-31')")
    cursor.execute(f"insert into ineuron.course (coursename, fees, start_date, end_date) values('Full Stack Data Analysis', 10000, '2022-06-01', '2022-10-31')")
    cursor.execute(f"insert into ineuron.course (coursename, fees, start_date, end_date) values('Full Stack Front-End Developer', 12000, '2022-07-01', '2023-03-31')")
    in_db.commit()
    in_db.close()