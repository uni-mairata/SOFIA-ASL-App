import cv2
import threading
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


# -----------------------------
# Camera widget using OpenCV
# -----------------------------
class CameraWidget(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.capture = cv2.VideoCapture(0)  # USB camera
        self.running = True

        # Start camera thread
        threading.Thread(target=self.update_camera, daemon=True).start()

    def update_camera(self):
        while self.running:
            ret, frame = self.capture.read()
            if ret:
                # Convert BGR → RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                buf = frame.tobytes()

                # Create texture
                texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='rgb')
                texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')

                # Update UI on main thread
                Clock.schedule_once(lambda dt: self.update_texture(texture))

    def update