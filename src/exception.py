import sys
from logger import logging

def error_message_detail(error_message, error_detail):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    
    error_message = "Error occurred in Python script [{0}] at line [{1}]: {2}".format(
        file_name, line_number, str(error_message)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message
    
if __name__ == "__main__":
    try:
        a = 1/0
    except ZeroDivisionError as e:
        logging.info("Divide by Zero")
        raise CustomException(e,sys)