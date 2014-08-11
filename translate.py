import subprocess
import os

path = os.getcwd()
arg = '*vi.po'

list_path = subprocess.check_output(['find', path, '-name', arg], shell=False)

sum_path = []
print '-' * 100
list_all = list_path.split('\n')
print path

print '-' * 100
print 'hi'

subprocess.check_output(['mkdir', path + '/translate'])
trans_path = path + '/translate'
 
for path in list_all:
    try:
        print '----> path --> %s' % path
        path_ls = path.split('/')[6]
        print 'open --> %s' % path
        ifile = open(path, 'rb')
 
        path_out = trans_path + '/' + path_ls + '.po'
 
        print 'outfile --> %s' % path_out
        ofile = open(path_out, 'wb')
        ofile.write(ifile.read())
        ofile.close()
        ifile.close()
        #
        print 'finish --> %s' % trans_path
    except Exception, e:
        print path
        print e
        continue





