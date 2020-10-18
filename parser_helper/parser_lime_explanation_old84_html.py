#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:13:57 2020

@author: adilson lopes khouri
NUSP: 6411994
"""

import glob
import re
from Experiment import Experiment


class parser_lime_explanation_old84_html:

    def __init__(self, file_name):
        self.file_name = file_name
    pass

    def parse_all_experiment(self):

        experiment = self.__parse_file_name()
        exp_and_feat_imp = self.__parse_file_content(experiment)

        return(exp_and_feat_imp)
    pass

    #TODO: add some try catch logic
    def __parse_file_name(self):

        parameters_together = self.file_name.replace("../serialized_explanation/old_exec/", "").replace(".html", "")
        parameters = parameters_together.split("_")

        #Vanila experiment
        discretize_continuous = None
        model = parameters[0].strip()
        dataset = parameters[1].strip()
        instance_index = int(parameters[3].strip())
        n_features = int(parameters[6].strip())
        feature_selection = None
        discretizer = None
        sample_around_instance = None
        kernel_width = None

        experiment = Experiment(kernel_width,
                                feature_selection,
                                discretize_continuous,
                                discretizer,
                                instance_index,
                                sample_around_instance,
                                dataset,
                                model,
                                n_features)
        return(experiment)
    pass

    def __parse_file_content(self, experiment):

        with open(self.file_name, mode='r') as reader:
            texto = reader.read()

            #new lime.PredictProba(pp_svg, ["doente", "saudável"], [0.9538461538461539, 0.046153846153846156]);
            ma = re.search("new lime.PredictProba\(pp_svg,.*\);", texto)
            class_probs_raw = texto[ma.span()[0]:ma.span()[1]]
            feature_importance_sem_tag = class_probs_raw.replace("new lime.PredictProba(pp_svg,", "").replace(");", "").replace(
                "]", "").replace("[", "")
            feature_importance_sem_aspas = feature_importance_sem_tag.replace("\"", "")
            feature_importance_quebrado_por_feature = feature_importance_sem_aspas.split(",")
            print(feature_importance_quebrado_por_feature[0].strip())
            print(feature_importance_quebrado_por_feature[1].strip())
            print(feature_importance_quebrado_por_feature[2].strip())
            print(feature_importance_quebrado_por_feature[3].strip())

            # class0 weigths
            ma = re.search("exp.show.*0, exp_div\);", texto)
            class_probs_raw = texto[ma.span()[0]:ma.span()[1]]
            feature_importance_sem_tag = class_probs_raw.replace("exp.show(", "").replace(", 0, exp_div);", "").replace(
                "]]", "]").replace("[[", "[")
            feature_importance_quebrado_por_feature = feature_importance_sem_tag.split(", [")

            for feat_imp in range(len(feature_importance_quebrado_por_feature)):
                sem_colchete_dir = feature_importance_quebrado_por_feature[feat_imp].replace("]", "")
                sem_colchete_esq = sem_colchete_dir.replace("[", "")
                sem_aspa_dupla = sem_colchete_esq.replace("\"", "")
                separa_feat_peso = sem_aspa_dupla.split(",")
                experiment.add_feature_weigth_c0(separa_feat_peso[0], 'classe0' ,separa_feat_peso[1])

            # class1 weigths
            ma = re.search("exp.show.*1, exp_div\);", texto)
            class_probs_raw = texto[ma.span()[0]:ma.span()[1]]
            feature_importance_sem_tag = class_probs_raw.replace("exp.show(", "").replace(", 1, exp_div);", "").replace(
                "]]", "]").replace("[[", "[")
            feature_importance_quebrado_por_feature = feature_importance_sem_tag.split(", [")

            for feat_imp in range(len(feature_importance_quebrado_por_feature)):
                sem_colchete_dir = feature_importance_quebrado_por_feature[feat_imp].replace("]", "")
                sem_colchete_esq = sem_colchete_dir.replace("[", "")
                sem_aspa_dupla = sem_colchete_esq.replace("\"", "")
                separa_feat_peso = sem_aspa_dupla.split(",")
                experiment.add_feature_weigth_c1(separa_feat_peso[0], 'classe1' ,separa_feat_peso[1])

            # variable values
            ma = re.search("exp.show_raw_tabular.*, raw_div\);", texto)
            # print(ma)
            class_probs_raw = texto[ma.span()[0]:ma.span()[1]]
            feature_importance_sem_tag = class_probs_raw.replace("exp.show_raw_tabular(", "").replace(", 0, raw_div);", "").replace(
                "]]", "]").replace("[[", "[")
            feature_importance_quebrado_por_feature = feature_importance_sem_tag.split(", [")

            for feat_imp in range(len(feature_importance_quebrado_por_feature)):
                sem_colchete_dir = feature_importance_quebrado_por_feature[feat_imp].replace("]", "")
                sem_colchete_esq = sem_colchete_dir.replace("[", "")
                sem_aspa_dupla = sem_colchete_esq.replace("\"", "")
                separa_feat_peso = sem_aspa_dupla.split(",")
                experiment.add_feature_value(separa_feat_peso[0], separa_feat_peso[1])

        return(experiment)
    pass

pass