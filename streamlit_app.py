import streamlit
import pandas
import snowflake.connector
from urllib.error import URLError

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

try:   
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("please select fruit to get information")
    else:
        fruitvise_response = requests.get("https://www.fruityvice.com/api/fruit/"+fruit_choice_name)
        fruitvise_normalized = pandas.json_normalize(fruitvise_response.json())
        streamlit.dataframe(fruitvise_normalized)
except URLError as e:
    streamlit.error()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.text("The Fruit load list contains:")
streamlit.text(my_data_row)


add_fruit = streamlit.text_input('What fruit would you like to add')
streamlit.write('Thanks for adding',add_fruit)
