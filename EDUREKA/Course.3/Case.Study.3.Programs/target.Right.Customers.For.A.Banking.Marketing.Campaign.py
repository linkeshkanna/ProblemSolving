"""
A Bank runs marketing campaign to offer loans to clients
Loan is offered to only clients with particular professions
List of successful campaigns (with client data) is given in attached dataset
You have to come up with program which reads the file and builds a set of unique profession list
Get input from User for the "Profession of Client"
System tells whether client is eligible to be approached for marketing campaign

Key issues:
Tele Caller can only make x number of cold calls in a day.
Hence to increase her effectiveness only eligible customers should be called Considerations
Current system does not differentiate clients based on age and profession

Data volume:
bank-data.csv

Business benefits:
Company can achieve between 15% to 20% higher conversion by targeting right clients

Approach to Solve
Build a Class using OOPs concepts with Modules, Errors and Exceptions
Program should be designed in a way that in future if any changes required to add age or any other factor
to consider, the system should be easy to inherit/extend without changes in the main campaign

1. Read file bank-data.csv
2. Build a set of unique jobs
3. Read the input from command line
4. Check if profession is in list
5. Print whether client is eligible
"""
import csv
import pandas as pd
import re
print('Enter InputFileName&path ex :F:/Python/bank-data.csv')
FilePath = input()
Data = pd.read_csv(FilePath, usecols=['job'])
UniqueData = Data.drop_duplicates(keep='first').sort_values(by=['job'])
Uniq_Result = UniqueData.to_string(index=False, header=False)
To_Job_Match = Uniq_Result.split()
print ('List of Jobs Professional in File :' )
print (Uniq_Result)
print ('Enter the Job  Eligibel for Loan :')
Job = input()
for jobcheck in To_Job_Match:
    if  re.sub(r'[- ]', '',jobcheck.lower()) ==  re.sub(r'[- ]', '',Job.lower()):
        print ('Given Job Avialble.Check Output CSV for Details' )
        # print ('Enter OutFile Name along with path ex: F:/Python/bankdata_toTelecall.csv')
        # Output_File = input()
        df = pd.read_csv(FilePath)
        df['Find_Eligibel'] = ['yes' if  x.strip() == Job.strip() else 'No' for x in Data['job']]
        # df.to_csv(Output_File,index=False)
        #print (df)
        break
else:
        print ('Given Job Not Avialble.Enter the Valid Profession' )