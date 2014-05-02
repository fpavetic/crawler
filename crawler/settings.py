# Scrapy settings for crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

# Delay between two requests in seconds
# (to prevent blocking for too many requests)
# default: 0
# DOWNLOAD_DELAY = 0.1

DOWNLOADER_MIDDLEWARES = {
'scrapy.contrib.downloadermiddleware.downloadtimeout.DownloadTimeoutMiddleware': 1
}

# Timeout for request towards a single page in seconds
# default: 180
# DOWNLOAD_TIMEOUT = 30

# default: 16
# CONCURRENT_REQUESTS = 16

# default: 8
# CONCURRENT_REQUESTS_PER_DOMAIN = 8

# First request given is the first triggered
# http://stackoverflow.com/questions/8379065/order-of-crawling-in-scrapy
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'
