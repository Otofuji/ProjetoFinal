# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 19:43:16 2015

@author: Insper
"""

import Leap, sys, thread, time, math
#importando todos os gestos 
from Leap import SwipeGesture


class LeapMotionListener(Leap.Listener): 

    '''Inicializando o objeto'''

    def on_init(self, controller):
        print 'Initialized' # indicando que o listner foi inicializado
        
        
    '''criação dos métodos'''


        
    def on_connect(self, controller):
        print 'Motion Sensor Conected!'
        #criação da detecção dos gestos que serão feitos
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        
    def on_diconnect(self, controller):
        print 'Motion Sensor Disconnected'
    
    def on_exit(self, controller):
        print 'Exited'
    


    #parte mais importante

    def on_frame(self, controller):
        frame = controller.frame() 
        
        for gesture in frame.gestures():
            
            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                
                swipe = SwipeGesture(gesture)
                swipeDir = swipe.direction
                
                if (swipeDir.x > 0 and math.fabs(swipeDir.x) > math.fabs(swipeDir.y)):
                    print 'Swiped right'
                elif(swipeDir.x < 0 and math.fabs(swipeDir.x) > math.fabs(swipeDir.y)):
                    print 'Swiped left'
                elif(swipeDir.y > 0 and math.fabs(swipeDir.x) < math.fabs(swipeDir.y)):
                    print 'Swiped up'
                elif(swipeDir.x > 0 and math.fabs(swipeDir.x) < math.fabs(swipeDir.y)):
                    print 'Swiped down'
                
        
        
        
        
        
def  main():
    
    listener = LeapMotionListener() #cria o objeto
    controller = Leap.Controller() #cria o objeto
        
    controller.add_listener(listener)
        
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
    
            
        
        
        
        
        
        