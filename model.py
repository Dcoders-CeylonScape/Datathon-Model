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
        result_places = places[:5]
    
    return result_places
