# tiny_spider
a easy spider for get info from OA system

Yesteday I got a task from boss, which was copy a lot series items from a webpage. For he didn't konw that I CAN WRITE A SCRIPT, he gave me two work-days to finish this task. Well, you know how could I do this such a boring and repeatable task. So I wrote a tiny spider using python to get info from webpage automaticlly.

Because this spider script is so tiny to describe, so I just put the origenal code to hub.(for review at one day in the future.)

But even thought the script is so tihy and simple, I still catch some troubles.

__1. Hack The OA Account Check.__

OA system is a complex infomation system for enterprize, so it has a high level security politics such as Identify Check or others. In this project, one trouble for me is how to cheat the OA system that I am a people rathor than a python Robot. One convinent method is using the Cookies in that moment. 

For specific, we should obtain the cookies info from web inspect page (Ctrl + Shift + I). Do any operation in the page and then get the cookies info from network's files, such as this:

 ![alt-text](https://github.com/StrangeData-v/tiny_spider/blob/master/show_cookies.png)

And then use the cookies to create a headers:

```
import requests
import bs4

url = url
hd = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36','Cookie':'languageidweaver=7; __clusterSessionCookieName=122C10202D87F4DEDA654B7A04BB459A; JSESSIONID=ebdOTRujJYs_74JJuNk7w; ecology_JSessionId=ebdOTRujJYs_74JJuNk7w; Systemlanguid=7; loginidweaver=wzhf2019; loginuuids=11685; xzutyzw=3BBC0A2F238026BEF04F4BEDEC06E06E6050B9FD7CEE1AFAAA345A693EABDB4A86306C4AE5CF650048C63634154E37C424019CB424F9DB530F6DBD0636C13C28; rutixcd=dbf5965d-e27a-442c-bd38-23d58396e686; SERVERID=e8b1347689a1e5b15b5fd45029743bb5|1575358694|1575357336'}

response = requests.get(url = url , headers = hd)
soup = bs4.BeautifulSoup(response.content)
```

__2. Analyse Html File__

Just use bs4 and built-in function to finish this part. A commen process of getting information from a page html file. But in this part, using __re__ (regular expression) will be better. 
