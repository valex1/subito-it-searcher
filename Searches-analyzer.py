import os.path
import json

queries = dict()
dbFile = "searches.tracked"

# load from file
def load_from_file(fileName):
    global queries
    if not os.path.isfile(fileName):
        return

    with open(fileName) as file:
        queries = json.load(file)

class Tracked:
    global queries
    def __init__(self, result_url, title, price, location):
        global queries
        self.title = title
        self.result_url = result_url
        self.price = price
        self.location = location

if __name__ == '__main__':

    load_from_file(dbFile)
