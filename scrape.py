import requests
import os

urls_which_are_awkward = ["ncsc.gov.uk/section/keep-up-to-date/ncsc-news?q=&defaultTypes=news,information&sort=date%2Bdesc",
                          "wired.com/category/security/",
                          "securityweek.com/",
                          ]

urls_that_work = ["thehackernews.com",
        "cybersecuritynews.com/",
        "theregister.com/security/",
        "bleepingcomputer.com/",
        ]

def get_webpage(webpage):
    """get the webpage data and write it to a file"""

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"} 
    # can be discover current user_agent through httpbin.org (may need changing if the pages block this one)
    webpage_url = f"https://www.{webpage}"
    webpage_request = requests.get(webpage_url, headers=headers)
    webpage_text = webpage_request.text
    #print(webpage_request.status_code)
    with open(f"{webpage.split('.')[0]}.html","w") as file:
        file.write(webpage_text)


def scrape():
    """full scrape function. Scrape data ready to be made pretty"""    
    os.chdir("webpages")
    for url in urls_that_work:
        try:
            get_webpage(url)
            #print("scrape successful \n")
        except Exception as e:
            print(f"{url} scrape failed")
            print(f"\n {e} \n")
    os.chdir("../")
    
#scrape()