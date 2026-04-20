from kivy.config import Config
# Enable fullscreen before Kivy loads
# Config.set('graphics', 'fullscreen', 'auto') # TODO: UNCOMMENT THIS AFTER DONE DESIGNING UI
# Config.set('graphics', 'borderless', '1') # TODO: UNCOMMENT THIS AFTER DONE DESIGNING UI
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.clock import Clock

# from sign_practice_game_rpi import run_game # TODO: UNCOMMENT THIS AFTER DONE DESIGNING UI
import time

LabelBase.register(name="Icons", fn_regular="material-design-icons/font/MaterialIcons-Regular.ttf")


# -----------------------------
# Main Menu Screen
# -----------------------------
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Outer layout with padding
        outer_layout = BoxLayout(orientation="vertical", spacing=10, padding=40)

        # Title text
        title = Label(
            text="Choose the ASL sign you want to learn",
            font_size=32,
            #size_hint=(1, 0.15),
            size_hint=(None, None),
            size=(600, 70),
            valign="middle"
        )
        exit_btn = Button(
            text="\ue8ac",
            font_size=30,
            font_name="Icons",
            size_hint=(None, None),
            width=70,
            height=70
        )
        exit_btn.bind(on_press=self.exit_app)
        logo = Image(source='Teddy_BEAR_logo.png')
        inner_layout = BoxLayout(orientation="horizontal", size_hint=(1, None), height=60)
        inner_layout.add_widget(exit_btn)
        inner_layout.add_widget(title)
        inner_layout.add_widget(logo)
        outer_layout.add_widget(inner_layout)

        # Scrollable area
        scroll = ScrollView(size_hint=(1, 0.85))

        # Grid of buttons (5 per row), minimal spacing
        grid = GridLayout(
            cols=5,
            spacing=15,       # spacing between buttons
            padding=20,       # padding inside grid
            size_hint_y=None
        )
        grid.bind(minimum_height=grid.setter("height"))

        self.btn_cooldown = False
        # Create square buttons A–Z
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            btn = Button(
                text=letter,
                font_size=40,
                size_hint=(None, None),
                width=160,
                height=160,
                background_color=(233/255, 196/255, 106/255, 1)  # e9c46a
            )

            # btn.bind(on_release=lambda b: self.go_to_feedback(b.text))
            btn.bind(on_press=lambda b: self.test_run_game(b.text))
            grid.add_widget(btn)

        scroll.add_widget(grid)
        outer_layout.add_widget(scroll)
        self.add_widget(outer_layout)

    def go_to_feedback(self, text):
        feedback = self.manager.get_screen("feedback")
        feedback.update_text(text)
        self.manager.current = "feedback"

    def test_run_game(self, text):
        if not self.btn_cooldown:
            self.btn_cooldown = True
            # feedback = self.manager.get_screen("feedback")
            # feedback.update_text(text)
            # self.manager.current = "feedback"
            # run_game(start_letter=text) # TODO: UNCOMMENT THIS AFTER UI DESIGNING IS DONE
            Clock.schedule_once(lambda dt: self.end_cooldown(), 3) # Should wait for 3 seconds
    
    def end_cooldown(self):
        self.btn_cooldown = False


    def exit_app(self, instance): 
        App.get_running_app().stop()
        Window.close() # Close window entirely


# -----------------------------
# Feedback Screen (text + back button)
# -----------------------------
class FeedbackScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", spacing=20, padding=20)

        # Main title text
        self.label_main = Label(text="", font_size=50, size_hint=(1, 0.3))

        # Secondary text
        self.label_sub = Label(text="", font_size=40, size_hint=(1, 0.3))

        # Back button
        back_btn = Button(text="Back", font_size=35, size_hint=(1, 0.2))
        back_btn.bind(on_release=self.go_back)

        layout.add_widget(self.label_main)
        layout.add_widget(self.label_sub)
        layout.add_widget(back_btn)

        self.add_widget(layout)


        # time.sleep(100)

    def update_text(self, letter):
        self.label_main.text = f"Great, let's learn: {letter}"
        self.label_sub.text = "You're signing ____ right now"


    def go_back(self, instance):
        self.manager.current = "menu"


# -----------------------------
# App
# -----------------------------
class MyApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(FeedbackScreen(name="feedback"))
        return sm


if __name__ == "__main__":
    MyApp().run()
