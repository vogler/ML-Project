#from libs.pybrain.structure import FeedForwardNetwork
import os, sys
import scipy.io

#current_dir = os.path.dirname(os.path.abspath(__file__))
#sys.path.append(os.path.join(current_dir, 'libs'))

from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import ClassificationDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.utilities import percentError
from pybrain.tools.validation import CrossValidator


config = scipy.io.loadmat('nn/config.mat')
input_layer_size = config['input_layer_size'][0][0]
hidden_layer_size = config['hidden_layer_size'][0][0]
num_labels = int(config['num_labels'][0][0])
mat = scipy.io.loadmat('data/cache.mat')
X = mat['X']
y = mat['y']

def prepare_dataset():
    alldata = ClassificationDataSet(input_layer_size, 1, nb_classes=num_labels)
    for (i,j) in zip(X,y):
        alldata.addSample(i,j-1)
    return alldata
    
def get_2layer_nn():
    return buildNetwork(input_layer_size, hidden_layer_size, num_labels)
    
def main():
    alldata = prepare_dataset()

    #trainer = BackpropTrainer(n, alldata)
    #alldata._convertToOneOfMany()
    #CrossValidator(trainer, 
    
    tstdata, trndata = alldata.splitWithProportion(0.25)
    trndata._convertToOneOfMany()
    tstdata._convertToOneOfMany()

    trndata.calculateStatistics()
    print trndata.classHist
    
    n = get_2layer_nn()
    trainer = BackpropTrainer(n, dataset=trndata, verbose=True)
    trainer.trainEpochs(50)
    trnresult = percentError( trainer.testOnClassData(), trndata['class'] )
    tstresult = percentError( trainer.testOnClassData(dataset=tstdata ), tstdata['class'] )
    
    print "epoch: %4d" % trainer.totalepochs, \
          "  train error: %5.2f%%" % trnresult, \
          "  test error: %5.2f%%" % tstresult

main()
