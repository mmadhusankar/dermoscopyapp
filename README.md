# Skin-Lesion-Classifier
A classifier written in native Keras and converted to TensorFlow.js that can be used to classify seven different types of skin lesions.

This model uses the MobileNet architecture and was retrained on the HAM10000 dataset which contains approximately 10,000 documented images of skin lesions.
https://arxiv.org/abs/1803.10417

The goal of the project was to deploy the final model as a web application. The live version can be found at: https://dermoscopyapp.appspot.com/

The model obtains an accuracy of approximately 80%, with a top-3 accuracy of approximately 94%. 


    • Actinic Keratoses(akiecc)
      Actinic keratoses describes lesions on the outer skin layer caused by too much exposure to the ultraviolet rays of sunlight. They are also the beginnings of skin cancer, most often appearing after age 40. (WebMD)


    • Basal Cell Carcinoma(bcc)
      Basal cell carcinoma is a cancer that grows on parts of your skin that get a lot of sun. It's the least risky type of skin cancer and is unlikely to spread to other parts of your body. (WebMD)


    • Seborrheic Keratosis(bkl)
      Seborrheic keratoses are noncancerous skin growths that some people develop as they age. They often appear on the back or chest, but can occur on any part of the body. (WebMD)


    • Dermatofibroma(df)
      Dermatofibromas are harmless round, red-brownish skin growths that are most commonly found on the arms and legs. Dermatofibromas contains scar tissue and feel like hard lumps in the skin. (WebMD)


    • Malignant Melanoma(mel)
      Melanoma, the most serious type of skin cancer, develops in the cells (melanocytes) that produce melanin — the pigment that gives your skin its color. Melanoma can also form in your eyes and, rarely, in internal organs, such as your intestines. (MayoClinic)


    • Melanocytic Nevi(nv)
      Melanocytic nevi are benign neoplasms or hamartomas composed of melanocytes, the pigment-producing cells that constitutively colonize the epidermis. (eMedicine)


    • Vascular Lesions(vasc)
      The most common vascular lesions in childhood are the hemangiomas of infancy and, in adulthood, the cherry angiomas. Hemangiomas and angiomas are benign proliferations of blood vessels. (Dermoscopedia)


