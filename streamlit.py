# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 11:18:12 2022

@author: ANH
"""
#!pip install streamlit 
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
from sklearn import datasets
from PIL import Image
import seaborn as sns


value = st.slider('val')
st.write(value, 'squared is', value * value)
st.sidebar.header('📖Content beer review')

st.sidebar.subheader('🍻 Overview')


st.sidebar.write('🌿 Review base on review time, apperrance, aroma, taste')
st.sidebar.write('🌿 Beerstyle, ABV_Alcohol By Volume')

st.sidebar.subheader('🍻 Table of the top 10 beer_name based on review_Times')

st.sidebar.write('🌿Comparations and Charts')

st.sidebar.write('🌿Popular Words')

st.sidebar.write('Sources')

st.title("BEER REVIEWS! THE TOP 10 :beer::beer:")

if st.button("Subscrible"):
    st.write("Like this video too")


st.header("Do you like beers?:heart::heart::heart:")

checkbox_one = st.checkbox("Yes")
checkbox_two = st.checkbox("No")
if checkbox_one: value = "Yes"
elif checkbox_two: value = "No"
else: value = "No value selected"
st.write(f"You selected: {value}")

st.subheader('📝 Overview')
st.write('I obtained a database of millions of short beer reviews, which I have generated graphs and word clouds from and performed a small amount of analysis. I made use of matplotlib along with the python wordcloud library, to generate graphs and word clouds respectively.')

st.video('https://www.youtube.com/watch?v=f_SZjiEMH6g')

st.write('With the global beer market valued at over $623 billion dollars worldwide,it’s no wonder that beer is something of a universal language, unifying drinkers across oceans. With such international interest, it’s not surprising, then, that news outlets rush annually to aggregate the most popular brews from all corners of the globe.The overall Top 10 active beers as determined by our worldwide community of beer raters:medal:')

a = [1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape((2,4))
dic = {
      "name":["beer1", "beer2"],
      "review":["aroma", "appearance"],
      "overal":["love","hate"]
      }
st.image('https://beermaverick.com/wp-content/uploads/2021/04/beer-price.png')
st.subheader(":medal:Rating base on review time") 
st.write('The following table display the number of beers for the top 10 beer review')
beer = pd.read_csv(r'C:\Users\James\Desktop\stream\df1.csv')
st.table(beer)
st.write('👉The most reviewing beer is Belgo Sutra, the second place belong to Crank Yanker IPA')

st.subheader(":medal:rating base on review_appearance")
st.write('The following table display the number of beers for the top 10 beer_appearance')
beer1 = pd.read_csv(r'C:\Users\James\Desktop\stream\df2.csv')
st.table(beer1)
st.write('👉The best appearance beer is Tall Tale Pale Ale, the second place belong to Portsmouth Crazed Cossack Russian Imperial Stoutnk Yanker IPA')

st.subheader(':medal:Rating base on review_aroma')
st.write('The following table display the number of beers for the top 10 beer review base on Aroma')
beer2 = pd.read_csv(r'C:\Users\James\Desktop\stream\df3.csv')
st.table(beer2)
st.write('👉The best Aroma reviewing beer is Southampton Belgian Red Ale, the second is Mittenwalder Werdenfelser Weisse')

st.subheader(':medal:Rating base on review_taste')
st.write('The following table display the number of beers for the top 10 beer review base on the Taste')
beer3 = pd.read_csv(r'C:\Users\James\Desktop\stream\df4.csv')
st.table(beer3)
st.write('👉The best taste reviewing is The Ascent, the second place is Oak Aged Old Dipsea Barleywine')

st.subheader('🍀 Beer Styles')
st.write('The following graph depicts the number of beers for the top 20 beer styles.')
st.image('https://www.anfractuosity.com/wp-content/uploads/2018/01/styles-1.png')
st.write('The top style of beer by a far distance is the IPA, followed by the American Pale Ale')

st.subheader('🍀 ABV_Alcohol By Volume')
st.image('https://www.anfractuosity.com/wp-content/uploads/2018/01/beers_abv-1.png')
st.write('👉As you can see the most common ABV of a beer is around 6%')

st.subheader('📒Table of beer reviewing Top Beer_name based on review_Times')
beername=pd.read_csv(r'C:\Users\James\Desktop\stream\beername.csv')
st.table(beername)

st.subheader('🍻review: taste and appearance.scatter_chart')
st.image(Image.open("C:/Users/James/Desktop/stream/review taste and time.png"))
st.write('As you see that the type of beers have many review is not alsway have a good rate in taste')

st.subheader('🍻review: taste and appearance.Line_chart')
beername = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['review_taste','review_appearance'])
st.line_chart(beername)

st.subheader('🍻review: taste,appearance,aroma.Bar_chart')
beername=pd.DataFrame(
    np.random.randn(10, 3),
    columns=['review_aroma','review_appearance','review_taste'])
st.bar_chart(beername)

st.subheader('🍻review: overall,appearance,palate and taste.Area_chart')
beername = pd.DataFrame(
    np.random.randn(20, 4),
    columns=['review_overall','review_appearance','review_palate','review_taste'])
st.area_chart(beername)

st.subheader('🍻review: appearance and taste.Hexbin Chart')
st.image(Image.open("C:/Users/James/Desktop/stream/review.png"))

brewery=pd.read_csv(r'C:\Users\James\Desktop\stream\brewery.csv')

st.subheader('🍻review: Overall')
st.image(Image.open("C:/Users/James/Desktop/stream/review overal.png"))

st.subheader('🍻review: overall,appearance,palate and taste.scatter_chart')
st.image(Image.open("C:/Users/James/Desktop/stream/review appearance and taste.png"))

st.subheader('🍻review: overall,taste, aroma. heart_chart')
st.image(Image.open("C:/Users/James/Desktop/stream/hearchart.png"))

st.subheader('💬Popular Words')
st.write('💦The following image depicts a word cloud of the most popular words.')
st.image('https://www.anfractuosity.com/wp-content/uploads/2018/01/cloud-1.png')

st.subheader('💬Popular Words from very positive ratings')
st.write('💦For this and the next word cloud, I removed words such as “bottle,flavour,flavor,really”, to try to obtain words which describe the beer in terms of flavour and appearance.')
st.image('https://www.anfractuosity.com/wp-content/uploads/2018/07/cloud_good_flavour.png')

st.subheader('💬Popular Words from very negative ratings')
st.write('💦For this and the next word cloud, Popular Words from very negative ratings')
st.image('https://www.anfractuosity.com/wp-content/uploads/2018/01/cloud_bad_flavour.png')



st.write('source:https://beermaverick.com/some-of-the-most-interesting-data-visualizations-on-beer/')
st.write('https://www.anfractuosity.com/projects/beer-review-analysis/')
st.write('https://www.youtube.com/watch?v=f_SZjiEMH6g')

st.subheader('🍻New comments:')
st.text_input("Name")
address = st.text_area("Enter your comments")
st.write(address)








