import pandas as pd
import numpy as np
from pathlib import Path
from coingecko import json_path
from definitions import change_direction

csv_path = Path("homeworks") / "fejeszsolt" / "hw_07_extract_transform" / "top50.csv" 

df_coingecko=pd.read_json(json_path)


empty_cells = df_coingecko.isnull().sum()
print (empty_cells)

total_market_cap = df_coingecko['market_cap'].sum()
print(total_market_cap)

top50_df=df_coingecko.sort_values('current_price', ascending=False).head(50)

top50_df=top50_df.sort_values('price_change_percentage_24h',ascending=False)


#top50_df['change_direction']=np.where(
#    top50_df['price_change_percentage_24h']> 0,
#    '+',
#    np.where(
#        top50_df['price_change_percentage_24h']< 0,
#    '-',
#    0
#    )
#    )


top50_df['change_direction'] = top50_df.apply(change_direction, axis=1)
print(top50_df)

top50_df.to_csv(csv_path, index=False)
