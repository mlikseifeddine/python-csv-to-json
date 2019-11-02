import codecs

data = {}
with codecs.open('listings.csv', encoding='utf-8') as f:
    for line in f.readlines():
        # Use some logic here to load each line into a dict, like:
        data = line
        print(data)