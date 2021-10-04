import pymel.core as pm

def make():
    normal=pm.polyNormalPerVertex(q=True,xyz=True)

    print (normal)

make()