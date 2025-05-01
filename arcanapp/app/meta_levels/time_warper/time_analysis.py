from prophet import Prophet
import pandas as pd

class TimeCyclePredictor:
    def __init__(self):
        self.model = Prophet(seasonality_mode='multiplicative')

    def predict_cycles(self, df):
        self.model.fit(df)
        future = self.model.make_future_dataframe(periods=30)
        forecast = self.model.predict(future)
        return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
