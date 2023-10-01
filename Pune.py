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
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())

    restaurant_element = soup.find_all('div', class_='styled__StyledRestaurantGridCard-sc-fcg6mi-0 lgOeYp')

    # print(restaurant_element)
    
    if restaurant_element:
       
      for restaurant in restaurant_element:
        # Extract information from each <a> element and its child <div> elements
        restaurant_name = restaurant.find('div', class_='sc-beySbM cwvucc').text.strip()
        rating = restaurant.find('span', class_='sc-beySbM fTVWWG').text.strip()
        data = restaurant.find_all('div', class_='sc-beySbM iTWFZi')
       

        print(f'Restaurant Name: {restaurant_name}')
        print(f'Rating: {rating}')
        
        count = 0
        for i in data:
          if(count == 0):
            print('Cuisine: ', i.text.strip())
          if(count == 1):
            print('Location: ', i.text.strip())
          
          count += 1
        
       
   
else:
    print('Failed to retrieve the webpage.')

