import requests
from bs4 import BeautifulSoup
import csv # To store the data in a CSV file

# URL of Swiggy's restaurant page
url = 'https://www.swiggy.com/city/bangalore/best-restaurants'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

try:
  response = requests.get(url, headers=headers)

  # Send an HTTP GET request

  print(f"Status Code: {response.status_code}")

  # open or create a csv file
  csv_file = open('csv/Bangalore.csv', 'w')
  writer = csv.writer(csv_file)
  writer.writerow(['Restaurant Name', 'Rating', 'Cuisine', 'Location'])

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
        print(f'Cuisine: {data[0].text.strip()}')
        print(f'Location: {data[1].text.strip()}')
        
        # write the data to csv file
        writer.writerow([restaurant_name, rating, data[0].text.strip(), data[1].text.strip()])
        
       
   
  else:
    print('Failed to retrieve the webpage.')

except requests.exceptions.HTTPError as err:
        print(f"HTTP Error Occured: {err}")
        print(err)
