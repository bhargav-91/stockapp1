from nsepy import get_history
from datetime import date
import matplotlib.pyplot as plt
import pandas as pd 



data = get_history(symbol="EICHERMOT", start=date(2015,1,1), end=date(2020,5,1))
print(data)
#data[['Close']].plot()
x = data.index.values.tolist()
y = data['Prev Close']

plt.plot(x,y)
plt.xlabel('Date ')
plt.ylabel('Stock Price  - Eicher Motors')

plt.title('Line graph!')

plt.show()
