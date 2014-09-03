'''
Copyright 2014 AFour Technologies

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

# Author: AFourTech 
# Copyright: 2014 AFour Technologies.

"""
A Exception Function class specialize  for Exception Handling.
this module define following classes:

- `ExceptionInfo`, a Basic Exception information
- `Mapping`, Finding Exception
- `StepConditionEnum`, Related to exception condition
"""

__docformat__ = 'restructuredtext'

import datetime
import os
import sys 
import traceback    
import xml.etree.ElementTree as ET
from enum import Enum


class ExceptionInfo(object):
    """
    Represents a class that provides general information about exception.
    """
    
    message=None
    """ Gets the exception message for exception. """
   
    stackTrace=None 
    """ Gets the stack trace information about exception ."""    
    
    exceptionType=None 
    """ 
    Gets the type of exception. 
    Type of exception:Functional/Environmental/Other.
    """
    
    className=None
    """ Gets the base class name where exception occurred. """
    
    alternateText=None
    """ Gets alternate text for the exception.  """
    
    statusCode=None
    """Gets the status code for the call indicating success or failure.  """
      
exInfo=ExceptionInfo()  


class StepConditionEnum(Enum):
    """
    Enum to find StepCondition type.
    """
    GIVEN =1
    WHEN =2
              
                  
class Mapping(object):
    """
    Mapper Class represents a class that returns description of exception in the form of ExceptionInfo Object.
    """
    xmlFilePath=None
    """ Specify the file path where ExceptionMapping.xml is located. """
    exceptionTypeHashtable=None
    messageHashtable=None
    exceptionType=None
    whenGivenConditionChecker=0
    mainDir=None;
    statusCodeDictionary=None
    statusCodeDictionaryFinder=100
    fileCount=0;
    
    def __init__(self): 
        """
        This method initialize Error Code Dictionary and cache xml file. 
        """      
        Mapping.initializeErrorCodeDict(self)
        Mapping.cacheXMLDocument(self)
        
    
    def initializeErrorCodeDict(self):
        """
        Method to initialize Error codes in dictionary.
        """
        global statusCodeDictionary     
        statusCodeDictionary = {}             
        statusCodeDictionary[100]="Success"
        statusCodeDictionary[101]="An Error has occurred in our library please contact AFourTech for further Information on debugging this error."
        statusCodeDictionary[102]="File Could not be found at following location :" 
        statusCodeDictionary[103]="Syntax Error in file. Please follow proper syntax" 
   
    def cacheXMLDocument(self):  
        """
        Method to cache xml file to Hashtable.
        """
        global statusCodeDictionaryFinder
        global statusCodeDictionary    
        global exceptionTypeHashtable
         
        try:
            if Mapping.xmlFilePath==None:
                packageDir=os.path.dirname(os.path.abspath(__file__))           
                srcDir=os.path.dirname(packageDir)
                global mainDir
                mainDir=os.path.dirname(srcDir)
                xmlFilePath=mainDir+"\\resourses\ExceptionMapping.xml"       
                  
            xmlFile = ET.parse(xmlFilePath)
            exceptionTypeElements = xmlFile.getroot()            
            exceptionTypeHashtable={}
            for exceptionElements in exceptionTypeElements:                 
                messageHashtable={}
                for messageElement in exceptionElements:                          
                    messageHashtable[messageElement.text] = messageElement.get('alternateText')
                exceptionTypeHashtable[exceptionElements.get('text')]=messageHashtable 
            statusCodeDictionaryFinder=100  
               
        except SyntaxError as e1:                    
            statusCodeDictionaryFinder=103
            exInfo.statusCode=statusCodeDictionaryFinder;
        except Exception as e:                    
            statusCodeDictionaryFinder=102
            statusCodeDictionary[statusCodeDictionaryFinder]=statusCodeDictionary[statusCodeDictionaryFinder],xmlFilePath
            exInfo.statusCode=statusCodeDictionaryFinder;
        
       
    def getExceptionInfo(self,exception, stepString=None):
        """
        Function to return information about Exception given by user with step level condition provided as parameter.

        Parameters:
        - `exception`: exception object of Exception class.
        - `stepString`: stepString   String such as Given ,When ,Then and And
                
        returns: object of ExceptionInfo class.
        """      
        global whenGivenConditionChecker
        whenGivenConditionChecker=0
        global statusCodeDictionaryFinder
        global statusCodeDictionary        
        exceptionType=None
        try:  
                        
            #To check stepString is null or not.   
            if  stepString!=None:
                stepString=stepString.upper();
                if (StepConditionEnum.GIVEN.name==stepString) or (StepConditionEnum.WHEN.name==stepString):                   
                    exceptionType="Environmental"          ''          
                    whenGivenConditionChecker=1
                    
            if(statusCodeDictionaryFinder==100):                                                
                #To read content from XML file.           
                for exceptionElementName in exceptionTypeHashtable:                                
                    messageTable=exceptionTypeHashtable[exceptionElementName]
                    for message in messageTable:                                    
                        if (message == str(exception)):                                              
                            exceptionType=exceptionElementName                     
                            if (exceptionType=="Functional")and(whenGivenConditionChecker==1):                                       
                                exInfo.alternateText = ""                                                                         
                            else:
                                exInfo.alternateText=messageTable[message]                                                    
                            if(whenGivenConditionChecker==1):                                   
                                exceptionType="Environmental"
                            break                                                                                 
                #to get exception class name ,message and alternateText    
                exc_type, exc_obj, exc_tb = sys.exc_info()
                exInfo.message=exception
                exInfo.className=exc_type.__name__
                if exceptionType==None:
                    exceptionType="other"                            
                if exInfo.alternateText==None:              
                    exInfo.alternateText="";
                # to get stack Trace    
                stackdetails=str(traceback.format_exc())
                exInfo.stackTrace=stackdetails
                # to write stack trace into text file 
                global mainDir
                logDir=mainDir+"\StackLog"
                if not os.path.exists(logDir):
                    os.makedirs(logDir)                 
                os.chdir(logDir)
                now = datetime.datetime.utcnow()                
                time=now.strftime("%Y-%m-%d %I-%M-%S")+"-"+str(now.microsecond)
                logFileName="StackLog "+str(time)+".log"  
                if os.path.isfile(logFileName):                                                        
                    Mapping.fileCount=Mapping.fileCount+1;                                                
                    logFileName="StackLog "+str(time)+"_"+str(Mapping.fileCount)+".log"                   
                file=open(logFileName,'w')                
                file.write(str(stackdetails))
                file.close()       
        except Exception as e1:           
            statusCodeDictionaryFinder=101
        #to set exception status code and  type
        exInfo.statusCode=statusCodeDictionaryFinder,statusCodeDictionary[statusCodeDictionaryFinder]
        exInfo.exceptionType=exceptionType
        return exInfo 
