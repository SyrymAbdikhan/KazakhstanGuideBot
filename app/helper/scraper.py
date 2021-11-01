
import os


def get_data(root):
    rootname = root.split('/')[-1]

    result = {rootname: {'files': []}}
    for name in os.listdir(root):
        path = os.path.join(root, name)
        if os.path.isdir(path):
            result[rootname] = result[rootname] | get_data(path)
        else:
            result[rootname]['files'].append(os.path.split(path)[-1])
    return result


def get_key(data, i):
    keys = sorted(data.keys())
    if 'files' in keys: keys.remove('files')
    return keys[i]


def index_to_path(arr):
    path = []
    cdata = data.copy()
    for el in arr:
        key = get_key(cdata.copy(), int(el))
        path.append(key)
        cdata = cdata[key]
    return path


def get_subdirs(arr, fromindex=0):
    cdata = data.copy()
    for el in arr:
        if fromindex:
            el = get_key(cdata.copy(), int(el))
        cdata = cdata[el]
    return cdata.copy()


data = get_data('./app/data')
