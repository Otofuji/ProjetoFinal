# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import Leap, sys, thread, time
#importando todos os gestos 
from Leap import CircleGesture, ScreenTapGesture, SwipeGesture, KeyTapGesture



class LeapMotionListner(Leap.Listener): #criação obrigatoria do listner class

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

    #criação da detecção dos gestos que serão feitos
        
    def on_connect(self, controller):
        print 'Motion Sensor Conected!'
        
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE); 
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        
    def on_diconnect(self, controller):
        print 'Motion Sensor Disconnected'
    
    def on_exit(self, controller):
        print 'Exited'
    
    def on_frame(self, controller):

        frame = controller.frame()
        
        
   
        
        print 'Frame ID:  ' + str(frame.id) \
            + 'Timestamp: ' + str(frame.timestramp) \
            + '# of Hands'  + str(len(frame.hands)) \
            + '# of fingers' + str(len(frame.fingers)) \
            + '# of Tools' + str(len(frame.tools)) \
            + '# of Gestures ' + str(len(frame.gestures()))
        
        
        for hand in frame.hands:
            handType = 'Left Hand' if hand.is_left else 'Right Hand'
            
            print handtype + 'Hand ID:' + str(hand.id) + 'Palm Position: ' + str
        
        print 'Frame ID:', str(frame.id), 'Timestamp:', str(frame.timestramp)
    
#------------------------------------------------------------------------------
    

    

#------------------------------------------------------------------------------        
        

        
if __name__=='__main__':
    
    listner = LeapMotionListner() #cria o objeto
    controller = Leap.Controller() #cria o objeto
        
    controller.add_listener(listner)
        
    print 'Press enter to quit'
        
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)