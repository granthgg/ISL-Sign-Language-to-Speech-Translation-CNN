# ISL Sign Language to Speech Translation CNN

## Overview
This project aims to translate Indian Sign Language (ISL) into speech using Convolutional Neural Networks (CNN). It is designed to bridge the communication gap between the deaf and hearing communities by converting sign language gestures into audible speech.

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

## License
This project is open-sourced under the MIT License. See the LICENSE file for more details.
