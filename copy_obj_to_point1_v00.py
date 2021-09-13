import pymel.core as pm

def copy_obj(name, x, y, z):
    copy=pm.duplicate(name)
    pm.move(copy,x,y,z,ws=True)

def get_positions():
    S_obj=pm.selected(fl=True)
    getpos=pm.xform(S_obj, q=True, ws=True, t=True)
    pos_list=[]
    for i in range(len(getpos)/3):
        x=getpos[i*3]
        y=getpos[i*3+1]
        z=getpos[i*3+2]
        pos_list.append((x, y, z))
    return pos_list
    

def do(name):
    for x, y, z in get_positions():
        #copy_obj(name, x, y, z)
        print(x, y, z)
        copy_obj(name, x, y, z)
do("pSphere1")
