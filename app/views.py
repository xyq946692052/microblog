from flask import render_template,flash,redirect
from app import app
from .forms import LoginForm

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

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login requirested for openID="'+form.openid.data+'",remember_me='+str(form.remember_me.data ))
        return redirect('/index')
    return render_template('login.html',title='Sign In',form=form,
        providers=app.config['OPENID_PROVIDERS'])

