import pandas as pd
from sklearn.naive_bayes import GaussianNB

def GNB_model (file_path, result_name, validation_path):
    training_df = pd.read_csv (file_path, header=None)

    # the label is the last column of the dataset
    label = training_df[1024].to_numpy()

    # deletes label of EACH ROW (somehow pandas makes magic like this happen) and sends features to array
    del training_df[1024]

    # df.to_numpy() is csv in 2d array format
    training_features = [x for x in training_df.to_numpy()]

    # fit model 
    model = GaussianNB()
    model.fit(training_features,label)

    # get other csv to try model on
    df = pd.read_csv(validation_path, header=None)
    del df[1024]
    features = [x for x in df.to_numpy()]

    # predict based on data and transform into a list object in order to index
    predicted = model.predict([ feature for feature in features ]).tolist()

    # print results
    incorrect_results = 0
  
    results = []
    for i in range(len(features)):
        results.append([predicted[i]])
        print(f'Row #{i} predicts {predicted[i]} and the actual label is {label[i]}')
        if predicted[i] != label[i]:
            incorrect_results += 1
        
    print(f'For a total of {len(features)} letters, {incorrect_results} were incorrect results for GNB model.')
    csv_results = pd.DataFrame(results, columns=['Predicted'])
    csv_results.to_csv(result_name)