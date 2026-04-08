from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


# -----------------------------
# Main Menu Screen
# -----------------------------
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = GridLayout(cols=3, spacing=10, padding=20)

        for i in range(9):
            btn = Button(text=f"Button {i+1}", font_size=32)
            btn.bind(on_release=lambda b: self.go_to_detail(b.text))
            layout.add_widget(btn)

        self.add_widget(layout)

    def go_to_detail(self, text):
        detail = self.manager.get_screen("detail")
        detail.update_text(text)
        self.manager.current = "detail"


# -----------------------------
# Detail Screen (text only)
# -----------------------------
class DetailScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", spacing=20, padding=20)

        self.label = Label(text="", font_size=40)
        layout.add_widget(self.label)

        self.add_widget(layout)

    def update_text(self, text):
        self.label.text = f"You pressed: {text}"


# -----------------------------
# App
# -----------------------------
class MyApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(DetailScreen(name="detail"))
        return sm


if __name__ == "__main__":
    MyApp().run()
