# -*- coding: utf-8 -*-
"""
Created on Sun May 24 22:49:43 2015

@author: Insper
"""

import Leap, sys, thread, time
from Leap import CircleGesture, ScreenTapGesture, SwipeGesture


class LeapMotionListner(Leap.listener): #criação obrigatoria do listner class
    
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bones_names = ['Metacarpal', 'Proximal', 'Intermidiate', 'Distal']
    state_name = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    
    '''Inicializando o objeto'''
    def on_init(self, controller):
        print('Initialized')
        
        
    '''criação dos métodos'''
    
        
    def on_connect(self, controller):
        print('Motion Sensor Conected!')
        
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        
    def on_diconnect(self, controller):
        print('Motion Sensor Disconnected')
    
    def on_exit(self, controller):
        print('Exited')
    
    def on_frame(self, controller):
        frame = controller.frame()
        
        
    #Essa terminologia funciona
        
        print 'Frame ID:  ' + str(frame.id) \
            + 'Timestamp: ' + str(frame.timestramp) \
            + '# of Hands'  + str(len(frame.hands)) \
            + '# of fingers' + str(len(frame.fingers)) \
            + '# of Tools' + str(len(frame.tools)) \
            + '# of Gestures ' + str(len(frame.gestures()))
        
        
        for hand in frame.hands:
            handType = 'Left Hand' if hand.is_left else 'Right Hand'
            
            print handtype + 'Hand ID:' + str(hand.id) + 'Palm Position: ' + str
        
        print('Frame ID:', str(frame.id), 'Timestamp:', str(frame.timestramp) 
    
#------------------------------------------------------------------------------
    
def main():
    
    listner = LeapMotionListner() #cria o objeto
    controller = Leap.Controller() #cria o objeto
    
    controller.add_listener(listner)
    
    print('Press enter to quit')
    
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

#------------------------------------------------------------------------------        
        
if __name__ == '__main__':
    
    main()    
    
    
    
        
        