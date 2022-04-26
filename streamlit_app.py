import streamlit
import pandas

streamlit.title("MY Mom\'s New Healthy Diner")


streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')               

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")

fruit_selected = streamlit.multiselect("Pick some Fruits:", list(my_fruit_list.index),["Avocado","Strawberries"])
fruit_to_show = my_fruit_list.loc[fruit_selected]

streamlit.dataframe(fruit_to_show)

# New Section to display API response
streamlit.header('Fruitvise Fruit Advice!')  
import requests
fruitvise_response = requests.get("https://www.fruityvice.com/api/fruit/watermelon")
streamlit.text(fruitvise_response.json())
