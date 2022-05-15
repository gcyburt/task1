import json

# geting JSON file from the provided page and storing whole struct in sellersDeserialized
with open("sellers.json", "r") as read_file:
    sellersDeserialized = json.load(read_file)