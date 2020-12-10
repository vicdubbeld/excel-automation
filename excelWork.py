import csv
import hashlib
import binascii
from binascii import hexlify
from io import StringIO
from datetime import datetime
import os
import time
import pandas as pd

print('')
print('')
print('-------------------------Welcome to the master automation machine---------------------------------')
print('')

now = datetime.now()
today_date = now.strftime("%m-%d-%Y")
print("-------------------------Good Morning! Today is:", today_date, "----------------------------------")
print('')
print('')

# Capital Block
if os.path.isfile('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Capital_Survey_Invites_-_New_Survey.csv') == True:
    # Read input file 'csvfile'
    data = pd.read_csv(r'/Users/victor/PYTHON-SURVEY-DOWNLOADS/Capital_Survey_Invites_-_New_Survey.csv')
    data[~data.duplicated(subset=['Email'])].to_csv('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Capital_Survey_Invites_-_New_Survey (clean).csv', index=False)
    with open('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Capital_Survey_Invites_-_New_Survey (clean).csv') as csvfile: 
        with open('/Users/victor/Dropbox (Perspective Group)/Victor/SURVEYS/DAILY WORK/'+ today_date +'CAPITAL.csv', "a") as output:
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
            print(data)
   
            print("Success - Capital done")
else:
    print("Nothing for Capital today :(")

print("Loading Costa...")

time.sleep(1)
# deletes input file
# os.remove('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Capital_Survey_Invites_-_New_Survey.csv')


#Costa Block
if os.path.isfile('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Survey_Invite_File_-_Costa_Sur_ALL.csv') == True:
    # Read input file 'csvfile'
    data = pd.read_csv(r'/Users/victor/PYTHON-SURVEY-DOWNLOADS/Survey_Invite_File_-_Costa_Sur_ALL.csv')
    data[~data.duplicated(subset=['Email'])].to_csv('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Survey_Invite_File_-_Costa_Sur_ALL (clean).csv', index=False)
    with open('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Survey_Invite_File_-_Costa_Sur_ALL (clean).csv') as csvfile3:
        with open('/Users/victor/Dropbox (Perspective Group)/Victor/SURVEYS/DAILY WORK/'+ today_date +'COSTA.csv', "a") as output:
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
            print("Success - Costa done")
else:
    print("Nothing for Costa today :(")

print("Loading Galleon...")
time.sleep(1)
# deletes input file
# os.remove('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Survey_Invite_File_-_Costa_Sur_ALL.csv')


#Galleon Block
if os.path.isfile('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Galleon_-_Invites.csv') == True:
    # Read input file 'csvfile'
    data = pd.read_csv(r'/Users/victor/PYTHON-SURVEY-DOWNLOADS/Galleon_-_Invites.csv')
    data[~data.duplicated(subset=['Email'])].to_csv('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Galleon_-_Invites (clean).csv', index=False)
    with open('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Galleon_-_Invites (clean).csv') as csvfile3:
        with open('/Users/victor/Dropbox (Perspective Group)/Victor/SURVEYS/DAILY WORK/'+ today_date +'GALLEON.csv', "a") as output:
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
            print("Success - Galleon done")
else:
    print("Nothing for Galleon today :(")

print("Loading Kings...")
time.sleep(1)
# deletes input file
# os.remove('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Galleon_-_Invites.csv')


#King's Block
if os.path.isfile('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Survey_Invite_-_Kings_Creek.csv') == True:
    data = pd.read_csv(r'/Users/victor/PYTHON-SURVEY-DOWNLOADS/Survey_Invite_-_Kings_Creek.csv')
    data[~data.duplicated(subset=['Email'])].to_csv('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Survey_Invite_-_Kings_Creek (clean).csv', index=False)
    with open('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Survey_Invite_-_Kings_Creek (clean).csv') as csvfile4:
        with open('/Users/victor/Dropbox (Perspective Group)/Victor/SURVEYS/DAILY WORK/'+ today_date +'KINGS.csv', "a") as output:
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
            print("Success - King's Creek done")
else: 
    print("Nothing for King's Creek today :(")

print("All done! Have a nice day.")
time.sleep(1)
# deletes input file
# os.remove('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Survey_Invite_-_Kings_Creek.csv')


