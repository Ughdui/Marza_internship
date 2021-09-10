import random
import pymel.core as pm

def copyobj(ws):
    obj_scale=ws['float1'].getValue()
    obj_rotate=ws['float2'].getValue()

    S_obj=pm.selected(fl=True)
    getpos=pm.xform(S_obj, q=True, ws=True, t=True)
    getnum=pm.xform(S_obj, q=True, ws=True, t=True)
    #print (getpos)
    #print (len(getnum)/3)

    for i in range(len(getnum)/3):
        pm.select(ws['obj'])
        x=getpos[i*3]
        y=getpos[i*3+1]
        z=getpos[i*3+2]
        pm.duplicate()
        ranscale=random.uniform(obj_scale-1, obj_scale+1)
        ranrotate=random.uniform(obj_rotate-20, obj_rotate+20)

        if ws['cb1'].getValue():
            pm.scale([ranscale, ranscale, ranscale])
        if ws['cb2'].getValue():
            pm.rotate([ranrotate, ranrotate, ranrotate])    
        pm.move(x, y, z, ws=True)


def selectedobj(ws):
    ws['obj']=pm.selected()
    
def makeWindow():
    ws={}  
    with pm.window(title='window'):
        with pm.autoLayout():
            with pm.autoLayout():
                ws={}
                ws['cb1']=pm.checkBox(label='random scale')
                ws['cb2']=pm.checkBox(label='random rotate')
                ws['float1']=pm.floatSliderGrp(label='scale', field=True, min=0.0, max=10.0, step=0.1, value=1.0)
                ws['float2']=pm.floatSliderGrp(label='rotate', field=True, min=0.0, max=360.0, step=0.1, value=0.0)
            with pm.horizontalLayout():
                pm.button(label='selectedobj', command =pm.Callback(selectedobj,ws))
                pm.button(label='copyobj', command =pm.Callback(copyobj,ws))
            
makeWindow()

