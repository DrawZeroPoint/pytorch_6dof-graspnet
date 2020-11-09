import os
import subprocess


def run_simplify(f):
    """
    """
    st = subprocess.check_output(['./simplify', '-i', f, '-o', f, '-m', '-r', '0.02'])
    st_str = st.decode('utf-8')
    print(st_str)


if __name__ == '__main__':
    files = os.listdir('.')
    for f in files:
        if f.find('obj') < 0:
            continue
        run_simplify(f)
