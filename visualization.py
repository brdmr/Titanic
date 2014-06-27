# Simple visualisation of the dataset.

import csv as csv
import numpy as np

csv_file = csv.reader(open('dataset/train.csv', 'rb'))
# Don't know why we save the header, it should just be skipped.
header = csv_file.next()

#transform csv to array
data = []

for row in csv_file:
  data.append(row[0:])
data = np.array(data) # I guess the difference between list and np array is the
                      # speed numpy allows.

print len(data[13::,9])
