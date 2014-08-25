import csv as csv
import numpy as np
import random as rand

# Simple randomforest
# Based of a descision tree
# Then split the dataset into a number of sets to make the decision tree
# this is what makes it a "forest"
# this will be removed before first commit OK?

#the way I would like to develop the decision tree is to take first question
# lets say if the person is a Man? Then we say yes or no
# the next step would be, and this is the point where I might be wrong,
# to get rid of all cases where the datapoint is NOT a Man
# (if we assume the answer to the question before was Yes)
# Then next question would keep splitting until we get a subset of the chosen
# dataset that represents the questions answered.

# Best case senario is that we have multiple datapoints, all telling the sam decision
# Second best would be that we have multiple or some datapoints, where
# the majority points towards a decision, then the majority is the decision

# Worst case is that we would end up with a set of features that does not match
# any previous datapoint. Then we would either have to say that we were unable to
# make a decision or try to trace back some step until we have some datapoints and
# then make a decision from that point.

# What I do not like about this approach is that by each step we approximately
# loose 1/2 of the datapoints. that means that if we have 5 decision nodes in the tree
# we would at the last node just take into account 1/32 which is < 3.2% of the datapoints

# Another thing, on the same note is that this does not really feel like a decision tree,
# but more like a collaborative filtering, or maybe just a filtering. We just keep cutting
# off parts of the dataset that we do not feel fitting until we can decide a matching point
# and then we just take majority.

# I'd like to weight the old datapoints lower if they do not match all the way.
# but it would be a bit hard to say that just because a person have a Business class ticket
# a person with the same attributes, but with an Economic class ticket would not tell us anything useful at all.
# Anyway this may be a later extension to the solution. Right now we got to find out how to make even a simple
# multifeature decision tree.

csv_file = csv.reader(open("dataset/train.csv", 'rb'))
# Save the header, but should not be part of the dataset
header = csv_file.next()



##############################Functions#########################################

# Splits the dataset into splitSize number of splits
def split_dataset(dataset, datasetSize, splitSize):
  array = np.empty([splitSize, datasetSize])
  print array
  print array[1,3]
  #for row in dataset:

  #
  # loop through the dataset
  # randomize a number between 0 and splitSize-1
  # add line from dataset to that index, if index < datset length / splitsize (round up)
  # this gives randomized splits and all splits have the same size (+-1)
  #
#count number of rows in dataset needed for the split
datasetSize = sum(1 for row in csv_file)
splitSize = 2
split_dataset(csv_file, 4, splitSize)
