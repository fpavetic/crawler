from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
import threading

class BfsSpider(CrawlSpider):
    name = "bfs"
    start_urls = []
    max_depth = 0

    # runtime variables
    depth = {}
    depth_lock = threading.Lock()

    output_file = None
    output_file_lock = threading.Lock()

    def __init__(self, start_urls, max_depth, output_file):
        # | is used as a delimited between start urls
        self.start_urls = start_urls.split("|")
        self.max_depth = int(max_depth)
        self.output_file = open(output_file, 'w')
        
        for url in self.start_urls:
            self.depth[url] = 0

    def parse(self, response):
        url = response.url
        if 'redirect_urls' in response.meta:
            url = response.meta['redirect_urls'][0]

        stop_spreading = False
        self.depth_lock.acquire()
        if url not in self.depth:
            print "WEIRD " + url
            stop_spreading = True
        elif self.depth[url] >= self.max_depth:
            stop_spreading = True
        self.depth_lock.release()
        
        if stop_spreading == True:
            return

        link_extractor = SgmlLinkExtractor(unique=False)
        links = link_extractor.extract_links(response)
        
        requests = []
        print len(links)
        for link in links:
            if link.text.strip() != '':
                self.output_file_lock.acquire()
                self.output_file.write(url)
                self.output_file.write('|')
                self.output_file.write(link.url)
                self.output_file.write('|')
                self.output_file.write(link.text.encode('utf-8', 'replace'))
                self.output_file.write('\n')
                self.output_file_lock.release()

                self.depth_lock.acquire()
                should_spread = False
                if link.url not in self.depth or self.depth[url] + 1 < self.depth[link.url]:
                    self.depth[link.url] = self.depth[url] + 1
                    should_spread = True
                self.depth_lock.release()

                if should_spread == True:
                    yield Request(url=link.url)
