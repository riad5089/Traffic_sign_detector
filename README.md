# Traffic_sign_detector
An image classification model from data collection, cleaning, model training, deployment and API integration.<br/>
The model can classify 18 different types of traffic_sign. <br/>
The types are following: <br/>
1. Construction Signs
 2. Hospital Signs
 3. Informational Signs
 4. Lane Control Signs
 5. Motorway Signs
 6. Parking Signs 
 7. Pedestrian Crossing Signs
 8. Priority Signs
 9. Pedestrian Signs 
 10. Prohibitory Signs
 11. Railroad  Signs
 12. Regulatory Signs
 13. Regulatory Signs for Bicycles
 14. Roundabout Signs
 15. School Zone Signs
 16. Speed Limit Signs
 17. Tourist Information Signs
 18. Warning Signs

 
# Dataset Preparation
 <b>Data Collection: </b> Images are downloaded using the duckduckgo.</br>
 <b>DataLoader : </b> DataLoader is created using the fastai DataBlock API to handle the dataset.</br>
 <b>Data Augmentation:</b> Using Fastai provides default data augmentation function that can be applied to images in order to increase dataset.</br>
 Details can be found in `Traffic sign detection_data_prep.ipynb`.
# Project Summary And Deployment
The recognition task i  experimented with three pre-trained models: ResNet-34, DenseNet-121, and ResNet-50, and evaluated their performance on two separate categories: 18 categories and 25 categories. After comparing the results, the results revealed that the ResNet-34 model achieved the highest accuracy of 81% when classifying images into the 18 predefined categories. Based on this result i deployed the ResNet-34 model with 18 categoriey for my project. I deployed the model to HuggingFace Spaces Gradio App. The implementation can be found in `app` folder or [here](https://huggingface.co/spaces/MdRiad/traffic_sign_recognizer).

 <img src="images/resnet_34_18.png" width=900 height=350>
 
# Training and Data Cleaning
<b>Training: </b>After multiple times fine-tuning with the ResNet-50 model on Category 18 signs got an accuracy of 81%.</br>
<b>Data Cleaning: </b>In the data collection process from the browser, there were many noise were encountered, including images that contained mixed categories, after undergoing multiple rounds of cleaning, the dataset was significantly reduced. However, it is important to note that the refinement process did not yield the desired level of improvement in model performance.


# API integration with GitHub Pages
The deployed model API is integrated [here](https://github.com/riad5089/Traffic_sign_detector) in GitHub Pages Website. Implementation and other details can be found in `docs` folder.

