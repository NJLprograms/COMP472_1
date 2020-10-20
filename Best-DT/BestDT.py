import pandas as pd 
from sklearn.tree import DecisionTreeClassifier

def best_DT_model(training_file):
  df = pd.read_csv(training_file, header=None)
  labels = df[1024]

  del df[1024]
  features = [feature for feature in df.to_numpy()]

  decision_tree = DecisionTreeClassifier(criterion="gini",max_depth=None, min_samples_split=2, min_impurity_decrease=0, class_weight=None)
  decision_tree.fit(features, labels)

  return decision_tree