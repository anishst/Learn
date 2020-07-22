import requests

# Git hub
# API info: https://jobs.github.com/api
# using in Node: https://www.youtube.com/watch?v=fxY1q4SCB64&t=188s


def test_search_by_description():
    # Arrange
    # url = 'https://jobs.github.com/positions.json?description=quality&full_time=true&location=mclean'
    url = 'https://jobs.github.com/positions.json?description=testing&full_time=true'

    # Act
    response = requests.get(url)
    json_string = response.json()
    print(json_string)
    print(f"Found {len(json_string)} jobs ")
    for item in json_string:
        print(item["title"])
        print(item["url"])
        # print(item["description"])


# Indeed

#https://opensource.indeedeng.io/api-documentation/docs/job-search/
# guide: https://medium.com/@alberto_moura/build-a-jobs-database-using-indeeds-api-8f95316be842

def test_indeed_job():
    # UNDER DEV - not working
    parameters = {
        'q': "python developer",
        'l': "Austin, TX",
        'sort': "date",
        'fromage': "5",
        'limit': "25",
        'filter': "1",
        'useragent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)"
    }
    url = f'https://api.indeed.com/ads/apisearch?{parameters}'

    response = requests.get(url, verify=False)
    json_string = response.json()
    print(json_string)

