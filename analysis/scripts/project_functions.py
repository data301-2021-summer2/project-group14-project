{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a7411b29-8196-4359-b5c2-74f6800c3519",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

import seaborn as sns
import pandas as pd

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