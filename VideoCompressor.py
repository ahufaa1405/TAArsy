import cv2
import os

for files in os.listdir():
    if files.endswith('.mp4'):
      cap = cv2.VideoCapture(f'{files}')
      frame_w, frame_h = cap.get(3), cap.get(4)

      fourcc = cv2.VideoWriter_fourcc(*'XVID')
      out = cv2.VideoWriter(f'Converted/{files[:-4]}.avi', fourcc, 24.0, (int(frame_w//5.4), int(frame_h//5.4)))

      while cap.isOpened():
        ret, image = cap.read()
        if ret != True:
          break

        res = cv2.resize(image, (int(frame_w//5.4), int(frame_h//5.4)))
        out.write(res)
        if cv2.waitKey(1) & 0xFF == ord('q'):
          break

      cap.release()
      out.release() 
# cv2.destroyAllWindows()
