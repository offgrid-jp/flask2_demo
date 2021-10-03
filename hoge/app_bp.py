from flask import Flask, Blueprint
from route import web

app = Flask(__name__)

app.register_blueprint(web.bp)

if __name__ == "__main__":
  app.run()