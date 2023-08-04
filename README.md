# Car Crash Classification using a Convolutional Neural Network

## Requirements
Python (>=3.6)
TensorFlow (>=2.0) or other compatible deep learning frameworks
Jupyter Notebook (for running the provided notebooks)


## Introduction
This repository contains code and resources for a deep learning model that utilizes a CNN to 
classify between authentic car crash photographs and stable diffusion generated images, 
helping to identify potential deceptive or misleading content.

## Dataset
The dataset used to train and evaluate the model consists of two categories: "Real" and "Fake." 
> Real: The real car crash images were obtained from a publicly available dataset on Kaggle. The Kaggle dataset contains a collection of authentic car crash photographs from various sources, ensuring diversity in real-world scenarios.

> Fake: The stable diffusion generated images were obtained using Playground AI and OpenArt AI platforms. 
These platforms leverage artificial intelligence to create synthetic car crash images, simulating potential scenarios.
The data cleaning process involved using the datacleaning.py script, which was responsible for renaming and reformatting all images to JPEG.

The dataset comprises a total of 116 real car crash images and 116 AI-generated car crash images.
To ensure a proper evaluation of the model, a standard 80-10-10 split was employed. 
Specifically, the dataset was divided into 80% for training, 10% for validation, and 
10% for testing the model's performance.

## Model Architecture
The deep learning model employs a CNN architecture to learn and classify the input images effectively. 
The model is a Convolutional Neural Network (CNN) with three convolutional layers, 
each followed by a max-pooling layer. It has a fully connected layer with ReLU activation, 
and the final output layer uses the sigmoid function for binary classification between real and AI-generated car crashes.

## Limitations
Due to a limited dataset gathering time (16 hrs), our model faced overfitting issues since it 
lacked diverse samples for training. Consequently, it achieved an accuracy of 72% for fake images 
and 91% for real images. A larger and more diverse dataset is needed to improve the model's 
generalization and overall performance.

