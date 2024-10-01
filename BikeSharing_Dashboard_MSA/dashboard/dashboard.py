from streamlit.web.cli import activate
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

all_df = pd.read_csv('all_data.csv')
st.write(
    """
    # Bike Sharing Dashboard
    """
)
image_url = "https://bcassetcdn.com/public/blog/wp-content/uploads/2019/06/18095552/bike-share.png"
with st.sidebar:
    st.image(image_url)
    st.write("by Muhamad Sahidul Akhfa")


tab1, tab2 = st.tabs(["Sharing by Times", "Sharing by Situations"])
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        penyewa_registered = all_df['registered'].sum()
        penyewa_registered_formatted = f"{penyewa_registered:,.0f}"
        st.metric(label="Registered Sharing", value=penyewa_registered_formatted)

    with col2:
        penyewa_casual = all_df['casual'].sum()
        penyewa_casual_formatted = f"{penyewa_casual:,.0f}"
        st.metric(label="Casual Sharing", value=penyewa_casual_formatted)


    with st.container():
        st.header("Sharing by Hour")
        plt.figure(figsize=(12, 6))

        sns.lineplot(x='hr', y='casual', data=all_df, estimator=sum, label='Casual', errorbar=None, color='blue',
                     marker='o')

        sns.lineplot(x='hr', y='registered', data=all_df, estimator=sum, label='Registered', errorbar=None, color='green',
                     marker='o')

        plt.xlabel('Hour')
        plt.ylabel('Total Sharing')

        plt.xticks(ticks=range(24),
                   labels=['12am', '1am', '2am', '3am', '4am', '5am', '6am', '7am', '8am', '9am', '10am', '11am',
                           '12pm', '1pm', '2pm', '3pm', '4pm', '5pm', '6pm', '7pm', '8pm', '9pm', '10pm', '11pm'],
                   rotation=45)

        plt.legend(title='Sharing Type')

        st.pyplot(plt)

    with st.container():
        st.header("Sharing by Day")
        plt.figure(figsize=(12, 6))

        sns.lineplot(y='casual', x='weekday', data=all_df, estimator=sum, label='Casual', errorbar=None, color='blue',
                     marker='o')

        sns.lineplot(y='registered', x='weekday', data=all_df, estimator=sum, label='Registered', errorbar=None,
                     color='green', marker='o')

        plt.xlabel('Day')
        plt.ylabel('Total Sharing')

        plt.legend(title='Sharing Type')

        st.pyplot(plt)

    with st.container():
        st.header("Sharing by Month")
        plt.figure(figsize=(12, 6))

        sns.lineplot(x='mnth', y='casual', data=all_df, estimator=sum, label='Casual', errorbar=None, color='blue',
                     marker='o')

        sns.lineplot(x='mnth', y='registered', data=all_df, estimator=sum, label='Registered', errorbar=None,
                     color='green', marker='o')

        plt.xlabel('Month')
        plt.ylabel('Total Sharing')

        plt.legend(title='Sharing Type')

        st.pyplot(plt)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        penyewa_registered = all_df['registered'].sum()
        penyewa_registered_formatted = f"{penyewa_registered:,.0f}"
        st.metric(label="Registered Sharing", value=penyewa_registered_formatted)

    with col2:
        penyewa_casual = all_df['casual'].sum()
        penyewa_casual_formatted = f"{penyewa_casual:,.0f}"
        st.metric(label="Casual Sharing", value=penyewa_casual_formatted)

    with st.container():
        st.header("Sharing by Season")
        season_order = all_df.groupby('season')['cnt'].sum().sort_values(ascending=False).index

        plt.figure(figsize=(10, 6))

        ax = sns.barplot(x='season', y='cnt', data=all_df, estimator=sum, errorbar=None, order=season_order)

        for p in ax.patches:
            ax.annotate(f'{int(p.get_height()):,}', (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='baseline', fontsize=11, color='black', xytext=(0, 5),
                        textcoords='offset points')

        plt.xlabel('Season', fontsize=12)
        plt.ylabel('Total Sharing', fontsize=12)

        st.pyplot(plt)

    with st.container():
        st.header("Sharing by Weather")
        weather_order = all_df.groupby('weathersit')['cnt'].sum().sort_values(ascending=False).index

        plt.figure(figsize=(10, 6))

        ax = sns.barplot(x='weathersit', y='cnt', data=all_df, estimator=sum, errorbar=None, order=weather_order,
                         color='blue')

        for p in ax.patches:
            ax.annotate(f'{int(p.get_height()):,}', (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='baseline', fontsize=11, color='black', xytext=(0, 5),
                        textcoords='offset points')

        barplot = sns.barplot(x='weathersit', y='cnt', data=all_df, estimator=sum, errorbar=None, order=weather_order)

        plt.xlabel('Weather', fontsize=12)
        plt.ylabel('Total Sharing', fontsize=12)

        st.pyplot(plt)

    with st.container():
        st.header("Sharing by Temperature")
        plt.figure(figsize=(12, 6))

        sns.lineplot(x='temp', y='casual', data=all_df, estimator=sum, label='Casual', errorbar=None, color='blue',
                     marker='o')

        sns.lineplot(x='temp', y='registered', data=all_df, estimator=sum, label='Registered', errorbar=None,
                     color='green', marker='o')

        plt.xlabel('Month')
        plt.ylabel('Total Sharing')

        plt.legend(title='Sharing Type')

        st.pyplot(plt)
