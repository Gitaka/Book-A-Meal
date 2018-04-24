from flask import Flask


#initialize the application
app = Flask(__name__,instance_relative_config=True)


#load the config file
app.config.from_object('config')