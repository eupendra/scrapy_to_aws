SPIDER_MODULES = ['books.spiders']



ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
IMAGES_STORE = 's3://coderecode-scrapy-demo/images/'
IMAGES_STORE_S3_ACL = 'public-read'


