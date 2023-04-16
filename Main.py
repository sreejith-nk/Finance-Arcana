import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Settings
page_title="Financial Analysis Tool"
layout="centered"
page_icon=":money_with_wings:"

st.set_page_config(page_title=page_title,page_icon=page_icon,layout=layout)
st.title(page_title+" "+page_icon)

df=pd.read_csv("Arcana_score_final.csv")
symbol=pd.read_csv("symbol-entity-names.csv")
stock=pd.read_csv("stocknew.csv")

with st.form("entry_form",clear_on_submit=False):
    
    
    company=st.text_input("",placeholder="Enter the company here")

    submitted=st.form_submit_button("View Insights")

    if submitted:
        df_comp=df.loc[df["company_name"]==company]
        company_name=symbol.loc[symbol["symbol"]==company]["Company"].values[0]
        st.write('<span style="font-size:24px;">Company name : ' + company_name + '</span>', unsafe_allow_html=True)
        with st.expander("Sentiment Bar charts"):
            for _,row in df_comp.iterrows():
                x = ['Positive', 'Neutral', 'Negative']
                y = [row["Positive"],row["Neutral"], row["Negative"]]
                fig = go.Figure([go.Bar(x=x, y=y)])
                #fig.update_layout(title='Sentiment', xaxis_title=row["year"], yaxis_title='Number of Sales')
                fig.update_layout( title='Sentiment analysis from earning calls for year {}'.format(row["year"]),
                                   xaxis_title='Sentiment',
                                   yaxis_title='Intensity of sentiment',
                                   font=dict(
                                    family='Arial',
                                    size=12,
                                    color='black'),
                                    bargap=0.2,
                                    bargroupgap=0.1,
                                    hovermode='closest',
                                    showlegend=False)
                st.plotly_chart(fig,use_container_width=True)

        with st.expander("Stock market performance of the company"):
            df_comp=stock.loc[stock['symbol']==company]
            trace = go.Scatter(x=df_comp['ds'], y=df_comp['Product'], mode='lines')
            layout = go.Layout(title='Stock performace of the company',xaxis_title="date", yaxis_title='Trading worth')
            figure = go.Figure(data=[trace], layout=layout)
            st.plotly_chart(figure,use_container_width=True)
            st.write("This line chart shows the performance of the company in the last 5 months in the stock market, The y-axis gives the worth of the company in the stock market which is the product of the closing price and the volume traded")

        with st.expander("How to read the bar chart?"):
            st.write("Sentiment analysis of earnings calls refers to the process of using natural language processing (NLP) techniques to determine the overall emotional tone of a company's earnings call, which can be classified as positive, negative, or neutral. Here's how each sentiment analysis can be interpreted:")
            st.write("Positive sentiment analysis: If the sentiment analysis of an earnings call is positive, it means that the overall tone of the call was optimistic and upbeat, with a focus on good news and positive developments within the company. This may include strong revenue growth, new product launches, successful marketing campaigns, or other positive developments that are driving the company's success. Investors and analysts may interpret this as a signal of positive momentum and potential future growth for the company")

            st.write("Negative sentiment analysis:If the sentiment analysis of an earnings call is negative, it means that the overall tone of the call was pessimistic and downbeat, with a focus on bad news and negative developments within the company. This may include declining revenue, missed earnings targets, or other negative developments that are causing concerns about the company's financial health. Investors and analysts may interpret this as a signal of potential risks and challenges that the company may face in the future")
            st.write("Neutral sentiment analysis:")
            st.write("If the sentiment analysis of an earnings call is neutral, it means that the overall tone of the call was neither particularly positive nor negative. This may include a focus on routine updates, non-material information, or a balanced presentation of both positive and negative news. Investors and analysts may interpret this as a signal of stability and predictability within the company, but may also be looking for more clarity or guidance on the company's future prospects.")
