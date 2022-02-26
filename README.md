# CS361-Grab-Data-Microservice

Description:

           Provide two types of functions to grab corresponding website data (Note: Use the provided text file to communicate & Refer to Assignment 2)

           1. Receive the time zone (-12 ~ +14), and grab the time data from https://www.utctime.net/
           
           Note: Please only enter the value in the range specified above. As for UTC, enter either +0 or -0.
           
           2. Receive a word, and grab the word definition data from https://dictionaryapi.dev/
           
           Note: Please only enter "one" word, or you will receive an error message 
           
           Warning: Please do not leave blank in the provided file
           
How to run:

           First, run the python file
          
           $ python3 GrabData.py
           
           Second, change the word (and save) in the provided text file to either a value between -12 ~ +14 (include the sign) or a single word, then you can get the corresponding data in the same text file.
           
           For example,
           
           Enter +0 in the provided file and save, and you will get the current UTC time
           
           Eg. 20:14:01
               26th Saturday February 2022
           
           Enter a word hello, then you will get the definition of that word in the JSON format written in the text file
           
           Please refer to the example provided in the following website: https://dictionaryapi.dev/

           
