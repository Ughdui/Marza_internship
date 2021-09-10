import pymel.core as pm

def copyobj(name):

    S_obj=pm.selected(fl=True)
    getpos=pm.xform(S_obj, q=True, ws=True, t=True)
    getnum=pm.xform(S_obj, q=True, ws=True, t=True)

    for i in range(len(getnum)/3):
        name=pm.sphere()
        x=getpos[i*3]
        y=getpos[i*3+1]
        z=getpos[i*3+2]
        pm.move(x, y, z, name, ws=True)
         
copyobj("pSphere1")
