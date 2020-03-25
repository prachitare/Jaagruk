from flask import Flask, render_template, url_for
from scraper import get_count
from dashboard import make_graph
from apscheduler.schedulers.blocking import BlockingScheduler

app = Flask(__name__)

sched = BlockingScheduler()
@sched.scheduled_job('interval', hours = 24)
def timed_job():
    make_graph()

getcount = get_count()
count = getcount[0]
timestamp = getcount[1]


@app.route('/')
def index():
	return render_template('index.html', timestamp = timestamp, count = count)

@app.route('/generic')
def generic():
	return render_template('generic.html')

if __name__ == '__main__':
    app.run(debug = True)
