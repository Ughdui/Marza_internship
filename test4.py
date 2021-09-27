import pymel.core as pm
def copy_obj(name):
    pm.instance(name, leaf=True)

def copy_name_obj():


    uinames=['Obj_name']
    namelist=[]
    for uiname in uinames :
        name=pm.textScrollList(uiname, q=True, si=True)
        namelist.append(name)
    print (namelist)
    #copy_obj(namelist)


def makeWindow():    
    with pm.window(title='window'):
        with pm.autoLayout():
            pm.text(label='object name',h=100)
            with pm.paneLayout():
                namelist=pm.ls(assemblies=True, ca=False, v=True)
                pm.textScrollList('Obj_name', numberOfRows=8, ams=True, h=200, append=namelist)
               
            pm.button(label='copy', h=90, command =pm.Callback(copy_name_obj))
           
makeWindow()
