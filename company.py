import logger  # module being imported
lg = logger.logger()


class Company:
    __companyname = "ineuron"  # private class variable

    def getCompanyName(self):  # encapsulation
        print(f"Parent Company name is {Company.__companyname}")
        lg.logfile_info(f"Parent Company name is {Company.__companyname}")

    def setCompanyName(self, new_name):  # encapsulation
        try:
            if type(new_name) == str:
                Company.__companyname = new_name
                print(f"New Company name is {Company.__companyname}")
                lg.logfile_info(f"New Company name is {Company.__companyname}")
            else:
                raise TypeError("New Company name entered is not a string")
        except TypeError as te:
            lg.logfile_error(te)
        else:
            lg.logfile_info("New company name has been updated")
