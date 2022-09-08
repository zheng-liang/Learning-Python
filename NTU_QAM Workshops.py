import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('BTC-USD.csv')

# Exploring the data frame
print(df.head())
print(df.tail(10))
df.describe()
df.columns

# Plot Close and Adjusted Close prices
df.plot(x="Date",
        y=["Close"],
        kind="line",
        title="BTC USD",
        xlabel="Date",
        ylabel="Price")
plt.show()

# Generate Simple Moving Averages
df['SMA20'] = df['Close'].rolling(window=20, min_periods=1).mean()
df['SMA50'] = df['Close'].rolling(window=50, min_periods=1).mean()
df['SMA200'] = df['Close'].rolling(window=200, min_periods=1).mean()
df.plot(x="Date",
        y=["Close", "SMA20", "SMA50", "SMA200"],
        kind="line",
        title="BTC USD",
        xlabel="Date",
        ylabel="Price")
plt.show()

# Generate Exponential Moving Averages
df['EMA10'] = df['Close'].ewm(span=20, adjust=False).mean()
df['EMA20'] = df['Close'].ewm(span=30, adjust=False).mean()
df['EMA50'] = df['Close'].ewm(span=50, adjust=False).mean()
df.plot(x="Date",
        y=["Close", "EMA10", "EMA20", "EMA50"],
        kind="line",
        title="BTC USD",
        xlabel="Date",
        ylabel="Price")
plt.show()

# Histogram of Daily Return
df = df.set_index('Date')
df['daily_chg'] = df['Adj Close'].pct_change(periods=1)
sns.displot(df['daily_chg'].dropna(),
            bins=50,
            color='blue',
            kde=True,
            height=6,
            aspect=1.5)
plt.suptitle('Daily Return of BTC (in %), \n 05 Sept 2021 to 04 Sept 2022',
             fontsize=12,
             color='black')
plt.grid(True)
plt.show()
