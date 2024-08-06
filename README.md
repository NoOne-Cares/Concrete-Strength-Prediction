# Concrete Strength Prediction using Machine Learning

This repository contains the code and resources for predicting the compressive strength of concrete using machine learning techniques. The project includes data preprocessing, model development, and evaluation using both regression and neural network models.

## Table of Contents
1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Data](#data)
4. [Models](#models)
5. [Results](#results)
6. [Discussion](#discussion)
7. [Conclusion](#conclusion)
8. [Dependencies](#dependencies)

## Introduction

Concrete is a widely used building material, and its compressive strength is a crucial parameter for ensuring structural integrity. Traditional methods for determining concrete strength involve physical testing, which can be time-consuming and costly. This project explores the application of machine learning to predict concrete strength based on its composition, providing a more efficient and cost-effective solution.

## Project Structure


## Data

The dataset used in this project contains records of concrete mix designs and their corresponding compressive strength values. The key features in the dataset include:

- Cement Content (kg/m³)
- Superplasticizer (kg/m³)
- Blast furnace slag (kg/m³)
- Fly Ash (kg/m³)
- Water (kg/m³)
- Coarse Aggregate (kg/m³)
- Fine Aggregate (kg/m³)
- Age (days)
- Compressive Strength (MPa)

## Models

The project involves the development of two primary models:

1. **Regression Model:**
   - Uses a Voting Regressor, which combines multiple regression techniques (linear regression, Lasso, decision trees) to predict concrete strength.
   - Performance metrics: 
     - Mean Absolute Error (MAE): 3.3248 MPa
     - Mean Squared Error (MSE): 25.7350 MPa²
     - R-squared (R²): 0.9125

2. **Neural Network Model:**
   - A neural network with 3 layers, trained with 2000 epochs and a batch size of 150.
   - Performance metrics:
     - Mean Absolute Error (MAE): 4.0887 MPa
     - Mean Squared Error (MSE): 47.4282 MPa²
     - R-squared (R²): 0.8159

## Results

The regression model demonstrated superior performance compared to the neural network model. The R-squared value of 0.9125 indicates that the regression model explains 91.2% of the variance in the concrete strength data, making it a highly effective predictive tool.

## Discussion

### Overview of Model Performance
This project aimed to predict concrete compressive strength using machine learning, focusing on a regression model and a neural network. The results underscore the potential of these techniques but also highlight their respective strengths and limitations.

### Regression Model
The Voting Regressor performed well with an R-squared of 0.9125, indicating it explains 91.2% of the variance in concrete strength. With a Mean Absolute Error (MAE) of 3.3248 MPa and Mean Squared Error (MSE) of 25.7350 MPa², the model effectively predicts strength by integrating multiple regression algorithms. This ensemble approach enhances robustness and reduces overfitting.

### Neural Network Model
The neural network achieved an R-squared of 0.8159, explaining 81.6% of the variance. However, it showed lower accuracy with an MAE of 4.0887 MPa and MSE of 47.4282 MPa². Performance may be limited by model complexity, insufficient training data, and potential overfitting. The network's architecture and training parameters might need further optimization.

### Comparison and Practical Implications
The regression model outperformed the neural network in accuracy and computational efficiency. Its simpler nature allows for faster training, making it more practical for real-time applications. Nevertheless, with additional data and tuning, the neural network could become more competitive, especially in scenarios involving complex, non-linear feature interactions.

### Limitations and Future Work
**Limitations:**
- Data Quality and Quantity: The dataset may not cover all concrete mix scenarios.
- Feature Engineering: More advanced techniques could improve performance.

**Future Work:**
- Model Tuning: Further adjustments to the neural network could enhance its accuracy.
- Data Expansion: Including more diverse samples would improve model robustness.
- Advanced Algorithms: Exploring other machine learning techniques might enhance predictive capabilities.

## Conclusion
This project effectively demonstrated the use of machine learning to predict concrete compressive strength. The Voting Regressor proved highly effective and efficient, while the neural network showed potential with room for improvement. These findings highlight machine learning's ability to optimize concrete mixtures and contribute to safer, more efficient construction practices. Future developments could lead to more accurate and versatile predictive models in civil engineering.

## Dependencies

The project requires the following Python packages:

- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- tensorflow

## Project Members
- Sourav Das
- Masoom Sahu
- Aditya Ranjan
- Suman Das
- Rupsnigdha Kashyap
- Chayan Gulgulia 

