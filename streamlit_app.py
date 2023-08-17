import streamlit
import pandas
import requests

streamlit.title("Test App")

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.text('🥣🥗🐔🥑🍞')

#load dataset
streamlit.header('Fruits Database')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#add list to allow users to pick fruits
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display data
streamlit.dataframe(fruits_to_show)

#add fruityvice api test
streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

# normalize json response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output data in table format
streamlit.dataframe(fruityvice_normalized)
