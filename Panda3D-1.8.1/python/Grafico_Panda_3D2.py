# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 09:21:19 2015

@author: Insper
"""

from math import pi, sin, cos
 
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
 
import Leap, sys, thread, time, math
#importando todos os gestos 
from Leap import CircleGesture, ScreenTapGesture, SwipeGesture, KeyTapGesture


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
                        previous = CircleGesture(controller.frame(1).gesture(circle.id)) #criando um novo frame ao escrever frame(1)
                        swept_angle = (circle.progress - previous.progress) * 2 * Leap.PI
                    # imprime no console o tamanho do circulo que voê gesticula 
                        
                    print "Radius: " + str(circle.radius) + " " + clockwiseness
                    
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


class MyApp(ShowBase):
    
    def __init__(self):
        ShowBase.__init__(self)
        # codigo do Leap        
        listener = LeapMotionListener() #cria o objeto
        controller = Leap.Controller() #cria o objeto
        controller.add_listener(listener)
 
        # Disable the camera trackball controls.
        self.disableMouse()
 
        # Load the environment model.
        self.environ = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.environ.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)
 
        # Add the spinCameraTask procedure to the task manager.
        #self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
 
        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")
 
        # Create the four lerp intervals needed for the panda to
        # walk back and forth.
        pandaPosInterval1 = self.pandaActor.posInterval(13,
                                                        Point3(0, -10, 0),
                                                        startPos=Point3(0, 10, 0))
        pandaPosInterval2 = self.pandaActor.posInterval(13,
                                                        Point3(0, 10, 0),
                                                        startPos=Point3(0, -10, 0))
        pandaHprInterval1 = self.pandaActor.hprInterval(3,
                                                        Point3(180, 0, 0),
                                                        startHpr=Point3(0, 0, 0))
        pandaHprInterval2 = self.pandaActor.hprInterval(3,
                                                        Point3(0, 0, 0),
                                                        startHpr=Point3(180, 0, 0))
 
        # Create and play the sequence that coordinates the intervals.
        self.pandaPace = Sequence(pandaPosInterval1,
                                  pandaHprInterval1,
                                  pandaPosInterval2,
                                  pandaHprInterval2,
                                  name="pandaPace")
        #self.pandaPace.loop()
 
    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont




#------------------------------------------------------------------------------        
        
if __name__=='__main__':
    app = MyApp()
    app.run()
    
