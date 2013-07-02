import sys
from voyages.apps.voyage.models import *

# Load the source csv to the database
if len(sys.argv) > 0:
    input_file = open(sys.argv[0], 'r')
else:
    input_file = open('sources.csv', 'r')

NULL_VAL = "\N"
DELIMITER = ','
first_line = input_file.readline()
data = first_line.split(DELIMITER)
varNameDict = {}

for index, term in enumerate(data):
    varNameDict[term] = index


def getFieldValue(fieldname):
    return data[varNameDict[fieldname]]

for line in input_file:
    data = line.split(DELIMITER)

    source = VoyageSources()
    source.short_ref = getFieldValue('id')
    source.long_ref = getFieldValue('name')

    source.save()