import os

if __name__ == '__main__':
    objs = []
    files = os.listdir('.')
    for f in files:
        if f.find('obj') > 0:
            objs.append(f)

    with open('/home/dzp/Project_UPEN/pytorch_6dof-graspnet/shapenet_ids_sem.txt', 'r') as ids:
        lines = ids.readlines()
        for line in lines:
            match = False
            for obj in objs:
                if line[:-1] in obj:
                    match = True
                    break
            if not match:
                print('{} not match'.format(line))
