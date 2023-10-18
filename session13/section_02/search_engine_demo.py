# folder = {'c drive': ['a.pptx', 'b.docx', []]}

# survey_results = {
#     'A': 20,
#     'B': 10,
# }

# customers = {'maria': {'address':'Wellesley', 'phone': '123-456-7890'}, 'rohan': []}

# customers['maria']['phone']
# Search Engine

# keywords -> Google -> URLs

# data is a dict
raw_data = {
    'www.babson.edu': ['Babson', 'college'],
    'www.bentleyrejects.com': ['Babson'],
    'www.mit.edu': ['college'],
    'canvas.babson.edu': ['Babson', 'college'],
}

data = {
    "Babson": ['www.babson.edu', 'www.bentleyrejects.com'],
    'college': ['www.babson.edu', 'www.mit.edu'],
}


def search(keyword):
    return data[keyword]


def search_queries(queries: list):
    """
    1. iterate over queries, build the result list
    2. merge URL lists together, then iterate over queries
    3. Reversed lookup map
    """
    results = []
    for url in raw_data:
        if raw_data[url] == queries:
            results.append(url)
    return results


queries = ['Babson', 'college']
print(search_queries(queries))


keyword = 'Babson'
results = search('Babson')  # a list

for result in results:
    print(result)
