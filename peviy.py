from tkinter import *
import random
# создать окна
window = Tk ()
# задаём переменные для хранения ширины и высоты окна
w= 600
h=600
# задать размер окна
window.geometry (f'{w}x{h}')
#создаем холст для отрисовки игрового поля
canvas = Canvas (window, width = w, height = h)
#располагаем холст на окне
canvas.place (in_=window, x=0, y=0)
#подгружаем картинку с зад фоном
bg = PhotoImage(name='photo_2024-10-03_23-33-14.png')


#создаемм класс рыцарь
class knight:
    def __init__(self):
       self.x = 70
       self.y = h//2
       #скорость рыцаря
       self.v = 0
       #изображение рыцаря
       self.img = PhotoImage(name='knight.png')

knight = knight()
#функция перемещения вверх
def up(self, event):
    self.v =-3
#функция перемещения вниз
def stop (self, event):
    self.v=3
#make class dragon
class dragon:
    def _init_(self):
        self.x=750
        self.y=random.randint(100,500)
        self.v=random.randint(2,3)
        self.photo=PhotoImage(name='DRAGON.png')
#make function game(animation, quickly change kadr)
def game():
    #ochicsaem pole ot objects
    canvas. delete ('all')
    #otobrajaem zadniy fone
    canvas.create_image(300,300, image=bg)
    #otobrajaem rycar
    canvas.create_image(knight.x, knight.y, image=knight.photo)

    ccurrent_dragon = 0
    #index dragon, which need to delete from holst
    dragon_to_delele = -1
    #prohodimsy po every dragon
    for dragon in dragons:
        #mooving dragon to left, to est to khinght
        dragon.x -= dragon.v
        #otobrajaem dragon more lef
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo)
        #if knight stolknulsiy s dragon
        if ((knight.x -dragon.x)**2+(knight.y-dragon.y)**2)<=96**2:
            dragon_to_delete=ccurrent_dragon
        #переходим к некст дракону
        сurrent_dragon += 1
        #if hoty bi one dragon fly через левый край
        if dragon.x <=0:
            canvas.delete ('all')
            canvas.create_text (w//2, h//2, text ='you losel', font='Arial 50', fill='red')
            break
        #если есть дракон, которого нужно удалить
        if dragon_to_delete > -1:
            #delete gragon hollsta
            del dragons [dragon_to_delete]
            #создаём объект рыцаря
            knight = knight()
            #создаем список с драконами
            dragons=[]
            for i in range (random.randint(2,5)):
                dragons.append (dragon())
        #закрепляем кнопки за вызовами функций движения рыцаря
        window .bind ('<key-up>', knight.up)
        window.bind ('<key-down>', knight.down)
        window.bind ('<keyRelease>', knight.stop)






window.mainloop()

