import pymel.core as pm

pm.window()
pm.paneLayout()

namelist=pm.ls(assemblies=True, ca=False, v=True)
List=pm.textScrollList(ams=True, append=namelist)
print(len(List)-1)

pm.showWindow()
