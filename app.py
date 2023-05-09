import os
import subprocess
import random
import string
import requests
from flask import Flask, request, send_file

app = Flask(__name__)


def getFilename(s):
    new_file_name = ''
    if all(x in s for x in ['/', '.']):
        return s.split('/')[-1]
    else:
        return 'raw.bin'
# Create your views here.
@app.route('/', methods=["GET"])
def index():
    # Get URL to download from
    url = request.args.get("url", default="")
    password = request.args.get("password", default="")
    if not url:
        return
    if not password:
        password = "1234"
    # Generate
    uid = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    enc_name = uid + '.zip'
    # Download raw file
    raw_name = getFilename(url)
    r = requests.get(url, allow_redirects=True)
    f = open(raw_name, 'wb')
    f.write(r.content)
    f.close()

    # Encrypt raw file
    subprocess.Popen(['zip', '-P', password, enc_name, raw_name]).wait()

    # Delete raw file
    subprocess.Popen(['rm', raw_name]).wait()

    # Read encrypted file
    f = open(enc_name, 'rb')
    size = os.path.getsize(enc_name)
    data = f.read()
    f.close()
    # Delete encrypted file after reading contents into memory
    subprocess.Popen(['rm', enc_name]).wait()

    # Return encrypted file

    return send_file(data, as_attachment=True, download_name=enc_name)
