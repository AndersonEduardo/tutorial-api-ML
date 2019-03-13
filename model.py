# Importando dependencias
import pandas as pd
import numpy as np

# Abrindo dataset em um dataframe e incluir as features de interesse
url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
df = pd.read_csv(url)
include = ['Age', 'Sex', 'Embarked', 'Survived'] # Only four features
df_ = df[include]

# Preprocessamento dos dados
categoricals = []
for col, col_type in df_.dtypes.iteritems():
     if col_type == 'O':
          categoricals.append(col)
     else:
          df_[col].fillna(0, inplace=True)

df_ohe = pd.get_dummies(df_, columns=categoricals, dummy_na=True)

# Classificador
from sklearn.linear_model import LogisticRegression
dependent_variable = 'Survived'
x = df_ohe[df_ohe.columns.difference([dependent_variable])]
y = df_ohe[dependent_variable]
lr = LogisticRegression()
lr.fit(x, y)

# Salvando modelo
from sklearn.externals import joblib
joblib.dump(lr, 'model.pkl')
print("Model dumped!")

## Para carregar o modelo:
#lr = joblib.load('model.pkl')

# Salvando referencia para as tabelas
model_columns = list(x.columns)
joblib.dump(model_columns, 'model_columns.pkl')
print("Models columns dumped!")
