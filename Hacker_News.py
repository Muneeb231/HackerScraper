

# Import required libraries
import requests
from bs4 import BeautifulSoup
import pprint

# Create responses for the two pages
res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

# Create soup objects for the two pages
soup_object = BeautifulSoup(res.text, 'html.parser')
soup_object2 = BeautifulSoup(res2.text, 'html.parser')

# Select the required classes from the soup objects
articles = soup_object.select('.titleline')
subtext = soup_object.select('.subtext')
articles2 = soup_object2.select('.titleline')
subtext2 = soup_object2.select('.subtext')

# Combine the articles and subtext from the two pages
combine_articles = articles + articles2
combine_subtext = subtext + subtext2

# Function to sort the stories by votes


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


# Function to create custom Hacker News
def create_custom_hn(articles, votes):
    hn = []
    for index, item in enumerate(art):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace('points', ''))

            if (points > 99):
                hn.append({'title': title, 'link': href, 'votes': points})

    # Sort the stories by votes
    return sort_stories_by_votes(hn)


# Print the custom Hacker News
pprint.pprint(create_custom_hn(combine_articles, combine_subtext))
