from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_sqlalchemy import SQLAlchemy


from content import content_mapper
from content import sectiontitle_list
content_dict=content_mapper()

sec_list=sectiontitle_list()

 
app = Flask(__name__)
db=SQLAlchemy(app)
@app.route('/') 
@app.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html',content_dict=content_dict,sec_list=sec_list)
 
if __name__ == "__main__":
    app.run(debug=True)