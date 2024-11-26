# -*- coding: utf-8 -*-
"""
COMP-2040 - Assignment 5 - LRM

This code is about: 
Created on Thu Feb  1 14:25:04 2024

@author: Mariah Quinquito
"""

class LinRegModel:
    def __init__(self, slope=0, bias=0):
        self.slope = slope
        self.bias = bias

    def __repr__(self):
        return ("***************************************\n"
                f"Model parameters:\nslope = {self.slope}\n"
                f"bias = {self.bias}\n"
                "***************************************\n")

    def predict(self, x):
        return [self.bias + self.slope * xi for xi in x]

def rmse(yhat, y):
    n = len(y)
    
    sum_squared_diff = 0
    for y_i, yhat_i in zip(y, yhat):
        diff = y_i - yhat_i
        squared_diff = diff**2
        sum_squared_diff += squared_diff

    rmse_value = (sum_squared_diff / n)**0.5
    return rmse_value
