from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/recommendation-system', methods=['POST']) #GET requests will be blocked
def recommendation_system():
	for key in request.form:
		print(key, ":", request.form[key])
	return jsonify(request.form)
	
app.run(debug=False, port=5000)