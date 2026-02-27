import matplotlib.pyplot as plt
import numpy as np


def plot_predictions(y_true, y_pred):
    """Plot the true vs predicted values."""
    plt.figure(figsize=(10, 6))
    plt.plot(y_true, label='True Values', color='blue')
    plt.plot(y_pred, label='Predicted Values', color='red', linestyle='--')
    plt.title('True vs Predicted Values')
    plt.xlabel('Sample Index')
    plt.ylabel('Value')
    plt.legend()
    plt.grid()
    plt.show()


def evaluate_model(y_true, y_pred):
    """Evaluate the model's performance using MSE and R2 score."""
    from sklearn.metrics import mean_squared_error, r2_score
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return {'MSE': mse, 'R2 Score': r2}
