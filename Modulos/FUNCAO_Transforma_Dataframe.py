
import pandas as pd

def transforma_dataframe(dataframe):
    
    df = dataframe.copy()
    
    # Dropando coluna ID
    df = df.drop(columns = ['show_id'])
    
    # Transformando coluna em datetime
    df['date_added'] = pd.to_datetime(df['date_added'])
    
    return df


