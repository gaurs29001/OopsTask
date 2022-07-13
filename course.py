import logger
import dbconnection as db
lg = logger.logger()


class Course:

    def course_details(self):
        try:
            db.mysql_select(f"select * from ineuron.course")
        except Exception as e:
            print(e)
            lg.logfile_error(e)
        else:
            lg.logfile_info("All course records shown successfully")


    def course_assignment(self, student_rollno, course_id):
        try:
            db.mysql_query_exec(f"insert into ineuron.student_course_detail (courseid, student_id) values ({student_rollno}, {course_id})")
        except Exception as e:
            print(e)
            lg.logfile_error(e)
        else:
            print("Course assignment done successfully")
            lg.logfile_info("Course assignment done successfully")


    def course_assignment_details(self):
        try:
            db.mysql_select(f"select st.firstname, st.lastname, cs.coursename from ineuron.student st , ineuron.course cs, ineuron.student_course_detail csd where st.rollno = csd.student_id and csd.courseid = cs.courseid")
        except Exception as e:
            print(e)
            lg.logfile_error(e)
        else:
            lg.logfile_info("All course records shown successfully")
