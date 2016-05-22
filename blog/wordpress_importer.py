""" Imports old Posts from Wordpress Database to new Blog."""
import mysql.connector

class WordPressImporter(object):
	def __init__(self):
		self.cnx = mysql.connector.connect(
			user='mjr_com', password='NMVjRvYhrQatsUxq',
			host='127.0.0.1',
			database='mjrosengrant_com')

		if self.cnx.is_connected():
			print('Connected to WordPress database')
		else:
			print("Failed to connect to DB")
		
		self.cursor = self.cnx.cursor()
		print type(self.cursor)
	
	def get_posts(self):
		query = ("SELECT `post_title`,`post_content`,`post_date` from `wp_posts` WHERE `post_status`='publish'")
		self.cursor.execute(query)

		post = self.cursor.fetchone()
        print post
        # while row is not None:
        # 	print "iterating"
        # 	row = self.cursor.fetchone()
        # 	print type(row)