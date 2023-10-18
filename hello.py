from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello():
	return 'hello'

def main():
	app.run(host='127.0.0.1',debug=True,port=5001)

if __name__ == '__main__':
	main()