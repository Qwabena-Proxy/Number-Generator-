# importing libs
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import random

# loading kivy language file
Builder.load_file('Random.kv')

# Design class
class MikeRandom(Widget):
  def __init__(self,**kwargs):
    super(MikeRandom,self).__init__(**kwargs)
  def gen(self):
    a = random.randint(0,255)/255
    b = random.randint(0,255)/255
    c = random.randint(0,255)/255

    self.random_label.text=str(random.randint(0,1000))
    self.random_label.color=(a,b,c)
    self.title.color=(c,a,b)
 
# App class
class Random(App):
  def build(self):
    return MikeRandom()

#Class calling  
if __name__=='__main__':
  Random().run() 
 
