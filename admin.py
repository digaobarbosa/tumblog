__author__ = 'digao'
from flask.ext.admin import Admin
from flask.ext.admin.contrib.mongoengine import ModelView
from models import *


admin = Admin(name='Tumblog')
# Add administrative views here
admin.add_view(ModelView(TestCase))
admin.add_view(ModelView(Post))
admin.add_view(ModelView(Comment))
