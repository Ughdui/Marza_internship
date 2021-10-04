import pymel.core as pm

def make():
    normal=pm.polyNormalPerVertex(q=True,xyz=True)
    x=normal[3]
    y=normal[4]
    z=normal[5]
    pm.polyCone()
    pm.rotate(x, y, z, ws=True)
    print (normal)

make()