# -*- coding: utf-8 -*-
"""
Created on Sun Jun 07 23:03:23 2015

@author: Insper
"""


import Leap, sys, thread, time
#importando todos os gestos 
from Leap import CircleGesture, ScreenTapGesture, SwipeGesture, KeyTapGesture

'''
duvidas:
-como fazer para rodar isso igual ao video? 
-
'''


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
        #criação da detecção dos gestos que serão feitos
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
        frame = controller.frame() 
        
        '''print "Frame ID:  " + str(frame.id) \
            + "Timestamp: " + str(frame.timestramp) \
            + "# of Hands"  + str(len(frame.hands)) \
            + "# of fingers" + str(len(frame.fingers)) \
            + "# of Tools" + str(len(frame.tools)) \
            + "# of Gestures " + str(len(frame.gestures()))'''
            
        for hand in frame.hands:
            
            '''handType = 'Left Hand' if hand.is_left else 'Right Hand'
            #para cada entrada com  a mão teremos um novo ID para cada ação
            print handType + 'Hand ID:' + str(hand.id) + 'Palm Position: ' + str(hand.palm_position)
            
            normal = hand.palm_normal
            direction = hand.direction
            #criação de parte do campo dos tres eixos - Funcao Vector - Direction Vector
            print "Pitch: " + str(direction.pitch*Leap.RAD_TO_DEG) + "Roll: " + str(normal.roll*Leap.RAD_TO_DEG) + "Yaw: " + str(direction.yaw*Leap.RAD_TO_DEG) #tranformção em graus
            #leitura do braço
            arm = hand.arm
            print "Arm Direction: " + str(arm.direction) + " Wrist Position: " + str(arm.wrist_position) + " Elbow Position: " +str(arm.elbow_position)'''
            
            '''for finger in hand.fingers:
                print "Type: " + self.finger_names[finger.type()] + "ID: " + str(finger.id) + " Lenght (mm): " + str(finger.length) + "Width (mm): " + str(finger.width)
               
                for b in range(0,4): 
                    bone = finger.bone(b)
                    print "Bone: " + self.bone_names[bone.type] + " Start: " + str(bone.prev_joint) + "End: " + str(bone.next_joint) + "Direction: " + str(bone.direction)'''
            
            '''for tool in frame.tools:
                print " Tool ID: " + str(tool.id) + " Tip Position: " + str(tool.tip_position) + "Direction: " + str(tool.direction)'''

            for gesture in frame.gestures():
                #cada gesto tem seu ID criado 
                if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                    circle= CircleGesture(gesture) # aqui o movimento circular é o de rotacionar o dedo na frente do computador
                    
                    if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
                        clockwiseness= "clockwise" # indica que o circulo esta em sentido horario
                    else:
                        clockwiseness= "counter-clockwise" #indica que o circulo esta em sentido anti
                        #swept angle vai dizer o qual longe vc foi no circulo desde a ultimo circulo identificado

           
                    swept_angle = 0
                    if circle.state != Leap.Gesture.STATE_START:
                        previous=CircleGesture(controller.frame(1).gesture(circle.id)) #criando um novo frame ao escrever frame(1)
                        swept_angle = (circle.progress - previous.progress) * 2 * Leap.PI
                    # imprime no console o tamanho do circulo que voê gesticula 
                    print "ID: " + str(circle.id) + "Progres: " + str(circle.progress) + "Radius: " + str(circle.radius) + "Swept_Angle: " + str(swept_angle * Leap.RAD_TO_DEG) + " " + clockwiseness

                    '''if gesture.type == Leap.Gesture.TYPE_SWIPE:
                        swipe= SwipeGesture(gesture)
                    print "Swipe ID: " + str(swipe.id) + "State: " + self.state_names[gesture.state] + "Position: " + str(swipe.position) + "Direction: " + str(swipe.direction) + "Speed(m/s): " + str(swipe.speed)'''
'''
if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
screentap= Screentap.Gesture(gesture)
print "Screen Tap ID: " + str(gesture.id) + "State: " + self.state_names[gesture.state] + "Position: " + str(screentap.position) + "Direction: " + str(screentap.direction)
if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
keytap= KeytapGesture(gesture)
print "Key tap ID: " + str(gesture.id) + "State: " + self.state_names[gesture.state] + "Position: " + str(keytap.position) + "Direction: " + str(keytap.direction)
'''

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
    
    
        
        