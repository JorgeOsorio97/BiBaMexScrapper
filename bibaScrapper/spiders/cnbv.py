import scrapy
from scrapy.http import Request


class CnbvSpider(scrapy.Spider):
    debug_name = ('===== CNBV ===== : ')
    name = 'cnbv'
    allowed_domains = [
        'picomponentebi.cnbv.gob.mx']
    start_urls = ['https://picomponentebi.cnbv.gob.mx/ReportViwer/ReportService?sector=40&tema=2&subTema=3&tipoInformacion=0&subTipoInformacion=0&idReporte=040_11q_BIPER0&idPortafolio=0&idTipoReporteBI=1068']

    def parse(self, response):
        url_list = response.url.split('/')
        url = ''.join(['//'.join([url_list[0], url_list[2]]),
                       response.xpath('//iframe[@id="IFrame_Container"]/@src').get()])
        print(self.debug_name)
        print(len(response.xpath('//iframe')))
        print(self.debug_name)
        # print(response.body)
        yield Request(url=url, callback=self.parse_iframe_1)

    def parse_iframe_1(self, response):
        print(self.debug_name + str(response))
        print(self.debug_name + str(response.xpath('//iframe/@src')))
        print(self.debug_name + str(response.body))
        yield response.xpath('//iframe/@src')
