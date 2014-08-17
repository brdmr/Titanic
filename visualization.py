# Simple visualisation of the dataset.

import csv as csv
import numpy as np

#----------------------------------------------#
# Links between the data headers and the index.#
# Not suited for changes in the data-----------#
# another option might be better.--------------#
#----------------------------------------------#

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

# Extract some data to get to know the dataset.

#Declare variables storing the data we want.
numMales = 0
numFemales = 0
age = []
numWomenDead = 0
numWomenSurvive = 0
numMenDead = 0
numMenSurvive = 0
numSurvive = 0
numDead = 0

# Single-loop for data extraction.
for row in data :
  # Get number of Males and Females respectively from the passenger list
  if row[4] == 'male':
    numMales = numMales + 1
    if row[1] == "0":
      numMenDead = numMenDead + 1
    if row[1] == "1":
      numMenSurvive = numMenSurvive + 1

  if row[4] == 'female':
    numFemales = numFemales + 1
    if row[1] == "0":
      numWomenDead = numWomenDead + 1
    if row[1] == "1":
      numWomenSurvive = numWomenSurvive + 1

  # Get all ages represented among the passengers
  if row[5] != '':
    if float(row[5]) not in age:
      age.append(float(row[5]))

numSurvive = numWomenSurvive + numMenSurvive
numDead = numWomenDead + numMenDead


# Print the extracted data

# print header <<-- Good to see what the columns are named
print "Number of entries: ", len(data)
print "------------------------------------"
print "Women Survivors: ", numWomenSurvive
print "Men Survivors: ", numMenSurvive
print "Total Survivors: ", numSurvive
print "------------------------------------"
print "Women Casulties: ", numWomenDead
print "Men Casulties: ", numMenDead
print "Total Casulties: ", numDead
print "------------------------------------"
print "Ages:", age
print "Number of different ages: ", len(age)
print "Number of females: ", numFemales
print "Number of males: ", numMales
print "Is all passengers considered Male of Female? : ", (numFemales + numMales) == len(data)
#print data[13::,9] # This prints column 9 from each row, starting at row 13.
