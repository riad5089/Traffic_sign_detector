# Traffic_sign_detector
An image classification model from data collection, cleaning, model training, deployment and API integration.<br/>
The model can classify 25 different types of traffic_sign. And deployed the model to HuggingFace Spaces Gradio App. <br/>
The types are following: <br/>
1. Regulatory Signs
 2. Warning Signs
 3. Informational Signs
 4. Construction Signs
 5. School Zone Signs
 6. Regulatory Signs for Bicycles
 7. Railroad Signs
 8. Pedestrian Signs
 9. Motorway Signs
 10. Speed Limit Signs
 11. Priority Signs
 12. Lane Control Signs
 13. Destination Signs
 14. Roundabout Signs
 15. Parking Signs
 16. Hospital Signs
 17. Tourist Information Signs
 18. No Left Turn Signs
 19. No Right Turn Signs
 20. No Passing Zone Signs
 21. Road Narrows Signs
 22. Yield Signs
 23. Low Clearance Signs
 24. Traffic Signal Ahead Signs
 25. Detour Signs

# Dataset Preparation
 <b>Data Collection: </b> Images are downloaded using the duckduckgo.</br>
 <b>DataLoader : </b> DataLoader is created using the fastai DataBlock API to handle the dataset.</br>
 <b>Data Augmentation:</b> Using Fastai provides default data augmentation function that can be applied to images in order to increase dataset.

# Project Summary And Deployment
The recognition task is accomplished by leveraging three pretrained models: ResNet-34, DenseNet-121, and ResNet-50.The project focuses on two specific categories like 18 and 25 categories. The Summary of models and categories describe in below:

 <b>1. ResNet-34</b></br>
 
 `For 18 Categories`: After multiple times data cleaning and fine-tuning with the ResNet-34 model on Category 18 signs got an accuracy of 81%. The implementation can be found in [here](https://huggingface.co/spaces/MdRiad/traffic_sign_recognizer).
 
 <img src="images/resnet_34_18.png" width=900 height=350>

 `For 25 Categories`: After multiple times data cleaning and fine-tuning with the ResNet-34 model on Category 25 signs got an accuracy of 80%. The implementation can be found in [here](https://huggingface.co/spaces/MdRiad/traffic_sign_recognizer_resnet34_25cat).
 
<img src="images/traffic_sign_resnet34_25_cat.png" width=900 height=350>

I deployed the model to HuggingFace Spaces Gradio App. The implementation can be found in `app` folder or [here](https://huggingface.co/spaces/MdRiad/traffic_sign_recognizer).

<img src="images/resnet_34_18.png" width=900 height=400>

<b>1. DenseNet-121</b></br>
`For 18 Categories`: After multiple times data cleaning and fine-tuning with the ResNet-34 model on Category 18 signs got an accuracy of 81%.
# API integration with GitHub Pages
The deployed model API is integrated [here](https://github.com/riad5089/Traffic_sign_detector) in GitHub Pages Website. Implementation and other details can be found in `docs` folder.
