import os
path='basic_app/pdf/'
def ren_pdf(x,y):
    if(y[-3:]!='pdf'):
        os.rename(path+x,path+y+'.pdf')
    else:
        os.rename(path+x,path+y)