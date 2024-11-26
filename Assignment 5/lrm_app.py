from lrm import LinRegModel, rmse
"""
COMP-2040 - Assignment 5 - LRM

This code is about: 
Created on Thu Feb  1 14:26:28 2024

@author: Mariah Quinquito
"""

model_1 = LinRegModel()
model_2 = LinRegModel(slope=-1, bias=4)
model_3 = LinRegModel(slope=1, bias=1)

print("Model 1: \n")
print(model_1)
print("Model 2:")
print(model_2)
print("Model 3:")
print(model_3)

x_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
predictions_mode_1 = model_1.predict(x_list)
predictions_model_2 = model_2.predict(x_list)
predictions_model_3 = model_3.predict(x_list)

y_list = [4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
rmse_model_1 = rmse(predictions_mode_1, y_list)
rmse_model_2 = rmse(predictions_model_2, y_list)
rmse_model_3 = rmse(predictions_model_3, y_list)

print("\nRoot Mean Squared Error for Model 1:", rmse_model_1)
print("Root Mean Squared Error for Model 2:", rmse_model_2)
print("Root Mean Squared Error for Model 2:", rmse_model_3)