from googlesearch import search

# to search
test_query = "mohit kumar github"


def important_link(query):
    for j in search(query, num_results=5):
        print(j)


important_link(test_query)
