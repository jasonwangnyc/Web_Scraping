from scrapy import Spider, Request
from Youtube.items import YoutubeItem
import re

class YoutubeSpider(Spider):
	name = 'Youtube_spider'
	allowed_urls = ['https://socialblade.com/']
	start_urls = ['https://socialblade.com/youtube/top/5000/mostsubscribed']

	def parse(self, response):
		URL_list=response.xpath('//div[@style="float: left; width: 350px; line-height: 25px;"]/a/@href').extract()	

		for i in range(len(URL_list)):
			Subscribe_Rank = i+1
			yield Request(url='http://socialblade.com'+URL_list[i],meta={'name':Subscribe_Rank}, callback=self.parse_result) 
	def parse_result(self, response):
		Subscribe_Rank = response.meta['name']
		Username = response.xpath('//*[@id="YouTubeUserTopInfoBlockTop"]/div[1]/h1/text()').extract()
		Uploads = response.xpath('//*[@id="YouTubeUserTopInfoBlock"]/div[2]/span[2]/text()').extract()
		Subscribers = response.xpath('//*[@id="YouTubeUserTopInfoBlock"]/div[3]/span[2]/text()').extract()
		Views = response.xpath('//*[@id="YouTubeUserTopInfoBlock"]/div[4]/span[2]/text()').extract()
		Country = response.xpath('//*[@id="youtube-user-page-country"]/text()').extract()
		Type = response.xpath('//*[@id="youtube-user-page-channeltype"]/text()').extract()
		Created_Date = response.xpath('//*[@id="YouTubeUserTopInfoBlock"]/div[7]/span[2]/text()').extract()
		Views_Rank = response.xpath('//*[@id="afd-header-videoview-rank"]/text()').extract()
		Estimated_Yearly_Earning = response.xpath('/html/body/div[15]/div[2]/div[1]/div[2]/div[3]/div[2]/p[1]/text()').extract()

		item = YoutubeItem()
		item['Username'] = Username
		item['Uploads'] = Uploads
		item['Subscribers'] = Subscribers
		item['Views'] = Views
		item['Country'] = Country
		item['Type'] = Type
		item['Created_Date'] = Created_Date
		item['Subscribe_Rank'] = Subscribe_Rank
		item['Views_Rank'] = Views_Rank
		item['Estimated_Yearly_Earning'] = Estimated_Yearly_Earning

		yield item