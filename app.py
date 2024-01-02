import streamlit as st
from moneycontrol import MoneyControlAPI
from textblob import TextBlob  # for sentiment analysis

# Function to fetch stock details
def get_stock_details(symbol):
    api = MoneyControlAPI()
    stock_data = api.get_stock_info(symbol)
    return stock_data

# Function to fetch news articles and generate sentiment scores
def analyze_stock_news(symbol):
    api = MoneyControlAPI()
    news_data = api.get_stock_news(symbol)

    sentiment_scores = []

    for article in news_data:
        text = article['title'] + ' ' + article['summary']
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        sentiment_scores.append(sentiment_score)

    average_sentiment = sum(sentiment_scores) / len(sentiment_scores)
    return news_data, average_sentiment

# Streamlit app
def main():
    st.title("Stock Analyzer App")

    # User input for stock symbol
    symbol = st.text_input("Enter Stock Symbol (e.g., TCS, AAPL):")

    if symbol:
        # Display stock details
        stock_details = get_stock_details(symbol)
        st.subheader("Stock Details")
        st.write(stock_details)

        # Analyze news and display sentiment scores
        news_data, average_sentiment = analyze_stock_news(symbol)

        st.subheader("Latest News Articles")
        for article in news_data:
            st.write(f"- **{article['title']}**")
            st.write(f"  *Summary: {article['summary']}")
            st.write(f"  *Link: {article['link']}")

        st.subheader("Sentiment Analysis")
        st.write(f"Average Sentiment Score: {average_sentiment:.2f}")

if __name__ == "__main__":
    main()
