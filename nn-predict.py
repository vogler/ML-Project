from pybrain.tools.customxml import NetworkReader
from scipy.io import loadmat

def main():
    net = NetworkReader.readFrom('net')
    input = loadmat('octave/inputAndPredictedValues.mat')
    X = input['X']
    field = input['field']
    for i in range(0,len(X)):
        r = net.activate(X[i])
        #print field[i][0]
        print "%d - %d" %(field[i][0], r.argmax()+1)
        
main()
