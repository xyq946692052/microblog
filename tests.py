#!venv/bin/python
import os
import unittest

from config import basedir
from app import app,db
from app.models import User

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING']=True
        app.config['WTF_CSRF_ENABLED']=False
        app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'test.db')
        self.app=app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_make_unique_nickname(self):
        u=User(nickname='Join',email='xyq2312@sina.com')
        db.session.add(u)
        db.session.commit()
        nickname=User.make_unique_nickname('John')
        assert nickname !='John'
        u=User(nickname=nickname,email='946692052@qq.com')
        db.session.add(u)
        db.session.commit()
        nickname2=User.make_unique_nickname('John')
        assert nickname2!='John'
        assert nickname2!=nickname

    def test_follow(self):
        u1=User(nickname='John',email='xyq2312@sina.com')
        u2=User(nickname='Kevin',email='xyq20103139@sina.com'
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        assert u1.unfollow(u2)==None
        u=u1.follow(u2)
        db.session.add(u)
        db.session.commit()
        assert u1.follow(u2)==None
        assert u1.is_following(u2)
        assert u1.followed.count()==1
              

if __name__=='__main__':
    unittest.main()
