import requests

def finestFoodOutlet(city, votes):
    base_url = "https://jsonmock.hackerrank.com/api/food_outlets"
    page_no = 1  # Starting page number
    
    # Initialize variables to store the finest food outlet's details
    finest_outlet = None
    finest_rating = 0
    finest_votes = 0
    
    while True:
        # Construct the API URL with dynamic values for 'city', 'page_no', and 'per_page'
        api_url = f"{base_url}?city={city}&page={page_no}"

        try:
            # Send an HTTP GET request to the API URL
            response = requests.get(api_url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                data = response.json()
                total_pages = data['total_pages']
                per_page = data['per_page']
                total_results = data['total']
                
                # Iterate through the data 'data' array
                for outlet in data['data']:
                    # Extract relevant information
                    outlet_name = outlet['name']
                    rating = outlet['user_rating']['average_rating']
                    outlet_votes = outlet['user_rating']['votes']

                    # Check if the outlet meets the criteria
                    if rating > finest_rating or (rating == finest_rating and outlet_votes > finest_votes):
                        if outlet_votes >= votes:
                            finest_outlet = outlet_name
                            finest_rating = rating
                            finest_votes = outlet_votes
                            
                # Check if there are more pages of data
                if page_no < total_pages:
                    page_no += 1
                else:
                    break
            else:
                print(f"Failed to retrieve data from API. Status code: {response.status_code}")
                break
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break

    if finest_outlet:
        return finest_outlet
    else:
        return "No matching food outlet found"

# Example usage:
city_name = "Omaha"
minimum_votes = 100
result = finestFoodOutlet(city_name, minimum_votes)
print(f"The finest food outlet in {city_name} is: {result}")
