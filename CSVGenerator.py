__author__ = 'youhanwang'
import csv


if __name__ == "__main__":
    with open('Causes_of_Death.csv', 'w') as writeFile:
        fieldnames = ['Ethnicity', 'Sex', 'Cause_of_Death']
        writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
        with open('New_York_City_Leading_Causes_of_Death.csv', 'rb') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                count = row[-2]
                if count == 'Count':
                    continue
                for i in range(int(count)):
                    ethnicity = row[1]
                    sex = row[2]
                    CoD = row[3]
                    writer.writerow({'Ethnicity':ethnicity, 'Sex':sex, 'Cause_of_Death':CoD})


