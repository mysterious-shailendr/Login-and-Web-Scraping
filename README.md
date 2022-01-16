# Login and Web Scraping Project
## Web scraping project, which requires you to first login and then performs scraping<br/>
A project where you have to first login to scrape the data.<br/>
Mechanize module is used to send request to browser( I used it to login to the requested webpage ), very simple to use and we can perform various operations.<br/>
Beautiful Soup library is used for extracting my response data. It creates a parse tree from page source code that can be used to extract data in a hierarchical and more readable manner, basically a Python library for pulling data out of HTML and XML files.<br/><br/>
I have done scraping on this website: "https://www.jurnal.id/en/"<br/>
First create your account, then you have to create a demo company<br/>
Then just look for the data you want to scrap, i have scraped this accounts section: "https://my.jurnal.id/accounts/chart_of_accounts"<br/>
It's a basic demo, just for understanding purpose.<br/>
You can use this code to scrap any website data which requires login first.<br/><br/>
### Do these installs before running the project,<br/>
> pip install mechanize<br/>
> pip install beautifulsoup4

If anyone got any module error, then install that module like<br/>
> pip install module_name

### Reference <br/>

1). https://mechanize.readthedocs.io/ <br/>
2). https://beautiful-soup-4.readthedocs.io/

#### For any doubts, raise your issues, willingly waiting to help you and clear your doubts...
