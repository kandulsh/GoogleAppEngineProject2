#!/usr/bin/env python
#

import webapp2
from google.appengine.api import memcache
from google.appengine.api import users
import time


def factorial(n):
	n = int(n)
	cachednumber = memcache.get(str(n))
	if cachednumber != None:
		return cachednumber
	if n == 0:
		return 1
	else:
		ret = n*factorial(n-1)
	memcache.set(str(n), ret)
	return ret

class MainPage(webapp2.RequestHandler):
  def get(self):
	user = users.get_current_user()
	if user:
		self.response.out.write('<html><body><h1>Hello ')
		self.response.out.write(user.nickname() + "</h1>" )
		self.response.out.write('<br>')
		self.response.out.write('<h2>  Displays factorial of the entered number</h2>')
		
		if 'f' in self.request.GET.keys():
			memcache.flush_all()
		
		start = time.time()
	
		if 'n' in self.request.GET.keys():
			self.response.out.write("Factorial of " + self.request.GET['n'])
			self.response.out.write(" is : " + str(factorial(self.request.GET['n'])))
			self.response.out.write('<br><br>')

		elapsed = time.time() - start
		self.response.out.write('Time: ' + str(elapsed))
		self.response.out.write('<br><br>')
		self.response.out.write('<form method = "GET">')
		self.response.out.write('Enter your number:<input name="n" type="text">')
		self.response.out.write('<input type= "submit">')
		self.response.out.write('<br><br>')
		self.response.out.write('<a href="'+ users.create_logout_url('/'))
		self.response.out.write(' "> Log Out</a> ')
		self.response.out.write('</form></body></html>')
		
	else:
		self.response.out.write('<a href="'+ users.create_login_url('/'))
		self.response.out.write(' "> Log in for Users</a>')

app = webapp2.WSGIApplication([
  ('/', MainPage),
 ], debug=True)
