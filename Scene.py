'''
Created on Jan 5, 2015

@author: ericrudisill
'''

class Scene(object):

    def __init__(self):
        self.sceneobjects = []
        
    def addSceneObject(self, obj):
        self.sceneobjects.append(obj)
        
    
        