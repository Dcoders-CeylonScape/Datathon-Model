from flask import Flask, request, jsonify
from model import mock_model

app = Flask(__name__)

@app.route('/recommendations', methods=['POST'])
def get_places():
    data = request.json
    activities = data.get('activities', [])
    bucket_list = data.get('bucket_list', [])
    
    places = mock_model(activities, bucket_list)
    
    return jsonify(places)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')