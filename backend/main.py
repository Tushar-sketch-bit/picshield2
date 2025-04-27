from flask import Flask,request,send_file,render_template,Request,jsonify
from steganography import encoded_img
import os
import numpy as np
from werkzeug.utils import secure_filename
from encoding import iterate_over_images



app=Flask(__name__)
UPLOAD_FOLDER='../uploads'
OUTPUT_FOLDER='../outputs'
os.makedirs(UPLOAD_FOLDER,exist_ok=True)
os.makedirs(OUTPUT_FOLDER,exist_ok=True)


#home page
@app.route('/')
def index():
    return render_template('home.html')


#user uploads image
@app.route('/upload',methods=['POST'])
def upload():
    if 'image' not in request.files:
      return "no image selected"
  
    image=request.files['image']
    if image.filename=='':
        return "no selected file"
    
    save_path=os.path.join(UPLOAD_FOLDER,image.filename)
    image.save(save_path)
    
    return f"image saved"
    
    
#then it goes in encoding    
@app.route('/encode',methods=['POST'])
def encode_image():
    if 'image' not in Request.files:
        return jsonify({'error': 'no image file provided'}), 400
                       
    image_file=Request.files['image']
    message=Request.form.__get__('message','')
    
    image_path=os.path.join(UPLOAD_FOLDER,image_file.filename)
    image_file.save(image_path)
    output_image_path=os.path.join(OUTPUT_FOLDER, 'encoded_'+image_file.filename)
    if message== None :
        message=np.random.rand(3,3)
        
    encoded_img(image_path,message,output_image_path)
    return send_file(output_image_path,mimetype='image/png')




if __name__=='__main__':
    app.run(debug=True)























