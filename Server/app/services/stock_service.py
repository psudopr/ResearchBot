from alpha_vantage.timeseries import TimeSeries
from app.core.config import Config

def get_stock_data(symbol: str):
    """Fetches the last 12 months of daily adjusted stock data."""
    try:
        ts = TimeSeries(key=Config.ALPHA_VANTAGE_API_KEY, output_format='pandas')
        # The free tier has limitations, so a full 12 months might require
        # the 'full' outputsize, or this may need to be adjusted based on the API.
        data, meta_data = ts.get_daily_adjusted(symbol=symbol, outputsize='compact')
        # Convert data to a more JSON-friendly format
        data['date'] = data.index
        # Limit to roughly the last year (252 trading days)
        data = data.head(252)
        return data.to_dict('records')
    except Exception as e:
        print(f"Error fetching stock data for {symbol}: {e}")
        return None
