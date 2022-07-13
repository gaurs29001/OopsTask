import dataentry_checker as dc  # modules being imported
import logger
import dbconnection as db
lg = logger.logger()


class Student:


    def student_entry(self):
        try:
            self.firstname = input("Enter FirstName: ")
            self.lastname = input("Enter LastName: ")
            self.dob = input("Enter Date of birth (YYYY-MM-DD): ")
            if dc.dateChecker(self.dob):
                raise Exception('Date check failed')
            self.email = input("Enter Email: ")
            if not dc.emailChecker(self.email):
                raise Exception('Email check failed')
            self.address = input("Enter Address: ")
        except Exception as e:
            print(e)
            lg.logfile_error(e)
        else:
            try:
                db.mysql_query_exec(f"insert into ineuron.student ( FirstName, LastName, DoB, email, Address) values ('{self.firstname}', '{self.lastname}', '{self.dob}', '{self.email}', '{self.address}')")
            except Exception as e:
                print(e)
                lg.logfile_error(e)
            else:
                print("Student record successfully created")
                lg.logfile_info("Student record successfully created")

    def student_details(self):
        try:
            db.mysql_select(f"select * from ineuron.student")
        except Exception as e:
            print(e)
            lg.logfile_error(e)
        else:
            lg.logfile_info("All student records shown successfully")

    def student_search(self, search_term):
        try:
            db.mysql_select(f"select * from ineuron.student where upper(concat(firstname,lastname)) like upper('%{search_term}%')")
        except Exception as e:
            print(e)
            lg.logfile_error(e)
        else:
            lg.logfile_info("Requested student records shown successfully")