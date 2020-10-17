#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:13:57 2020

@author: adilson lopes khouri
"""
import joblib
import glob
from Experiment import Experiment
from parser_lime_explanation_html import parser_lime_explanation_html

def serialize(object, file_name):
    joblib.dump(object, file_name)
pass

def deserialize(file_name):
    return(joblib.load(file_name))
pass

if __name__ == "__main__":

	# experiments = []
	# for file in glob.glob("../serialized_explanation/*.html"):
	# 	print(file)
	# 	exp = parser_lime_explanation_html(file).parse_all_experiment()
	# 	experiments.append(exp)
	#
	# serialize(experiments, 'my_beautiful_experiments.pkl')

	my_beautiful_obj = deserialize('my_beautiful_experiments.pkl')

	for experiment in range(len(my_beautiful_obj)):
		my_beautiful_obj[experiment].print_experiment()

	print(len(my_beautiful_obj))
pass

# arquivo = """../serialized_explanation/DT#diabetes#instance:86#num_features:11#feat_selec:auto#discre:decile#sai:False#kernel_s:2.html"""
	# Exp = parser_lime_explanation_html(arquivo).parse_all_experiment()
	# Exp.print_experiment()
