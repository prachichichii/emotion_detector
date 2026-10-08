\# **Real-Time Facial Emotion Detection**



A computer vision application for real-time facial emotion recognition using Python, OpenCV, DeepFace, and TensorFlow.



The application captures video from a connected camera, detects faces within the video stream, and analyzes facial expressions to estimate the subject's current emotional state.



\## Overview



The project combines conventional computer vision techniques with a deep-learning-based facial analysis framework.



OpenCV is used for camera access and face detection, while DeepFace performs facial emotion analysis using a TensorFlow-based backend.



The system produces an estimated emotion together with a confidence score for the detected face.



Example output:



```text

Emotion: happy

Confidence: 99.960106 %

```



\## Recognized Emotions



The underlying emotion recognition model supports the following categories:



\- Angry

\- Disgust

\- Fear

\- Happy

\- Sad

\- Surprise

\- Neutral



\## Technology Stack



| Component | Technology |

|---|---|

| Programming language | Python 3.11 |

| Computer vision | OpenCV |

| Facial analysis | DeepFace |

| Machine learning backend | TensorFlow |

| Face detection | Haar Cascade |

| Operating system | Windows |

| External camera | Camo-compatible camera devices |



\## Project Structure



```text

emotion\_detector/

│

├── main.py

├── camera\_test.py

├── haarcascade\_frontalface\_default.xml

├── haarcascade\_eye.xml

├── face\_1.png

├── test.png

├── .gitignore

└── README.md

```



\### File Description



\*\*`main.py`\*\*  

Main application responsible for facial emotion detection.



\*\*`camera\_test.py`\*\*  

Utility script used to verify camera access and video capture through OpenCV.



\*\*`haarcascade\_frontalface\_default.xml`\*\*  

Haar Cascade classifier used for frontal face detection.



\*\*`haarcascade\_eye.xml`\*\*  

Haar Cascade classifier for eye detection.



\*\*`.gitignore`\*\*  

Prevents the local Python virtual environment and generated Python files from being committed to the repository.



\## Requirements



\- Windows

\- Python 3.11

\- A working camera or compatible external camera

\- Internet access for initial package installation

\- Sufficient system resources for TensorFlow and DeepFace



\## Installation



\### 1. Clone the repository



Replace `YOUR-USERNAME` with the GitHub account that owns the repository.



```bash

git clone https://github.com/YOUR-USERNAME/emotion-detector.git

cd emotion-detector

```



\### 2. Create a virtual environment



```cmd

python -m venv venv311

```



\### 3. Activate the virtual environment



```cmd

venv311\\Scripts\\activate

```



After activation, the command prompt should indicate that the virtual environment is active.



\### 4. Install dependencies



```cmd

pip install tensorflow deepface opencv-python

```



If the required DeepFace dependencies are not installed automatically in your environment, install the TensorFlow backend explicitly:



```cmd

pip install "deepface\[tensorflow]"

```



\## Running the Application



Activate the virtual environment:



```cmd

venv311\\Scripts\\activate

```



Then start the application:



```cmd

python main.py

```



The application will attempt to access the configured camera, detect a face, and perform emotion analysis.



\## Camera Configuration



The application requires a camera that is accessible to Windows and OpenCV.



For systems without a built-in webcam, a smartphone can be used as an external camera. During development, an iPhone was connected to the Windows system using Camo.



The camera should be verified independently before running the emotion detection application.



To test camera access:



```cmd

python camera\_test.py

```



If the camera is accessible, the script should display the incoming video stream.



\## Processing Pipeline



The application follows this general processing pipeline:



```text

Camera Input

&#x20;    │

&#x20;    ▼

Video Frame

&#x20;    │

&#x20;    ▼

Face Detection

&#x20;    │

&#x20;    ▼

Detected Face

&#x20;    │

&#x20;    ▼

DeepFace Analysis

&#x20;    │

&#x20;    ▼

Emotion Classification

&#x20;    │

&#x20;    ▼

Emotion + Confidence Score

```



\## Model and Detection



Face detection is performed using OpenCV's Haar Cascade classifier.



Emotion classification is performed through DeepFace. The analysis is backed by TensorFlow and evaluates facial characteristics to estimate the most likely emotional category.



The reported confidence represents the model's confidence in its predicted classification and should not be interpreted as a definitive measurement of a person's actual emotional state.



\## Development Environment



The project was developed and tested using:



```text

Operating System: Windows

Python:           3.11

CPU:              Intel Core i5-12400

OpenCV:           5.0.0

TensorFlow:       2.21.0

DeepFace:         0.0.101

```



Package versions may differ depending on the environment in which the project is installed.



\## Virtual Environment



The Python virtual environment is intentionally excluded from version control.



A new environment should be created locally after cloning the repository rather than committing `venv311` to GitHub.



This keeps the repository smaller and avoids platform-specific binaries and installed packages being stored in source control.



\## Limitations



The system provides an estimate based on visible facial characteristics. Facial expressions do not necessarily correspond directly to a person's internal emotional state, and model predictions can be affected by factors such as:



\- Lighting conditions

\- Camera quality

\- Face orientation

\- Occlusion

\- Image resolution

\- Facial appearance

\- Multiple faces in the frame



The output should therefore be treated as a machine-learning prediction rather than a definitive assessment of emotional state.



\## License



No license has currently been specified for this project.



If this repository is intended for public reuse or distribution, an appropriate open-source license should be added.



\## Author



Emotion Detection



A computer vision project focused on real-time facial emotion recognition using Python and deep-learning-based facial analysis.

