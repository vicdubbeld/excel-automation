import csv
import hashlib
import binascii
from binascii import hexlify
from io import StringIO

print('')
print('-------------------------All Data from File---------------------------------')
print('')


# Get downloaded csv file and print all data in terminal

with open('/Users/victor/Downloads/Capital_Survey_Invites_-_New_Survey (29).csv') as csvfile:
    filereader = csv.reader(csvfile, delimiter= ",", quotechar='|')
    for row in filereader:
        print(', '.join(row))

#Convert last two columns to hash and hex, then drop in new file

print('')
print('-------------------------Converting HashString column to MD5 Hash & HexString column to ascii hex---------------------------------')
print('')
# Capital Block
with open('/Users/victor/Downloads/Capital_Survey_Invites_-_New_Survey (29).csv') as csvfile4:
    with open('/Users/victor/12-06-20CAPITAL.csv', "r+") as output:
        reader = csv.DictReader(csvfile4, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)
        writer = csv.DictWriter(output, reader.fieldnames)
        # writer.writeheader()
        for i, r in enumerate(reader):
            # writing csv headers
            if i == 0:
                output.write(','.join(r) + '\n')

            # all data in HashString column replaced with hashed version of data
            r['HashString'] = hashlib.md5((r['HashString']).encode('utf-8')).hexdigest()
            # all data in HexString column replaced with ascii hex version of data
            r['HexString'] = r['HexString'].encode().hex()

            writer.writerow(r)

            # output.write(','.join(r.values()) + '\n')
            

          
        print("Success - Capital done")






        