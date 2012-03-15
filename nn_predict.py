from pybrain.tools.customxml import NetworkReader
from scipy.io import loadmat

def predict(output=False):
    net = NetworkReader.readFrom('net.xml')
    input = loadmat('octave/inputAndPredictedValues.mat')
    X = input['X']
    field = input['field']
    pPyBrain = []
    for i in range(0,len(X)):
        r = net.activate(X[i])
        #print field[i][0]
        pPyBrain.append(r.argmax()+1)
        if(output): print "%d - %d" %(field[i][0], r.argmax()+1)
    return pPyBrain
    
if __name__ == '__main__':
    predict(True)