import csv
import hashlib
import binascii
from binascii import hexlify
from io import StringIO
from datetime import datetime
import os
import time
import pandas as pd
import itertools
import threading
import time
import sys
from selenium import webdriver

now = datetime.now()
today_date = now.strftime("%m-%d-%Y")
today_date2 = now.strftime("%A, %m-%d-%Y" + " %H:%M:%S")

print('')
print('')
print('-------------------------Welcome to the master automation machine---------------------------------')
print('')
print('')
time.sleep(1)
print("-------------------------Today is:", today_date2, "-----------------------------")
print('')
print('')


# files defined
capital = '/Users/victor/PYTHON-SURVEY-DOWNLOADS/Capital_Survey_Invites_-_New_Survey.csv'
capital2 = '/Users/victor/PYTHON-SURVEY-DOWNLOADS/Capital_Survey_Invites_-_New_Survey (clean).csv'
capital3 = '/Users/victor/Dropbox (Perspective Group)/Victor/SURVEYS/DAILY WORK/'+ today_date +'CAPITAL.csv'
capitalta = '/Users/victor/PYTHON-SURVEY-DOWNLOADS/Capital_Survey_Invites_-_TA_Only.csv'
capitalta2 = '/Users/victor/PYTHON-SURVEY-DOWNLOADS/Capital_Survey_Invites_-_TA_Only (clean).csv'
capitalta3 = '/Users/victor/Dropbox (Perspective Group)/Victor/SURVEYS/DAILY WORK/'+ today_date +'CAPITALTA.csv'
costa = '/Users/victor/PYTHON-SURVEY-DOWNLOADS/Survey_Invite_File_-_Costa_Sur_ALL.csv'
costa2 = '/Users/victor/PYTHON-SURVEY-DOWNLOADS/Survey_Invite_File_-_Costa_Sur_ALL (clean).csv'
costa3 = '/Users/victor/Dropbox (Perspective Group)/Victor/SURVEYS/DAILY WORK/'+ today_date +'COSTA.csv'
costata = '/Users/victor/PYTHON-SURVEY-DOWNLOADS/TA_Survey_Invites.csv'
costata2 = '/Users/victor/PYTHON-SURVEY-DOWNLOADS/TA_Survey_Invites (clean).csv'
costata3 = '/Users/victor/Dropbox (Perspective Group)/Victor/SURVEYS/DAILY WORK/'+ today_date +'COSTATA.csv'
galleon = '/Users/victor/PYTHON-SURVEY-DOWNLOADS/Galleon_-_Invites.csv'
galleon2 = '/Users/victor/PYTHON-SURVEY-DOWNLOADS/Galleon_-_Invites (clean).csv'
galleon3 = '/Users/victor/Dropbox (Perspective Group)/Victor/SURVEYS/DAILY WORK/'+ today_date +'GALLEON.csv'
kings = '/Users/victor/PYTHON-SURVEY-DOWNLOADS/Survey_Invite_-_Kings_Creek.csv'
kings2 = '/Users/victor/PYTHON-SURVEY-DOWNLOADS/Survey_Invite_-_Kings_Creek (clean).csv'
kings3 = '/Users/victor/Dropbox (Perspective Group)/Victor/SURVEYS/DAILY WORK/'+ today_date +'KINGS.csv'
kingsta = '/Users/victor/PYTHON-SURVEY-DOWNLOADS/TA_Survey_Invite_Report.csv'
kingsta2 = '/Users/victor/PYTHON-SURVEY-DOWNLOADS/TA_Survey_Invite_Report (clean).csv'
kingsta3 = '/Users/victor/Dropbox (Perspective Group)/Victor/SURVEYS/DAILY WORK/'+ today_date +'KINGSTA.csv'

time.sleep(1)
print("Loading Capital\n")
# Capital Block
if os.path.isfile(capital) == True:
    # Read input file 'csvfile'
    data = pd.read_csv(capital)
    # creates new file with duplicated data dropped
    data[~data.duplicated(subset=['Email'])].to_csv(capital2, index=False)
    with open(capital2) as csvfile: 
        with open(capital3, "a") as output:
            reader = csv.DictReader(csvfile, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)
            # Define new columns for hashed/hexed data in output file
            fieldnames = reader.fieldnames + ['TA1', 'TA2']
            writer = csv.DictWriter(output, fieldnames)
            # writes column names
            writer.writeheader()
            # writes data to each row
            for i, r in enumerate(reader):        
                # all data in HashString column replaced with hashed version of data
                r['TA1'] = hashlib.md5((r['HashString']).encode('utf-8')).hexdigest()
                # all data in HexString column replaced with ascii hex version of data
                r['TA2'] = r['HexString'].encode().hex()
                # writes data to new file
                writer.writerow(r)
            # prints to terminal to verify duplicates are gone and that hash/hex formulas worked
            # print(data)
            time.sleep(1)
            print("Success - Capital done")
            time.sleep(1)
            print("Removing input files...\n")
            # os.remove(capital)
            # os.remove(capital2)
else:
    time.sleep(1)
    print("Nothing for Capital today :(")
time.sleep(1)
print("Loading Capital TA...\n")


# Capital TA Block
if os.path.isfile(capitalta) == True:
    # Read input file 'csvfile'
    data = pd.read_csv(capitalta)
    # creates new file with duplicated data dropped
    data[~data.duplicated(subset=['Email'])].to_csv(capitalta2, index=False)
    with open(capitalta2) as csvfile: 
        with open(capitalta3, "a") as output:
            reader = csv.DictReader(csvfile, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)
            # Define new columns for hashed/hexed data in output file
            fieldnames = reader.fieldnames + ['TA1', 'TA2']
            writer = csv.DictWriter(output, fieldnames)
            # writes column names
            writer.writeheader()
            # writes data to each row
            for i, r in enumerate(reader):        
                # all data in HashString column replaced with hashed version of data
                r['TA1'] = hashlib.md5((r['HashString']).encode('utf-8')).hexdigest()
                # all data in HexString column replaced with ascii hex version of data
                r['TA2'] = r['HexString'].encode().hex()
                # writes data to new file
                writer.writerow(r)
            # prints to terminal to verify duplicates are gone and that hash/hex formulas worked
            # print(data)
            time.sleep(1)
            print("Success - Capital TA done")
            time.sleep(1)
            print("Removing input files\n")
            # os.remove(capitalta)
            # os.remove(capitalta2)
   
else:
    time.sleep(1)
    print("Nothing for Capital TA today :(\n")
time.sleep(1)
print("Loading Costa...\n")


#Costa Block
if os.path.isfile(costa) == True:
    # Read input file 'csvfile'
    data = pd.read_csv(costa)
    data[~data.duplicated(subset=['Email'])].to_csv(costa2, index=False)
    with open(costa2) as csvfile3:
        with open(costa3, "a") as output:
            reader = csv.DictReader(csvfile3, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)
            
            # Add new columns for hashed/hexed data
            fieldnames = reader.fieldnames + ['TA1', 'TA2']
            writer = csv.DictWriter(output, fieldnames)
            # Add all columns to output file
            writer.writeheader()
            # check for duplicate emails

            # print(result_dups)
            for i, r in enumerate(reader):  
                # if value already exists in list, skip writing whole row to output file
                
                # all data in HashString column replaced with hashed version of data in new column
                r['TA1'] = hashlib.md5((r['HashString']).encode('utf-8')).hexdigest()
                # all data in HexString column replaced with ascii hex version of data in new column
                r['TA2'] = r['HexString'].encode().hex()
                
                writer.writerow(r)


            time.sleep(1)    
            print("Success - Costa done")
            time.sleep(1)
            print("Removing input files\n")
            # deletes input file
            # os.remove(costa)
            # os.remove(costa2)
else:
    time.sleep(1)
    print("Nothing for Costa today :(\n")
time.sleep(1)
print("Loading Costa TA...\n")


#Costa TA Block
if os.path.isfile(costata) == True:
    # Read input file 'csvfile'
    data = pd.read_csv(costata)
    data[~data.duplicated(subset=['Email'])].to_csv(costata2, index=False)
    with open(costata2) as csvfile3:
        with open(costata3, "a") as output:
            reader = csv.DictReader(csvfile3, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)
            # Add new columns for hashed/hexed data
            fieldnames = reader.fieldnames + ['TA1', 'TA2']
            writer = csv.DictWriter(output, fieldnames)
            # Add all columns to output file
            writer.writeheader()
            # check for duplicate emails

            # print(result_dups)
            for i, r in enumerate(reader):  
                # if value already exists in list, skip writing whole row to output file
                
                # all data in HashString column replaced with hashed version of data in new column
                r['TA1'] = hashlib.md5((r['HashString']).encode('utf-8')).hexdigest()
                # all data in HexString column replaced with ascii hex version of data in new column
                r['TA2'] = r['HexString'].encode().hex()
                
                writer.writerow(r)

            time.sleep(1)    
            print("Success - Costa TA done")
            time.sleep(1)
            print("Removing input files\n")
            # deletes input file
            # os.remove(costata)
            # os.remove(costata2)
else:
    time.sleep(1)
    print("Nothing for Costa TA today because it's not Wednesday :(\n")
time.sleep(1)
print("Loading Galleon...\n")


#Galleon Block
if os.path.isfile(galleon) == True:
    # Read input file 'csvfile'
    data = pd.read_csv(galleon)
    data[~data.duplicated(subset=['Email'])].to_csv(galleon2, index=False)
    with open(galleon2) as csvfile3:
        with open(galleon3, "a") as output:
            reader = csv.DictReader(csvfile3, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)
            # Add new columns for hashed/hexed data
            fieldnames = reader.fieldnames + ['TA1', 'TA2']
            writer = csv.DictWriter(output, fieldnames)
            writer.writeheader()
            # fieldnames = reader.fieldnames + ['NewColum1'] 
            for i, r in enumerate(reader):        
                # all data in HashString column replaced with hashed version of data
                r['TA1'] = hashlib.md5((r['HashString']).encode('utf-8')).hexdigest()
                # all data in HexString column replaced with ascii hex version of data
                r['TA2'] = r['HexString'].encode().hex()

                writer.writerow(r)
            time.sleep(1)
            print("Success - Galleon done")
            time.sleep(1)  
            print("Removing input files\n") 
            # deletes input file
            # os.remove(galleon)
            # os.remove(galleon2)
else:
    time.sleep(1)
    print("Nothing for Galleon today :(\n")
time.sleep(1)
print("Loading Kings...\n")


#King's Block
if os.path.isfile(kings) == True:
    data = pd.read_csv(kings)
    data[~data.duplicated(subset=['Email'])].to_csv(kings2, index=False)
    with open(kings2) as csvfile4:
        with open(kings3, "a") as output:
            reader = csv.DictReader(csvfile4, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)
            # Add new columns for hashed/hexed data
            fieldnames = reader.fieldnames + ['TA1', 'TA2']
            writer = csv.DictWriter(output, fieldnames)
            writer.writeheader()
            # fieldnames = reader.fieldnames + ['NewColum1'] 
            for i, r in enumerate(reader):        
                # all data in HashString column replaced with hashed version of data
                r['TA1'] = hashlib.md5((r['HashString']).encode('utf-8')).hexdigest()
                # all data in HexString column replaced with ascii hex version of data
                r['TA2'] = r['HexString'].encode().hex()

                writer.writerow(r)
            time.sleep(1)
            print("Success - King's Creek done")
            time.sleep(1)
            print("Removing input files\n") 
            # deletes input file
            # os.remove(kings)
            # os.remove(kings2)
else:
    time.sleep(1) 
    print("Nothing for King's Creek today :(\n")
time.sleep(1)
print("Loading Kings TA...\n")

#King's TA Block
if os.path.isfile(kingsta) == True:
    data = pd.read_csv(kingsta)
    data[~data.duplicated(subset=['Email Address'])].to_csv(kingsta2, index=False)
    with open(kingsta2) as csvfile4:
        with open(kingsta3, "a") as output:
            reader = csv.DictReader(csvfile4, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)
            # Add new columns for hashed/hexed data
            fieldnames = reader.fieldnames + ['TA1', 'TA2']
            writer = csv.DictWriter(output, fieldnames)
            writer.writeheader()
            # fieldnames = reader.fieldnames + ['NewColum1'] 
            for i, r in enumerate(reader):        
                # all data in HashString column replaced with hashed version of data
                r['TA1'] = hashlib.md5((r['HashString']).encode('utf-8')).hexdigest()
                # all data in HexString column replaced with ascii hex version of data
                r['TA2'] = r['HexString'].encode().hex()

                writer.writerow(r)
            time.sleep(1)
            print("Success - King's Creek TA done")
            time.sleep(1)
            print("Removing input files\n") 
            # deletes input file
            # os.remove(kingsta)
            # os.remove(kingsta2)
else:
    time.sleep(1) 
    print("Nothing for King's Creek TA today because it's not Wednesday :(\n")
time.sleep(1)


print('')
print("All done! Now go make yourself a nice cup of coffee. You deserve it after all the hard work.")
print('')
print('')


# Web Scraper to upload to contact manager

print('')
print("Let the webscraping begin! \n")

url = 'https://survey.intuitionbrandmarketing.com/Member/ContactView/List.action'
browser = webdriver.Chrome()

browser.find_element_by_xpath('//*[@id=treeViewNode_1_-41512190_1_41512190"]').click()



