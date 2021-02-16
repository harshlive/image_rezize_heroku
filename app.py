from flask import Flask, redirect, url_for, request
import io
import base64
from PIL import Image

app = Flask(__name__)


@app.route("/", methods=['POST'])
def home():
    request_data = request.get_json()
    base64_str = request_data['url_string']
    buffer = io.BytesIO()
    imgdata = base64.b64decode(base64_str)
    img = Image.open(io.BytesIO(imgdata))
    # new_img = img.resize((400, 400))
    # new_img.save(buffer, format="PNG", quality=70)
    img.save(buffer, format="JPEG", quality=50)
    img_b64 = base64.b64encode(buffer.getvalue())
    return str(img_b64)[2:-1]
