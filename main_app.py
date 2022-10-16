from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window
color = (0,0,100,1)
Window.clearcolor = color
class Instruction(Screen):
    def __init__(self, name='inst'):
        super().__init__(name=name) 
        vertical = BoxLayout(orientation='vertical',padding = 80)
        label_ins = Label(text = 'Это приложение может считать площади: треугольника и круга, а так же может решать квадратные уравнения.')
        vertical.add_widget(label_ins)

        hor1 = BoxLayout()
        label_1 = Label(text= 'Введите Фигуру:')
        self.btn_int1 = TextInput(size_hint = (.9,.2),pos_hint = {'center-x':.6,'center_y':.5})
        # изменение поля text вызывает метод check
        self.btn_int1.bind(text = self.check)
        hor1.add_widget(label_1)
        hor1.add_widget(self.btn_int1)
        #hori = BoxLayout()
        #btn_start = Button(text = 'Погнали дальше!')
        #hori.add_widget(btn_start)
        #btn_start.on_press = self.check
        
        vertical.add_widget(hor1)
        #vertical.add_widget(hori)
        self.add_widget(vertical)

    def next1(self):
        self.manager.transition.direction = 'right' 
        self.manager.current = 'triangle'

    def next2(self):
        self.manager.transition.direction = 'left' 
        self.manager.current = 'circle'

    def next3(self):
        self.manager.transition.direction = 'right' 
        self.manager.current = 'square'
    def next4(self):
        self.manager.transition.direction = 'left' 
        self.manager.current = 'equation'

    def check(self, *args):
        # print('check')
        text = self.btn_int1.text.lower()
        if text == 'треугольник':
            self.next1()
        elif text == 'круг':
            self.next2()
        #elif text == 'квадрат':
            #self.next3()
        elif text == 'квадратное уравнение':
            self.next4()

class Triangle(Screen):
    def __init__(self, name='triangle'):
        super().__init__(name=name)
        vertical2 = BoxLayout(orientation='vertical',padding = 20)
        wimg = Image(source='tri.jpg')
        #label_2 = Label(text ='Triangle')
        self.label3 = Label(text = 'Ваш Будущий Ответ....')
        #vertical2.add_widget(label_2)
        vertical2.add_widget(wimg)
        vertical2.add_widget(self.label3)

        hor2 = BoxLayout()
        label1 = Label(text = 'Введите Высоту:')
        self.btn_int2 = TextInput(size_hint = (.9,.3),pos_hint = {'center_x':.6,'center_y':.5})
        hor2.add_widget(label1)
        hor2.add_widget(self.btn_int2)

        hor3 = BoxLayout()
        label2 = Label(text = 'Введите Основание:')
        self.btn_int3 = TextInput(size_hint = (.9,.3),pos_hint = {'center_x':.6,'center_y':.5})
        hor3.add_widget(label2)
        hor3.add_widget(self.btn_int3)

        hor4 = BoxLayout()
        btn_ok1 = Button(text = 'ДОМОЙ')
        btn_total = Button(text = 'ПОДСЧИТАТЬ')
        btn_ok1.on_press = self.next
        btn_total.on_press = self.square_t
        hor4.add_widget(btn_total)
        hor4.add_widget(btn_ok1)
    
        vertical2.add_widget(hor2)
        vertical2.add_widget(hor3)
        vertical2.add_widget(hor4)
        self.add_widget(vertical2)


    def next(self):
        self.manager.transition.direction = 'down' 
        self.manager.current = 'inst'

    def square_t(self):
        try:
            total_square  = int(self.btn_int2.text) * int(self.btn_int3.text) * 0.5
            self.label3.text = ('Ваш Ответ: ' +str(total_square))
        except:
            self.label3.text = 'Вы ввели некорректные данные'

class Circle(Screen):
    def __init__(self, name='circle'):
        super().__init__(name=name)
        vertical_lay = BoxLayout(orientation='vertical',padding = 20)
        #photo = Label(text ='Circle')
        wimg2 = Image(source='images.png')
        self.label123 = Label(text = 'Ваш Будущий Ответ....')
        vertical_lay.add_widget(wimg2)
        #vertical_lay.add_widget(photo)
        vertical_lay.add_widget(self.label123)

        horisont = BoxLayout()
        label_vvod = Label(text = 'Введите Радиус:')
        self.btn_int4 = TextInput(size_hint = (.9,.3),pos_hint = {'center_x':.6,'center_y':.5})
        horisont.add_widget(label_vvod)
        horisont.add_widget(self.btn_int4)

        horisont2 = BoxLayout()
        btn_ok2 = Button(text = 'ДОМОЙ')
        btn_total2 = Button(text = 'ПОДСЧИТАТЬ')
        btn_ok2.on_press = self.next
        btn_total2.on_press = self.square_c
        horisont2.add_widget(btn_total2)
        horisont2.add_widget(btn_ok2)
    
        vertical_lay.add_widget(horisont)
        vertical_lay.add_widget(horisont2)
        self.add_widget(vertical_lay)

    def next(self):
        self.manager.transition.direction = 'down' 
        self.manager.current = 'inst'

    def square_c(self):
        try:
            total_square_circle  = int(self.btn_int4.text) * 3,14
            self.label123.text = ('Ваш Ответ: ' +str(total_square_circle))
        except:
            self.label123.text = 'Вы ввели некорректные данные'

class Quadratic_equation(Screen):
    def __init__(self, name='equation'):
        super().__init__(name=name)
        verti = BoxLayout(orientation='vertical',padding = 20)
        label_quad = Label(text='Введите коэфиценты уравнения...')
        self.label_total = Label(text='Ваш будущий ответ...')
        verti.add_widget(label_quad)
        verti.add_widget(self.label_total)

        hori1 = BoxLayout()
        label_vvod_1 = Label(text = 'Введите a:')
        self.text_inp = TextInput(size_hint = (.9,.3),pos_hint = {'center_x':.6,'center_y':.5})
        hori1.add_widget(label_vvod_1)
        hori1.add_widget(self.text_inp)

        hori2 = BoxLayout()
        label_vvod_2 = Label(text = 'Введите b:')
        self.text_inp2 = TextInput(size_hint = (.9,.3),pos_hint = {'center_x':.6,'center_y':.5})
        hori2.add_widget(label_vvod_2)
        hori2.add_widget(self.text_inp2)

        hori3 = BoxLayout()
        label_vvod_3 = Label(text = 'Введите c:')
        self.text_inp3 = TextInput(size_hint = (.9,.3),pos_hint = {'center_x':.6,'center_y':.5})
        hori3.add_widget(label_vvod_3)
        hori3.add_widget(self.text_inp3)

        hori4 = BoxLayout()
        btn_home = Button(text = 'ДОМОЙ')
        total_score = Button(text = 'ПОДСЧИТАТЬ')
        btn_home.on_press = self.next
        total_score.on_press = self.quadratic
        hori4.add_widget(total_score)
        hori4.add_widget(btn_home)
        
        verti.add_widget(hori1)
        verti.add_widget(hori2)
        verti.add_widget(hori3)
        verti.add_widget(hori4)
        self.add_widget(verti)

    def next(self):
        self.manager.transition.direction = 'down' 
        self.manager.current = 'inst'
    
    def quadratic(self):
        discrimenant = int(self.text_inp2.text)* int(self.text_inp2.text) - 4 * int(self.text_inp.text)* int(self.text_inp3.text)
        if discrimenant < 0:
            self.label_total.text = 'Корней нет'
        elif discrimenant == 0:
            x = -int(self.text_inp2.text)/2*int(self.text_inp.text)
            self.label_total.text = 'Корень уравнения:' + str(x)
        elif discrimenant >0:
            x1 = -int(int((self.text_inp2.text))- int(discrimenant))/(2*int(self.text_inp.text))
            x2 = -int(int((self.text_inp2.text)) + int(discrimenant))/(2*int(self.text_inp.text))
            self.label_total.text = "Корни уравнения:" +str(x1)+', '+str(x2)
        #except:
            #self.label_total.text = "Вы ввели некорректные данные"


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Instruction())
        sm.add_widget(Triangle())
        sm.add_widget(Circle())
        sm.add_widget(Quadratic_equation())
        #sm.add_widget(FiveScr())
        return sm

app = MyApp()
app.run()





# class FirstScr(Screen):
#     def __init__(self, name='first'):
#         super().__init__(name=name) 

#         h1 = BoxLayout()
#         label = Label(text='Выберите экран')
#         h1.add_widget(label)

#         v1 = BoxLayout(orientation='vertical',padding = 8,spacing = 8)
#         btn1=Button(text='1')
#         btn2=Button(text='2')
#         btn3=Button(text='3')
#         btn4=Button(text='4')
#         v1.add_widget(btn1)
#         v1.add_widget(btn2)
#         v1.add_widget(btn3)
#         v1.add_widget(btn4)

#         h1.add_widget(v1)
#         self.add_widget(h1)
#         btn1.on_press = self.next1
#         btn2.on_press = self.next2
#         btn3.on_press = self.next3
#         btn4.on_press = self.next4
#     def next1(self):
#         self.manager.transition.direction = 'down' 
#         self.manager.current = 'second'

#     def next2(self):
#         self.manager.transition.direction = 'up' 
#         self.manager.current = 'third'

#     def next3(self):
#         self.manager.transition.direction = 'right' 
#         self.manager.current = 'four'
    
#     def next4(self):
#         self.manager.transition.direction = 'left' 
#         self.manager.current = 'four'

# class SecondScr(Screen):
#     def __init__(self, name='second'):
#         super().__init__(name=name)
#         v2 = BoxLayout(orientation='vertical',padding = 8,spacing = 8)
#         h2 = BoxLayout()
#         btn_ok =Button(text = 'OK')
#         btn_back =Button(text = 'BACK')
#         h2.add_widget(btn_ok)
#         h2.add_widget(btn_back)
#         self.text1 = Label(text = "Введите пароль!")
#         self.btn_input = TextInput()
#         v2.add_widget(self.text1)
#         v2.add_widget(self.btn_input)
#         btn_ok.on_press = self.check
#         btn_back.on_press = self.next5
#         h2.add_widget(v2)
#         self.add_widget(h2)
        
#     def next(self):
#         self.manager.transition.direction = 'down' 
#         self.manager.current = 'first'
    
#     def next5(self):
#         self.manager.transition.direction = 'down' 
#         self.manager.current = 'first'

#     def check(self):
#         if self.btn_input.text == '12345':
#             self.next5()
#         else:
#             self.text1.text = "Неправильно!Еще раз!"
    
# class ThirdScr(Screen):
#     def __init__(self, name='third'):
#         super().__init__(name=name)
#         btn_ok2 = Button(text="OK",pos_hint = {'left_x':0,'left_y':0})
#         btn_back2 = Button(text = 'Back',pos_hint = {'right_x':10,'right_y':10})
#         btn_back2.on_press = self.next
#         btn_ok2.on_press = self.next
#         h3 = BoxLayout()
#         h3.add_widget(btn_ok2)
#         h3.add_widget(btn_back2)
#         self.add_widget(h3)
        
#     def next(self):
#         self.manager.transition.direction = 'up' 
#         self.manager.current = 'first'

# class FourScr(Screen):
#     def __init__(self, name='four'):
#         super().__init__(name=name)
#         btn = Button(text="Вернись, вернись!")
#         btn.on_press = self.next
#         self.add_widget(btn)
        
#     def next(self):
#         self.manager.transition.direction = 'right' 
#         self.manager.current = 'first'


# class MyApp(App):
#     def build(self):
#         sm = ScreenManager()
#         sm.add_widget(FirstScr())
#         sm.add_widget(SecondScr())
#         sm.add_widget(ThirdScr())
#         sm.add_widget(FourScr())
#         #sm.add_widget(FiveScr())
#         return sm






# app = MyApp()
# app.run()