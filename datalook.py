
# coding: utf-8

import sys

import numpy
import matplotlib.pyplot


#filename= sorted (glob.glob('data/weather*.csv'))
#filename= filename [0:3] #takes 01, 02, 03 files from data/weather only


def analyse (filename, outfile=None):
    data= numpy.loadtxt (fname=filename, delimiter= ',')
     #create a wide figure to hold the subplots
    fig = matplotlib.pyplot.figure (figsize=(10.0, 3.0))

    #create placeholders for plots
    subplot1= fig.add_subplot(1,3,1
                        )
    subplot2= fig.add_subplot(1,3,2)
    subplot3= fig.add_subplot(1,3,3)

    subplot1.set_ylabel('average')
    subplot1.plot(numpy.mean(data, axis=0))

    subplot2.set_ylabel('min')
    subplot2.plot(numpy.min(data, axis=0))

    subplot3.set_ylabel('max')
    subplot3.plot(numpy.max(data, axis=0))

    fig.tight_layout()
   # matplotlib.pyplot.show()
    
    if outfile is None:
        matplotlib.pyplot.show()
    else:
        matplotlib.pyplot.savefig(outfile)


# In[26]:

def detect_problems (filename):
    """Some of our temperature files have problems, check for these
       
       This function reads a file (filename arguent) and reports on 
       odd looking maxima and minima that add up to zero. this seems
       to happen when the sensors break.
       The function does not return any data.
    """
    data= numpy.loadtxt (fname=filename, delimiter= ',')
    if numpy.max (data, axis=0)[0] ==0 and numpy.max (data, axis=0)[20]==20:
        print ("suspicious looking maxima") #if the first max value is 0 and the 20th one is 20c
    elif numpy.sum (numpy.min(data, axis=0))==0:
        print ("minima add up to zero")
    else:
        print ("data looks ok")


# In[22]:

if __name__=="__main__":

    print ("Running", sys.argv[0])
    print (sys.argv[1])
    analyse (sys.argv[1], outfile=sys.argv[2])
    detect_problems (sys.argv[1])


