import os
import subprocess


def run_manifold(f):
    """
    """
    st = subprocess.check_output(['./manifold', f, f, '-s'])
    st_str = st.decode('utf-8')
    if '[-s]' in st_str:
        print('failed')
        return False
    else:
        return True


if __name__ == '__main__':
    files = os.listdir('.')
    for f in files:
        if f.find('obj') < 0:
            continue
        print(f)
        run_manifold(f)
