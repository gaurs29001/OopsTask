import re
from datetime import datetime
import logger  # module being imported
lg = logger.logger()


def dateChecker(in_date):
    try:
        date_check = bool(datetime.strptime(in_date, "%Y-%m-%d"))
    except ValueError as ve:
        lg.logfile_error(ve)
    else:
        lg.logfile_info('DateChecker done')


def emailChecker(in_email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    check = lambda email: re.search(regex, email)
    return bool(check(in_email))
