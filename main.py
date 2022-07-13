import menu
import pre_setupfile as ps
import logger  # module being imported
lg = logger.logger()
lg.logfile_creation('oops')

if __name__ == '__main__':
    ps.pre_setup_db()
    ps.pre_setup_student()
    ps.pre_setup_course()
    ps.pre_setup_course_detail()
    menu.menu()
