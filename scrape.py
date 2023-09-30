import requests
from bs4 import BeautifulSoup

# URL of Swiggy's restaurant page
url = 'https://www.swiggy.com/city/pune/best-restaurants'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

response = requests.get(url, headers=headers)

# Send an HTTP GET request

print(f"Status Code: {response.status_code}")



# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')


    restaurant_element = soup.find('div', class_='styled__StyledRestaurantGridCard-sc-fcg6mi-0 lgOeYp')

    # print(restaurant_element)
    
    if restaurant_element:
       
      for restaurant in restaurant_element:
        # Extract information from each <a> element and its child <div> elements
        restaurant_name = restaurant.find('div', class_='margin-left:12px').text.strip()
        print(f'Restaurant Name: {restaurant_name}')
       
   
else:
    print('Failed to retrieve the webpage.')

