import requests

# Define the API endpoint
url = "https://bd5ua6mqac.execute-api.ap-southeast-2.amazonaws.com/prod/v1/facebook-page-details?channel_id="

# Define the headers, including the x-api-key
headers = {
    "x-api-key": "8jkX3YWMC85bULT36R6B76UeWg1hZIcooVjWK8vb"
}

channel_ids = [3900585713]

for i in channel_ids:

    url1 = url + str(i)

    # Send GET request
    response = requests.get(url1, headers=headers)

    # Check the response status code and print the response
    if response.status_code == 200:
        print("Data fetched successfully!")
        print(response.json())  # Assuming the response is JSON
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        print("Response:", response.text)
