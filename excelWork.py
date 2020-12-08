import csv
import hashlib
import binascii
from binascii import hexlify
from io import StringIO
from datetime import datetime
import os
import time

print('')
print('-------------------------Converting HashString column to MD5 Hash & HexString column to ascii hex---------------------------------')
print('')


now = datetime.now()
today_date = now.strftime("%m-%d-%Y")

print("The date is: ", today_date)


# Capital Block
path = os.getcwd()
print(path)
# os.chdir(os.path.dirname('/Users/victor/PYTHON-SURVEY-DOWNLOADS/'))
directory = '/Users/victor/excel-auto/excel-automation/PYTHON-SURVEY-DOWNLOADS/'

# for root,dirs,files in os.walk(path): 
for file in os.listdir(directory):
    # for file in files:
        # print("verified files are only csv...")
        if file.endswith('.csv'):
            print(os.path.join(directory, file))
            # f=open(file, 'r')
            # with open('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Capital_Survey_Invites_-_New_Survey.csv') as csvfile4:
            with open(os.path.join(directory, file)) as csvfile4:
                print("error handler 2")
                with open('/Users/victor/Dropbox (Perspective Group)/Victor/SURVEYS/DAILY WORK/'+ today_date +'CAPITALpython.csv', "a") as output:
                    print("error handler 3")
                    reader = csv.DictReader(csvfile4, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)

                    writer = csv.DictWriter(output, reader.fieldnames)

                    for i, r in enumerate(reader):
                    
                        # writing csv headers

                        if i == 0:
                        
                            output.write(','.join(r) + '\n')



                        # all data in HashString column replaced with hashed version of data

                        r['HashString'] = hashlib.md5((r['HashString']).encode('utf-8')).hexdigest()

                        # all data in HexString column replaced with ascii hex version of data

                        r['HexString'] = r['HexString'].encode().hex()

                        writer.writerow(r)
                        


                    print("Success - done")



            time.sleep(5)


    
    # os.remove('/Users/victor/PYTHON-SURVEY-DOWNLOADS/Capital_Survey_Invites_-_New_Survey.csv')
# Costa Block
# Galleon Block
# King's Creek Block
