import tensorflow as tf

def evaluate_model(model, test_data):
    results = model.evaluate(test_data)
    print("Test Loss, Test Accuracy:", results)
    return results
