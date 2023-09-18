from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import random
import requests
from bs4 import BeautifulSoup
import queue

class CrawlingSpider(CrawlSpider):
    name = "OurCrawler"
    allowed_domains =["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Main_Page"]


   

    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item")
    )

    def parse_item(self,response):

        yield{

               "title":response.css(".product_main h1::text").get(),
               "price":response.css(".price_color ::text").get(),
               "availability":response.css(".availability ::text")[1].get().replace("\n", "").replace(" ", "")
            }

            # #Here's some sample code in Python to address some of the problems faced by web crawlers:

# Duplicate content:
visited_pages = set()

def crawl_page(urls):
    if urls in visited_pages:
        return

    # process page and extract relevant information
    visited_pages.add(urls)
    

# Blocked pages:


user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    # ...
]

def crawl_page(urls):
    headers = {
        "User-Agent": random.choice(user_agents)
    }

    # send request with headers and process the page
    
    
# Dynamic pages:


def crawl_page(urls):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # extract relevant information from the page
    
    
# Large websites:


page_queue = queue.PriorityQueue()

def crawl_page(urls, priority=0):
    page_queue.put((priority, urls))

    # process pages in the queue with the highest priority first

    from collections import deque

visited_pages = set()
page_queue = deque()

def crawl_page(url):
    if url in visited_pages:
        return

    # process page and extract relevant information


    
    visited_pages.add(url)
    page_queue.append(url)

    while page_queue:
        current_url = page_queue.popleft()
        # do something with the current page
        # ...
        # add the next set of pages to the queue
        for next_page in get_next_pages(current_url):
            page_queue.append(next_page)