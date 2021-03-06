#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : ML_Project_2
# @Author       : Wei Jiang, Xiaoyu Lin, Yao Di
# @File         : evaluation.py
# @Discription  : Run this file can get the averaged quality of trained model among all frames in test dataset,
#                 comparing with ground truth.

from yeastSegHelpers import quality_measures
import skimage

# Load the frames
truth = skimage.io.imread('../dataset/test/mask/ground_truth.tif')
pred = skimage.io.imread('../dataset/test/mask/results_ero5_10lun.tif')

# Create a dictionary to save measured quality
evaluation = dict()
evaluation["Number Fusions"] = 0
evaluation["Number Splits"] = 0
evaluation["Nb False Positives"] = 0
evaluation["Nb False Negatives"] = 0
evaluation["Average Overshoot"] = 0
evaluation["Average Undershoot"] = 0
evaluation["Av. True Area"] = 0
evaluation["Av. Pred Area"] = 0
evaluation["Nb Considered Cells"] = 0

# Loop all images in the frame sequence
for i in range(truth.shape[0]):
    measures = quality_measures.quality_measures(truth[i], pred[i])
    evaluation["Number Fusions"] += measures["Number Fusions"]
    evaluation["Number Splits"] += measures["Number Splits"]
    evaluation["Nb False Positives"] += measures["Nb False Positives"]
    evaluation["Nb False Negatives"] += measures["Nb False Negatives"]
    evaluation["Average Overshoot"] += measures["Average Overshoot"]
    evaluation["Average Undershoot"] += measures["Average Undershoot"]
    evaluation["Av. True Area"] += measures["Av. True Area"]
    evaluation["Av. Pred Area"] += measures["Av. Pred Area"]
    evaluation["Nb Considered Cells"] += measures["Nb Considered Cells"]

# Average the measured quality
evaluation["Number Fusions"] = evaluation["Number Fusions"] / truth.shape[0]
evaluation["Number Splits"] = evaluation["Number Splits"] / truth.shape[0]
evaluation["Nb False Positives"] = evaluation["Nb False Positives"] / truth.shape[0]
evaluation["Nb False Negatives"] = evaluation["Nb False Negatives"] / truth.shape[0]
evaluation["Average Overshoot"] = evaluation["Average Overshoot"] / truth.shape[0]
evaluation["Average Undershoot"] = evaluation["Average Undershoot"] / truth.shape[0]
evaluation["Av. True Area"] = evaluation["Av. True Area"] / truth.shape[0]
evaluation["Av. Pred Area"] = evaluation["Av. Pred Area"] / truth.shape[0]
evaluation["Nb Considered Cells"] = evaluation["Nb Considered Cells"] / truth.shape[0]

# Print the results
print(evaluation)
