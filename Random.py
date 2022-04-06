import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import random

Builder.load_file('Random.kv')

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

class Random(App):
  def build(self):
    return MikeRandom()
    
if __name__=='__main__':
  Random().run() 
 
