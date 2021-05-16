
# How to Integrate Dataset Quality Metrics And Flywheel in MLOps Pipeline 

# ( Demonstration using License Plate Recognition App )
![Viewer](static/P21.png)
### Authors

[Changsin lee](https://www.linkedin.com/), [Mahavir Dwivedi](https://www.linkedin.com/in/mahavir-dwivedi/)

## Introduction
As we know that an AI system involves two major pillars, one is code(model + algorithm) and the other is data. In a recent [interview]((https://panel.holoviz.org/reference/panes/HoloViews.html)) Andrew Ng mentioned the importance of high quality data.
Through this project we would like to focus on the data aspect of an AI system.
The project aims to demonstrate the improvement in model performance using Data Quality Metrics and Data Flywheel concept.
![Viewer](static/flywheel.png)

### Data Quality Metric

### Repository Structure
Training code can be found in training directory.
Notebooks used can be found in notebooks directory.
License Plate Recognition app in license_plate_recogniser directory.

### License Plate Recognition Application (LPR)

To use LPR application install docker app. 
Clone the repository and go inside the license_plate_recogniser directory, build the docker image using command:
docker build --network host -t lpr:latest .

To start the container run.
docker run -it --network host -p 8080:8080 lpr

Now visit your browser and access the url:
localhost:8080

You should be at this page:
![Viewer](static/prediction.png)
