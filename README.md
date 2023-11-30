# Arcana-Royal Warriors
We are Team Royal Warriors
The Members are - 
PS Hari Govind - (CE19B070)
Sreejith NK - (CH19B090)
Sreedars S J - (ME19B174)
Nallana Divya - (MM21B041)

You can find the guide to using it on https://www.youtube.com/watch?v=9hXBZX1NaVw. The one given on google form is not the correct one.

----------------------------------------------------------------------------------

OUR PRODUCT IS CALLED FAT (Finanical Analysis Tool)

Please note you need to search the company in Capital Letters
 
We used the Transcipt data set given to create a Sentiment Analysis model using the Finbert model which is a complex model
by Hugging face and Prosus AI.
Using this we made an scoring matrix to capture the emotions of the people speaking and plotted a bar chart for every company, The model ran for 4 hours on 
every dataset and created the sentiment matrix

Then from the prices data set we created a new feature which gives the trading worth of the company in the stock market, which is the product of the closing price and volume traded, we thought that this would be a better perfomance indicator rather than just the closing price and violume traded.

Now we deployed the model on a platform called Streamlit share, and we have provided the links and video recording (the clarity is a bit low) in the submission.

After searching for a company, you will get the full form, the sentiment score, the trading performance as well as a brief description on how to read the graphs.



Running on local syste.
1. Clone this repo on your pc.
2. Install the libraries mentioned in requirements.txt
3. Run the following command in the command line

`streamlit run Main.py`
