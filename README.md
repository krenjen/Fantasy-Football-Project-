# Fantasy Football Project: Analyzing Fantasy Football Data from 2017-2022
##### By Max Fleming and Kunal Renjen
### Link Below to Google CoLab worksheet  
[Colab Code](final_project.py)
### Data Source
[Link to Kaggle Data](https://www.kaggle.com/datasets/gbolduc/fantasy-football-data-2017-2023) 
### Final Project Analysis Process 
Import necessary python libraries and gooogle drive. <br>
Read the data set into colab. <br>
Exame the titles of all the columns in the dataset for further reference. <br>
Rename columns and create new columns used for later analysis. <br>
Create data frames that only contain Running Backs, Quarterbacks and Receivers. <br>
Plot distributions of Running Back, Quarterback and Receivers data by total yards. <br>
Create subdata sets by year for Wide Receiver data and graph wide receiver data. <br>
Repeat this process for Running Backs and Quarterbacks. <br>
Use data from 2017-2021 for Wide Receivers, only utilizing total yards data in the 50% quartile and above. <br>
Calculate correlation of metrics used and plot using scatter plots. <br>
Repeat process for Running Backs and Quarterbacks.

### Distribution Plots
{% include_relative  Distribution_of_Receiving_Yards.html %}

{% include_relative  Distribution_of_Rushing_Yards.html %}

{% include_relative  Distribution_of_Passing_Yards.html %}

### Top Positional Players
{% include_relative  Top5wr2022.html %}

{% include_relative  Top_receiving_players.html %}

{% include_relative  Top_rushing_players.html %}

{% include_relative  Top_passing_players.html %}
### Scatter Plots
{% include_relative  Scatter_YR_PPR.html %} <br>
{% include_relative  Scatter_YardsperTouchdown_PPR.html %} <br>
{% include_relative  Scatter_YA_PPR.html %} <br>
{% include_relative  Scatter_YardsRushingTouchdown_PPR.html %} <br>
{% include_relative  Scatter_CompPCT_PPR.html %} 


