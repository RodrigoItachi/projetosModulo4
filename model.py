from unicodedata import numeric
import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report


with open(r'/home/monkeydluffy/Documentos/ibc/projetoSpam/diabetes.pkl', 'rb') as f:
  X_diabetes_treinamento, X_diabetes_test, y_diabetes_treinamento, y_diabetes_test = pickle.load(f)

rede_neural = pickle.load(open(r'/home/monkeydluffy/Documentos/ibc/projetoSpam/rede_diabete_finalicxvzada.sav', 'rb'))

print(X_diabetes_treinamento.shape,'\n',X_diabetes_test.shape,'\n')
print(y_diabetes_treinamento.shape,'\n',y_diabetes_test.shape,'\n')

print(type(rede_neural))


pre = input('insira quantas vezes você ja engravidou: \n')
glu = input('insira a sua taxa de Glicose: \n')
bP = input('insira a pressão do seu sangue: \n')
ST = input('insira a espressura da sua pele: \n')
insu = input('insira sua taxa de insulina: \n')
bmi = input('insira seu indice de massa corporal: \n')
dpf = input('insira sua função de linhagem de diabetes: \n')
age = input('insira sua idade: \n')

# previsores = np.array(, dtype=numeric)
# previsores = rede_neural.predict([[pre,glu,bP,ST,insu,bmi,dpf,age]])
# print(previsores)

previsores = np.array(rede_neural.predict([[pre,glu,bP,ST,insu,bmi,dpf,age]]), dtype=numeric)
print(previsores)