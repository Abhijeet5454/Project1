from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route to handle the form page
@app.route('/', methods=['GET','POST'])
def index():
    # if request.method == 'POST':
    #      return redirect(url_for('index'))
    return render_template('newTechEntry.html')

# @app.route('/newTechEntry')
# def index():
#     return render_template('newTechEntry.html')

# # Route to handle the data submission
# @app.route('/verifyDuplicate', methods=['POST'])
# def submit_data():
#     # Get data from the form
#     newTechName = request.get_json()

#     # response = verify_duplicate(newTechName)
#     response = newTechName + "is entered"
#     # Return result to the HTML page
#     return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
    