Web scraping refers to the extraction of data from a website. 
This information is collected and then exported into a format that is more useful for the user. 
Be it a spreadsheet or an API.

Although web scraping can be done manually, in most cases, automated tools are preferred when scraping web data as they can be less costly and work at a faster rate.

In this project, we have gone along different libraries of python to beautifully present the data of any website.
->First we installed requests module, BeautifulSoup and html8lib in a file through terminal
Steps:
    ->pip install requests
    ->pip install bs4
    ->pip install html5lib

requests->Requests allows you to send HTTP/1.1 requests extremely easily. 
          There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method!
          here we will use this to send our request thru the url.

bs4->Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching,        and   modifying the parse tree.

html5lib->html5lib is a pure-python library for parsing HTML.
         It is designed to conform to the WHATWG HTML specification, as is implemented by all major web browsers.

After using the commands in 'main.py' we get the html page in the terminal.
There are other commands that can be used to get the various parts of the page -> refer to 'READMECode.txt'

By Prakriti Mandal