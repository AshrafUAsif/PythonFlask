from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'location' : 'Dhaka',
        'salary' : 'Taka 30,000'
    },
    {
        'id' : 2,
        'title' : 'Front-End Developer',
        'location' : 'Remote',
    },
    {
        'id' : 1,
        'title' : 'Back-End Developer',
        'location' : 'Chittagong',
        'salary' : 'Taka 50,000'
    },
    
]
#This is it

@app.route('/')
def index():
    return render_template('home.html', jobs = JOBS)


@app.route('/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)