from bs4 import BeautifulSoup as BS 
import re
import os

buzzwords = ["malware", 
             "vulnerability", 
             "dark web",
             "exploit",
             "infostealer",
             "backdoor",
             "exploited",
             "hacked",
             "hackers",
             "malicious",
             ]

def output_pretty_hackernews():
    """Output scraped data from thehackernews in a nice easy to view format without images"""
    with open("webpages/thehackernews.html") as fp:
        soup = BS(fp, 'html.parser')
    links = []
    output = soup.find_all('a',class_='story-link')
    count = 0
    for x in output:
        links.append((str(x)+'\n'))
        count += 1
        if count == 5:
            break
    # regex_output = soup.find_all(string=re.compile('(?i)(?:malware|vulnerability|dark web|exploit|infostealer|backdoor|exploited|hacked|hackers|malicious|href)')) ---- Incase the need for this arises
    with open('output/thehackernews_temp_output.html','w', encoding='utf-8') as file:
        for x in links:
            file.write(x)
    with open('output/thehackernews_temp_output.html','r') as ifile:
        reading = ifile.readlines()
        with open('output/thehackernews_final_output.html','w') as ofile:
            for x in reading:
                if 'img' in x:
                    pass
                if 'href' in x:
                    x = x.replace('<a class="story-link"','<h4><a ')
                    x = x.replace('\n', '')
                    y = x.split('"')[1]
                    ofile.write(x+y+'</a></h4>\n')
    os.remove('output/thehackernews_temp_output.html')

def output_pretty_cybersecuritynews():
    """Output scraped data from cybersecuritynews in a nice easy to view format without images"""
    with open('webpages/cybersecuritynews.html') as fp:
        soup = BS(fp, 'html.parser')
    links = []
    output = soup.find_all('h3', class_='entry-title td-module-title')
    for x in output:
        links.append((str(x)+'\n'))
    with open('output/cybersecuritynews_temp_output.html','w',encoding='utf-8') as file:
        for x in links:
            file.write(x)
    with open('output/cybersecuritynews_temp_output.html','r') as ifile:
        reading = ifile.readlines()
        with open('output/cybersecuritynews_final_output.html','w') as ofile:
            count = 0
            for x in reading:
                x = x.replace('h3', 'h4')
                ofile.write(x)
                count+=1
                if count == 5:
                    break
    os.remove('output/cybersecuritynews_temp_output.html')

def output_pretty_bleepingcomputer():
    """Output scraped data from bleepingcomputer in a nice easy to view format without images"""
    with open('webpages/bleepingcomputer.html') as fp:
        soup = BS(fp, 'html.parser')
    links = []
    output = soup.find_all('h4')
    count = 0
    for x in output:
        links.append((str(x)+'\n'))
        count += 1
        if count == 15:
            break
    with open('output/bleepingcomputer_temp_output.html','w',encoding='utf-8') as file:
        for x in links:
            file.write(x)
    with open('output/bleepingcomputer_temp_output.html','r') as ifile:
        reading = ifile.readlines()
        with open('output/bleepingcomputer_final_output.html','w') as ofile:
            count = 0
            for x in reading:
                if 'href' in x and count !=5:
                    ofile.write(x)
                    count += 1
                else:
                    pass
    os.remove('output/bleepingcomputer_temp_output.html')

def output_pretty_theregister():
    """Output scraped data from theregister in a nice easy to view format without images"""
    with open("webpages/theregister.html") as fp:
        soup = BS(fp, 'html.parser')
    links = []
    output = soup.find_all('article')
    count = 0
    for x in output:
        links.append((str(x)+'\n'))
        count += 1
        if count == 5:
            break
    with open('output/theregister_temp_output.html','w', encoding='utf-8') as file:
        for x in links:
            file.write(x)
    with open('output/theregister_temp_output.html','r') as ifile:
        reading = ifile.readlines()
        with open('output/theregister_final_output.html','w') as ofile:
            for x in reading:
                if 'href' in x:
                    x = x.replace('href="', 'href="https://theregister.com')
                    x = x.replace('<a class="story_link"','<h4><a ')
                    x = x.replace('\n', '')
                    y = x.split('"')[1]
                    ofile.write(x+y+'</a></h4>\n')
    os.remove('output/theregister_temp_output.html')


def make_pretty():
    """take the data from scrape and make it presentable on a html page"""
    output_pretty_hackernews()
    output_pretty_cybersecuritynews()
    output_pretty_bleepingcomputer()
    output_pretty_theregister()
    directories = os.listdir('output')
    os.chdir('output')
    complete_output = ""
    #equals = "="*50
    for x in directories:
        if x == 'index.html':
            pass
        else:
            with open(x,'r') as file:
                reading = file.read()
                complete_output += f"<hr>\n<h3>{x.split('_')[0]}</h3>\n<hr>\n{reading}\n"
    with open('index.html','w') as file:
        file.write(complete_output)
    for x in directories:
        if x == 'index.html':
            pass
        else:
            os.remove(x)
    os.chdir('../')

#make_pretty()


