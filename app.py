from flask import Flask, render_template, jsonify
from markupsafe import escape
'''
venv\Scripts\activate
'''
app = Flask(__name__)

JOBS = [
    {
       'id':1,
       'title': 'Data Analyst',
       'location':'San Pedro, San José',
       'salary': '$975'
    },
    {
       'id':2,
       'title': 'Data Analyst II',
       'location':'San Pedro, San José',
       'salary': '$1350'
    },
    {
       'id':3,
       'title': 'Junior Python Developer',
       'location':'Santa Ana, Heredia',
       'salary': '$1500'
    },
    {
       'id':4,
       'title': 'Senior Python Developer',
       'location':'Hybrid',
       
    },
]

@app.route('/')
def index():
    return render_template('home.html', jobs = JOBS, company_name = 'Leone Jobs')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)