from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route to handle the form page
@app.route('/')
def index():
    return render_template('newTechEntry.html')

# Route to handle the form submission
@app.route('/submit_data', methods=['POST'])
def submit_data():
    # Get data from the form
    data = request.get_json()
    newTechName = data.get('newTech')
    response = { 'newTech' : newTechName, 'message' : 'verified' }

    # Return result to the HTML page
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('newTechEntry.html')

# if __name__ == '__main__':
#     app.run(debug=True)