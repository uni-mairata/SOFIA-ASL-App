from kivy.config import Config
# Enable fullscreen before Kivy loads
Config.set('graphics', 'fullscreen', 'auto')
Config.set('graphics', 'borderless', '1')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView


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
            font_size=40,
            size_hint=(1, 0.15)
        )
        exit_btn = Button(
            text="power",
            font_size=30,
            width=20,
            height=20
        )
        outer_layout.add_widget(exit_btn)
        outer_layout.add_widget(title)

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

        # Create square buttons A–Z
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            btn = Button(
                text=letter,
                font_size=40,
                size_hint=(None, None),
                width=160,
                height=160
            )

            # btn.bind(size=self.make_square)
            btn.bind(on_release=lambda b: self.go_to_feedback(b.text))
            grid.add_widget(btn)

        scroll.add_widget(grid)
        outer_layout.add_widget(scroll)
        self.add_widget(outer_layout)

    def go_to_feedback(self, text):
        feedback = self.manager.get_screen("feedback")
        feedback.update_text(text)
        self.manager.current = "feedback"


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
