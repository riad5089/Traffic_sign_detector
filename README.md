# Traffic_sign_detector
An image classification model from data collection, cleaning, model training, deployment and API integration.<br/>
The model can classify 18 different types of traffic_sign. And deployed the model to HuggingFace Spaces Gradio App. <br/>
The types are following: <br/>
1. Construction Signs
 2. Hospital Signs
 3. Informational Signs
 4. Lane Control Signs
 5. Motorway Signs
 6. Parking Signs 
 7. Pedestrian Crossing Signs
 8. Pedestrian Signs
 9. Priority Signs
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
 <b>Data Augmentation:</b> Using Fastai provides default data augmentation function that can be applied to images in order to increase dataset.

# Project Summary And Deployment
The recognition task i  experimented with three pre-trained models: ResNet-34, DenseNet-121, and ResNet-50, and evaluated their performance on two separate categories: 18 categories and 25 categories. After comparing the results, the results revealed that the ResNet-34 model achieved the highest accuracy of 81% when classifying images into the 18 predefined categories. Based on this result i deployed the ResNet-34 model with 18 categoriey for my project.



# API integration with GitHub Pages
The deployed model API is integrated [here](https://github.com/riad5089/Traffic_sign_detector) in GitHub Pages Website. Implementation and other details can be found in `docs` folder.
