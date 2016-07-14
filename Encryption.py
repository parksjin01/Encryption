import random
import hashlib
import mimetypes
import binascii
import os

def already_en(filename):
    with open('/Users/Knight/nonononon', 'rt') as f:
        while True:
            tar=f.readline()
            if not tar:
                break
            if filename in tar:
                return True
    return False

def recover_en(value, key):
    res=value+key
    if res>255:
        res-=256
    return res

def recover_de(value, key):
    res=value-key
    if res<0:
        res+=256
    return res

def Encryption(filename):
    isText=(mimetypes.guess_type(filename)[0]=='text/plain')
    if not already_en(filename):
        if not isText:
            try:
                seed=random.randint(1, 1000)
                l=list(str(int(hashlib.sha1(str(seed)).hexdigest(), 16)))
                l=map(int, l)
                key=sum(l)%200
                home='/Users/Knight'
                with open(home+'/nonononon', 'at') as f:
                    f.write(filename+';'+str(key)+'\n')
                with open(filename, 'rb') as f:
                    with open('tmp', 'wb') as w:
                        for i in range(10000):
                            tar=int(binascii.hexlify(f.read(1)), 16)
                            w.write(str(chr(recover_en(tar, key))))
                with open('tmp', 'rb') as f:
                    with open(filename, 'r+') as w:
                        while True:
                            tar=f.readline()
                            if not tar:
                                break
                            w.write(tar)
                os.remove('tmp')
                print 'Finished'
            except Exception, err:
                print 'Error! ', err

        else:
            try:
                seed=random.randint(1, 1000)
                l=list(str(int(hashlib.sha1(str(seed)).hexdigest(), 16)))
                l=map(int, l)
                key=sum(l)
                home='/Users/Knight'
                with open(home+'/nonononon', 'at') as f:
                    f.write(filename+';'+str(key)+'\n')
                with open(filename, 'rt') as f:
                    with open('tmp', 'wt') as w:
                        while True:
                            tar=list(f.readline())
                            tar=map(ord, tar)
                            for i in tar:
                                w.write(str(i+key)+'\n')
                            if not tar:
                                break
                print 'Finished'
                os.rename('tmp', filename)
            except Exception, err:
                print 'Error ', err
    else:
        print filename+' is already encrypted'


def Decryption(filename):
    isText=(mimetypes.guess_type(filename)[0]=='text/plain')
    home='/Users/Knight'
    remain=''
    if already_en(filename):
        if isText:
            try:
                with open(home+'/nonononon', 'rt') as f:
                    while True:
                        seed=f.readline()
                        tempFilename=seed.split(';')[0]
                        if filename==tempFilename:
                            key=int(seed.split(';')[1].strip())
                            remain+=f.read()
                            break
                        else:
                            remain+=seed
                with open(home+'/nonononon', 'wt') as f:
                    f.write(remain)
                with open(filename, 'rt') as f:
                    with open('tmp', 'wt') as w:
                        while True:
                            tar=f.readline().strip()
                            if not tar:
                                break
                            tar=int(tar)
                            w.write(str(chr(tar-key)))
                os.rename('tmp', filename)
                print 'Finished'
            except Exception, err:
                print 'Error! ', err
        else:
            with open(home+'/nonononon', 'rt') as f:
                    while True:
                        seed=f.readline()
                        tempFilename=seed.split(';')[0]
                        if filename==tempFilename:
                            key=int(seed.split(';')[1].strip())
                            remain+=f.read()
                            break
                        else:
                            remain+=seed
            with open(home+'/nonononon', 'wt') as f:
                f.write(remain)
            try:
                with open(filename, 'rb') as f:
                    with open('tmp', 'wb') as w:
                        for i in range(10000):
                            tar=f.read(1)
                            w.write(tar)

                with open('tmp', 'rb') as f:
                    with open(filename, 'r+') as w:
                        for i in range(10000):
                            tar=int(binascii.hexlify(f.read(1)), 16)
                            w.write(str(chr(recover_de(tar, key))))
                os.remove('tmp')
                print 'Finished'
            except Exception, err:
                print 'Error ', err
    else:
        print filename+' is not yet encrypted'


def Key_gen(l):
    avail='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789'
    avail=list(avail)
    key=[]
    ret=''
    for i in xrange(l*3):
        r=random.randint(0, len(avail)-1)
        key.append(avail.pop(r))
    for i in xrange(l):
        ret+=''.join(key[i*3:(i+1)*3])+'-'
    return ret[:-1]

def login():
    with open(home+'/nonononon', 'rt') as f:
        pw=(f.readline().strip())
        user=(raw_input('Please type password: ').strip())
        if user==pw:
            return True
        else:
            #return print user, pw
            return False

if __name__ == '__main__':
    home='/Users/Knight'
    try:
        open(home+'/nonononon', 'r')
    except:
        if not os._exists(home+'/nonononon'):
            while True:
                pw=raw_input('Your first use this, Please make your own password: ')
                rpw=raw_input('Please type again: ')
                if pw==rpw:
                    with open(home+'/nonononon', 'wt') as f:
                        f.write(pw+'\n')
                    break


    op=raw_input('If you want login please tpye "l", If you want to change password please type "c": ')
    if op=='c':
        while True:
            if raw_input('Please type current password: ') != open(os.getcwd()+'/tnonigntbiu', 'rt').readline().strip():
                print 'Current password is wrong'
                continue
            pw=raw_input('You want to change password, Please make your own password: ')
            rpw=raw_input('Please type again: ')
            if pw==rpw:
                with open(home+'/nonononon', 'rt') as f:
                    f.readline()
                    remain=f.read()
                with open(home+'/nonononon', 'wt') as f:
                    f.write(pw+'\n')
                    if remain:
                        f.write(remain)
                break

    if op=='l':
        if login():
            oper=raw_input('If you want Encryption, please type e, If you want Decryption, please type d: ')
            if oper=='e':
                Encryption(raw_input('Please Type File Name: '))
            elif oper=='d':
                Decryption(raw_input('Please Type File Name: '))

        else:
            print 'Password is wrong'
