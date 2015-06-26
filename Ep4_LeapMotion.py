# -*- coding: utf-8 -*-
"""
Created on Sun Jun 07 23:03:23 2015

@author: Insper
"""

import Leap, sys, thread, time, math # importando a biblioteca do leap
from Leap import CircleGesture, ScreenTapGesture, SwipeGesture, KeyTapGesture #importando a biblioteca de gestos do leap
import turtle # Usa a biblioteca de turtle graphics

caneta = turtle.Turtle()
caneta.setpos(0,0)
caneta.penup()


class LeapMotionListener(Leap.Listener): 
#criação obrigatoria do listner class


# mostra qual tipo de gesto será reconhecido
# o que será feito quando o leap motion for conectado
# o que será feito quando o leap motion for desconectado
 
 
 
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky'] 
    bones_names = ['Metacarpal', 'Proximal', 'Intermidiate', 'Distal']
    state_name = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    
    '''Inicializando o objeto'''

    def on_init(self, controller):
        print 'Initialized' # indicando que o listner foi inicializado
        
        
    '''criação dos métodos'''

    
        
    def on_connect(self, controller):
        print 'Motion Sensor Conected!'
        #habilitações dos possiveis gestos proprcionado pelo LeaMotion
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE); 
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        
    def on_diconnect(self, controller):
        print 'Motion Sensor Disconnected'
    
    def on_exit(self, controller):
        print 'Exited'
    

    #parte mais importante

    def on_frame(self, controller):
        frame = controller.frame() # atribuindo a variavel frame o retorno de informações dos ultimos qudros captadas pelo leap motion
        #frame_penultimo_gesto = controller.frame(1) # atribuindo a variavel frame_penultimo_gesto o retorno de informações do penultimo gesto
            
        for hand in frame.hands:
            
            for gesture in frame.gestures():
                #cada gesto tem seu ID criado
                if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                    circle= CircleGesture(gesture) 
                    #instanciando o objeto da classe gesto circulo
                    # aqui o movimento circular é o de rotacionar o dedo na frente do computador
                    if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
                        clockwiseness= "clockwise" # indica que o circulo esta em sentido horario
                    else:
                        clockwiseness= "counter-clockwise" #indica que o circulo esta em sentido anti
                        #swept angle vai dizer o qual longe vc foi no circulo desde a ultimo circulo identificado

           
                    swept_angle = 0
                    if circle.state != Leap.Gesture.STATE_START:
                        previous = CircleGesture(controller.frame(1).gesture(circle.id)) #criando um novo frame ao escrever frame(1)
                        swept_angle = (circle.progress - previous.progress) * 2 * Leap.PI
                        # imprime no console o tamanho do circulo que voê gesticula e o sentido horario ou anti-horario 
                        caneta.pensize(2)
                        caneta.circle(circle.radius)
                    print "Radius: " + str(circle.radius) + " " + clockwiseness
                    
                if gesture.type == Leap.Gesture.TYPE_SWIPE:
                        #instanciando o objeto da classe gesto swipe
                        swipe = SwipeGesture(gesture)
                        #instnciando o objet da classe gesto da direção do swipe
                        swipeDir = swipe.direction
                        #criações das condições dos prints de acordo com as cordenadas estabelecidas pelo leap
                        if (swipeDir.x > 0 and math.fabs(swipeDir.x) > math.fabs(swipeDir.y)): #se a posição da mão nas cordenas do leap for  x>0, o seja mão indo para a direita
                            print 'Swiped right'     #(parte do and):também precisa priorisara leitura do movimento em x para facilitar a leitura do leap
                            caneta.seth(0)
                            caneta.ht()
                            caneta.fd(10)
                        elif(swipeDir.x < 0 and math.fabs(swipeDir.x) > math.fabs(swipeDir.y)): #se a posiçao da mão nas coodernadas do Leap  x<0, ou seja, mão indo para esquerda
                            print 'Swiped left'       #(parte do and):também precisa priorisara leitura do movimento em x para facilitar a leitura do leap
                            caneta.seth(180)
                            caneta.ht()
                            caneta.fd(10)
                        elif(swipeDir.y > 0 and math.fabs(swipeDir.x) < math.fabs(swipeDir.y)): #se a posiçao da mão nas coodernadas do Leap  y>0, ou seja, mão indo para cima
                            print 'Swiped up'        #(parte do and):também precisa priorisara leitura do movimento em y para facilitar a leitura do leap 
                            caneta.seth(90)
                            caneta.ht()
                            caneta.fd(10)
                        elif(swipeDir.y < 0 and math.fabs(swipeDir.x) < math.fabs(swipeDir.y)): #se a posiçao da mão nas coodernadas do Leap  x<0, ou seja, mão indo para baixo
                            print 'Swiped down'      #(parte do and):também precisa priorisara leitura do movimento em y para facilitar a leitura do leap 
                            caneta.seth(270)
                            caneta.ht()
                            caneta.fd(10)
                if gesture.type == Leap.Gesture.TYPE_KEY_TAP: #gesto de pinça 
                        key_tap = Leap.KeyTapGesture(gesture)
                        tap_point = key_tap.position
                        tapper = key_tap.pointable
                        caneta.pd()
                        print('caneta down')
                if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP: #gesto de touch na tela    
                        screen_tap = Leap.ScreenTapGesture(gesture)
                        caneta.pu()
                        print('caneta up')
def  main():
    
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Dextra Magus")
    listener = LeapMotionListener() #cria o objeto
    controller = Leap.Controller() #cria o objeto / estabelece nossa conection com as duas duplas cameras do controlezinho    
    controller.add_listener(listener) # fazendo o controle receber os eventos criado no listener
        
    print 'Press enter to quit'
        
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

#------------------------------------------------------------------------------        
        
if __name__=='__main__':
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Dextra Magus ")
    listener = LeapMotionListener() #cria o objeto
    controller = Leap.Controller() #cria o objeto / estabelece nossa conection com as duas duplas cameras do controlezinho    
    controller.add_listener(listener) # fazendo o controle receber os eventos criado no listener
        
    print 'Press enter to quit'
        
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)
        

  
    
        
        





























            