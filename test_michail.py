import pandas as pd
import mplfinance as mpf
import matplotlib
matplotlib.use('TkAgg')
# Функция для расчета EMA
def calculate_ema(data, span):
    return data.ewm(span=span, adjust=False).mean()
# Загрузка данных из CSV-файла
file_path = r"C:\Users\Анатолий\Downloads\prices.csv\prices.csv"
data = pd.read_csv(file_path)

# Преобразование временной метки в формат datetime
data['TS'] = pd.to_datetime(data['TS'])

# Группировка данных и формирование свечей
ohlc_data = data.resample('5T', on='TS').agg({
    'PRICE': ['first', 'max', 'min', 'last']
})
ohlc_data.columns = ['Open', 'High', 'Low', 'Close']
print(ohlc_data)
# Расчет EMA для разных периодов
ema_7 = calculate_ema(ohlc_data['Close'], 7)
print(ema_7)
ema_14 = calculate_ema(ohlc_data['Close'], 14)
print(ema_14)
ema_21 = calculate_ema(ohlc_data['Close'], 21)
print(ema_21)

# Добавление EMA на график свечей
ap = [mpf.make_addplot(ema_7, color='blue', label='EMA 7'),
      mpf.make_addplot(ema_14, color='orange', label='EMA 14'),
      mpf.make_addplot(ema_21, color='green', label='EMA 21')]

mpf.plot(ohlc_data, type='candle', style='charles', title='График свечей с EMA', volume=False, warn_too_much_data=10000, addplot=ap)
