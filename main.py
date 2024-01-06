import os
from scrape import scrape
from make_pretty import make_pretty

def main():
    scrape()
    make_pretty()
    os.remove('/var/www/html/index.html')
    os.rename('output/index.html','/var/www/html/index.html')

main()