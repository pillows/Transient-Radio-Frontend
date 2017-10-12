from flask import Flask, render_template, request, make_response, send_file
from web1 import guplot
from web import form
import numpy as np
import shutil
import string
import random
import os
import sys
import glob
import sqlite3
import hashlib
import shutil
app = Flask(__name__)
@app.route('/',methods=['GET', 'POST'])

def index():
    postmd5 = hashlib.md5(str(request.get_data())).hexdigest()
    if request.method == "POST":
      fframe = request.form['fframe']
      ftframe = request.form['ftframe']
      snmin = request.form['snmin']
      dmmin = request.form['dmmin']
      dmmax = request.form['dmmax']
      tmin = request.form['tmin']
      tmax = request.form['tmax']
      guplot(postmd5,float(fframe),float(ftframe),float(snmin), float(dmmin),float(dmmax),float(tmin),float(tmax))
      shutil.move(postmd5+".png","static/img/"+postmd5+".png")
      
      return render_template('index.html',postmd5=postmd5)
    else:
      return render_template('index.html')

if __name__ == '__main__':

      app.run(host='0.0.0.0', port=6008, debug=True)
