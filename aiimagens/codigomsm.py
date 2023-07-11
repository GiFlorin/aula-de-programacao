import tensorflow as tf
import numpy as np
from tensorflow.keras.applications import imagenet_utils
from tensorflow.keras.preprocessing import image

# Carregar o modelo pré-treinado
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Carregar a imagem de teste
image_path = 'cadeira.jpg'
img = image.load_img(image_path, target_size=(224, 224))
x = image.img_to_array(img)
x = tf.keras.applications.mobilenet_v2.preprocess_input(x)
x = np.expand_dims(x, axis=0)

# Fazer a previsão usando o modelo
preds = model.predict(x)
results = imagenet_utils.decode_predictions(preds, top=5)[0]

# Exibir os resultados
print('Resultados:')
for result in results:
    print(f'{result[1]}: {result[2]*100}%')
