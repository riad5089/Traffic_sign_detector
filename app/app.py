from fastai.vision.all import load_learner
# import pathlib 
# temp=pathlib.PosixPath
# pathlib.PosixPath=pathlib.WindowsPath

import gradio as gr
traffic_sign_labels=(


 'Construction Signs',
  'Hospital Signs',
  'Informational Signs',
  'Lane Control Signs',
  'Motorway Signs',
  'Parking Signs',
  'Pedestrian Crossing Signs',
  'Pedestrian Signs',
  'Priority Signs',
  'Prohibitory Signs',
  'Railroad Signs',
  'Regulatory Signs',
  'Regulatory Signs for Bicycles',
  'Roundabout Signs',
  'School Zone Signs',
  'Speed Limit Signs',
  'Tourist Information Signs',
  'Warning Signs'
  )
model = load_learner("models/traffic_sign-recognizer-v3.pkl")

def recognize_image(image):
   pred, idx, probs = model.predict(image)
   return dict(zip(traffic_sign_labels, map(float, probs)))

#!export
image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label()
examples = [
    'test_images/download (2).png',
    'test_images/download (3).jpg',
    'test_images/download.png',
    'test_images/download (4).jpg'
    ]

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=True)