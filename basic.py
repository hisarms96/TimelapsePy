# https://github.com/hisarms96/TimelapsePy.git
import cv2
import os
import time

# 촬영 간격(초) 및 기간(일)
interval_seconds = 30 * 60  # 30분 간격
duration_days = 5

# 저장할 이미지 폴더 경로
image_folder = 'images'

# 이미지 저장 경로가 없으면 생성
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# 비디오 생성을 위한 설정
frame_width = 1920  # 비디오 프레임 너비
frame_height = 1080  # 비디오 프레임 높이
video_filename = 'timelapse.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(video_filename, fourcc, 20.0, (frame_width, frame_height))

# 촬영 시작 시간
start_time = time.time()

# 타임랩스 생성
for day in range(1, duration_days + 1):
    for hour in range(0, 24):
        for minute in range(0, 60):
            timestamp = time.time() - start_time
            image_filename = f'{image_folder}/{day:02d}_{hour:02d}_{minute:02d}.jpg'
            
            # 이미지 촬영 및 저장
            # 실제로 카메라를 사용하여 이미지를 촬영하는 코드를 추가해야 합니다.
            # 여기서는 이미지를 만들지 않고 파일명만 출력합니다.
            print(f'Saved: {image_filename}')

            # 이미지를 비디오에 추가
            img = cv2.imread(image_filename)
            out.write(img)

            # 촬영 간격만큼 대기
            time.sleep(interval_seconds)

# 비디오 파일 닫기
out.release()

print('타임랩스 비디오 생성이 완료되었습니다.')
