import pymel.core as pm

def copy_obj(name, x, y, z):
    copy=pm.instance(name, leaf=True)
    pm.move(x, y, z, copy, ws=True)

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

def return_name(name):
    n=0
    numlist=pm.textScrollList('Obj_name', q=True, si=True)
    for x, y, z in get_positions():
        L_name=name[n%len(numlist)]
        copy_obj(L_name, x, y, z)
        n+=1
        

def copy_name_obj():

    namelist=pm.textScrollList('Obj_name', q=True, si=True)
    #print(len(namelist))
    return_name(namelist)


def makeWindow():    
    with pm.window(title='window'):
        with pm.autoLayout():
            pm.text(label='object name',h=100)

            allobjlist=pm.ls(assemblies=True, ca=False, v=True)
            pm.textScrollList('Obj_name', numberOfRows=8, ams=True, h=200, append=allobjlist)
            
            pm.button(label='copy', h=90, command =pm.Callback(copy_name_obj))
            
makeWindow()
