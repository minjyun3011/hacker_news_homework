import requests
import time


def get_top_news():
    response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    
    if response.status_code != 200:
        print("APIからデータを取得できませんでした。")
        return

    top_news_list = response.json()[:30] 

    for id in top_news_list:
        top_news_url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
        url_response = requests.get(top_news_url)
        
        if url_response.status_code != 200:
            print(f"ニュース {id} のデータを取得できませんでした。")
            continue

        news_data = url_response.json()
        title = news_data.get('title')
        link = news_data.get('url')

        print({'title': title, 'link': link})
        time.sleep(1)


if __name__ == "__main__":
    get_top_news()
