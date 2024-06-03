
# coding: utf-8

# In[ ]:


import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import ImageDataGenerator

def predict():

    model = load_model('ML/model_dummy_test.hdf5')
    
    # Load and preprocess the test image
    img_path = 'media/input/test/test.jpg'
    img = image.load_img(img_path, target_size=(200, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    
    # Make prediction
    pred = model.predict(x)
    print(pred)

    predicted_class_indices = np.argmax(pred, axis=1)
    print(predicted_class_indices)
    
    label = [
        'Alpinia Galanga (Rasna)', 
        'Amaranthus Viridis (Arive-Dantu)', 
        'Azadirachta Indica (Neem)', 
        'Ficus Religiosa (Peepal Tree)',
        'Mentha (Mint)',
        'Moringa Oleifera (Drumstick)',
        'Ocimum Tenuiflorum (Tulsi)',
        'Piper Betle (Betel)',
        'Pongamia Pinnata (Indian Beech)',
        'Psidium Guajava (Guava)'
    ]
    print(label[predicted_class_indices[0]])
    
    return label[predicted_class_indices[0]]