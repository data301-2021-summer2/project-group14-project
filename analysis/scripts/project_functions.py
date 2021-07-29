import seaborn as sns
import pandas as pd
path = 'data/raw/waterpotability.csv'

def load_process(path):
    df = (
        pd.read_csv(path)
        .rename(columns={'ph': 'pH',
              'Hardness': 'Hardness (mg/L)',
              'Solids': 'Solids (ppm)',
              'Chloramines': 'Chloramines (ppm)',
              'Sulfate': 'Sulfate (mg/L)',
              'Conductivity': 'Conductivity (μS/cm)',
              'Organic_carbon': 'Organic Carbon (ppm)',
              'Trihalomethanes': 'Trihalomethanes (μg/L)',
              'Turbidity': 'Turbidity (NTU)',
              'Potability': 'Potable'})
        .dropna().reset_index(drop=True)
        .replace(1, 'Yes')
        .replace(0, 'No')
     )
    
    return df