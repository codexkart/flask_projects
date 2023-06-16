from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [
      {
        'id':1,
        'title':'Data Analyst',
        'location' : 'Bengaluru,India',
        'salary' : 'Rs. 30,00,000'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location' : 'Mumbai,India',
        'salary' : 'Rs. 60,00,000'
    },
    {
        'id':3,
        'title':'Front-End Engineer',
        'location' : 'Remote',
        'salary' : 'Rs. 12,00,000'
    },
    {
        'id':4,
        'title':'Back-End Engineer',
        'location' : 'Remote',
        'salary' : 'Rs. 15,00,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('index.html',jobs = JOBS,company_name = 'CareerEasy')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True,port=5000)