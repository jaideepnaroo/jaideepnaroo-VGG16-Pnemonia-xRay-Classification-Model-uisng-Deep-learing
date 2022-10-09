To classify the images, i have used VGG16. The code is created and executed in JUPYTER notebook.
1. Used the X ray Pnemonia Dataset from Kaggle.
2. uploaded the input file and extracted the data in input_data.
3. Split the folders in 8:1:1 ratio as train, test and val, and saved the folders in datasets folder.
4. Developed the Classification model with VGG16
5. install the requirements.
6. Used the pretrained classification weights of VGG16 of imagenet.
7. vgg = VGG16(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top= False)
   using the above command, weights is initiated.
8. Use the acitvation Code in repo to use for predictionT
9. Test data is predicted , according to the results.
10. All the results are downloaded and saved.
12. he results are saved in runs/exp/weights.
11. You can also download the model that i have trained on my machine. from drive link

https://drive.google.com/file/d/1K73pawWY2M6KUp4qlPebHcQgLWNZQoLV/view?usp=sharing