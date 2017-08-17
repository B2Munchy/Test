import webapp2

class MainPage(webapp2.RequestHandler):
	self.response.headers['Content-Type'] = 'text/plain'
	self.response.out.write('Hello, webapp World!')


app = webapp2.WSGIApplication([('/', MainPage)], debug = True)
