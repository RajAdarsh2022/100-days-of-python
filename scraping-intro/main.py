import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/news"
response = requests.get(url=url)
response.raise_for_status()

y_combinator_soup = BeautifulSoup(response.text, 'html.parser')


# Getting the news title and its directed link
news_titles = []
news_titles_tr = y_combinator_soup.find_all("tr", class_= "athing")
for news_title_tr in news_titles_tr:
    title_span = news_title_tr.find("span", class_="titleline")
    title_text = title_span.find("a").get_text()
    title_directed_link = title_span.find("a")['href']
    news_titles.append({
        'title' : title_text,
        'link' : title_directed_link
    })
# print(len(news_titles))

# Getting the upvote count for the particular title
news_upvote_scores_span = y_combinator_soup.find_all("span", class_= "score")
news_upvote_scores = [int(item.get_text().split(' ')[0])  for item in news_upvote_scores_span]
# print(len(news_upvote_scores))
# print(news_upvote_scores)
# Getting the article with maximum upvotes
maximum_upvote = max(news_upvote_scores)
maximum_upvote_news_number = news_upvote_scores.index(maximum_upvote)
news_article_data = news_titles[maximum_upvote_news_number]
news_article_data['upvote_count'] = maximum_upvote

print("News article having maximum upvote is : ")
print(news_article_data)



