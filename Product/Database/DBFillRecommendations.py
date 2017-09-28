from Product.Database.DBConn import session
#!/bin/bash
import csv
with open('movies.csv', 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)