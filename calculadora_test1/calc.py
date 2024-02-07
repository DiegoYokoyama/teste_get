from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Set the app size
Window.size = (500,700)

# Designate Our .kv design file 
Builder.load_file('calc.kv')

class MyLayout(Widget):
	def clear(self):
		self.ids.calc_input.text = '0'


class CalculatorApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	CalculatorApp().run()















 def raiz(self):
        try:
           value = self.ids.txtinput.text
           new_value = math.sqrt(float(value))
           self.ids.txtinput.text = str(new_value)
        except:
          self.ids.txtinput.text = 'Error' 
