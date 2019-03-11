import kivy

from kivy.config import Config
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import BoundedNumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from tkinter import Tk
from kivy.uix.button import Button
class Gauge(Widget):
    '''
    Gauge class
    '''

    unit = NumericProperty(1.65)
    value = BoundedNumericProperty(0, min=0, max=140, errorvalue=0)
    file_gauge = StringProperty("meter_i3s.png")
    file_needle = StringProperty("needle_i3s.png")
    size_gauge = BoundedNumericProperty(128, min=128, max=256, errorvalue=128)
    size_text = NumericProperty(100)

    def __init__(self, **kwargs):
        super(Gauge, self).__init__(**kwargs)
            
        self._gauge = Scatter(
            size=(self.size_gauge, self.size_gauge),
            do_rotation=False, 
            do_scale=False,
            do_translation=False
            )

        _img_gauge = Image(source=self.file_gauge, size=(self.size_gauge, 
            self.size_gauge))

        self._needle = Scatter(
            size=(self.size_gauge, self.size_gauge),
            do_rotation=False,
            do_scale=False,
            do_translation=False
            )

        _img_needle = Image(source=self.file_needle, size=(self.size_gauge, 
            self.size_gauge))

        self._glab = Label(font_size=self.size_text, markup=True)
        self._progress = ProgressBar(max=140, height=300, value=self.value)
       
        self._gauge.add_widget(_img_gauge)
        self._needle.add_widget(_img_needle)
        
        self.add_widget(self._gauge)
        self.add_widget(self._needle)
        self.add_widget(self._glab)
        self.add_widget(self._progress)

        self.bind(pos=self._update)
        self.bind(size=self._update)
        self.bind(value=self._turn)
        
        
    def _update(self, *args):
        '''
        Update gauge and needle positions after sizing or positioning.
        '''
        self._gauge.pos = self.pos
        self._needle.pos = (self.x, self.y)
        self._needle.center = self._gauge.center
        self._glab.center_x = self._gauge.center_x+50
        self._glab.center_y = self._gauge.center_y + (self.size_gauge/4)+150
        self._progress.x = self._gauge.x+70
        self._progress.y = self._gauge.y + (self.size_gauge / 4)+90
        self._progress.width = self.size_gauge


      
    def _turn(self, *args):
        '''
        Turn needle, 1 degree = 1 unit, 0 degree point start on 50 value.
        '''
        self._needle.center_x = self._gauge.center_x
        self._needle.center_y = self._gauge.center_y
        self._needle.rotation = (self.unit) - (self.value * self.unit)
        self._glab.text = "[b]{0:.0f}[/b]".format(self.value)
        self._progress.value = self.value


class GaugeApp(App):
        def build(self):
            from kivy.uix.slider import Slider

            def test(*ars):
                gauge.value = s.value
              
                print(s.value)

            def test_(*ars):
          
                gauge_.value = s1.value
                print(s.value)
            
            def callback(instance):
                if(instance==button1):
                    print("Change speed to 20km/hr")
                    gauge_.value = 20
                elif(instance == button2):
                    print("Change speed to 60km/hr")
                    gauge_.value = 60
                else:
                    print("Change speed to 100km/hr")
                    gauge_.value = 100


            box = BoxLayout(orientation='horizontal', spacing=10, padding=10)
            gauge_ = Gauge(value=150, size_gauge=256, size_text=19)

            
            box.add_widget(gauge_)
            
            s = Slider(min=0, max=140, value=0)

            s1 = Slider(min=0, max=140, value=0)

            s1.bind(value=test_)
            box.add_widget(s1)

            button1 = Button(text='20Km/hr', font_size=14, size_hint_x=0.3, size_hint_y=0.2)
            button2 = Button(text='60Km/hr', font_size=14,  size_hint_x=0.3, size_hint_y=0.2)
            button3 = Button(text='100Km/hr', font_size=14, size_hint_x=0.3, size_hint_y=0.2)
            
            box.add_widget(button1)
            button1.bind(on_press=callback)

            box.add_widget(button2)
            button2.bind(on_press=callback)

            box.add_widget(button3)
            button3.bind(on_press=callback)

            return box
            
if __name__ == '__main__':
    GaugeApp().run()
