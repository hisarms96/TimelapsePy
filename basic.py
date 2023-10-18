# https://github.com/hisarms96/TimelapsePy.git
import cv2
import os
import time

# �Կ� ����(��) �� �Ⱓ(��)
interval_seconds = 30 * 60  # 30�� ����
duration_days = 5

# ������ �̹��� ���� ���
image_folder = 'images'

# �̹��� ���� ��ΰ� ������ ����
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# ���� ������ ���� ����
frame_width = 1920  # ���� ������ �ʺ�
frame_height = 1080  # ���� ������ ����
video_filename = 'timelapse.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(video_filename, fourcc, 20.0, (frame_width, frame_height))

# �Կ� ���� �ð�
start_time = time.time()

# Ÿ�ӷ��� ����
for day in range(1, duration_days + 1):
    for hour in range(0, 24):
        for minute in range(0, 60):
            timestamp = time.time() - start_time
            image_filename = f'{image_folder}/{day:02d}_{hour:02d}_{minute:02d}.jpg'
            
            # �̹��� �Կ� �� ����
            # ������ ī�޶� ����Ͽ� �̹����� �Կ��ϴ� �ڵ带 �߰��ؾ� �մϴ�.
            # ���⼭�� �̹����� ������ �ʰ� ���ϸ� ����մϴ�.
            print(f'Saved: {image_filename}')

            # �̹����� ������ �߰�
            img = cv2.imread(image_filename)
            out.write(img)

            # �Կ� ���ݸ�ŭ ���
            time.sleep(interval_seconds)

# ���� ���� �ݱ�
out.release()

print('Ÿ�ӷ��� ���� ������ �Ϸ�Ǿ����ϴ�.')
