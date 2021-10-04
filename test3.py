import random
import pymel.core as pm

def copy_obj(name, x, y, z):
    copy=pm.instance(name, leaf=True)
    #scale
    start_num=pm.floatSliderGrp('s_scale', q=True, value=True)
    over_num=pm.floatSliderGrp('o_scale', q=True, value=True)
    obj_scale=random.uniform(start_num, over_num)
    pm.xform(copy, s=[obj_scale, obj_scale, obj_scale], absolute=True)
    #move
    pm.move(x, y, z, copy, ws=True)

    #rotate
    #pm.xform(copy, s=[obj_scale, obj_scale, obj_scale], absolute=True)
    abc=pm.polyNormalPerVertex(query=True, xyz=True)
    pm.rotate(copy, abc[0], abc[1], abc[2],ws=True) 

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
    
def copy_name_obj(ui):
    n=0
    numlist=pm.textScrollList(ui, q=True, si=True)
    if len(numlist) == 0:
        return
    for x, y, z in get_positions():
        L_name=numlist[n%len(numlist)]
        copy_obj(L_name, x, y, z)
        n+=1


def add_name(ui):
    sel=pm.ls(sl=True)
    abc=pm.textScrollList(ui, e=True, append=sel)
    print(abc)

def remove_name(ui):
    for obj in pm.textScrollList(ui,q=True,si=True):
        pm.textScrollList(ui,e=True,ri=obj)
    

def makeWindow():    
    with pm.window(title='window'):
        with pm.autoLayout():
            pm.text(label='object name')
            
            ui=pm.textScrollList('Obj_name', numberOfRows=8, ams=True, h=200)

            with pm.gridLayout()as gr:
                gr.setNumberOfColumns(2)
                gr.setCellWidth(90)
                gr.setCellHeight(30)
                pm.button(label='add', h=90, command =pm.Callback(add_name,ui))
                pm.button(label='remove', h=90, command =pm.Callback(remove_name,ui))
            with pm.frameLayout(label='scale'):    
                with pm.autoLayout():
                    pm.floatSliderGrp('s_scale', label='start', field=True, min=0.0, max=10.0, value=1.0)
                    pm.floatSliderGrp('o_scale', label='over', field=True, min=0.0, max=10.0, value=1.0)


            pm.button(label='copy', h=90, command =pm.Callback(copy_name_obj,ui))
                
makeWindow()
