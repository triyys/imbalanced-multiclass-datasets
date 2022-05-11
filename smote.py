import pandas as pd

df = pd.read_csv('glass.csv')

features = []
for feature in df.columns:
    if feature != 'target':
        features.append(feature)
X = df[features]
y = df['target']
print(X)