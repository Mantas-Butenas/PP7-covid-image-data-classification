from fastai.vision.all import *

# Load the trained model
learn = load_learner('path_to_your_model.pkl')

# Function to classify an image
def classify_image(image_path):
    # Classify the image using the trained model
    pred, pred_idx, probs = learn.predict(image_path)
    print(f"Prediction: {pred}; Probability: {probs[pred_idx]:.4f}")

# negative case
image_path = 'path_to_your_image.jpg'
classify_image(image_path)
