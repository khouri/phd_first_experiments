import pandas as pd
import numpy as np
from numpy import sort
from xgboost import XGBClassifier
import xgboost as xgb
from xgboost import plot_importance
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import scale
from matplotlib import pyplot as plt
import datetime as dt
import time
from functools import reduce
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
import seaborn as sns 
from dateutil.rrule import rrule, DAILY, MONTHLY
from sklearn.utils import resample

#lib para serializar objetos
# from sklearn.externals import joblib
import joblib

from datetime import datetime, timedelta, date
import sys
import logging
import time
import itertools

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

def train_model(predictors, 
                target, 
                folds,
                param_to_be_tunned, 
                estimator):

    X_train, X_test, y_train, y_test = train_test_split(predictors, 
                                                        target, 
                                                        test_size = 0.25, 
                                                        random_state = 6411994)

    tuned_parameters = param_to_be_tunned

    # scores = ['precision', 'recall', 'f1']
    scores = ['f1']

    for score in scores:
        print("# Tuning hyper-parameters for %s" % score)
        print()

        model = GridSearchCV(estimator, 
                           tuned_parameters, 
                           scoring='%s_macro' % score, 
                           cv = folds,
                           iid = False
                          )

        model.fit(X_train, y_train)

        print("Best parameters set found on development set:")
        print()
        print(model.best_params_)
        print()
#         print("Grid scores on development set:")
#         print()
#         means = model.cv_results_['mean_test_score']
#         stds = model.cv_results_['std_test_score']
#         for mean, std, params in zip(means, stds, model.cv_results_['params']):
#             print("%0.3f (+/-%0.03f) for %r" % (mean, std * 2, params))
#         print()

        print("Detailed classification report:")
        print()
        print("The model is trained on the full development set.")
        print("The scores are computed on the full evaluation set.")
        print()
        y_true, y_pred = y_test, model.predict(X_test)
        print(classification_report(y_true, y_pred))
        print()

        return(model)
pass

