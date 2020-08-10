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

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore")

#lib para serializar objetos
# from sklearn.externals import joblib
import joblib

from datetime import datetime, timedelta, date
import sys
import logging
import time
import itertools

def serialize_model(model, file_name):
    joblib.dump(model, file_name)
pass


def load_model(file_name):
    return(joblib.load(file_name))
pass

