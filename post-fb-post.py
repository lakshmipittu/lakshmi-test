

list1 = [{
"channel_id_type":"post",
"channel_name":"TODAY Play Facebook Page",
"channel_category":"OTHERS",
"trigger_system":"IBT",
"channel_source":"Facebook IBT Channel",
"channel_id":"3900585713",
"datetime_updated":"",
"channel_language":"th_TH",
"channel_country":"TH",
"channel_url":"http://www.facebook.com/183638208373712?sk=wall",
"to_monitor":"1"
}]


import requests

# Define the API endpoint (replace with your actual URL)
url = "https://bd5ua6mqac.execute-api.ap-southeast-2.amazonaws.com/prod/v1/facebook-page-details"



# Optional: Define headers (if required)
headers = {
    "x-api-key": "8jkX3YWMC85bULT36R6B76UeWg1hZIcooVjWK8vb"
}


for data in list1:

    # Send POST request
    response = requests.post(url, json=data, headers=headers)

    # Check the response status code and print the response
    if response.status_code == 200:  # or 201 for successful creation
        print("Data inserted successfully!")
        print("Response:", response.json())  # Display response content (if any)
    else:
        print(f"Failed to insert data. Status code: {response.status_code}")
        print("Response:", response.text)

