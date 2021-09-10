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
        #if checkBox1.getValue():
        ranscale=random.uniform(obj_scale-1, obj_scale+1)
        ranRotate=random.uniform(obj_rotate-20, obj_rotate+20)

        pm.rotate([ranRotate, ranRotate, ranRotate])
        pm.scale([ranscale, ranscale, ranscale])
        pm.move(x, y, z, ws=True)


def selectedobj(ws):
    ws['obj']=pm.selected()
    
def makeWindow():
    ws={}  
    with pm.window(title='window'):
        with pm.autoLayout():
            with pm.autoLayout():
                ws={}
                #checkBox1=pm.checkBox(label='random')
                ws['float1']=pm.floatSliderGrp(label='scale', field=True, min=0.0, max=10.0, step=0.1, value=1.0)
                ws['float2']=pm.floatSliderGrp(label='scale', field=True, min=0.0, max=360.0, step=0.1, value=30.0)
            with pm.horizontalLayout():
                pm.button(label='selectedobj', command =pm.Callback(selectedobj,ws))
                pm.button(label='copyobj', command =pm.Callback(copyobj,ws))
            
makeWindow()

