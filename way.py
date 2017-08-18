"""Pet project to explore objects introspection
in more human language approach for self learning purposes.
In no means it compares to the flexibility and versatility of
Inspect module
https://docs.python.org/3.5/library/inspect.html
"""

import inspect
import logging

    
class WAY:
    """Who Are You"""
    def __init__(self, obj):
        self.obj = obj
        
    def WIYN(self):
        """What is your name"""
        if hasattr(self.obj, "__name__"):         
            return self.obj.__name__
        else:
            return self.obj.__class__.__name__ 
    
    def WIYI(self):
        """What is your identity"""
        return id(self.obj)
    def WAYA(self):
        """"What are your arguments"""
        return inspect.getargspec(self.obj.__init__).args[1:]
    def WAYP(self):
        """Who are your parents"""
        ### !!!Needs extensive testing!!!
        if hasattr(self.obj, "__mro__"):
            return inspect.getmro(self.obj)[1:]
        else:
            return "Object without object resolution order"
        
    def WIYT(self):
        """What is your type"""
        return self.obj
    
    
    def WAYFP(self):
        """What are arguments that belongs to your parents(none repetative)"""
        ### !!!Hides exact overalping arguments useful just for general 
        ### !!!information!!!  
        args_a = []
        args_b = inspect.getargspec(self.obj.__init__).args[1:]
        if hasattr(self.obj, "__mro__"):
            for ob_parent in self.obj.__mro__:               
                if ob_parent.__name__!= self.obj.__name__:
                    if '__init__' in ob_parent.__dict__:
                        args_a += inspect.getargspec(ob_parent).args[1:]
        
            return args_a + args_b
    #def WAYFPtest(self):
        #"""What are and to what objects arguments belong"""
        #args_a = {}
        #args_a[Namer(self.obj)]=inspect.getargspec(self.obj).args[1:]
        #if hasattr(self.obj, "__mro__"):
            #for ob_parent in self.obj.__mro__:
                #if ob_parent.__name__!= self.obj.__name__:
                    #if '__init__' in ob_parent.__dict__:
                        #args_a[Namer(ob_parent)]=inspect.getargspec(ob_parent).args[1:]               
        #return args_a#
                    
    def WAYAV(self):
        """What are your argument values if exist"""
        if hasattr(self.obj,"__dict__"):
            return list(self.obj.__dict__.values())
        else:
            pass
    def WAYAA(self):
        """What are instance variables including arguments"""
        if hasattr(self.obj,"__dict__"):
            logging.info("Returning instance variables including arguments")
            return list(self.obj.__dict__)
        else:
            logging.info("Object doesn't have __dict__")
            pass
            
        
def ArgParent(ob, arg):
    """Retrieves information what is object name of the argument"""
    a = WAY(ob)
    for k, v in a.WAYFPtest().items():
        for item in v:
            if item == arg:
                return k
                


                
                

                
   
    







        

    
    
