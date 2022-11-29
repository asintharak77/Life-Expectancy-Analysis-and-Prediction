#!/usr/bin/env python
# coding: utf-8

# In[1]:


from ast import Return
from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('life.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['Schooling']
    data2 = request.form['Income composition of resources']
    data3 = request.form[' BMI ']
    data4 = request.form['Diphtheria ']
    data5= request.form['Polio']
    data6= request.form['under-five deaths ']
    data7= request.form[' thinness 5-9 years']
    data8= request.form[' thinness  1-19 years']
    data9= request.form[' HIV/AIDS']
    data10= request.form['Adult Mortality']

    
    arr = np.array([[data1, data2, data3, data4,data5,data6,data7,data8,data9,data10]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)



# %%
