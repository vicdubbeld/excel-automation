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
print('-------------------------Welcome to the master automation machine---------------------------------')
print('')

now = datetime.now()
today_date = now.strftime("%m-%d-%Y")
print("Good Morning! Today is:", today_date)


# Capital Block
if os.path.isfile('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Capital_Survey_Invites_-_New_Survey.csv') == True:
    with open('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Capital_Survey_Invites_-_New_Survey.csv') as csvfile: 
        with open('/Users/victor/Dropbox (Perspective Group)/Victor/SURVEYS/DAILY WORK/'+ today_date +'CAPITAL.csv', "a") as output:
            reader = csv.DictReader(csvfile, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)
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
            print("Success - Capital done")
else:
    print("Nothing for Capital today :(")

print("Loading next...")

time.sleep(3)
# os.remove('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Capital_Survey_Invites_-_New_Survey.csv')



#Costa Block
if os.path.isfile('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Survey_Invite_File_-_Costa_Sur_ALL.csv') == True:
    with open('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Survey_Invite_File_-_Costa_Sur_ALL.csv') as csvfile3:
        # with open('/Users/victor/12-06-20CAPITAL.csv', "r+") as output:
        with open('/Users/victor/Dropbox (Perspective Group)/Victor/SURVEYS/DAILY WORK/'+ today_date +'COSTA.csv', "a") as output:
            reader = csv.DictReader(csvfile3, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)
            # Add new columns attempt
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



            print("Success - Costa done")
else:
    print("Nothing for Costa today :(")

print("Loading next...")
time.sleep(3)
# os.remove('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Survey_Invite_File_-_Costa_Sur_ALL.csv')


#Galleon Block
if os.path.isfile('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Galleon_-_Invites.csv') == True:
    with open('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Galleon_-_Invites.csv') as csvfile3:
        # with open('/Users/victor/12-06-20CAPITAL.csv', "r+") as output:
        with open('/Users/victor/Dropbox (Perspective Group)/Victor/SURVEYS/DAILY WORK/'+ today_date +'GALLEON.csv', "a") as output:
            reader = csv.DictReader(csvfile3, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)
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

print("Loading next...")
time.sleep(3)
# os.remove('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Galleon_-_Invites.csv')


#King's Block
if os.path.isfile('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Survey_Invite_-_Kings_Creek.csv') == True:
    with open('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Survey_Invite_-_Kings_Creek.csv') as csvfile4:
        # with open('/Users/victor/12-06-20CAPITAL.csv', "r+") as output:
        with open('/Users/victor/Dropbox (Perspective Group)/Victor/SURVEYS/DAILY WORK/'+ today_date +'KINGS.csv', "a") as output:
            reader = csv.DictReader(csvfile4, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)
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

print("All done")
time.sleep(3)
# os.remove('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Survey_Invite_-_Kings_Creek.csv')









# print('-------------------------Ideal Loop Version---------------------------------')
# now = datetime.now()
# # today_date = now.strftime("%h:%M:S-%m-%d-%y")
# today_date = now.strftime('%m-%d-%Y-%H:%M:%S.%f')
# print("The date is: ", today_date)


# # Capital Block
# path = os.getcwd()
# print(path)
# # os.chdir(os.path.dirname('/Users/victor/PYTHON-SURVEY-DOWNLOADS/'))
# directory = '/Users/victor/PYTHON-SURVEY-DOWNLOADS/'

# # for root,dirs,files in os.walk(path): 
# for file in os.listdir(directory):
#     # for file in files:
#         # print("verified files are only csv...")
#         if file.endswith('.csv'):
#             print(os.path.join(directory, file))
#             # f=open(file, 'r')
#             # with open('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Capital_Survey_Invites_-_New_Survey.csv') as csvfile4:
#             with open(os.path.join(directory, file)) as csvfile4:
#                 print("Opening input file...")
#                 with open('/Users/victor/Dropbox (Perspective Group)/Victor/SURVEYS/DAILY WORK/'+ today_date +'-CAPITALpython.csv', "a+") as output:
#                     print("Opening export file...")
#                     reader = csv.DictReader(csvfile4, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)

#                     writer = csv.DictWriter(output, reader.fieldnames)

#                     for i, r in enumerate(reader):
                    
#                         # writing csv headers

#                         if i == 0:
                        
#                             output.write(','.join(r) + '\n')



#                         # all data in HashString column replaced with hashed version of data

#                         r['HashString'] = hashlib.md5((r['HashString']).encode('utf-8')).hexdigest()

#                         # all data in HexString column replaced with ascii hex version of data

#                         r['HexString'] = r['HexString'].encode().hex()

#                         writer.writerow(r)

                        


#                     print("Success - done")



#             time.sleep(5)


    
#     # os.remove('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Capital_Survey_Invites_-_New_Survey.csv')

