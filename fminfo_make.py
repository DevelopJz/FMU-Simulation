import sys
import fmpy as fm

fmu="./FMU_TEST.fmu"

f=open("./fmu_info.txt","w",encoding="utf-8")
stdout=sys.stdout
sys.stdout=f
fm.dump(fmu)
f.close()
sys.stdout=stdout
