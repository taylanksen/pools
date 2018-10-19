#!/usr/bin/env python3
"""
-------------------------------------------------------------------------------
Simple example on how python's concurrent.futures can be used to parallelize,
for example, processing multiple files with os.system calls.
-------------------------------------------------------------------------------
"""

import concurrent.futures as cf
import glob
import os


NUM_CPU = 2 # use None to use all CPUs 

def worker(f):
    print('im am the worker:', f)
    os.system('echo os call')
    os.system('sleep 5')
    return 'worker ' + f + ' completed'


if __name__ == '__main__':
    args = glob.glob('test/*')
    with cf.ProcessPoolExecutor(max_workers=NUM_CPU) as ex:       
        for arg,result in zip(args, ex.map(worker,args)):
            print('worker returned (arg:%s, result: %s)' %(arg, result))
    print('all processes completed')

