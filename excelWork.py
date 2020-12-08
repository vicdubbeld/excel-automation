import csv
import hashlib
import binascii
from binascii import hexlify
from io import StringIO

print('')
print('-------------------------All Data from File---------------------------------')
print('')


# Get downloaded csv file and print all data

with open('/Users/victor/Downloads/Capital_Survey_Invites_-_New_Survey (29).csv') as csvfile:
    filereader = csv.reader(csvfile, delimiter= ",", quotechar='|')
    for row in filereader:
        print(', '.join(row))


# print('')
# print('-------------------------HashString & HexString---------------------------------')
# print('')


# Prints hash and hex strings in terminal
# with open('/Users/victor/Downloads/Galleon_-_Invites - 2020-11-30T071729.708.csv') as csvfile2:
#     filereader2 = csv.DictReader(csvfile2)
#     for row in filereader2:
#         print(row['HashString'], row['HexString'])


# print('')
# print('-------------------------Converting HashString column to MD5 Hash & HexString column to ascii hex---------------------------------')
# print('')


# Convert 'HashString' column to MD5 Hash (lowercase)
# with open('/Users/victor/Downloads/Galleon_-_Invites - 2020-11-30T071729.708.csv') as csvfile3:
#     with open('/Users/victor/Documents/Code/Python/excel-automation/hashed2-file.csv', "r+") as output:
#         reader = csv.DictReader(csvfile3)
#         for i, r in enumerate(reader):
#             # writing csv headers
#             if i is 0:
#                 output.write(','.join(r) + '\n')

#             # all data in HashString column replaced with hashed version of data
#             r['HashString'] = hashlib.md5((r['HashString']).encode('utf-8')).hexdigest()
#             # all data in HexString column replaced with ascii hex version of data
#             r['HexString'] = r['HexString'].encode().hex()
            
#             output.write(','.join(r.values()) + '\n')

#             # try converting string to byte-like object to hex
#         print("Success - conversion done")
print('')
print('-------------------------Converting HashString column to MD5 Hash & HexString column to ascii hex---------------------------------')
print('')
# Capital Block
with open('/Users/victor/Downloads/Capital_Survey_Invites_-_New_Survey (29).csv') as csvfile4:
    with open('/Users/victor/12-06-20CAPITAL.csv', "r+") as output:
        reader = csv.DictReader(csvfile4, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)
        writer = csv.DictWriter(output, reader.fieldnames)
        writer.writeheader()
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

print('-------------------------New Method  w/ DictWriter---------------------------------')
# See below. Replace csvfile4 = ... and output = ...
# data = '''\
# UniqueID, LastName,FirstName, Language, Email, Resort, SurveySent, stayMonth, stayYear, LocationID, Image, HashString, HexString
# SPI12345, Smith, Joe, EN, example@test.com, Example Resort, "03 Dec, 2020",12, 2020, 111111, image.jpg, "G, E=s:0at9n_$@b(P7.E:lC?2)Rm6MOnUniqueID=SPI1652859&locationId=547961&email=example@test.com&firstName=JOE&lastName=SMITH&city=LEXINGTON&stayMonth=12&stayYear=2020",UniqueID=SPI12345&locationId=111111&email=example@test.com&firstName=JOE&lastName=SMITH&city=LEXINGTON&stayMonth=12&stayYear=2020
# '''


# csvfile4 = StringIO(data) # open('file1')
# output = StringIO('/Users/victor/12-06-20CAPITAL.csv') # open('file2', 'w', newline='')


# reader = csv.DictReader(
#     csvfile4,
#     quotechar='"',
#     delimiter=",",
#     quoting=csv.QUOTE_ALL,
#     skipinitialspace=True)
# writer = csv.DictWriter(output, reader.fieldnames)
# writer.writeheader()
# for i, r in enumerate(reader):
#     # all data in HashString column replaced with hashed version of data
#     r['HashString'] = hashlib.md5(
#         (r['HashString']).encode('utf-8')).hexdigest()
#     # all data in HexString column replaced with ascii hex version of data
#     r['HexString'] = r['HexString'].encode().hex()

#     writer.writerow(r)

# print(output.getvalue())




        