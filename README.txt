README
Project 3 from Advanced Database Systems.

a. Team members
Youhan Wang(yw2663)
Meng Wang(mw2972)

b. A list of all the files
run.sh --> Shell script to run the code.
ADB_proj3.py --> Main program to run the algorithm and generate output file.
CSVGenerator.py (optional) --> The code to generate the INTEGRATED-DATASET.csv.
INTEGRATED-DATASET.csv --> CSV version of INTEGRATED-DATASET.
example-run.txt --> Sample output file of the algorithm on INTEGRATED-DATASET.


c. 
(a) which NYC Open Data data set(s) you used to generate the INTEGRATED-DATASET file:
We used dataset --> New York City Leading Causes of Death. https://data.cityofnewyork.us/Health/New-York-City-Leading-Causes-of-Death/jb7j-dtam


(b) what (high-level) procedure you used to map the original NYC Open Data data set(s) into your INTEGRATED-DATASET file.
Note: We have included the procedure as an optional file in this directory.
The original datasets including each Year-Ethnicity-Sex-Cause of Death-Count-Percent as one row. To better apply the algorithm to this dataset, We translated the count number to lines of same records. To verify this procedure, we can regard each one line in the resulting dataset to be one specific person with a character of this year, ethnicity, sex, cause of death.
Also, we originally want to preserve the year record to see if there are variation between different years, however, it shows similar ratio for different causes since the time span is so trival(2010 - 2014) Eventually, we also eliminated the year column to better visualize the result. 

After we cleaned the data, the columns we have are: Ethnicity, Sex, CoD(Cause-of-Death),

(c) what makes your choice of INTEGRATED-DATASET file interesting 
The intention of choosing this dataset is that we want to see is there a difference of cause of death between different sex and ethnicity. As we mentioned in (a) and (b).
We choosed New York City Leading Causes of Death. https://data.cityofnewyork.us/Health/New-York-City-Leading-Causes-of-Death/jb7j-dtam.
Then, we eliminated the year column and percentage column and expand the count column to be that number of lines of same records.


d. A clear description of how to run your program (note that your project must compile/run under Linux in your CS account)
To run this program, you can run the shell script using following command structure:
sh run.sh INTEGRATED-DATASET.csv min_sup min_conf
Then, the result will be outputting to output.txt


e. The command line specification of an interesting sample run (i.e., a min_sup, min_conf combination that produces interesting results). 
The sample run use the command:
sh run.sh INTEGRATED-DATASET.csv 0.05 0.1

As an interesting result, we found that:
1) Significantly more female than male are died because of diseases of heart.
['DISEASES OF HEART'] => ['FEMALE'] (Conf: 54.0482740722%, Supp: 21.8484432638%)
['DISEASES OF HEART'] => ['MALE'] (Conf: 45.9517259278%, Supp: 18.5754992929%)

2) NON-HISPANIC White males are more likely to die for MALIGNANT NEOPLASMS than average male.
['MALE', 'NON-HISPANIC WHITE'] => ['MALIGNANT NEOPLASMS'] (Conf: 28.6027179912%, Supp: 6.96009434002%)
['MALE'] => ['MALIGNANT NEOPLASMS'] (Conf: 27.5603038855%, Supp: 13.5647349625%)

