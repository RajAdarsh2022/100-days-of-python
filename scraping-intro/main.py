import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/news"
response = requests.get(url=url)
response.raise_for_status()

y_combinator_soup = BeautifulSoup(response.text, 'html.parser')


# Getting the news title and its directed link
news_titles = []
upvote_scores = []
news_titles_tr = y_combinator_soup.find_all("tr", class_= "athing")
for news_title_tr in news_titles_tr:
    # only store it in the list if the upvote count is present
    news_title_upvote_tr = news_title_tr.next_sibling
    news_title_upvote_score_span = news_title_upvote_tr.find("span", class_="score")
    if news_title_upvote_score_span:

        title_span = news_title_tr.find("span", class_="titleline")
        title_text = title_span.find("a").get_text()
        title_directed_link = title_span.find("a")['href']

        news_upvote_score = int(news_title_upvote_score_span.get_text().split(' ')[0])
        news_titles.append({
            'title' : title_text,
            'link' : title_directed_link
        })
        upvote_scores.append(news_upvote_score)
        # print(f"{title_text} : {news_upvote_score}")


# print(len(news_titles))
# print(len(upvote_scores))



# Getting the article with maximum upvotes
maximum_upvote = max(upvote_scores)
maximum_upvote_news_number = upvote_scores.index(maximum_upvote)
news_article_data = news_titles[maximum_upvote_news_number]
news_article_data['upvote_count'] = maximum_upvote

print("News article having maximum upvote is : ")
print(news_article_data)



