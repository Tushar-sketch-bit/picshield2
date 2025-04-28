from flask import Flask,request,send_file,render_template,Request,jsonify,redirect,url_for,flash
from steganography import encoded_img
import os
import numpy as np
from steganography import embed_data
from database import log_access
import datetime
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Goes up to /picshield2/
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")      # /picshield2/frontend/
HTML_DIR = os.path.join(FRONTEND_DIR, "html")  




app=Flask(__name__,
          template_folder=os.path.join(FRONTEND_DIR, "html"),
          static_folder=os.path.join(FRONTEND_DIR, "static"))
app.secret_key="tushar99"

          
UPLOAD_FOLDER='../uploads'
OUTPUT_FOLDER='../outputs'


os.makedirs(UPLOAD_FOLDER,exist_ok=True)
os.makedirs(OUTPUT_FOLDER,exist_ok=True)


#home page
@app.route('/',methods=['GET'])
def index():
    return render_template('upload.html')


#user uploads image
@app.route('/upload',methods=['POST'])
def upload():
    if 'image' not in request.files:
        flash('no image selected','error')
        return redirect(url_for('home'))
    img = request.files['image']
    if img.filename=='':
        flash('no image selected','error')
        return redirect(url_for('home'))
        
    uploaded_path=os.path.join(UPLOAD_FOLDER,img.filename)
    img.save(uploaded_path)
    flash('image uploaded succesfully!','success')
    
    tracking_data=f"IP:{request.remote_addr} | date,time:{datetime.date,datetime.time}"
    output_filename=f"encoded_{img.filename}"
    output_path=os.path.join(OUTPUT_FOLDER,output_filename)
    
    # 3. Save encoded image
    encoded_img(uploaded_path,tracking_data,output_path)
    
    
    return redirect(url_for('download',filename=output_filename))

#@app.route('/encoded/<image_id>')
def serve_image(image_id):
    # 4. Log access when someone views the image
    log_access(image_id, request.remote_addr)
    return send_file(f'encoded_{image_id}.png')

@app.route('/downloads/<filename>',methods=['GET'])
def download_img(filename):
    return send_file(
        os.path.join(OUTPUT_FOLDER,filename),
        as_attachment=True,
        download_name=filename
    )
    
    


if __name__=='__main__':
    app.run(debug=True)























