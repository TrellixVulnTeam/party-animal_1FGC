import os
import re
import csv
import json
from urllib.parse import urlparse

class Utilities:
	def __init__(self):
		return None
	# __init__

	def write_csv(self, report_path, file_name, csv_rows):
		"""
		basic utility function to write list of csv rows to a file
		"""
		full_file_path = report_path+'/'+file_name
		with open(full_file_path, 'w', newline='', encoding='utf-8') as csvfile:
			csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
			for row in csv_rows:
				csv_writer.writerow(row)
		print('\t\tOutput written to %s' % full_file_path)
	# write_csv

	def get_absolute_url_from_page_link(self,page_url,link_url):
		"""
		Given a page_url and a link_url from that page we determine
			the absolute url of the link from the page_url.
		"""

		# ex nihilo nihil fit
		if link_url == None: return None
		if len(link_url) == 0: return None

		# we use the info from the original url for converting 
		#	relative links to absolute
		parsed_page_url = urlparse(page_url)

		# this is an absolute url already, nothing further to do to
		if re.match('^https?://', link_url):
			return(link_url)
		# link with no scheme, paste it in
		elif re.match('^//', link_url):
			return(parsed_page_url.scheme+':'+link_url)
		# relative link, fix it up
		else:
			if link_url[0] != '/':
				return(parsed_page_url.scheme + '://' + parsed_page_url.netloc + '/' + link_url)
			else:
				return(parsed_page_url.scheme + '://' + parsed_page_url.netloc + link_url)

		# this only happens if something breaks
		return None
	# get_absolute_url_from_link
# Utilities	
