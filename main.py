import csv, json, codecs

# read the csv file
source = codecs.open('listings.csv', encoding='utf-8')

# parse the csv into json object
data = json.dumps([row for row in csv.DictReader(source)], indent=4)

# prepare the output file
output = codecs.open('output.json', 'w')

# write the final result
output.write(data)