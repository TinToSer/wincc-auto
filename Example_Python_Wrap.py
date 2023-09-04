#jay maa shaarde
#Developed by TinToSer for Mankind

import subprocess

winccpth="WinCRW.exe"
#Here taglst and tagv are list of tags and corresponding values
def tagset(taglst,tagv):
        cmdd=winccpth+" -t "+";".join(taglst)+" -v "+";".join([ k for k in tagv ])
        retdta=subprocess.Popen(cmdd,stdout=subprocess.PIPE,shell=True).communicate()

def tagqry(taglst):
    cmdd=winccpth+" -t "+";".join(taglst)+" -v "+";".join([ "NULL" for k in taglst ])
    retdta=subprocess.Popen(cmdd,stdout=subprocess.PIPE,shell=True).communicate()
    retdta=retdta[0].strip()
    retdt=retdta.split(";")
    retdict={}
    for rr in retdt:
        rr=rr.split(":")
        retdict[rr[0]]=rr[1]
    return retdict
