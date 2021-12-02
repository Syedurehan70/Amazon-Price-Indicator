# Amazon-Price-Indicator

So this is my first scrappping project, we're going to amazon.com page where we searched a product we're interested in,
once it's found we copy the URL, and saved it as product_url.

and finally after getting headers, we made a requests to the url, than we've parsed it with BeautifulSoup and scrapped the prize and the title of the product,
than we've separated the prize and compared it with the prize we think is suitable for that, if the prize is lower than what we want, we'll send an emmail alert.

which  tells us that the product is at lower prize right you can buy it, we can schedule thisa program to run every min or hour or everyday using "pyhton anywhere" service.
