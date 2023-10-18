# https://github.com/hisarms96/TimelapsePy.git
#pip install flask
from flask import Flask, render_template, request, redirect, url_for
import cv2
import os
import time

app = Flask(__name)

# �Կ� ����(��) �� �Ⱓ(��)
interval_seconds = 30 * 60  # 30�� ����
duration_days = 5

# ������ �̹��� ���� ���
image_folder = 'images'

# ���� ������ ���� ����
frame_width = 1920  # ���� ������ �ʺ�
frame_height = 1080  # ���� ������ ����
video_filename = 'timelapse.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(video_filename, fourcc, 20.0, (frame_width, frame_height)

# �Կ� ������ ����
shooting = False

# �̹��� ���� ��ΰ� ������ ����
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

@app.route('/', methods=['GET', 'POST'])
def index():
    global shooting

    if request.method == 'POST':
        if request.form.get('start'):
            shooting = True
            start_time = time.time()
            while shooting:
                timestamp = time.time() - start_time
                image_filename = f'{image_folder}/{int(timestamp)}.jpg'
                # �̹��� �Կ� �� ���� (���� �ϵ��� �°� �ڵ� �߰�)
                time.sleep(interval_seconds)
                img = cv2.imread(image_filename)
                out.write(img)
        elif request.form.get('stop'):
            shooting = False
            out.release()
            print('Ÿ�ӷ��� ���� ������ �Ϸ�Ǿ����ϴ�.')

    return render_template('index.html', shooting=shooting)

if __name__ == '__main__':
    app.run(debug=True)
