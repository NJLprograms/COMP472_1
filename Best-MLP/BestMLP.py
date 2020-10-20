import pandas as pd
from sklearn.neural_network import MLPClassifier

def best_MLP_model(training_file):
  df = pd.read_csv(training_file, header=None)
  labels = df[1024]

  del df[1024]
  features = [feature for feature in df.to_numpy()]

  model = MLPClassifier(activation='logistic', hidden_layer_sizes=(100,), solver='sgd',)
  model.fit(features, labels)

  return model