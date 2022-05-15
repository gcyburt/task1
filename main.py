import json
from prettytable import PrettyTable

# geting JSON file from the provided page and storing whole struct in sellersDeserialized
with open("sellers.json", "r") as read_file:
    sellersDeserialized = json.load(read_file)

outputFile = open('results.txt', 'w', encoding="utf-8")

table = PrettyTable(['ID', 'Name', 'Domain', 'Seller type', 'Direct domain?'])

for seller in sellersDeserialized['sellers']:
    if seller['seller_type'] in ['INTERMEDIARY', 'BOTH']:
        if 'via' in seller['name']:
            isDirect = "indirect"
        else:
            isDirect = "direct"
        table.add_row([seller['seller_id'], seller['name'], seller['domain'], seller['seller_type'], isDirect])

outputFile.write(str(table))
print(table)
outputFile.close()
