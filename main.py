from kivy.app import App
from plyer import notification
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder


class NotifyApp(App):
    def build(self):
    	self.click_count=0
    	b=BoxLayout()
    	btn=Button(text="Click ME !!!",
    		       font_size=50)
    	btn.bind(on_press=self.notify_clicks)
    	b.add_widget(btn)
        return b

    def notify_clicks(self,*kwargs):
    	self.click_count+=1
    	notification.notify('Click Count',str(self.click_count))


"""clickCounter = Builder.load_string('''
	BoxLayout:
	    orientation:'vertical'
	    Button:
	        text:'Click Me !!!'
	        on_press:root.notify_clicks()
''')"""

if __name__ == '__main__':
    NotifyApp().run()