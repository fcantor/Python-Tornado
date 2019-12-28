#!/usr/bin/python3

import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("Hello, world! This is a python command from the backend!")

class queryParamRequestHandler(tornado.web.RequestHandler):
  def get(self):
    num = self.get_argument("num")
    if (num.isdigit()):
      r = "odd" if int(num) % 2 else "even"
      self.write(f"{num} is {r}")
    else:
      self.write(f"{num} is not a valid integer")

class renderHTMLRequestHandler(tornado.web.RequestHandler):
  def get(self):
    self.render("index.html")

class resourceParamRequestHandler(tornado.web.RequestHandler):
  def get(self, studentName, courseID):
    self.write(f"Welcome, {studentName}! This is course number {courseID}")

if __name__ == "__main__":
  app = tornado.web.Application([
    (r"/", basicRequestHandler),
    (r"/animals", renderHTMLRequestHandler),
    (r"/isEven", queryParamRequestHandler),
    (r"/students/([A-Za-z]+)/([0-9]+)", resourceParamRequestHandler)
  ])

  port = 8882
  app.listen(port)
  print(f"Application is ready and listening to {port}")
  tornado.ioloop.IOLoop.current().start()
