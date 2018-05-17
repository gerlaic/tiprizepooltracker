# -*- coding: utf-8 -*-
import scrapy
import configparser
Config = configparser.ConfigParser()
import mysql.connector

class Ti8scrapperSpider(scrapy.Spider):
    name = 'ti8scrapper'
    allowed_domains = ['www.dota2.com/international/battlepass/']
    start_urls = ['http://www.dota2.com/international/battlepass//']

    def parse(self, response):
        prizepool = response.css(".PrizePool::text").extract_first() #'$9,251,067'
        # print(prizepool)
        prize_num = prizepool.replace(',','')[1:]
        # print(prize_num)
        # sending to db
        ## read config file
        conf_file = Config.read("config.ini")
        host = Config.get("DB-info", "host")
        user = Config.get("DB-info", "user")
        password = Config.get("DB-info", "password")
        database = Config.get("DB-info", "database")
        table = Config.get("DB-info", "table")

        cmd = ("insert into {0} "
            "(column1, column2, column3, ...)"
            "values "
            "(value1, value2, value3, ...)".format(table))
        
        config = {'host' : host,
                'user' : user,
                'password' : password,
                'database' : database}
        try:
            cnx = mysql.connector.connect(host=host,user=user,
                                        password=password,database=database)
        except mysql.connector.errors.InterfaceError as e:
            print("DB Interface Error")
        pass
        cursor = cnx.cursor()
        cursor.execute(cmd)
        cnx.commit()
        cursor.close()
        cnx.close()
        pass
