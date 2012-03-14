#from libs.pybrain.structure import FeedForwardNetwork
import os, sys
import scipy.io

#current_dir = os.path.dirname(os.path.abspath(__file__))
#sys.path.append(os.path.join(current_dir, 'libs'))

from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection

def main():
    mat = scipy.io.loadmat('data/cache.mat')
    X = mat['X']
    #print X[0]
    y = mat['y']
    config = scipy.io.loadmat('nn/config.mat')
    n = FeedForwardNetwork()
    inLayer = LinearLayer(config['input_layer_size'][0][0])
    hiddenLayer = SigmoidLayer(config['hidden_layer_size'][0][0])
    outLayer = LinearLayer(config['num_labels'][0][0])
    n.addInputModule(inLayer)
    n.addModule(hiddenLayer)
    n.addOutputModule(outLayer)
    in_to_hidden = FullConnection(inLayer, hiddenLayer)
    hidden_to_out = FullConnection(hiddenLayer, outLayer)
    n.addConnection(in_to_hidden)
    n.addConnection(hidden_to_out)
    n.sortModules()
    print n
    print n.activate(X[0])
    

main()
