# -*- coding: utf-8 -*-
"""Final Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17TaQvqRRwusx8j9VDipopc-1zp5XTgF8

# Final Project
### Max Fleming and Kunal Renjen
Fantasy Football Data from 2017-2022
Questions to answer:
* Who are the Rushing, Passing and Recieving Yards Leader statistic by Year?
* Using data from 2017-2021, are there specific metrics to predict what players to use in the next year (2022)?

Importing necessary python libraries and mounting google drive
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from scipy.stats import pearsonr
from google.colab import drive
drive.mount('/content/drive')

"""Reading the dataset in and printing the first five rows of data"""

fantasy_data = pd.read_csv('/content/drive/MyDrive/Intro Data Science Fall 2024/Final Project/fantasy_merged_7_17.csv')
fantasy_data.head()

"""Examining the titles of all the columns in the dataset for further reference"""

fantasy_data.info()

"""Renaming the Yds column to PassingYds. This will help with analysis later when seperating data for Quarterbacks, Running Backs and Wide Recievers"""

fantasy_data.rename(columns={'Yds': 'PassingYds'}, inplace=True)

fantasy_data['PassingYds/Int'] = fantasy_data['PassingYds'] / fantasy_data['Int']
fantasy_data['RushYds/Fmb'] = fantasy_data['RushYds'] / fantasy_data['Fmb']
fantasy_data['CompPct'] = fantasy_data['Cmp'] / fantasy_data['Att']
fantasy_data['RushYds/TD'] = fantasy_data['RushYds'] / fantasy_data['RushTD']
fantasy_data['RecYds/TD'] = fantasy_data['RecYds'] / fantasy_data['RecTD']
fantasy_data.head()

"""Creation of new dataframes that only contain Running Backs, Quarterbacks and Wide Recievers with data from 2017-2022."""

rb_data = fantasy_data[fantasy_data['FantPos'] == 'RB']
qb_data = fantasy_data[fantasy_data['FantPos'] == 'QB']
wr_data = fantasy_data[fantasy_data['FantPos'] == 'WR']

"""Distribution of Running Backs by Rushing Yards"""

# Create the histogram
fig = go.Figure(data=[go.Histogram(x=rb_data['RushYds'], nbinsx=50, marker_color='red')])

# Update the layout
fig.update_layout(
    title='Distribution of Rushing Yards',
    xaxis_title='Rushing Yards',
    yaxis_title='Count'
)

# Show the plot
fig.show()

"""Distribution of Wide Recievers by Receiving Yards"""

# Create the histogram
fig = go.Figure(data=[go.Histogram(x=wr_data['RecYds'], nbinsx=50, marker_color='green')])

# Update the layout
fig.update_layout(
    title='Distribution of Receiving Yards',
    xaxis_title='Receiving Yards',
    yaxis_title='Count'
)

# Show the plot
fig.show()

"""Distribution of Quarterbacks by Passing Yards"""

# Create the histogram
fig = go.Figure(data=[go.Histogram(x=qb_data['PassingYds'], nbinsx=50, marker_color='blue')])

# Update the layout
fig.update_layout(
    title='Distribution of Passing Yards',
    xaxis_title='Passing Yards',
    yaxis_title='Count'
)

# Show the plot
fig.show()

"""Creating datasets by year for Wide Reciever data"""

wr_2017 = wr_data[wr_data['Year'] == 2017]
wr_2018 = wr_data[wr_data['Year'] == 2018]
wr_2019 = wr_data[wr_data['Year'] == 2019]
wr_2020 = wr_data[wr_data['Year'] == 2020]
wr_2021 = wr_data[wr_data['Year'] == 2021]
wr_2022 = wr_data[wr_data['Year'] == 2022]
allWrData = pd.concat([wr_2017, wr_2018, wr_2019, wr_2020, wr_2021, wr_2022])

"""Graphing the top 5 Wide Recievers by Yards in 2022"""

top5wr_2022 = wr_2022.sort_values(by='RecYds', ascending=False)[:5][['Player', 'RecYds']]


fig = go.Figure(data=[
    go.Bar(name='Recieving Yards', x=top5wr_2022['Player'], y=top5wr_2022['RecYds'], marker_color='green')
])


fig.update_layout(
    title='Top 5 Players by Recieving Yards in 2022',
    xaxis_title='Player',
    yaxis_title='Recieving Yards',
    xaxis_tickangle=0
)

fig.show()

"""Graphing the top Wide Reciever by year in terms of recieving yards"""

topwr_2017 = wr_2017.sort_values(by='RecYds', ascending=False)[:1][['Player', 'RecYds', 'Year']]
topwr_2018 = wr_2018.sort_values(by='RecYds', ascending=False)[:1][['Player', 'RecYds', 'Year']]
topwr_2019 = wr_2019.sort_values(by='RecYds', ascending=False)[:1][['Player', 'RecYds', 'Year']]
topwr_2020 = wr_2020.sort_values(by='RecYds', ascending=False)[:1][['Player', 'RecYds', 'Year']]
topwr_2021 = wr_2021.sort_values(by='RecYds', ascending=False)[:1][['Player', 'RecYds', 'Year']]
topwr_2022 = wr_2022.sort_values(by='RecYds', ascending=False)[:1][['Player', 'RecYds', 'Year']]
topwr_data = pd.concat([topwr_2017, topwr_2018, topwr_2019, topwr_2020, topwr_2021, topwr_2022])

fig = go.Figure(data=[
    go.Bar(
        name='Receiving Yards',
        x=topwr_data['Year'],
        y=topwr_data['RecYds'],
        text=[f"{player}: {recyds} yards" for player, recyds in zip(topwr_data['Player'], topwr_data['RecYds'])],
        hoverinfo='text',
        marker_color='green'
    )
])

fig.update_layout(
    title='Top Receiving Player by Year',
    xaxis_title='Year',
    yaxis_title='Receiving Yards',
    xaxis_tickangle=0
)

fig.update_traces(textposition='none')

fig.show()

"""Creating datasets by year for Running Back data"""

rb_2017 = rb_data[rb_data['Year'] == 2017]
rb_2018 = rb_data[rb_data['Year'] == 2018]
rb_2019 = rb_data[rb_data['Year'] == 2019]
rb_2020 = rb_data[rb_data['Year'] == 2020]
rb_2021 = rb_data[rb_data['Year'] == 2021]
rb_2022 = rb_data[rb_data['Year'] == 2022]

"""Graphing the top Running Back
 by year in terms of rushing yards
"""

toprb_2017 = rb_2017.sort_values(by='RushYds', ascending=False)[:1][['Player', 'RushYds', 'Year']]
toprb_2018 = rb_2018.sort_values(by='RushYds', ascending=False)[:1][['Player', 'RushYds', 'Year']]
toprb_2019 = rb_2019.sort_values(by='RushYds', ascending=False)[:1][['Player', 'RushYds', 'Year']]
toprb_2020 = rb_2020.sort_values(by='RushYds', ascending=False)[:1][['Player', 'RushYds', 'Year']]
toprb_2021 = rb_2021.sort_values(by='RushYds', ascending=False)[:1][['Player', 'RushYds', 'Year']]
toprb_2022 = rb_2022.sort_values(by='RushYds', ascending=False)[:1][['Player', 'RushYds', 'Year']]
toprb_data = pd.concat([toprb_2017, toprb_2018, toprb_2019, toprb_2020, toprb_2021, toprb_2022])


fig = go.Figure(data=[
    go.Bar(
        name='Rushing Yards',
        x=toprb_data['Year'],
        y=toprb_data['RushYds'],
        text=[f"{player}: {rushyds} yards" for player, rushyds in zip(toprb_data['Player'], toprb_data['RushYds'])],
        hoverinfo='text',
        marker_color='red'
    )
])


fig.update_layout(
    title='Top Rushing Player by Year',
    xaxis_title='Year',
    yaxis_title='Rushing Yards',
    xaxis_tickangle=0
)


fig.update_traces(textposition='none')

fig.show()

"""Creating datasets by year for Quarterback data and graphing the top Quarterback by passing yards for each year"""

qb_2017 = qb_data[qb_data['Year'] == 2017]
qb_2018 = qb_data[qb_data['Year'] == 2018]
qb_2019 = qb_data[qb_data['Year'] == 2019]
qb_2020 = qb_data[qb_data['Year'] == 2020]
qb_2021 = qb_data[qb_data['Year'] == 2021]
qb_2022 = qb_data[qb_data['Year'] == 2022]
allQbData = pd.concat([qb_2017, qb_2018, qb_2019, qb_2020, qb_2021, qb_2022])
qb_2017.head()

topqb_2017 = qb_2017.sort_values(by='PassingYds', ascending=False)[:1][['Player', 'PassingYds', 'Year']]
topqb_2018 = qb_2018.sort_values(by='PassingYds', ascending=False)[:1][['Player', 'PassingYds', 'Year']]
topqb_2019 = qb_2019.sort_values(by='PassingYds', ascending=False)[:1][['Player', 'PassingYds', 'Year']]
topqb_2020 = qb_2020.sort_values(by='PassingYds', ascending=False)[:1][['Player', 'PassingYds', 'Year']]
topqb_2021 = qb_2021.sort_values(by='PassingYds', ascending=False)[:1][['Player', 'PassingYds', 'Year']]
topqb_2022 = qb_2022.sort_values(by='PassingYds', ascending=False)[:1][['Player', 'PassingYds', 'Year']]
topqb_data = pd.concat([topqb_2017, topqb_2018, topqb_2019, topqb_2020, topqb_2021, topqb_2022])
topqb_data

fig = go.Figure(data=[
    go.Bar(
        name='Passing Yards',
        x=topqb_data['Year'],
        y=topqb_data['PassingYds'],
        text=[f"{player}: {passyds} yards" for player, passyds in zip(topqb_data['Player'], topqb_data['PassingYds'])],
        hoverinfo='text',
        marker_color='blue'
    )
])

fig.update_layout(
    title='Top Passing Player by Year',
    xaxis_title='Year',
    yaxis_title='Passing Yards',
    xaxis_tickangle=0
)


fig.update_traces(textposition='none')

fig.show()

"""To answer our second question regarding specific metrics to predict PPR we decided to only look at Quarterbacks, Recievers and Running backs with a 50% quartile level and over for the years 2017-2021. We begin by creating  datasets for Running Backs, Quarterbacks and Wide Recievers that exclude the year 2022 as well as only including data entries that meet our criteria above.

"""

wrData2017_2021 = pd.concat([wr_2017, wr_2018, wr_2019, wr_2020, wr_2021])
wrData2017_2021['RecYds'].describe()

"""As seen above the 50% quartile level for RecYds is 248, so we will modify the dataset above to only include Wide Recievers with at least 248 yards and over."""

filtered_wrData2017_2021 = wrData2017_2021[wrData2017_2021['RecYds'] > 248]

"""Given this dataset we will use statistical code to compute the relationship between the wide reciever specific metric of Yards per Reception with PPR."""

correlation, _ = pearsonr(filtered_wrData2017_2021['YR'], filtered_wrData2017_2021['PPR'] )

print(f"The correlation between Yards per Reception and PPR points is: {correlation:.2f}")

"""Scatter Plot displaying Yards per Reception against Fantasy Points"""

fig = go.Figure(data=go.Scatter(
    x=filtered_wrData2017_2021['YR'],  # X-axis data
    y=filtered_wrData2017_2021['PPR'],  # Y-axis data
    mode='markers',
    text=[f"{player}: {recyds} yards" for player, recyds in zip(filtered_wrData2017_2021['Player'], filtered_wrData2017_2021['YR'])],
    marker=dict(color='green', size=10)  # Customize markers
))

fig.update_layout(
    title='Scatter Plot of Yards per Reception vs Fantasy Points',
    xaxis_title='Yards per Reception',
    yaxis_title='Fantasy Points'
)

fig.show()

"""We will now use statistical code to compute the relationship between the wide reciever specific metric of Receiving Yards per Touchdown with PPR. To do this we must drop Nan values from the Receiving Yards per Touchdown column, so in effect we must drop wide receivers with 0 touchdowns."""

cleaned_wrData2017_2021 = filtered_wrData2017_2021[filtered_wrData2017_2021['RecTD'] > 0]
cleaned_wrData2017_2021 = cleaned_wrData2017_2021.dropna(subset=['RecYds/TD'])

"""We will use statistical code to compute the relationship between the wide reciever specific metric of Receiving Yards per Touchdown with PPR."""

correlation, _ = pearsonr(cleaned_wrData2017_2021['RecYds/TD'], cleaned_wrData2017_2021['PPR'] )

print(f"The correlation between Receiving Yards per Touchdown and PPR points is: {correlation:.2f}")

"""Scatter Plot displaying Receiving Yards per Touchdown against Fantasy Points"""

fig = go.Figure(data=go.Scatter(
    x=cleaned_wrData2017_2021['RecYds/TD'],  # X-axis data
    y=cleaned_wrData2017_2021['PPR'],  # Y-axis data
    mode='markers',   # Marker mode for scatter plot
    text=[f"{player}: {recyds} yards" for player, recyds in zip(cleaned_wrData2017_2021['Player'], cleaned_wrData2017_2021['RecYds/TD'])],
    marker=dict(color='green', size=10)  # Customize markers
))

fig.update_layout(
    title='Scatter Plot of Receiving Yards per Touchdown vs Fantasy Points',
    xaxis_title='Recieving Yards per Touchdown',
    yaxis_title='Fantasy Points'
)

fig.show()

"""Analysis of Running Back data from 2017-2021, looking at the specifc metric of yards per attempt."""

rbData2017_2021 = pd.concat([rb_2017, rb_2018, rb_2019, rb_2020, rb_2021])
rbData2017_2021['RushYds'].describe()

filtered_rbData2017_2021 = rbData2017_2021[rbData2017_2021['RushYds'] > 157]

"""We will use statistical code to compute the relationship between the running back specific metric of Rushing yards per attempt with PPR."""

correlation, _ = pearsonr(filtered_rbData2017_2021['YA'], filtered_rbData2017_2021['PPR'] )

print(f"The correlation between Yards per Rush Attempt and PPR points is: {correlation:.2f}")

"""Scatter Plot displaying Rushing Yards per attempt against Fantasy Points"""

# Create the scatter plot
fig = go.Figure(data=go.Scatter(
    x=filtered_rbData2017_2021['YA'],  # X-axis data
    y=filtered_rbData2017_2021['PPR'],  # Y-axis data
    mode='markers',   # Marker mode for scatter plot
    text=[f"{player}: {recyds} yards" for player, recyds in zip(filtered_rbData2017_2021['Player'], filtered_rbData2017_2021['YA'])],
    marker=dict(color='red', size=10)  # Customize markers
))

# Update layout
fig.update_layout(
    title='Scatter Plot of Yards per Rush Attempt vs Fantasy Points',
    xaxis_title='Yards per Rush Attempt',
    yaxis_title='Fantasy Points'
)

# Show the plot
fig.show()

"""Analysis of Running Back data from 2017-2021, looking at the specifc metric of Rushing Yards per Touchdown."""

cleaned_rbData2017_2021 = filtered_rbData2017_2021[filtered_rbData2017_2021['RushTD'] > 0]
cleaned_rbData2017_2021 = cleaned_rbData2017_2021.dropna(subset=['RushYds/TD'])

"""We will use statistical code to compute the relationship between the running back specific metric of Rushing yards per touchdown with PPR."""

correlation, _ = pearsonr(cleaned_rbData2017_2021['RushYds/TD'], cleaned_rbData2017_2021['PPR'] )

print(f"The correlation between Rushing Yards per Touchdown and PPR points is: {correlation:.2f}")

"""Scatter Plot displaying Rushing Yards per touchdown against Fantasy Points"""

# Create the scatter plot
fig = go.Figure(data=go.Scatter(
    x=cleaned_rbData2017_2021['RushYds/TD'],  # X-axis data
    y=filtered_rbData2017_2021['PPR'],  # Y-axis data
    mode='markers',   # Marker mode for scatter plot
    text=[f"{player}: {recyds} yards" for player, recyds in zip(cleaned_rbData2017_2021['Player'], cleaned_rbData2017_2021['RushYds/TD'])],
    marker=dict(color='red', size=10)  # Customize markers
))

# Update layout
fig.update_layout(
    title='Scatter Plot of Rushing Yards per Touchdown vs Fantasy Points',
    xaxis_title='Rushing Yards per Touchdown',
    yaxis_title='Fantasy Points'
)

# Show the plot
fig.show()

"""Analysis of Quarterback data from 2017-2021, looking at the specifc metric of completion percentage."""

qbData2017_2021 = pd.concat([qb_2017, qb_2018, qb_2019, qb_2020, qb_2021])
qbData2017_2021[['CompPct', 'Att']].describe()
filtered_qbData2017_2021 = qbData2017_2021[(qbData2017_2021['Att'] > 156) & (qbData2017_2021['CompPct'] > .63)]

"""We will use statistical code to compute the relationship between the quarterback specific metric of completion percentage with PPR."""

correlation, _ = pearsonr(filtered_qbData2017_2021['CompPct'], filtered_qbData2017_2021['PPR'] )

print(f"The correlation between Completion Percentage and PPR points is: {correlation:.2f}")

"""Scatter Plot displaying Completion Percentage against Fantasy Points"""

# Create the scatter plot
fig = go.Figure(data=go.Scatter(
    x=filtered_qbData2017_2021['CompPct'],  # X-axis data
    y=filtered_qbData2017_2021['PPR'],  # Y-axis data
    mode='markers',   # Marker mode for scatter plot
    text=[f"{player}: {recyds} Percent" for player, recyds in zip(filtered_qbData2017_2021['Player'], filtered_qbData2017_2021['CompPct'])],
    marker=dict(color='blue', size=10)  # Customize markers
))

# Update layout
fig.update_layout(
    title='Scatter Plot of Completion Percentage vs Fantasy Points',
    xaxis_title='Completion Percentage',
    yaxis_title='Fantasy Points'
)

# Show the plot
fig.show()