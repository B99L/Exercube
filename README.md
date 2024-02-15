# Detection of Motion Anomalies with Transformer Autoencoders and Deep Embedded Clustering
**Type of Work Project:** Thesis in Data Science.   
**University:** ZHAW (Zurich University of Applied Sciences)
**Institute:** CAI (Centre for Artificial Intelligence)  
**Authors:**  Nevio Roccia & Bader Eddin Loukil  
**Date:** HS 2023  
**Supervisors:** Prof. Dr. Jasmina Bogojeska & Dr. Eveline Graf

#### Summary
This project thesis, titled "Detection of Motion Anomalies 
with Transformer Autoencoders and Deep Embedded Clustering"
focuses on detecting
anomalies in motion data. The data is captured during
a 25-minute training session in the Exercube, tracking
the position of hips, legs, and feet.
Our approach involves reading, processing,exploring,
and storing this data in a csv file using
[Data_Processing/](Data_Processing/),
and then reconstructing it using a model in [model.ipynb](model.ipynb).
We explored two architectures for the autoencoder:
a Transformer Autoencoder and
a Deep Embedded Clustering (DEC) model.
The key metrics for anomaly detection are 
the reconstruction error in the Transformer Autoencoder
and the silhouette score in the DEC model, both expected
to indicate significant changes in the motion data. 
However, the project could not conclusively
achieve this goal.

#### Repository Structure

[modules/](...): Includes multiple helper methods for reuse.     
[Data_Processing/](Data_Processing/): Processes incoming data and generates a Numpy array with all preprocessed data.  
[markers_reconstruction/](markers_reconstruction): The reconstruction of missing sensors on plates and those that were not mounted on plates.       
[model.ipynb](model.ipynb): Handles both model architecture (Tranformer-Autoencoder and DEC), compilation, training, evaluation, and result visualization.  

#### Goal
The aim of this project is to detect anomalies
in motion data by analyzing reconstruction error
and silhouette scores. The models used -
a Transformer Autoencoder and a Deep Embedded Clustering
(DEC) model - are trained on standard motion data.
An increase in reconstruction error and changes 
in silhouette scores are expected to indicate anomalous 
patterns in the data.


