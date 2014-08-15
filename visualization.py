# Simple visualisation of the dataset.

import csv as csv
import numpy as np
# These are the columns of the csv file.
# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
csv_file = csv.reader(open('dataset/train.csv', 'rb'))
# Don't know why we save the header, it should just be skipped.
header = csv_file.next()

#transform csv to array
data = []
for row in csv_file:
  data.append(row[0:])
data = np.array(data) # I guess the difference between list and np array is the
                      # speed numpy brings.

# extract some data to get to know the dataset
numMales = 0
numFemales = 0
age = []

for row in data :
  # Get number of Males and Females respectively from the passenger list
  if row[4] == 'male':
    numMales = numMales + 1
  if row[4] == 'female':
    numFemales = numFemales + 1

  # Get all ages represented among the passengers
  if row[5] != '':
    if float(row[5]) not in age:
      age.append(float(row[5]))


# Print the extracted data

print "Ages:"
print age
print "Number of different ages: ", len(age)
print "Number of entries: ", len(data)
print "Number of females: ", numFemales
print "Number of males: ", numMales
print "Is all passengers considered Male of Female? : ", (numFemales + numMales) == len(data) 
#print data[13::,9] # This prints column 9 from each row, starting at row 13.
