#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:13:57 2020

@author: adilson lopes khouri
"""
import joblib
import glob
import re
from Experiment import Experiment
from parser_lime_explanation_html import parser_lime_explanation_html
from parser_lime_explanation_old84_html import parser_lime_explanation_old84_html

import sys
sys.path.append('../excel_helper/')
import excel_helper.To_excel as excel
import excel_helper.To_excel_other as excel_other


def serialize(object, file_name):
    joblib.dump(object, file_name)
pass

def deserialize(file_name):
    return(joblib.load(file_name))
pass


if __name__ == "__main__":

    #84 base case to be analised
    # vanila_experiments = []
    # for file in glob.glob("../serialized_explanation/old_exec/*.html"):
    #     exp = parser_lime_explanation_old84_html(file).parse_all_experiment()
    #     vanila_experiments.append(exp)
    #
    # conversor_excel = excel.To_excel("Experiments.xlsx", "84_vanila")
    # conversor_excel.write_to_excel(experiment_list = vanila_experiments,
    #                                n_features = 5)
    #

    #other exp
    experiments = []
    for file in glob.glob("../serialized_explanation/*.html"):
        exp = parser_lime_explanation_html(file).parse_all_experiment()
        experiments.append(exp)
        # exp.print_experiment()

    conversor_excel = excel_other.To_excel_other("Experiments_non_vanila.xlsx", "experiments")
    conversor_excel.write_to_excel(experiment_list = experiments,
                                   n_features = 5)

pass