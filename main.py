import csv, json, codecs

codecs.open('output.json', 'w').write(json.dumps([row for row in csv.DictReader(codecs.open(r'listings.csv', encoding='latin1'))], indent=4))