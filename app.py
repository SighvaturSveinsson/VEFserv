from bottle import *
import os

@route('/')
def index():
  return "Hallo heimur"
  
run(host='0.0.0.0', port=os.environ.get("PORT"))
