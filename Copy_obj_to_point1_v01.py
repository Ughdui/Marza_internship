import random
import pymel.core as pm

def copyobj(ws):
    obj_scale=ws['float1'].getValue()#scaleを調整するSlider
    obj_rotate=ws['float2'].getValue()#rotateを調整するSlider

    S_obj=pm.selected(fl=True)#vertexを選択する
    getpos=pm.xform(S_obj, q=True, ws=True, t=True)#vertexの位置をgetする
    getnum=pm.xform(S_obj, q=True, ws=True, t=True)#vertexの数をgetする
    #print (getpos)
    #print (len(getnum)/3)

    for i in range(len(getnum)/3):#len(getnum)をgetした数字は座標の数字の個数、/3にするとvertexの個数の数字
        x=getpos[i*3]
        y=getpos[i*3+1]
        z=getpos[i*3+2]
        duplicated=pm.duplicate(ws['obj'])#この前選択したobjectを複製する
        ranscale=random.uniform(obj_scale-1, obj_scale+1)
        #(obj_scale-1, obj_scale+1)の範囲はRandom_Scaleの範囲
        ranrotate=random.uniform(obj_rotate-20, obj_rotate+20)
        #(obj_rotate-20, obj_rotate+20)の範囲はRandom_Rotateの範囲

        if ws['cb1'].getValue():
            pm.scale(duplicated, [ranscale, ranscale, ranscale])
        if ws['cb2'].getValue():
            pm.rotate(duplicated, [ranrotate, ranrotate, ranrotate])    
        pm.move(x, y, z, duplicated, ws=True)


def selectedobj(ws):
    ws['obj']=pm.selected()#選択したobjectを覚える
    
def makeWindow():
    ws={}  
    with pm.window(title='window'):
        with pm.autoLayout():
            with pm.autoLayout():
                ws={}
                pm.text(label='selectedobjはcopyしたいobjectをget')
                pm.text(label='copyobjは選択しているvertexにcopy')
                pm.text(label='random scaleにチェックを入れるとobjectのscaleをrandomにcopy')
                pm.text(label='random rotateにチェックを入れるとobjectのrotateをrandomにcopy')
                pm.setParent('..')
                ws['cb1']=pm.checkBox(label='random scale')
                ws['float1']=pm.floatSliderGrp(label='scale', field=True, min=0.0, max=10.0, step=0.1, value=1.0)
                pm.setParent('..')
            with pm.autoLayout():
                ws['cb2']=pm.checkBox(label='random rotate')
                ws['float2']=pm.floatSliderGrp(label='rotate', field=True, min=0.0, max=360.0, step=0.1, value=0.0)
                pm.setParent('..')
            with pm.horizontalLayout():
                pm.button(label='selectedobj', command =pm.Callback(selectedobj,ws))
                pm.button(label='copyobj', command =pm.Callback(copyobj,ws))
            
makeWindow()

