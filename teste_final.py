# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 10:38:54 2015

@author: Insper
"""

import Leap, sys, thread, time, math
#importando todos os gestos 
from Leap import CircleGesture, ScreenTapGesture, SwipeGesture, KeyTapGesture #importando a biblioteca de gestos do leap


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
        #abilitações dos possiveis gestos proprcionado pelo LeaMotion
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE); 
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        
    def on_diconnect(self, controller):
        print 'Motion Sensor Disconnected'
    
    def on_exit(self, controller):
        print 'Exited'
        
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
                    print "Raio: " + str(circle.radius) + " Sentido do Círculo: " + clockwiseness
                    
            
    def on_frame2(self, controller):
         frame2 = controller.frame() # atribuindo a variavel frame o retorno de informações dos ultimos qudros captadas pelo leap motion
         #frame_penultimo_gesto = controller.frame(1) # atribuindo a variavel frame_penultimo_gesto o retorno de informações do penultimo gesto
         for hand2 in frame2.hands:
            for gesture2 in frame2.gestures():
                #cada gesto tem seu ID criado
                if gesture2.type == Leap.Gesture.TYPE_SWIPE:
                        #instanciando o objeto da classe gesto swipe
                        swipe = SwipeGesture(gesture2)
                        #instnciando o objet da classe gesto da direção do swipe
                        swipeDir = swipe.direction
                        #criações das condições dos prints de acordo com as cordenadas estabelecidas pelo leap
                        if (swipeDir.x > 0 and math.fabs(swipeDir.x) > math.fabs(swipeDir.y)): #se a posição da mão nas cordenas do leap for  x>0, o seja mão indo para a direita
                            print 'Swiped right'     #(parte do and):também precisa priorisara leitura do movimento em x para facilitar a leitura do leap
                        elif(swipeDir.x < 0 and math.fabs(swipeDir.x) > math.fabs(swipeDir.y)): #se a posiçao da mão nas coodernadas do Leap  x<0, ou seja, mão indo para esquerda
                            print 'Swiped left'       #(parte do and):também precisa priorisara leitura do movimento em x para facilitar a leitura do leap 
                        elif(swipeDir.y > 0 and math.fabs(swipeDir.x) < math.fabs(swipeDir.y)): #se a posiçao da mão nas coodernadas do Leap  y>0, ou seja, mão indo para cima
                            print 'Swiped up'        #(parte do and):também precisa priorisara leitura do movimento em y para facilitar a leitura do leap 
                        elif(swipeDir.x > 0 and math.fabs(swipeDir.x) < math.fabs(swipeDir.y)): #se a posiçao da mão nas coodernadas do Leap  x<0, ou seja, mão indo para baixo
                            print 'Swiped down'      #(parte do and):também precisa priorisara leitura do movimento em y para facilitar a leitura do leap '''
        
        
        
        
        
        
        
def  main():
    
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
    main()
        
        
        