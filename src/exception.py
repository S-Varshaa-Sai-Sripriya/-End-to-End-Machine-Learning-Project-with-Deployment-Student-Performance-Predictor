import sys
from typing import Any
import types
from src.logger import logging

def error_message_detail(error, error_detail:types.ModuleType):
    _,_, exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno,str(error))
        
    return error_message

    
    
class CustomException(Exception):
    def __init__(self, error_message, error_detail: types.ModuleType):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    #@Override   
    def __str__(self) -> str:
        return str(self.error_message)
    

        
        