#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:13:57 2020

@author: adilson lopes khouri
NUSP: 6411994
"""
from Feature_Importance import Feature_Importance
from Feature_Value import Feature_Value

class Experiment:

    def __init__(self,
                 kernel_width,
                 feature_selection,
                 discretize_continuous,
                 discretizer,
                 instance_index,
                 sample_around_instance,
                 dataset,
                 model,
                 # class_inst_baseline,
                 n_features):
        self.kernel_width = kernel_width
        self.feature_selection = feature_selection
        self.discretize_continuous = discretize_continuous
        self.discretizer = discretizer
        self.sample_around_instance = sample_around_instance
        self.instance_index = instance_index
        self.dataset = dataset
        self.model = model
        # self.class_inst_baseline = class_inst_baseline
        self.feature_importance_c1 = list()
        self.feature_importance_c0 = list()
        self.feature_value = list()
        self.n_features = n_features
        self.class_inst_baseline = Experiment.__def_class_inst_baseline(instance_index, dataset)
    pass

    def set_c1_prob(self, predicted_proba_c1):
        self.predicted_proba_c1 = predicted_proba_c1
    pass

    def set_c0_prob(self, predicted_proba_c0):
        self.predicted_proba_c0 = predicted_proba_c0
    pass

    # TODO: add this relation in the file
    # name, to become less hard coded
    @staticmethod
    def __def_class_inst_baseline(instance_index, dataset_name):

        if(dataset_name == "heart"):
            if(instance_index == 143):
                return("FN")
            if(instance_index == 203):
                return("FP")
            if(instance_index == 242):
                return("TN")
            if(instance_index == 96):
                return("TP")

        if(dataset_name == "diabetes"):
            if(instance_index == 86):
                return("FN")
            if(instance_index == 1458):
                return("FP")
            if(instance_index == 791):
                return("TN")
            if(instance_index == 1003):
                return("TP")

        if(dataset_name == "wine"):
            if(instance_index == 291):
                return("FN")
            if(instance_index == 725):
                return("FP")
            if(instance_index == 60):
                return("TN")
            if(instance_index == 755):
                return("TP")

    pass

    def print_experiment(self):

        print("---------------------------------------")
        print("Experiment")
        print("---------------------------------------")

        dataset = """DS:\t\t\t\t{0}""".format(self.dataset)
        instance = """\ninstance:\t\t{0}""".format(self.instance_index)
        model = """\nmodel:\t\t\t{0}""".format(self.model)
        class_inst_baseline = """\nclass_inst_base:\t{0}""".format(self.class_inst_baseline)
        lime_param = """\n------LIME - parameters------"""
        sample_arr_inst = """\nSAI:\t\t\t\t{0}""".format(self.sample_around_instance)
        discretizer = """\ndiscretizer:\t\t{0}""".format(self.discretizer)
        discretize_continuous = """\ndisc_cont:\t\t{0}""".format(self.discretize_continuous)
        feature_selection = """\nfeature_sel:\t\t{0}""".format(self.feature_selection)
        kernel_width = """\nkernel_width:\t{0}""".format(self.kernel_width)

        print("""{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}""".format(dataset, instance,
                                                          model, class_inst_baseline,
                                                          lime_param,
                                                          sample_arr_inst, discretizer,
                                                          discretize_continuous,
                                                          feature_selection, kernel_width))

        print("---------------------------------------")
        print("Feature Importance obtained by LIME class 0")
        print("---------------------------------------")
        for fi in range(len(self.feature_importance_c0)):
            string = """feature_name: {0}\tfeature_weigth: {1}\tclass_name: {2}"""
            print(string.format(self.feature_importance_c0[fi].feature_name,
                                self.feature_importance_c0[fi].feature_weigth,
                                self.feature_importance_c0[fi].class_name))

        print("---------------------------------------")
        print("Feature Importance obtained by LIME class 1")
        print("---------------------------------------")
        for fi in range(len(self.feature_importance_c1)):
            string = """feature_name: {0}\tfeature_weigth: {1}\tclass_name: {2}"""
            print(string.format(self.feature_importance_c1[fi].feature_name,
                                self.feature_importance_c1[fi].feature_weigth,
                                self.feature_importance_c1[fi].class_name))

        print("---------------------------------------")
        print("Feature Values")
        print("---------------------------------------")
        for fi in range(len(self.feature_value)):
            string = """feature_name: {0}\tfeature_value: {1}"""
            print(string.format(self.feature_value[fi].feature_name,
                                self.feature_value[fi].feature_value))

    pass

    def add_feature_weigth_c1(self, feature_name, feature_weigth, class_name):
        feat_imp_obj = Feature_Importance(feature_name, feature_weigth, class_name)
        self.feature_importance_c1.append(feat_imp_obj)
    pass

    def add_feature_weigth_c0(self, feature_name, feature_weigth, class_name):
        feat_imp_obj = Feature_Importance(feature_name, feature_weigth, class_name)
        self.feature_importance_c0.append(feat_imp_obj)
    pass

    def add_feature_value(self, feature_name, feature_value):
        feat_imp_obj = Feature_Value(feature_name, feature_value)
        self.feature_value.append(feat_imp_obj)
    pass

    def number_of_features_c1(self):
        return(len(self.feature_importance_c1))
    pass

    def number_of_features_c0(self):
        return(len(self.feature_importance_c0))
    pass

pass