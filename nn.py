#from libs.pybrain.structure import FeedForwardNetwork
import os, sys
from scipy.io import loadmat

#current_dir = os.path.dirname(os.path.abspath(__file__))
#sys.path.append(os.path.join(current_dir, 'libs'))

from pybrain.tools.shortcuts     import buildNetwork
from pybrain.structure           import SigmoidLayer, TanhLayer, SoftmaxLayer
from pybrain.datasets            import ClassificationDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.utilities           import percentError
from pybrain.tests.helpers import gradientCheck

n_in = 400
n_hidden = 25
n_classes = 9

def main():
    config = loadmat('nn/config.mat')
    cache = config['data_folder'][0].replace('../', '')+'/'+config['cache_file'][0]
    if not os.path.exists(cache):
        raise Exception('Cache file ('+cache+') is missing and has to be generated first! Run octave version...')
    mat = loadmat(cache)
    X = mat['X']
    y = mat['y']
    
    ds = ClassificationDataSet(n_in, 1, nb_classes=n_classes)
    for (x, y) in zip(X, y):
        ds.addSample(x, [y-1])
    # ds.assignClasses()
    
    tstdata, trndata = ds.splitWithProportion(0.25)
    trndata._convertToOneOfMany(bounds=[0, 1])
    tstdata._convertToOneOfMany(bounds=[0, 1])
    
    trndata.calculateStatistics()
    print "Train data classes", trndata.classHist
    tstdata.calculateStatistics()
    print "Test data classes", tstdata.classHist
    
    print "Number of training patterns: ", len(trndata)
    print "Input and output dimensions: ", trndata.indim, trndata.outdim
    # print "First sample (input, target, class):"
    # print trndata['input'][0], trndata['target'][0], trndata['class'][0]
    
    net = buildNetwork(trndata.indim, n_hidden, trndata.outdim, bias=True, hiddenclass=SigmoidLayer, outclass=SoftmaxLayer) #, recurrent=True)
    trainer = BackpropTrainer(net, trndata)

    for i in xrange(50):
        # print trainer.train()
        # train the network for 1 epoch
        trainer.trainEpochs(1)
        # evaluate the result on the training and test data
        trnresult = percentError(trainer.testOnClassData(), trndata['class'])
        tstresult = percentError(trainer.testOnClassData(dataset=tstdata), tstdata['class'])
        print "epoch: %4d" % trainer.totalepochs, \
              "  train error: %5.2f%%" % trnresult, \
              "  test error: %5.2f%%" % tstresult
    # print trainer.trainUntilConvergence()
    
main()
