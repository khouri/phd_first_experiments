import pandas as pd
import numpy as np
import lime
import lime.lime_tabular
import sys
sys.path.append('./ml_helper')
import ml_helper_train_model as model_train
import ml_helper_serialize_model as serializer
from sklearn.model_selection import train_test_split


def sample_baseline_model(model, dataset):
    
    np.random.seed(1)

    predictors = dataset.loc[:, dataset.columns != 'target']
    target = dataset.target    

    X_train, X_test, y_train, y_test = model_train.get_train_test(predictors, target)

    predicoes = model.predict(X_test)
    mat_conf = pd.DataFrame(index = y_test.index)
    mat_conf['real_label'] = y_test
    mat_conf['pred_label'] = predicoes
    mat_conf['mat_conf_mod'] = np.select([
                                        ((mat_conf['real_label'] == 1) & (mat_conf['pred_label'] == 1)),
                                        ((mat_conf['real_label'] == 0) & (mat_conf['pred_label'] == 1)), 
                                        ((mat_conf['real_label'] == 0) & (mat_conf['pred_label'] == 0)), 
                                        ((mat_conf['real_label'] == 1) & (mat_conf['pred_label'] == 0)) 
                                         ], 
                                      [
                                        'TP',
                                        'FP',
                                        'TN',
                                        'FN'
                                      ], 
                                        default='Unknown'
                                    )


    #random sample by each possible value of confusion matrix
    grouped_data = mat_conf.groupby(['mat_conf_mod'])
    sample_by_group = grouped_data.sample(n = 1, random_state = 6411994)
    heart_index = sample_by_group.index

    return(heart_index)
pass


def explain_it(model, 
               dataset, 
               target_names, 
               num_features, 
               instance_index, 
               output_file_path):

    np.random.seed(1)

    predictors = dataset.loc[:, dataset.columns != 'target']
    target = dataset.target

    X_train, X_test, y_train, y_test = train_test_split(predictors, 
                                                        target, 
                                                        test_size = 0.25, 
                                                        random_state = 6411994)
    
    instace_to_be_explained = X_test.loc[instance_index,:].to_numpy()

    feature_names = list(dataset.columns.values)
    X_train = X_train.to_numpy()
    X_test = X_test.to_numpy()

    explainer = lime.lime_tabular.LimeTabularExplainer(X_train, 
                                                       feature_names = feature_names, 
                                                       class_names = target_names, 
                                                       discretize_continuous = True)

    exp = explainer.explain_instance(instace_to_be_explained,
                                     model.predict_proba, 
                                     num_features = num_features, 
                                     top_labels = 2)

    exp.save_to_file(output_file_path,
                     predict_proba = True, 
                     show_predicted_value = True)

pass


def to_float(dataset):

    columns = dataset.loc[:, dataset.columns != 'target'].columns
    
    for col in columns:
        dataset[col] = dataset[col].astype(np.float64) 
    
    return(dataset)
pass