import platform

if platform.system() is 'Windows':
    print 'Windows'
elif platform.system() is 'Linux':
    print 'Linux'
else:
    print 'System unknown'