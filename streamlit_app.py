import streamlit;

streamlit.title('My Moms New Healthy Diner');

streamlit.header('Breakfast favorites');
streamlit.text ('🥣Omega 3 & Blueberry Oatmeal');
streamlit.text('🥗Kale, Spinach & Rocket Smoothie');
streamlit.text ('🐔Hard-Boiled Free-Range Egg');
streamlit.text ('🥑🍞Avocado toast');

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇');

import pandas;
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
my_fruit_list = my_fruit_list.set_index('Fruit');

fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries']);
fruits_to_show = my_fruit_list.loc[fruit_selected];
streamlit.dataframe(fruits_to_show);

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon");
streamlit.text(fruityvice_response);

streamlit.header("Fruityvice Fruit Advice!");

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"  + fruit_choice);

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json());
streamlit.dataframe(fruityvice_normalized);

import snowflake.connector



