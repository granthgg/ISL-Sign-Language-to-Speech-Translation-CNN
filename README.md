# ISL SIGN LANGUAGE TO SPEECH TRANSLATION CNN

## Overview
This project aims to translate Indian Sign Language (ISL) into speech using Convolutional Neural Networks (CNN). It is designed to bridge the communication gap between the deaf and hearing communities by converting sign language gestures into audible speech.

<div>
<img src="https://github.com/granthgg/ISL-Sign-Language-to-Speech-Translation-CNN/assets/69439823/f3a0868a-5b17-4c24-984b-7b55b6a48622" width="320" height="295"/>&nbsp; 
<img src="https://github.com/granthgg/ISL-Sign-Language-to-Speech-Translation-CNN/assets/69439823/8c5ae02a-677d-402b-8292-91cb210680ae" width="320" height="295"/>&nbsp; 
<img src="https://github.com/granthgg/ISL-Sign-Language-to-Speech-Translation-CNN/assets/69439823/adb8f618-3be9-4666-b80a-2ff5a9c94162" width="320" height="295"/>&nbsp;
<img src="https://github.com/granthgg/ISL-Sign-Language-to-Speech-Translation-CNN/assets/69439823/aff9137b-1bed-4320-84a6-49e104276031" width="320" height="295"/>&nbsp; 
<div>


## Features
- **Data Preprocessing**: Scripts for preparing and augmenting the ISL dataset for training.
- **Model Training**: A Jupyter Notebook (`Training.ipynb`) detailing the process of training the CNN model on the ISL dataset.
- **Application**: A Python application (`Application.py`) for real-time sign language translation to speech.
- **Model Files**: Pre-trained model files (`ISL_1.h5`, `model-bw.h5`, and `model-bw.json`) for quick deployment and testing.

## Project Structure
- `data/`: Contains the ISL dataset organized by letters (A-Z) for training.
- `Model/`: Directory for storing model architecture and weights.
- `Application.py`: The main application script for translating ISL to speech.
- `Image_Check.py`, `Image_Create.py`, `Image_Move.py`, `Image_Preprocessing.py`, `Processing.py`: Utility scripts for image processing and data preparation.
- `Training.ipynb`: Jupyter Notebook for training the CNN model.

## Getting Started
1. **Clone the Repository**
2. **Install Dependencies**
- Ensure Python 3.x is installed.
- Install required Python packages:
  ```
  pip install -r requirements.txt
  ```
(Note: The `requirements.txt` file is assumed to be present or you may need to install dependencies based on the scripts.)

3. **Prepare the Dataset**
- Use the scripts in the root directory to preprocess and organize the ISL dataset.

4. **Train the Model**
- Open `Training.ipynb` in Jupyter Notebook or JupyterLab and follow the instructions to train the model.

5. **Run the Application**
- Execute `Application.py` to start the ISL to speech translation application.

## Contributing
Contributions to improve the project are welcome. Please follow the standard fork-and-pull request workflow.

