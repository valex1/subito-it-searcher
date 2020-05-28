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

class Tracked_search():
    def __init__(self, result_url, title, price, location):
        self.title = title
        self.result_url = result_url
        self.price = price
        self.location = location
    def __getattribute__(self, items):
        return super().__getattribute__(items)

class Searches():
    def __init__(self, name, query_url_list, search_results):
        self.name = name
        self.query_url_list = query_url_list
        self.search_results = search_results
    def __getattribute__(self, items):
        return super().__getattribute__(items)

if __name__ == '__main__':

    load_from_file(dbFile)

    # creating Search class and Tracked_search classes
    results_list = []
    search_results = {}
    query_url_list = []
    searches_list = []
    for research in queries.items():
        for query_url in research[1].items():
            for trackings in query_url[1].items():
                results_list.append(Tracked_search(trackings[0], trackings[1]['title'], trackings[1]['price'], trackings[1]['location']))
            search_results[query_url[0]] = results_list
            query_url_list.append(query_url)
        searches_list.append(Searches(research[0], query_url_list, search_results))
    # complete pathway: searches_list[0].search_results[query_url][0].price

print('fine')