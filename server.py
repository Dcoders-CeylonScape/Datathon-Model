from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock model function
def mock_model(activities, bucket_list):
    places = [
        "Beach Resort",
        "Mountain Cabin",
        "City Cafe",
        "Art Museum",
        "Historic Landmark"
    ]
    
    result_places = [place for place in places if any(activity.lower() in place.lower() for activity in activities)]
    if not result_places:
        result_places = places[:5]  # Return all places if no match found
    
    return result_places

@app.route('/get_places', methods=['POST'])
def get_places():
    data = request.json
    activities = data.get('activities', [])
    bucket_list = data.get('bucket_list', [])
    
    # Call the mock model function
    places = mock_model(activities, bucket_list)
    
    return jsonify(places)

if __name__ == '__main__':
    # Modify this line to bind to '0.0.0.0' so Flask is accessible from outside the container
    app.run(debug=True, host='0.0.0.0')