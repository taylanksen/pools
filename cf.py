import concurrent.futures as cf
import glob
import os


NUM_CPU = 2
def worker(f):
    print('im am the worker:', f)
    os.system('echo os call')
    os.system('sleep 5')
    return 'worker: ' + f + ' complete'

def main():
    files = glob.glob('test/*')

    with cf.ProcessPoolExecutor(max_workers=NUM_CPU) as ex:       
        for f,result in zip(files, ex.map(worker,files)):
            print('result returned from %s: %s' %(f, result))

if __name__ == '__main__':
    main()
