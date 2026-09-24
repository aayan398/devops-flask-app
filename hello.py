from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return"""
	    <p>Welcome! this is another string!</p>
	   <p><a href="/about">About</a></p>
           <p><a href="/contact>Contact</a></p>
	      """

@app.route("/about")
def about():
	return """
	<p>This application runs on the Flask web framework.</p>
	<p><a href="https://flask.palletsprojects.com/">Flask websites</a></p>
	<p><a href="https://www.python.org/">Visit the Python website</a></p>
	<p><a href="/">Home</a></p>
            """

@app.route("/contact")
def contact():
	return """
         <p>Contact: maayan200510@gmail.com</p>
	 <p><a href="/">Home</a></p>
		"""
