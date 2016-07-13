import os


CSRF_ENABLED=True          
SECRET_KEY='you-will-never-guess'

OPENID_PROVIDERS=[
    {'name':'Google','url':'https://www.google.com/accounts/o9/id'},
    {'name':'Baidu','url':'http://www.baidu.com'},
    {'name':'Taobao','url':'http://www.taobao.com'},
    {'name':'Sohu','url':'http://www.sohu.com'},
    {'name':'CSDN','url':'http://www.csdn.net'},
]

#=====================
#database
#=====================
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
