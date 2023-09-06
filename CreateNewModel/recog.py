import cv2
import time

# Khởi tạo camera
cap = cv2.VideoCapture(0)

# Thiết lập thông số videoq
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 30  # Số khung hình trên giây
video_duration = 1  # Thời lượng video (giây)
pause_duration = 2  # Thời gian dừng giữa các video (giây)

# Thiết lập codec và writer để ghi videoq
fourcc = cv2.VideoWriter_fourcc(*'XVID')

for i in range(45, 55):
    # Tạo tên file video
    video_name = f'metmoi_{i}.avi'

    # Khởi tạo writer để ghi video
    out = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

    # Quay video trong thời lượng đã cho
    start_time = time.time()
    while (time.time() - start_time) < video_duration:
        ret, frame = cap.read()

        # Ghi khung hình vào video
        out.write(frame)
        cv2.putText(frame, f"video: {i}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        # Hiển thị khung hình trong cửa sổ
        cv2.imshow('Recording', frame)
          # Hiển thị số giây trên khung hình
        

        # Thoát nếu nhấn phím 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Giải phóng writer
    out.release()

    # Dừng lại giữa các video

    start_time = time.time()
    while (time.time() - start_time) < pause_duration:
        ret, frame = cap.read()

        # Ghi khung hình vào video
        # out.write(frame)
        cv2.putText(frame, f"pausing", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        # Hiển thị khung hình trong cửa sổ
        cv2.imshow('Recording', frame)
          # Hiển thị số giây trên khung hình
        

        # Thoát nếu nhấn phím 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Giải phóng tài nguyên camera và đóng cửa sổ
cap.release()
cv2.destroyAllWindows()
