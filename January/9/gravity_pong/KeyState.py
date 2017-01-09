global keyState

class KeyState():
    def __init__(self, keyList):
        self.keyList = keyList
        self.keyValues = []
        for i in range(0,len(keyList)):
            self.keyValues.append(False)
            
    def isDown(self, kCode):
        for k in range(0,len(self.keyList)):
            if self.keyList[k] == kCode:
                return self.keyValues[k] 
        return False

def GetKeyState():
    global keyState
    return keyState

def CreateKeyState(keyList):
    global keyState
    keyState = KeyState(keyList)
    
def keyPressed():
    global keyState
    for k in range(0,len(keyState.keyList)):
        if keyState.keyList[k] == keyCode:
            keyState.keyValues[k] = True

def keyReleased():
    global keyState
    for k in range(0,len(keyState.keyList)):
        if keyState.keyList[k] == keyCode:
            keyState.keyValues[k] = False