#!/usr/bin/env python

"""Crawls through Amazon web for products of certain category and price range. Modify urls to appropriate for results"""

__author__      = "Kiran Yedugundla"
__copyright__   = "GNU PL"


from urllib2 import urlopen
import urllib2
import re
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
from pprint import pprint
import locale
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 


class Sample:
	link = ''
	title = ''
	values = None

def main():
	html_parser = HTMLParser()
	murl="http://www.amazon.com"
	#urls="http://www.amazon.com/s/ref=sr_pg_2?rh=n%3A15684181%2Cp_36%3A10-500&page=2&bbn=15684181&ie=UTF8&qid=1380599008"
	
	lp = 0.51
	hp = 1.0
	for stopper in 
	urli="http://www.amazon.com/s/ref=sr_nr_p_36_5?bbn=1055398&qid=1381306286&rh=n%3A1055398%2Cp_n_condition-type%3A6358196011&rnid=386465011&low-price="+str(lp)+"&high-price="+str(hp)+"&x=5&y=10"
	print urli
	req = urllib2.Request(urli)
	req.add_header('User-agent', 'Mozilla 5.10')
	r=urlopen(req).read()
	#print r
	soup = BeautifulSoup(r)
	h2 = soup.find("h2",{"class":"resultCount"})
	t = h2.span.text
	t = t.replace(",","")
	ti = re.findall('\d+', t)[2]
	print ti
	
	nps=[]
	for seem in soup.find_all("li",{"style":"margin-left: -2px;"}):
		sellink = seem.find("a").get("href")
	newselurl = murl + sellink
	req = urllib2.Request(newselurl)
	req.add_header('User-agent', 'Mozilla 5.10')
	r=urlopen(req).read()
	#print r
	soup = BeautifulSoup(r)
	for urln in soup.find_all("span", {"class": "pagnLink"}):
		s1 = Sample()
		s1.link = urln.find("a").get("href")
		s1.title=urln.find("a").text
		s1.values=[]
		nps.append(s1)
	del soup
	scount = 0
	itemxs = 0
	for ind in range(0, 27):
		newselurl = murl + nps[ind].link
		req = urllib2.Request(newselurl)
		req.add_header('User-agent', 'Mozilla 5.10')
		r=urlopen(req).read()
		soup = BeautifulSoup(r)
		for sv in soup.find_all("span", {"class": "narrowValue"}):
			s = sv.text
			v = s[s.find("(")+1:s.find(")")] 
			nps[ind].values.append(v)
		del soup
		print nps[ind].title
		tots = 0
		for x in nps[ind].values:
			print x,
			scount = scount + 1
			tots = tots + locale.atoi(x)
		print tots
		itemxs = itemxs + tots
	nps=[]
	f = open('OutputHomeandKitchenSellers.txt','w')
	ps = str(lp) + "-" + str (hp) + "-" + str(itemxs) + "-" + str(scount)+"-"+str(ti)
	f.write(ps)

if __name__ == '__main__':
    main()
