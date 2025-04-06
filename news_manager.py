


class news_manager:
    def __init__(self, news_list):
        self.news_list = news_list

    def add_news(self, news_item):
        self.news_list.append(news_item)

    def remove_news(self, news_item):
        if news_item in self.news_list:
            self.news_list.remove(news_item)
        else:
            print("News item not found.")

    def display_news(self):
        for news in self.news_list:
            print(news)