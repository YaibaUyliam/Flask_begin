import numpy as np
from flask import Flask, request, render_template
import utils
import os
import cv2
import imagenet

model = utils.load_model()
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static"

@app.route('/', methods=['GET', 'POST'])
def main_display():
    if request.method == "POST":
        try:
            image = request.files['file']
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
            
            if image:
                #img = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
                # Convert sang dạng array image
                #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                #print(img.shape)
                image_rz = utils._preprocess_image(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
                # Dự báo phân phối xác suất
                dist_probs = model.predict(image_rz)
                # argmax 5             
                argmax_k = np.argsort(dist_probs[0])[-1]
                #print(dist_probs[0][argmax_k])
                # classes
                kq = imagenet.classes[argmax_k]
	
                return render_template("giaodien.html", user_image = image.filename,
                                           msg="Tải file lên thành công", extra=kq)
                

            else:
                return render_template("giaodien.html", msg="Hãy chọn file để tải lên")
        except Exception as ex:
            # Nếu lỗi thì thông báo
            print(ex)
            return render_template('giaodien.html', msg='Không nhận diện được khuôn mặt')

    else:
        return render_template('giaodien.html')       

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
