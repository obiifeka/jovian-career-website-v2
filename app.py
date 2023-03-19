from flask import Flask,redirect,url_for,render_template,request,jsonify

app=Flask(__name__)

jobs = [
    {"id": 1, "title": "Software Engineer", "location": "San Francisco, CA", "salary": "$120,000 - $150,000 per year"},
    {"id": 2, "title": "Data Analyst", "location": "New York, NY", "salary": "$80,000 - $100,000 per year"},
    {"id": 3, "title": "Marketing Manager", "location": "Chicago, IL", "salary": "$90,000 - $110,000 per year"},
    {"id": 4, "title": "Product Designer", "location": "Seattle, WA", "salary": "$100,000 - $130,000 per year"},
    {"id": 5, "title": "Sales Executive", "location": "Los Angeles, CA", "salary": "$70,000 - $90,000 per year"},
     {"id": 6, "title": "Tecncal Support Assistant", "location": "Remote", "salary": ""}
]


@app.route('/')
def home():
        return render_template('index.html',jobs=jobs)
    

@app.route('/index')
def index():  
        return render_template('index.html',jobs=jobs)

@app.route('/jobs')
def list_jobs(): 
        return jsonify(jobs)
   
   
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)