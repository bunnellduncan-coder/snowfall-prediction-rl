# main.py

"""Orchestrates training and prediction for the Snowfall Prediction RL model."""

import train_module  # Assuming train_module handles the training of the model
import predict_module  # Assuming predict_module handles predictions


def main():
    # Step 1: Train the model
    print("Starting training...")
    model = train_module.train_model()  # Train the model and get the trained model object
    print("Training completed!")

    # Step 2: Make predictions
    print("Starting prediction...")
    predictions = predict_module.make_predictions(model)  # Make predictions using the trained model
    print("Predictions completed!")

    # Step 3: Output results
    print("Predictions:", predictions)


if __name__ == "__main__":
    main()