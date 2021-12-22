from kivymd.app import MDApp
from kivy.lang import Builder

builder_str = """
Screen:
	MDLabel:
		text:'Text'
		halign:'center'
		font_style:'H1'
		theme_text_color:'Secondary'
		pos_hint:{'center_x':.5,'center_y':.80}
"""
#For Custom:- theme_text_color:'Custom'
#text_color:255/255,65/255,229/255 (Pinkish Type)
class DemoApp(MDApp):
	def build(self):
		self.screen = Builder.load_string(builder_str)
		return self.screen

DemoApp().run()