# Course: CS361 - Software Engineering I
# Author: Cheng Ying Wu
# Grab Data Microservice
# Version: 1.1
# Description: Provide two types of functions to grab corresponding website data (Note: Use the text file to communicate)
#             1. Receive the time zone (-12 ~ +14), and grab the time data from https://www.utctime.net/
#             2. Receive a word, and grab the word definition data from https://api.dictionaryapi.dev/api/v2/entries/en/

import urllib.request as ur
import ssl
import time


while True:
    # Sleep for 1 second
    time.sleep(1)
    
    # Open the file grabdata-service.txt
    data_file = open("./grabdata-service.txt", "r", encoding="utf-8")
    # Read the file
    lines = data_file.readlines()
        
    # Check whether the line in the file begins with "+" or "-"
    if lines[0][0] == "+" or lines[0][0] == "-":
        print("Activate Grab Time Service!")
        
        # If yes, get the time zone in string type
        time_zone = lines[0][0] + str(int(lines[0][1:3]))
        
        # Check whether it is UTC and specify the corresponding URL to grab
        if time_zone == "+0" or time_zone == "-0":
            url = "https://www.utctime.net/"
        else:
            url = "https://www.utctime.net/utc" + time_zone + "-time-now"
        
        # Solve the SSL: CERTIFICATE_VERIFY_FAILED error
        context = ssl._create_unverified_context()

        # Send the request to the specified website and get the response from the URL
        request = ur.Request(url, data=None, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
        response = ur.urlopen(request, context=context)
        # Decode the response
        result = response.read().decode("utf-8")

        # Check whether it is UTC and get the corresponding data
        if time_zone == "+0" or time_zone == "-0":
            # Get the time data
            target_time = result.find('<span id="time2">')
            time_gotten = result[target_time+17:target_time+25]
            
            # Get the date data
            date_end = result.find(".<br />", target_time)
            date_gotten = result[target_time+69:date_end]
        else:
            # Get the time data
            target_time = result.find('<span id="time3">')
            time_gotten = result[target_time+17:target_time+25]
            
            # Get the date data
            target_date = result.find('<span id="time" class="fontbig">')
            date_end = result.find("</small>", target_date)
            date_gotten = result[target_date+61:date_end]
                
        # Write the time and date gotten from the URL into grabdata-service.txt
        data_file = open("./grabdata-service.txt", "w", encoding="utf-8")
        data_file.writelines(time_gotten + "\n")
        data_file.writelines(date_gotten)
        
        # Close the file
        print("Grab Time Service Finished!")
        data_file.close()
        
    # Function two: Get word definition in json format
    elif lines[0][0] != "[" and lines[0][0].isdigit() == False:
        print("Activate Grab Word Definition Service!")
        
        # Get the specified word, and send the request to the corresponding website
        word = lines[0]      
        url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word

        # Solve the SSL: CERTIFICATE_VERIFY_FAILED error
        context = ssl._create_unverified_context()

        # Send the request to the specified website and get the response from the URL
        request = ur.Request(url, data=None, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"})
        
        # Check whether the word exists in the database
        try:
            response = ur.urlopen(request, context=context)
        except:
            print("Error: No definition for this word!")
            # Write the data gotten from the URL into grabdata-service.txt
            data_file = open("./grabdata-service.txt", "w", encoding="utf-8")
            data_file.writelines("[\n")
            data_file.writelines("No definition for this word! Please change a word.")
            continue
        
        # Decode the response
        word_def = response.read().decode("utf-8")
        
        # Write the data gotten from the URL into grabdata-service.txt
        data_file = open("./grabdata-service.txt", "w", encoding="utf-8")
        data_file.writelines(word_def)
        
        # Close the file
        print("Grab Word Definition Service Finished!")
        data_file.close()
    
    # Not the desired data input format!
    else:
        continue
