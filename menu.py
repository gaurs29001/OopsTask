import dbconnection
import logger  # module being imported
import company
import course
import student
lg = logger.logger()


def menu():
    """Function to User Interaction"""
    try:
        while True:
            print("         1. Company Details")
            print("         2. Student Details")
            print("         3. Course Details")
            print("                 enter # to exit")
            choice = input("Enter your choice: ")
            lg.logfile_info(f"Menu choice entered is {choice}")
            if choice == "1":
                while True:
                    print("         1. Company Name")
                    print("         2. Update Company Name")
                    print("                 enter 0 for previous menu")
                    c1 = company.Company()
                    company_choice = input("Enter your choice: ")
                    lg.logfile_info(f"Company menu choice entered is {company_choice}")
                    if company_choice == "1":
                        c1.getCompanyName()
                    elif company_choice == "2":
                        new_name = input("Enter New Name: ")
                        c1.setCompanyName(new_name)
                    elif company_choice == "0":
                        break
                    else:
                        print("Enter the correct choice!!!")
            elif choice == "2":
                while True:
                    print("         1. Print all Student Details")
                    print("         2. Search any Student Details by name")
                    print("         3. Enter new Student details")
                    print("                 enter 0 for previous menu")
                    student_choice = input("Enter your choice: ")
                    lg.logfile_info(f"Student menu choice entered is {student_choice}")
                    s1 = student.Student()
                    if student_choice == "1":
                        s1.student_details()
                    elif student_choice == "2":
                        search_name = input("Enter the student name to be searched: ")
                        s1.student_search(search_name)
                    elif student_choice == "3":
                        s1.student_entry()
                    elif student_choice == "0":
                        break
                    else:
                        print("Enter the correct choice!!!")
            elif choice == "3":
                while True:
                    print("         1. Print all courses details")
                    print("         2. Assign course to any Student")
                    print("         3. Current Student Course assignment")
                    print("                 enter 0 for previous menu")
                    detail_choice = input("Enter your choice: ")
                    lg.logfile_info(f"Course Menu choice entered is {detail_choice}")
                    c1 = course.Course()
                    if detail_choice == "1":
                        c1.course_details()
                    elif detail_choice == "2":
                        in_student = int(input("Enter student roll no: "))
                        in_course = int(input("Enter course id: "))
                        c1.course_assignment(in_student, in_course)
                    elif detail_choice == "3":
                        c1.course_assignment_details()
                    elif detail_choice == "0":
                        break
                    else:
                        print("Enter the correct choice!!!")
            elif choice == '#':
                print("Thanks :)")
                break
            else:
                print("Enter correct choice!!!")
    except TypeError as te:
        lg.logfile_error(te)
    except ValueError as ve:
        lg.logfile_error(ve)
    except Exception as e:
        lg.logfile_error(e)
    else:
        lg.logfile_info("Program successfully executed")
    finally:
        dbconnection.mysql_dbconnect().close()
        lg.logfile_info("Database closed successfully")