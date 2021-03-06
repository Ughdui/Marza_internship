import pymel.core as pm

def copy_obj(name, x, y, z):
    copy=pm.duplicate(name)
    pm.move(x,y,z,copy,ws=True)

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
        #print(x, y, z)
        copy_obj(name, x, y, z)

def getname():
    objname=pm.textField('Obj_name', q=True, text=True)
    do(objname)

def makeWindow():    
    with pm.window(title='window'):
        with pm.autoLayout():
            pm.text(label='object name')
            pm.textField('Obj_name',text="")
            pm.button(label='copy', command =pm.Callback(getname))
            
makeWindow()




