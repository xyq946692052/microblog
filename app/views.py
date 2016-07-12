from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user={'nickname':'Kevin Xie'}  #fade user
    posts=[    #fade array of posts
              {'author':{'nickname':'John'},
                'body':'beautiful day in Portland!'
              },
              {
                'author':{'nickname':'Anne'},
                'body':'The Avengers movie was cool!'
              } 

          ]
    return render_template('index.html',title='Home',user=user,posts=posts)


