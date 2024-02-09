from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import _ctypes



class PopupApp(App):
    def build(self):
        btn = Button(text='Click here')
        btn.bind(on_press=self.show_popup)
        return btn

    def show_popup(self, instance):
        popup = Popup(title='Hi mahesh',
                      content=Button(text='Hi mahesh'),
                      size_hint=(None, None), size=(400, 400))
        popup.open()


if __name__ == '__main__':
    PopupApp().run()
