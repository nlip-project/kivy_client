from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, ObjectProperty
from client import get_response


def combine_response(old_msg:str, cur_msg:str, new_msg:str, server:str, port:int):
    return f'{old_msg}\n [b]You[/b]:[color=010101]{cur_msg}[/color]\n[b]{server}:{port}[/b]:[color=525252]{new_msg}[/color]'

class ScrollableLabel(ScrollView):
    text = StringProperty('')

class ServerBar(BoxLayout):
    def get_server(self):
        text = self.ids["server_input"].text
        if len(text) < 1:
            text = 'localhost'
        return text

    def get_port(self):
        port_text = self.ids["port_input"].text
        try:
            port = int(port_text)
            return port 
        except ValueError: 
            return 8000
        
class PortInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        newstring = ''.join(c for c in substring if c.isdigit())
        return super().insert_text(newstring, from_undo=from_undo)

class WrappedTextInput(TextInput):
    rootpar = ObjectProperty(None)
    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        if keycode[1] == 'enter':
            self.rootpar.button_pressed()
            #print('Enter was Called')
            #print(f'Root widget is {self.rootpar} -- {dir(self.rootpar)}')
        else: 
            super().keyboard_on_key_down(window, keycode, text, modifiers)

class SimpleWidget(BoxLayout):
    def button_pressed(self):
        text_input = self.ids["text_input"]
        text_display = self.ids["text_display"]
        top_bar = self.ids["top_bar"]
        cur_msg = text_input.text
        server = top_bar.get_server()
        port = top_bar.get_port()
        new_msg = get_response(server, port, cur_msg)
        text_display.text = combine_response(text_display.text, cur_msg, new_msg, server, port)
        text_input.text = ''

class SimpleApp(App):
    def build(self):
        return SimpleWidget()

if __name__ == '__main__': 
    SimpleApp().run()