# app/meta_levels/time_warper/time_analysis.py
from prophet import Prophet

def predict_cycles(df):
    m = Prophet(seasonality_mode='multiplicative')
    m.fit(df)
    future = m.make_future_dataframe(periods=90)
    forecast = m.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
