import os

def dir_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def memory(request):
    if not request.user:
        return {}
    else:
        dir = os.path.join('app/media', request.user.username)
        total_size = 52400000
        used_size = dir_size(dir)
        free_size = total_size - used_size
        return {'total_size': total_size, 'used_size': used_size, 'free_size': free_size}

def files_count(request):
    if not request.user:
        return {}
    else:
        dir = os.path.join('app/media', request.user.username)
        return {'files_count': len(os.listdir(dir))}
