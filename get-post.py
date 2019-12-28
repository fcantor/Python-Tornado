#!/usr/bin/python3

import tornado.web
import tornado.ioloop
import json

class listRequestHandler(tornado.web.RequestHandler):
  def get(self):
    file = open("list.txt", "r")
    starTrekCharacters = file.read().splitlines()
    file.close()
    self.write(json.dumps(starTrekCharacters))
  def post(self):
    character = self.get_argument("character")
    file = open("list.txt", "a")
    file.write(f"{character}\n")
    file.close()
    self.write(json.dumps({"message": "Character added successfully!"}))

if __name__ == "__main__":
  app = tornado.web.Application([
    (r"/characters", listRequestHandler)
  ])

  port = 8882
  app.listen(port)
  print(f"Application is ready and listening to port {port}")
  tornado.ioloop.IOLoop.current().start()