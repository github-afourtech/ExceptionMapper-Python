'''
Created on Aug 7, 2014
@author: afour
'''
import AFourTech.ExceptionMapper.ExceptionMapperClass as ex
from array import *
class Program(object):
    exinfo=ex.ExceptionInfo()
    expMapping=ex.Mapping()
    x=1
    y=4
    my_array = array('i',[1,2,3,4])
    
    try:
        z=4/0
        my_array[4]      
    except Exception as e:           
       
        exinfo=expMapping.getExceptionInfo(e)  
        '''exinfo=expMapping.getExceptionInfo(Exception("Stack Overflow"))  '''
        print("Status          =",exinfo.statusCode) 
        print("Message         =",exinfo.message)
        print("Class Name      =",exinfo.className) 
        print("Exception Type  =",exinfo.exceptionType)
        print("Alternate Text  =",exinfo.alternateText)
        print("Stack Trace     =",exinfo.stackTrace)          
        print("-----------------------------------------------------------------------------")                   
   
    try:
        z=4/0
        my_array[4]
    except Exception as e:           
        exinfo=expMapping.getExceptionInfo(e, "then") 
        '''exinfo=expMapping.getExceptionInfo(Exception("Stack Overflow"),"then")    '''
        print("Status          =",exinfo.statusCode) 
        print("Message         =",exinfo.message)
        print("Class Name      =",exinfo.className) 
        print("Exception Type  =",exinfo.exceptionType)
        print("Alternate Text  =",exinfo.alternateText)
        print("Stack Trace     =",exinfo.stackTrace)          
        print("-----------------------------------------------------------------------------")                   
    
    try:
        z=4/0
        '''my_array[4]'''
    except Exception as e:           
        exinfo=expMapping.getExceptionInfo(e, "when") 
        '''exinfo=expMapping.getExceptionInfo(Exception("Stack Overflow"),"when")   '''
        print("Status          =",exinfo.statusCode) 
        print("Message         =",exinfo.message)
        print("Class Name      =",exinfo.className) 
        print("Exception Type  =",exinfo.exceptionType)
        print("Alternate Text  =",exinfo.alternateText)
        print("Stack Trace     =",exinfo.stackTrace)          
        print("-----------------------------------------------------------------------------")                   
   
    try:
        z=4/0
        '''my_array[4]'''
    except Exception as e:           
        exinfo=expMapping.getExceptionInfo(e, "given")    
        '''exinfo=expMapping.getExceptionInfo(Exception("Stack Overflow"),"given") '''
        print("Status          =",exinfo.statusCode) 
        print("Message         =",exinfo.message)
        print("Class Name      =",exinfo.className) 
        print("Exception Type  =",exinfo.exceptionType)
        print("Alternate Text  =",exinfo.alternateText)
        print("Stack Trace     =",exinfo.stackTrace)          
        print("-----------------------------------------------------------------------------")                   
   

    try:
        z=4/0
        '''my_array[4]'''
    except Exception as e:           
        exinfo=expMapping.getExceptionInfo(e, "abcd")
        '''exinfo=expMapping.getExceptionInfo(Exception("Stack Overflow"),"abcd")  '''  
        print("Status          =",exinfo.statusCode) 
        print("Message         =",exinfo.message)
        print("Class Name      =",exinfo.className) 
        print("Exception Type  =",exinfo.exceptionType)
        print("Alternate Text  =",exinfo.alternateText)
        print("Stack Trace     =",exinfo.stackTrace)          
        print("-----------------------------------------------------------------------------")                   
   
        