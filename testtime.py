import joblib
import fbprophet
F=joblib.load('1863_prophet_model')
Pre = F.make_future_dataframe(freq='T', periods=180, include_history=False)
forcasts = F.predict(Pre)
print(forcasts)