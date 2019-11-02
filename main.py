import csv, json
open( 'output.json', 'w').write(json.dumps([row for row in csv.DictReader(open( 'listings.csv', 'r' ))], indent=4))