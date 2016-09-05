""" Imports old Posts from Wordpress Database to new Blog."""
import mysql.connector

class WordPressImporter(object):
	pass
	# def __init__(self):
	# 	self.cnx = mysql.connector.connect(
	# 		user='mjr_com', password='NMVjRvYhrQatsUxq',
	# 		host='127.0.0.1',
	# 		database='mjrosengrant_com')

	# 	if self.cnx.is_connected():
	# 		print('Connected to WordPress database')
	# 	else:
	# 		print("Failed to connect to DB")
		
	# 	self.cursor = self.cnx.cursor()
	
	# def get_posts(self):
	# 	#query = "SELECT `post_title`,`post_content`,`post_date` from `wp_posts` WHERE `post_status`='publish'"
	# 	# self.cursor.execute(query)

	# 	variable ="var" # self.cursor.fetchone()
 #        print variable
        
 #        # while row is not None:
 #        # 	print "iterating"
 #        # 	row = self.cursor.fetchone()
 #        # 	print type(row)