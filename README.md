## Part 1. Test Instruction

1. Go the the APP link: https://ancient-falls-36830.herokuapp.com and enter the keyword for query;
2. Or use the HTTP GET method directly, such as:
* https://ancient-falls-36830.herokuapp.com/query?keyword=YING+XIANG
* https://ancient-falls-36830.herokuapp.com/query?keyword=AZOV+ANCH

## Part 2. All Required Packages

beautifulsoup4==4.6.0  
bs4==0.0.1  
certifi==2018.1.18  
chardet==3.0.4    
click==6.7  
Flask==0.12.2  
gunicorn==19.7.1  
idna==2.6  
itsdangerous==0.24  
Jinja2==2.10  
lxml==4.1.1  
MarkupSafe==1.0  
requests==2.18.4  
urllib3==1.22  
Werkzeug==0.14.1

## Part 3. Self-evaluation

### Positive:
1. It does not require API key and uses User-Agent of the Chrome Developer Tools;
2. Deployed via Heroku;
3. It returns the records from all the pages for a keyword, and it supports all the 9 result types (i.e. 'Vessel', 'Callsign', 'Light', 'Exname', 'IMO number', 'MMSI number', 'Port', 'Station', 'Photographer').

### Negative:

1. The address I used for retrieving data from is: https://www.marinetraffic.com/en/ais/index/search/all?keyword=YUEJIANGCHENG90609, which does not accept other parameters like 'location'. Therefore, this API will only use one parameter, namely, 'keyword';
2. If the type you search is a 'Port', then you would notice there is a formatting problem with the variable 'Local Time', as I didn't find a way to convert it properly. For example: https://ancient-falls-36830.herokuapp.com/query?keyword=AZOV+ANCH;
3. Does not support too many records, so please do NOT enter keyword that will have hundreds of records (e.g. SHANGHAI), or the website might ban you temporarily.


