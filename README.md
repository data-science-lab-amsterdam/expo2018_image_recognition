# Multi-label-Inception-net Image Classification
Modified `retrain.py` script to allow multi-label image classification using pretrained [Inception net](https://github.com/tensorflow/models/tree/master/research/inception).

The `label_image.py` has also been slightly modified to write out the resulting class percentages into `results.txt`. 

Detailed explanation of all the changes and reasons behind them: 
https://medium.com/@bartyrad/multi-label-image-classification-with-inception-net-cbb2ee538e30

### Overview
All code is found in the src folder and temporary files that are created in the tmp folder. 

Images should be self-supplied.

### Training
1. Make sure you have images in the correct folders. In more detail: under image_files in the correct folder (i.e. hat or no hat).
2. run 'python src/create_labels.py' to create labels. Make sure 'tmp/labels.txt' contains the correct labels (e.g. male/female) corresponding to the subdirectories of e.g. image_files/male and image_files/female
3. Copy images from image_files to a folder containing all images with this folder-structure images/multi-label/. This folder containing all images is used for training (in contrast to the above one which was used for labelling). 
4. If cropped images are prefered, use the 'src/crop_faces.py' script to create another directory containing these images. I use images-cropped/multi-label/ as the output folder for the crop_faces script. (Don't forget to change the image folder to be used in the retrain.sh script in this case!)
4. train the model by 'bash src/retrain.sh'

For training on new data or categories check under 'additional info'. For both, it helps if you clear the tmp folder. 

A helper function which can instantly provide you the class balance of labels is 'python src/class_balance.py'

note: we recognize having images in multiple locations is suboptimal. However since there was a time constraint on this project, structure optimzation was not a priority as much as actual results! 

#### Visualize training progress
After the retraining is done you can view the logs by running:

`tensorboard --logdir retrain_logs`

and navigating to http://127.0.0.1:6006/ in your browser.

#### Testing the trained model
Run: `python src/label_image.py <image_name>` from project root to check an individual prediction

Run: 'python src/testing_function.py <image_folder/>' to predict results for multiple test images (results are printed in 'tmp/results_testing_function.txt')


### Additional info
If you want to try the original Inception net retraining, here is an excellent CodeLab: https://codelabs.developers.google.com/codelabs/tensorflow-for-poets

If you want to add extra fotos:
1. Add these fotos to image_files groups (so that new labels can be created)
2. Add these fotos to images/multi-label so that they can be used for training. 

If you want to create new categories:
1. Create corresponding folders in image_files so that labels can be assigned based on folder name (e.g.: dark,light, no_hair).
2. Put correct images in each folder and also add these to images/multi-label/ so they can be used for training.
3. Make sure src/labels.txt contains correct labels you want to use. 
4. retrain as explained under 'training'.

#### License
Apache License, Version 2.0
