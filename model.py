# model.py

def mock_model(activities, bucket_list):
    # This is a simple mock function that generates a list of places based on activities and bucket list
    places = [
        "Beach Resort",
        "Mountain Cabin",
        "City Cafe",
        "Art Museum",
        "Historic Landmark"
    ]
    
    # Mock logic to choose places based on activities and bucket list
    result_places = [place for place in places if any(activity.lower() in place.lower() for activity in activities)]
    if not result_places:
        result_places = places[:5]  # Return all places if no match found
    
    return result_places
