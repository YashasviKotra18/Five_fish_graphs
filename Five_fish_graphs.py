import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('Fish.csv')

st.markdown("### Five Streamlit Graphs- Fish Data Analysis")

option = st.radio('Selct a graph you would like to view!',
('Show all graphs','Bar Plot', 'Line','Box Plot','Pie Chart','Scatter Plot','Area Plot', 'Condensed Dataview'))

def BarPlot():
   st.subheader("Bar Plot")
   df.groupby(['Species'])['Length1'].mean()
   fig, ax = plt.subplots()
   species = df['Species'].unique()
   mean_ = df.groupby(['Species'])['Length1'].mean()
   ax.bar(species, mean_)
   ax.set_xlabel('Species')
   ax.set_ylabel('Mean of Length1')
   ax.set_title('Species by the Mean of Length1')
   st.pyplot(fig)
    
def linePlot():
   st.subheader("Line Plot")
   fig1, ax1 = plt.subplots()
   ax1.plot(df[['Length1','Length2','Length3']])
   ax1.title.set_text('Length1 vs Length2 vs Length3')
   ax1.set_xlabel('Fish Index')
   ax1.set_ylabel('Length')
   ax1.legend(['Length1','Length2','Length3'], loc="upper right")
   st.pyplot(fig1)

def boxPlot():
   st.subheader("Box Plot")
   fig2, ax2 = plt.subplots()
   df.boxplot(column='Weight', by='Species', ax=ax2)
   ax2.set_ylabel('Weight')
   st.pyplot(fig2)

def pieChart():
   st.subheader("Pie Chart")
   fig3, ax3 = plt.subplots()
   species = df.groupby('Species', axis=0).count()
   labels = species.index
   ax3.pie(species['Width'],labels=labels)
   st.pyplot(fig3)

def scatterPlot():
   st.subheader("Scatter Plot")
   fig4,ax4 = plt.subplots()
   df.plot.scatter(x= 'Species', y = 'Height', ax=ax4)
   ax4.set_title('Scatter plot depicting Heights of different fish species')
   st.pyplot(fig4)
    
def areaPlot():  
   st.subheader("Area Plot")
   fig5,ax5 = plt.subplots()
   df.plot.area(x='Species',y=['Length1','Length2','Length3'], color=["#FF0000", "#0000FF","#FFAA00"], ax=ax5)
   ax5.set_title('Correlation of Species and its corresponding Lengths')
   st.pyplot(fig5)

def condensed_table():
   st.subheader("Detailed Data View")
   st.dataframe(df)


if option =='Show all graphs':
   BarPlot()
   linePlot()
   boxPlot()
   pieChart()
   scatterPlot()
   areaPlot()
   condensed_table()
elif option=='Bar Plot':
   BarPlot()
elif option=='Line':
   linePlot()
elif option=='Box Plot':
   boxPlot()
elif option=='Pie Chart':
   pieChart()
elif option =='Scatter Plot':
   scatterPlot()
elif option=='Area Plot':
   areaPlot()
elif option =='Condensed Dataview':
   condensed_table()


tab1, tab2, tab3, tab4, tab5 = st.tabs(["observation 1", "observation 2","observation 3", "observation 4", "observation 5"])

with tab1:
   st.subheader("Observation_Bar Plot:")
   st.write("Highest and Lowest average recorded species are Parkki and Pike Species.")

with tab2:
   st.subheader("Observation_Line Plot:")
   st.write("As we move on fish Index the lengths show periodic increase and drop, the highest fish index is 140 and the length has been dropped to half(70)")
    
with tab3:
   st.subheader("Observation_Box Plot:")
   st.write("Highest and Lowest weights are recorded for the species: Pike and Smelt Species.")

with tab4:
   st.subheader("Observation_Pie Chart:")
   st.write("Largest and Smallest widths are recorded for the species: Perch and Whitefish Species.")

with tab5:
   st.subheader("Observation_Scatter Plot:")
   st.write("Longest and Shortest Heights are recorded for the species: Bream and Smelt Species.")

