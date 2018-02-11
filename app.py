from flask import Flask, render_template
from mixpanel import Mixpanel

class LoggingConsumer(object):
    def __init__(self):
        self.mp_log = open("MIXPANEL_LOG.txt", "w+")

    def send(self, endpoint, json_message):
        self.mp_log.write("{0}::{1}\n".format(endpoint, message))

logging_mp = Mixpanel('f702a5c5aed0b809faec1d3ec4d03d35', LoggingConsumer())

mp = Mixpanel('f702a5c5aed0b809faec1d3ec4d03d35')


mp.track('gyunseul9', 'Sent Message')
mp.track('gyunseul9', 'Plan Upgraded', {
    'Old Plan': 'Business',
    'New Plan': 'Premium'
})

app = Flask(__name__)

@app.route('/')

def main():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
