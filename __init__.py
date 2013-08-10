__author__ = 'digao'
from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "my_tumble_log"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"
db = MongoEngine()
db.init_app(app)

def register_blueprints(app):
    # Prevents circular imports
    from views import posts
    app.register_blueprint(posts)
    from admin import admin
    admin.init_app(app)


register_blueprints(app)


if __name__ == '__main__':
    app.run()

