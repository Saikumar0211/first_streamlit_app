
import streamlit
streamlit.title('My Parents New Healthy diner')
streamlit.header('Breakfast favorites')
streamlit.text('omega 3 & Blueberry')
streamlit.text('kale & Spinach')
streamlit.text('half boiled egg')

streamlit.header('bilid you own fruit smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)


