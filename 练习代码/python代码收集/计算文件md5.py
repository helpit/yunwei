import hashlib
 
 
def md5_file(file):
    _buffer = 1024 * 8
    m = hashlib.md5()
    f = open(file,'rb')
    while True:
        data = f.read(_buffer)
        m.update(data)
        if not data:
            break
    file.close()
    return m.hexdigest()
