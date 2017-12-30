import json
import requests


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

# query parameters are given to the requests.get function as a dictionary; this
# variable contains some starter parameters.
query_type = {"simple": {},
              "atr": {"inc": "aliases+tags+ratings"},
              "aliases": {"inc": "aliases"},
              "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    # This is the main function for making queries to the musicbrainz API.
    # A json document should be returned by the query.
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    # This adds an artist name to the query parameters before making
    # an API call to the function above.
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    # After we get our output, we can format it to be more readable
    # by using this function.
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data


def main():

  # Question 1: How many band named "First Aid Kit"?
  query_data = query_by_name(ARTIST_URL, query_type["simple"], "First Aid Kit")
  # pretty_print(query_data)
  count_FAK = 0
  for artist in query_data["artists"]:
    if artist["name"] == "First Aid Kit"
        count_FAK += 1
  print "\nQ1: There are {0} bandes named First Aid Kit".format(count_FAK)

  # Question 2: Begin_area name for Queen?
  query_data = query_by_name(ARTIST_URL, query_type["simple"], "Queen")
  # pretty_print(query_data)
  Queen = query_data["artists"][0]
  print "\nQ2: The begin-area name for Queen is " + Queen["begin-area"]["name"]

  # Question 3: Spanish alias for The Beatles?
  query_data = query_by_name(ARTIST_URL, query_type["simple"], "The Beatles")
  # pretty_print(query_data)
  for alias in query_data["artists"][0]["aliases"]:
    if alias["locale"] == "es":
        print "\nQ3: The Spanish alias for The Beatles is " + alias["name"]

  # Question 4: Nirvana disambiguation?
  query_data = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
  # pretty_print(query_data)
  print "\nQ4: The disambiguation for Nirvana is " query_data["artists"][0]["disambiguation"]

  # Question 5: Where was One Direction formed?
  query_data = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")
  print "\nQ5: One Direction was formed in " + query_data["artists"][0]["life-span"]["begin"]
        

if __name__ == '__main__':
    main()
