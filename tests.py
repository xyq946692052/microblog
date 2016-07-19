#!venv/bin/python
import os
import unittest

from config import basedir
from app import app,db
from app.models import User,Post
from datetime import datetime,timedelta


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
        u1=User(nickname='John',email='xyq@sina.com')
        u2=User(nickname='Anne',email='anne@sina.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        assert u1.unfollow(u2)==None
        u=u1.follow(u2)
        db.session.add(u)
        db.session.commit()
        assert u1.follow(u2)
        assert u1.is_folowing(u2)
        assert u1.followed.count()==1
        assert u1.followed.first().nickname=='Anne'
        assert u2.followers.count()==1
        assert u2.followers.first().nickname=='John'
        u=u1.unfollow(u2)
        assert u!=None
        db.session.add(u)
        db.session.commit()
        assert u1.is_following(u2)==False
        assert u1.followed.count()==0
        assert u1.followers.count()==0

    def test_follow_posts(self):
        #make four users
        u1=User(nickname='Peter',email='peter@sina.com')
        u2=User(nickname='Ken',email='ken@sina.com')
        u3=User(nickname='Tom',email='tom@sina.com')
        u4=User(nickname='Sue',email='sue@sina.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.add(u3)
        db.session.add(u4)
        #make four posts
        utcnow=datetime.utcnow()
        p1=Post(body='post from Peter',author=u1,timestamp=utcnow+timedelta(seconds=1))
        p2=Post(body='post from Ken',author=u2,timestamp=utcnow+timedelta(seconds=2))
        p3=Post(body='post from Tom',author=u3,timestamp=utcnow+timedelta(seconds=3))
        p4=Post(body='post from Sue',author=u4,timestamp=utcnow+timedelta(seconds=4))
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        u1.follow(u1)
        u1.follow(u2)
        u1.follow(u4)
        u2.follow(u2)
        u2.follow(u3)
        u3.follow(u3)
        u3.follow(u4)
        u4.follow(u4)
        db.session.add(u1)
        db.session.add(u2)
        db.session.add(u3)
        db.session.add(u4)
        db.session.commit()
        #check the followed posts of each other
        f1=u1.followed_posts().all()
        f2=u2.followed_posts().all()
        f3=u3.followed_posts().all()
        f4=u4.followed_posts().all()
        assert len(f1)==3
        assert len(f2)==2
        assert len(f3)==2
        assert len(f4)==1
        assert f1==[p4,p2,p1]
        assert f2==[p3,p2]
        assert f3==[p4,p3]
        assert f4==[p4]

if __name__=='__main__':
    unittest.main()


