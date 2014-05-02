crawler
=======
Scrapy based crawler: given a start URL it spreads to the pages at most <max_depth> distance from it in BFS fashion.

It is run by the following command:
```
scrapy crawl bfs -a start_urls=http://en.wikipedia.org/wiki/Main_Page -a max_depth=1 -a output_file=edges
```     

The output consists of edges between visited URLs in the format:
```
source|destination|text which contained the link
```
<br>
<br>
This crawler is created for testing the methods for web link analysis described in:<br>
Tamara G. Kolda, Brett W. Bader, Joseph P. Kenny: Higher-Order Web Link Analysis Using Multilinear Algebra
(http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=01565685&tag=1)


Dependencies
------------
Scrapy (http://scrapy.org/)

