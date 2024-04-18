import kociemba
import pytwisty
from kivy.factory import Factory
from kivy.metrics import dp
from kivy.config import Config
Config.set('graphics', 'width', "450")
Config.set('graphics', 'height', "800")
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDTextButton, MDRectangleFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.behaviors.motion_behavior import MotionBase
from kivymd.uix.screenmanager import MDScreenManager
#from rubik.cube import Cube
from kivy.uix.scrollview import ScrollView
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.uix.screenmanager import FadeTransition
from kivy.properties import ObjectProperty, Property
from kivy.utils import get_color_from_hex
class MenuHeader(MDBoxLayout):
    pass
class MainScreen(MDScreen):
    pass
class Screen3x3(MDScreen):
    pass
class Screen2x2(MDScreen):
    pass
class ScreenSignations(MDScreen):
    pass

class SM(MDScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cur(self,s):
        self.current_screen=s


ms=ObjectProperty()
class CubeApp(MDApp):
    color={'red':(0,0,255),
               'orange':(0,165,255),
               'blue':(255,0,0),
               'green':(0,255,0),
               'white':(255,255,255),
               'yellow':(0,255,255)}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style_switch_animation = False
        self.theme_cls.theme_style_switch_animation_duration = .8
        # sm = SM(transition=FadeTransition())
        self.theme_cls.theme_style =  "Light" #"Dark"
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.accent_palette='BlueGray' #'LightBlue','LightGreen',
        self.theme_cls.primary_light_hue='300'
        self.theme_cls.dynamic_color = False
        #self.theme_cls.theme_style_switch_animation= "Teal"
        #self.fps_monitor_start()
        return Builder.load_file('cubee.kv')

    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Teal" if self.theme_cls.primary_palette == "Cyan" else "Cyan"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

class sselection3(MDGridLayout):
    def __init__(self, **kwargs):
        super(sselection3, self).__init__(**kwargs)
        self.rows=3
        self.cols=3
        #self.size_hint=(1, 1)
        #self.minimum_size=(self.width, self.height)
        #self.col_default_width=self.width
        #self.row_default_height=self.height
        #self.col_force_default=True
        #self.row_force_default=True

        self.pos_hint={"center_x": .5, "center_y": .5}

        self.p=[None,None,None, None,None,None, None,None,None]
        self.sequence = ["up", "right", "front", "down", "left", "back"]
        self.now = -1
        self.raw = ''
        self.state = {'up': ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
                      'right': ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
                      'front': ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
                      'down': ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'],
                      'left': ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
                      'back': ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']}
        self.sign_conv = {"g": 'F',
                          "w": 'U',
                          "b": 'B',
                          "r": 'R',
                          "o": 'L',
                          "y": 'D'}
        self.pixel_color = ['w', 'r', 'g', 'y', 'o', 'b']
        self.color_now = [0,0,0, 0,0,0, 0,0,0]
        self.colors = ['#fff5ee', '#dc143c', '#36ff26', '#ffff42', '#ff6c00', '#098dff']
        self.middle_color_now=['#fff5ee', '#dc143c', '#36ff26', '#ffff42', '#ff6c00', '#098dff']

        self.side_create()

    def side_create(self):
        if self.now < 5:
            self.now += 1
        else:
            self.now = 0        #self.color_now=[(self.now+1)%6]*9
        self.clear_widgets()
        self.refill_side()

    def refill_side(self):
        #for x in range(0,9):
            #self.p[x]=MDRectangleFlatButton(md_bg_color=get_color_from_hex("#aeaeae"))
            #self.p[x].bind(on_release=lambda f:self.color_pixel(x))
            #self.add_widget(self.p[x])
        self.p[0]=MDRectangleFlatButton(md_bg_color=get_color_from_hex(self.middle_color_now[self.now]),size_hint=(1, 1), on_release=lambda f:self.color_pixel(0))
        self.p[1]=MDRectangleFlatButton(md_bg_color=get_color_from_hex(self.middle_color_now[self.now]),size_hint=(1, 1), on_release=lambda f:self.color_pixel(1))
        self.p[2]=MDRectangleFlatButton(md_bg_color=get_color_from_hex(self.middle_color_now[self.now]),size_hint=(1, 1), on_release=lambda f:self.color_pixel(2))
        self.p[3]=MDRectangleFlatButton(md_bg_color=get_color_from_hex(self.middle_color_now[self.now]),size_hint=(1, 1), on_release=lambda f:self.color_pixel(3))
        self.p[4]=MDRectangleFlatButton(md_bg_color=get_color_from_hex(self.middle_color_now[self.now]),size_hint=(1, 1), )#, on_release=lambda f:self.color_pixel(4)
        self.p[5]=MDRectangleFlatButton(md_bg_color=get_color_from_hex(self.middle_color_now[self.now]),size_hint=(1, 1), on_release=lambda f:self.color_pixel(5))
        self.p[6]=MDRectangleFlatButton(md_bg_color=get_color_from_hex(self.middle_color_now[self.now]),size_hint=(1, 1), on_release=lambda f:self.color_pixel(6))
        self.p[7]=MDRectangleFlatButton(md_bg_color=get_color_from_hex(self.middle_color_now[self.now]),size_hint=(1, 1), on_release=lambda f:self.color_pixel(7))
        self.p[8]=MDRectangleFlatButton(md_bg_color=get_color_from_hex(self.middle_color_now[self.now]),size_hint=(1, 1), on_release=lambda f:self.color_pixel(8))
        [self.add_widget(self.p[x]) for x in range(0,9)]

    def color_pixel(self, index):
        I=self.color_now[index]%6
        a=get_color_from_hex(self.colors[I])

        self.state[self.sequence[self.now]][index]=self.pixel_color[I]

        self.color_now[index]+=1
        if self.color_now[index]==6:
            self.color_now[index]=0
        #return a
        self.p[index].md_bg_color=a
        #print(index, self.color_now)

    def solve(self):
        for i in self.state:
            for j in self.state[i]:
                self.raw += self.sign_conv[j]
        solution = kociemba.solve(self.raw)
        self.raw = ''
        a='Решение : '+ str(solution)
        #print(a)
        return a

class sselection2(MDGridLayout):
    def __init__(self, **kwargs):
        super(sselection2, self).__init__(**kwargs)
        self.rows=2
        self.cols=2
        #self.size_hint=(1, 1)
        #self.minimum_size=(self.width, self.height)
        #self.col_default_width=self.width
        #self.row_default_height=self.height
        #self.col_force_default=True
        #self.row_force_default=True

        self.pos_hint={"center_x": .5, "center_y": .5}

        self.p=[None,None,None, None,None,None, None,None,None]
        self.sequence = ["front", "left", "right", "up", "down", "back"]
        self.now = -1
        self.raw = ''
        self.state = {'front': ['g', 'g', 'g', 'g'],
                      'left': ['o', 'o', 'o', 'o'],
                      'right': ['r', 'r', 'r', 'r'],
                      'up': ['w', 'w', 'w', 'w'],
                      'down': ['y', 'y', 'y', 'y'],
                      'back': ['b', 'b', 'b', 'b']}
        self.pixel_color = ['g', 'o', 'r', 'w', 'y', 'b']
        self.color_now = [[0,0, 0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4],[5,5,5,5]]
        self.colors = ['#36ff26', '#ff6c00', '#dc143c', '#fff5ee', '#ffff42', '#098dff']
        self.___=0
        #self.middle_color_now=['#fff5ee', '#dc143c', '#36ff26', '#ffff42', '#ff6c00', '#098dff']

        self.side_create()


    def side_create(self):
        if self.now < 5:
            self.now += 1
        else:
            self.now=0
        #self.color_now=[(self.now+1)%6]*4
        #for index in range(4):
        #    self.color_now=self.state[self.sequence[self.now]][index]
        self.clear_widgets()
        self.refill_side()

    def refill_side(self):
        #for x in range(0,9):
            #self.p[x]=MDRectangleFlatButton(md_bg_color=get_color_from_hex("#aeaeae"))
            #self.p[x].bind(on_release=lambda f:self.color_pixel(x))
            #self.add_widget(self.p[x])
        self.p[0]=MDRectangleFlatButton(md_bg_color=get_color_from_hex(self.colors[self.now]),size_hint=(1, 1), on_release=lambda f:self.color_pixel(0))
        self.p[1]=MDRectangleFlatButton(md_bg_color=get_color_from_hex(self.colors[self.now]),size_hint=(1, 1), on_release=lambda f:self.color_pixel(1))
        self.p[2]=MDRectangleFlatButton(md_bg_color=get_color_from_hex(self.colors[self.now]),size_hint=(1, 1), on_release=lambda f:self.color_pixel(2))
        self.p[3]=MDRectangleFlatButton(md_bg_color=get_color_from_hex(self.colors[self.now]),size_hint=(1, 1), on_release=lambda f:self.color_pixel(3))
        [self.add_widget(self.p[x]) for x in range(0,2)]
        [self.add_widget(self.p[x]) for x in range(3,1,-1)]

        if self.___ == 0:
            for x in range(0,4):
                self.color_pixel(x)
            self.___=1

    def color_pixel(self, index):
        if self.color_now[self.now][index]==6:
            self.color_now[self.now][index]=0
        I=self.color_now[self.now][index]
        a=get_color_from_hex(self.colors[I])

        self.state[self.sequence[self.now]][index]=self.pixel_color[I]

        self.color_now[self.now][index]+=1
        #return a
        self.p[index].md_bg_color=a
        #print(index, self.color_now)

    def solve(self):
        for i in self.state:
            for j in self.state[i]:
                self.raw += j.upper()
        print(self.raw)
        solution1 = pytwisty.solve222(self.raw) #'BWRRWWYGOYYWGBGOBBGRORYO'
        self.raw = ''
        a=solution1
        print(a)
        return 'Решение : '+'  '.join(a)


app=CubeApp()
app.run()
