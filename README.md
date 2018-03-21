# car-damage-evaluation-using-deep-learning

## Using deep learninig and computer-vision to classify damaged cars and making a simple web app using flask and bootstrap

Created a web-app to take input as images from an user and to classify those images as damaged(**multiclass** i.e. minor,moderate and severe). Given less data which was scarped from google images using **selenium(script uploaded in the code directory)**, the model performed well(comparable to an avg human). All the models related figure i.e. accuracy,precision,recall is reported in the pdf. We trained a pipeline of **convolution neural networks(CNN) model** using **transfer learning** on pretrained vgg16 model(i.e. removing it's fully top-connected layer) using keras and tensorflow.

Web app - [Car Damage Evaluation]() Updating later...

Get the data and pretrained models and more from this [drive link](https://drive.google.com/drive/folders/1cCOxtyycmNX8hZjmmre1qHSQU76G6hLR?usp=sharing) 

Get the updated model in json format from [here](https://github.com/halloTheCoder/web-app/tree/master/static/models)
