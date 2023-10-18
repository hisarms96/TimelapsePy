# https://github.com/hisarms96/TimelapsePy.git
#pip install flask
from flask import Flask, render_template, request, redirect, url_for
import cv2
import os
import time

app = Flask(__name)

# 촬영 간격(초) 및 기간(일)
interval_seconds = 30 * 60  # 30분 간격
duration_days = 5

# 저장할 이미지 폴더 경로
image_folder = 'images'

# 비디오 생성을 위한 설정
frame_width = 1920  # 비디오 프레임 너비
frame_height = 1080  # 비디오 프레임 높이
video_filename = 'timelapse.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(video_filename, fourcc, 20.0, (frame_width, frame_height)

# 촬영 중인지 여부
shooting = False

# 이미지 저장 경로가 없으면 생성
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
                # 이미지 촬영 및 저장 (실제 하드웨어에 맞게 코드 추가)
                time.sleep(interval_seconds)
                img = cv2.imread(image_filename)
                out.write(img)
        elif request.form.get('stop'):
            shooting = False
            out.release()
            print('타임랩스 비디오 생성이 완료되었습니다.')

    return render_template('index.html', shooting=shooting)

if __name__ == '__main__':
    app.run(debug=True)
