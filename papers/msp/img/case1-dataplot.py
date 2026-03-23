import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
fig = plt.figure()
import numpy as np 
import json
import pprint
import random 
import math
from matplotlib import rc

rc('font',**{'family':'sans-serif','sans-serif':['Computer Modern Roman']})
rc('text', usetex=True)


lum = []
gamma = []
gamma2 = []
lum2 = []
errorhigh2 =  []  
errorlow2 = []

E1 = []
Spec1 = []

E2 = []
Spec2 = []
errorhigh2 = []
errorlow2 = []  
error2 = []
errorcen2 = []

E3 = []
Spec3 = []
errorhigh3 = []
errorlow3 = []  
error3 = []
errorcen3 = []

E4 = []
Spec4 = []

E5 = []
Spec5 = []

E6 = []
Spec6 = []

E7 = []
Spec7 = []

E8 = []
Spec8 = []
errorhigh8 = []
errorlow8 = []  
error8 = []
errorcen8 = []

E9 = []
Spec9 = []
errorhigh9 = []
errorlow9 = []  
error9 = []
errorcen9 = []

E10 = []
Spec10 = []
errorhigh10 = []
errorlow10 = []  
error10 = []
errorcen10 = []

E11 = []
Spec11 = []
errorhigh11 = []
errorlow11 = []  
error11 = []
errorcen11 = []

gammaupper = []
gammalower = []
lumupper = []
lumlower = []
lumerrcen = []
lumerror = []
gammaerror = []
gammaerrcen = []

gamma2 = []
twosigmalower = []
onesigmalower = []
onesigmaupper = []
twosigmaupper = []


####################


#####################
#####################

infile = open('../RUN2/forfig.out', 'r')
for line in infile.readlines():
        params = line.split()
        
        gamma +=  [float(params[0])]
        gammaupper +=  [float(params[1])]
        gammalower +=  [float(params[2])]
        lum += [float(params[3])]  
        lumupper += [float(params[4])]  
        lumlower += [float(params[5])]  
        lumerrcen += [float(params[5])] 
        lumerror += [float(params[5])]
        gammaerrcen += [float(params[5])]
        gammaerror  += [float(params[5])]
        
for x in range(0, len(gamma)):
        gamma[x] = (gamma[x]/1000.0)        
        gammaupper[x] = (gammaupper[x]/1000.0)        
        gammalower[x] = (gammalower[x]/1000.0)       


for x in range(0, len(gamma)):
        lumerrcen[x] = (lumupper[x]+lumlower[x])*0.5
        lumerror[x] = (lumupper[x]-lumlower[x])*0.5
        gammaerrcen[x] = (gammaupper[x]+gammalower[x])*0.5
        gammaerror[x] = (gammaupper[x]-gammalower[x])*0.5

                
plt.scatter(gamma,lum,s=10,marker='o',color='red')

plt.errorbar(gamma,lumerrcen,yerr=lumerror,color='red',linewidth=1.0,linestyle='None',capsize=1)  

plt.errorbar(gammaerrcen,lum,xerr=gammaerror,color='red',linewidth=1.0,linestyle='None',capsize=1)  
#####################

infile = open('bandsforplot-case1.out', 'r')
for line in infile.readlines():
        params = line.split()
        
        gamma2 += [float(params[0])]
        twosigmalower += [float(params[1])]
        onesigmalower += [float(params[2])]
        onesigmaupper += [float(params[3])]
        twosigmaupper += [float(params[4])]
        
plt.fill_between(gamma2,onesigmaupper,onesigmalower,color='grey', alpha=0.5)

plt.fill_between(gamma2,twosigmaupper,twosigmalower,color='grey', alpha=0.25)


#####################

#infile = open('Stellar_Encounter_Rate_Errors.dat', 'r')
#for line in infile.readlines():
#        params = line.split()
        
#        gamma2 +=  [float(params[0])]    
#        lum2 += [float(params[1])]
#        errorhigh2 +=  [float(params[4])]  
#        errorlow2 +=  [float(params[5])]
#        errorcen2  +=  [float(params[3])]
#        error2  +=  [float(params[3])]

#for x in range(0, len(gamma2)):
#        gamma2[x] = gamma2[x]/1000.0        
  
        
#for x in range(0, len(gamma2)):
#         errorcen2[x] = 0.5*(gamma2[x]+errorhigh2[x]+gamma2[x]-errorlow2[x])   
#         error2[x] =  0.5*(errorhigh2[x]+errorlow2[x])

        
        
#plt.errorbar(errorcen2,lum,errorcen2,error2,color='red',linewidth=1.0,linestyle='None')        





#####################


#infile = open('COSMICRAYDATA/TIBET.dat', 'r')
#for line in infile.readlines():
#        params = line.split()
        
#        E2 +=  [float(params[0])]    
#        Spec2 += [float(params[1])]
#        errorhigh2 += [float(params[2])]
#        errorlow2 +=  [float(params[3])]
#        error2 += [float(params[2])]
#        errorcen2 += [float(params[2])]

#for x in range(0, len(E2)):
#        Spec2[x] = Spec2[x]/E2[x]**0.6
#        errorhigh2[x] = errorhigh2[x]/E2[x]**0.6
#        errorlow2[x] = errorlow2[x]/E2[x]**0.6
        
        
#for x in range(0, len(E2)):
#        errorcen2[x] = 0.5*(errorhigh2[x]+errorlow2[x])
#        error2[x] =  0.5*(errorhigh2[x]-errorlow2[x])


        
        
#plt.scatter(E2,Spec2,s=20,color='lightgrey')

#plt.errorbar(E2,errorcen2,error2,color='lightgrey',linewidth=2.0,linestyle='None')        
  



#####################


#infile = open('COSMICRAYDATA/AKENO.dat', 'r')
#for line in infile.readlines():
#        params = line.split()
        
#        E4 +=  [float(params[0])]    
#        Spec4 += [float(params[1])]  

#for x in range(0, len(E4)):
#        Spec4[x] = Spec4[x]/E4[x]**0.6            
  
#plt.scatter(E4,Spec4,s=40,marker='v',color='darkgrey')



#####################


#infile = open('COSMICRAYDATA/KASCADE.dat', 'r')
#for line in infile.readlines():
#        params = line.split()
        
#        E5 +=  [float(params[0])]    
#        Spec5 += [float(params[1])]  

#for x in range(0, len(E5)):
#        Spec5[x] = Spec5[x]/E5[x]**0.6            
  
#plt.scatter(E5,Spec5,s=20,marker='s',color='grey')


#####################


#infile = open('COSMICRAYDATA/MSU.dat', 'r')
#for line in infile.readlines():
#        params = line.split()
        
#        E6 +=  [float(params[0])]    
#        Spec6 += [float(params[1])]  

#for x in range(0, len(E6)):
#        Spec6[x] = Spec6[x]/E6[x]**0.6            
  
#plt.scatter(E6,Spec6,s=20,marker='*',color='black')


#####################


#infile = open('COSMICRAYDATA/KASCADEGRANDE.dat', 'r')
#for line in infile.readlines():
#        params = line.split()
        
#        E7 +=  [float(params[0])]    
#        Spec7 += [float(params[1])]  
       
#for x in range(0, len(E7)):
#        Spec7[x] = Spec7[x]/E7[x]**0.6    
        
#plt.scatter(E7,Spec7,s=15,marker='D',color='lightgrey')





########################

#infile = open('COSMICRAYDATA/CASAMIA.dat', 'r')
#for line in infile.readlines():
#        params = line.split()
        
#        E3 +=  [float(params[0])]    
#        Spec3 += [float(params[1])]  
#        errorhigh3 += [float(params[2])]
#        errorlow3 +=  [float(params[3])]
#        error3 += [float(params[2])]
#        errorcen3 += [float(params[2])]
        
#for x in range(0, len(E3)):
#        Spec3[x] = Spec3[x]/E3[x]**0.6
#        errorhigh3[x] = errorhigh3[x]/E3[x]**0.6
#        errorlow3[x] = errorlow3[x]/E3[x]**0.6
        
#for x in range(0, len(E3)):
#        errorcen3[x] = 0.5*(errorhigh3[x]+errorlow3[x])
#        error3[x] =  0.5*(errorhigh3[x]-errorlow3[x])
        
        
#plt.scatter(E3,Spec3,s=20,marker='8',color='black')

#plt.errorbar(E3,errorcen3,error3,color='black',linewidth=2.0,linestyle='None')


########################

#infile = open('COSMICRAYDATA/HIRES1.dat', 'r')
#for line in infile.readlines():
#        params = line.split()
        
#        E10 +=  [float(params[0])]    
#        Spec10 += [float(params[1])]  
#        errorhigh10 += [float(params[2])]
#        errorlow10 +=  [float(params[3])]
#        error10 += [float(params[2])]
#        errorcen10 += [float(params[2])]

#for x in range(0, len(E10)):
#        Spec10[x] = Spec10[x]/E10[x]**0.6
#        errorhigh10[x] = errorhigh10[x]/E10[x]**0.6
#        errorlow10[x] = errorlow10[x]/E10[x]**0.6        
        
#for x in range(0, len(E10)):
#        errorcen10[x] = 0.5*(errorhigh10[x]+errorlow10[x])
#        error10[x] =  0.5*(errorhigh10[x]-errorlow10[x])
        
        
#plt.scatter(E10,Spec10,s=10,color='darkgrey')

#plt.errorbar(E10,errorcen10,error10,color='darkgrey',linewidth=2.0,linestyle='None')


########################

#infile = open('COSMICRAYDATA/HIRES2.dat', 'r')
#for line in infile.readlines():
#        params = line.split()
        
#        E11 +=  [float(params[0])]    
#        Spec11 += [float(params[1])]  
#        errorhigh11 += [float(params[2])]
#        errorlow11 +=  [float(params[3])]
#        error11 += [float(params[2])]
#        errorcen11 += [float(params[2])]
        

#for x in range(0, len(E11)):
#        Spec11[x] = Spec11[x]/E11[x]**0.6
#        errorhigh11[x] = errorhigh11[x]/E11[x]**0.6
#        errorlow11[x] = errorlow11[x]/E11[x]**0.6
        
#for x in range(0, len(E11)):
#        errorcen11[x] = 0.5*(errorhigh11[x]+errorlow11[x])
#        error11[x] =  0.5*(errorhigh11[x]-errorlow11[x])
        
        
#plt.scatter(E11,Spec11,s=20,marker='s', color='lightgrey')

#plt.errorbar(E11,errorcen11,error11,color='lightgrey',linewidth=2.0,linestyle='None')



########################

#infile = open('COSMICRAYDATA/AUGER.dat', 'r')
#for line in infile.readlines():
#        params = line.split()
        
#        E9 +=  [float(params[0])]    
#        Spec9 += [float(params[1])]  
#        errorhigh9 += [float(params[2])]
#        errorlow9 +=  [float(params[3])]
#        error9 += [float(params[2])]
#        errorcen9 += [float(params[2])]
        
#for x in range(0, len(E9)):
#        Spec9[x] = Spec9[x]/E9[x]**0.6
#        errorhigh9[x] = errorhigh9[x]/E9[x]**0.6
#        errorlow9[x] = errorlow9[x]/E9[x]**0.6
        
#for x in range(0, len(E9)):
#        errorcen9[x] = 0.5*(errorhigh9[x]+errorlow9[x])
#        error9[x] =  0.5*(errorhigh9[x]-errorlow9[x])
        
        
#plt.scatter(E9,Spec9,s=30,marker='o',color='black')

#plt.errorbar(E9,errorcen9,error9,color='black',linewidth=2.0,linestyle='None')

########################

#infile = open('COSMICRAYDATA/TA.dat', 'r')
#for line in infile.readlines():
#        params = line.split()
        
#        E8 +=  [float(params[0])]    
#        Spec8 += [float(params[1])]  
#        errorhigh8 += [float(params[2])]
#        errorlow8 +=  [float(params[3])]
#        error8 += [float(params[2])]
#        errorcen8 += [float(params[2])]

#for x in range(0, len(E8)):
#        Spec8[x] = Spec8[x]/E8[x]**0.6
#        errorhigh8[x] = errorhigh8[x]/E8[x]**0.6
#        errorlow8[x] = errorlow8[x]/E8[x]**0.6        
        
#for x in range(0, len(E8)):
#        errorcen8[x] = 0.5*(errorhigh8[x]+errorlow8[x])
#        error8[x] =  0.5*(errorhigh8[x]-errorlow8[x])
        
        
#plt.scatter(E8,Spec8,s=20,marker='^',color='grey')

#plt.errorbar(E8,errorcen8,error8,color='grey',linewidth=2.0,linestyle='None')




#fig, ax1 = plt.subplots()

#line1, =plt.plot(xf,nXeq,'--',color='black',alpha=1.0,linewidth=1.0)
#dashes = [444444444, 4, 4, 4] # 1 points on, 5 off, 10 on, 5 off
#line1.set_dashes(dashes)

#line2, =plt.plot(k,CDMold,'--',color='black',alpha=1.0,linewidth=2.0)
#dashes = [4444444, 4, 4, 4] # 1 points on, 5 off, 10 on, 5 off
#line2.set_dashes(dashes)

#line3, =plt.plot(k,MPS,'--',color='black',alpha=1.0,linewidth=2.0)
#dashes = [888888, 4, 8, 4] # 1 points on, 5 off, 10 on, 5 off
#line3.set_dashes(dashes)

#line4, =plt.plot(k,tot,'--',color='black',alpha=1.0,linewidth=2.0)
#dashes = [8, 4, 8, 4] # 1 points on, 5 off, 10 on, 5 off
#line4.set_dashes(dashes)

####

#infile = open('lymanalpha.dat', 'r')
#for line in infile.readlines():
#        params = line.split()
#        
#        k1 +=  [float(params[0])]    
#        MPS1 += [float(params[1])]  
#        error1 += [float(params[2])]#

#for x in range(0, len(k1)):
#        k1[x] = k1[x]/0.7 
        
#plt.scatter(k1,MPS1,s=20,color='black')

#plt.errorbar(k1,MPS1,error1,color='black',linewidth=2.0,linestyle='None')

####

#infile = open('lymanalpha-last.dat', 'r')
#for line in infile.readlines():
#        params = line.split()
        
#        k8 +=  [float(params[0])]    
#        MPS8 += [float(params[1])]  
#        error8 += [float(params[2])]

#for x in range(0, len(k8)):
#        k8[x] = k8[x]/0.7 
        

#plt.errorbar(k8,MPS8,error8,color='black',linewidth=2.0,linestyle='None')

###################

#### k, P(k), sigma(P(k)), k_lower, k_upper

#infile = open('MPSplanckTT.dat', 'r')
#for line in infile.readlines():
#        params = line.split()
        
#        k2 +=  [float(params[0])]    
#        MPS2 += [float(params[1])]  
#        error2 += [float(params[2])]
#        klower2  += [float(params[3])]
#        kupper2 += [float(params[4])]
#        kerror2 += [float(params[4])]
#        kcen2 += [float(params[4])]
        
#for x in range(0, len(k2)):
#        kcen2[x] = (klower2[x]+kupper2[x])*0.5
#        kerror2[x] = (kupper2[x]-klower2[x])*0.5
#        kupper2[x] = kupper2[x]-kcen2[x]
#        klower2[x] = kcen2[x]-klower2[x]

#plt.scatter(k2,MPS2,s=20,marker='^',color='black')

#plt.errorbar(k2,MPS2,yerr=error2,xerr=[klower2, kupper2],color='black',linewidth=1.0,linestyle='None')

#infile = open('MPSplanckTT-1st.dat', 'r')
#for line in infile.readlines():
#        params = line.split()
#        
#        k3 +=  [float(params[0])]    
#        MPS3 += [float(params[1])]  
#        error3 += [float(params[2])]
#        klower3  += [float(params[3])]
#        kupper3 += [float(params[4])]


#plt.errorbar(k3,MPS3,error3,color='black',linewidth=1.0,linestyle='None')

####

#### k, P(k), sigma(P(k)), k_lower, k_upper

#infile = open('MPSplanckEE.dat', 'r')
#for line in infile.readlines():
#        params = line.split()
        
#        k4 +=  [float(params[0])]    
#        MPS4 += [float(params[1])]  
#        error4 += [float(params[2])]
#        klower4  += [float(params[3])]
#        kupper4 += [float(params[4])]#


#plt.scatter(k4,MPS4,s=20,marker='s',color='grey')

#plt.errorbar(k4,MPS4,yerr=error4,xerr=[klower4, kupper4],color='grey',linewidth=1.0,linestyle='None')


####


#plt.scatter(k5,MPS5,s=20,marker='D',color='grey')

#plt.errorbar(k5,MPS5,yerr=error5,xerr=[klower5, kupper5],color='grey',linewidth=1.0,linestyle='None')


####


#plt.scatter(k6,MPS6,s=10,color='magenta')

#plt.errorbar(k6,MPS6,yerr=error6,color='black',linewidth=3.0,linestyle='None')


####



#plt.scatter(k7,MPS7,s=20,marker='v',color='grey')

#plt.errorbar(k7,MPS7,yerr=error7,xerr=[klower7, kupper7],color='grey',linewidth=2.0,linestyle='None')

####


#infile = open('MPS-forkey.dat', 'r')
#for line in infile.readlines():
#        params = line.split()
#        
#        k9 +=  [float(params[0])]    
#        MPS9 += [float(params[1])]
#        error9 +=  [float(params[1])]
#        klower9 +=  [float(params[1])]
#        kupper9 +=  [float(params[1])]
      
#for x in range(0, len(k9)):
#        MPS9[x] = 1.15*MPS9[x]*100.0
#        error9[x] = error9[x]*20.0
#        klower9[x] = klower9[x]*0.0002
#        kupper9[x] = kupper9[x]*0.0003

#plt.scatter(k9,MPS9,s=20,marker='^',color='black')
#plt.errorbar(k9,MPS9,yerr=error9,xerr=[klower9, kupper9],color='black',linewidt#h=1.0,linestyle='None')

###

#for x in range(0, len(k9)):
#        MPS9[x] = MPS9[x]*0.5
#        error9[x] = error9[x]*0.5

#plt.scatter(k9,MPS9,s=20,marker='s',color='grey')
#plt.errorbar(k9,MPS9,yerr=error9,xerr=[klower9, kupper9],color='grey',linewidth#=1.0,linestyle='None')

####

#for x in range(0, len(k9)):
#        MPS9[x] = MPS9[x]*0.5
#        error9[x] = error9[x]*0.5

#plt.scatter(k9,MPS9,s=20,marker='D',color='grey')
#plt.errorbar(k9,MPS9,yerr=error9,xerr=[klower9, kupper9],color='grey',linewidth#=1.0,linestyle='None')

####

#for x in range(0, len(k9)):
#        MPS9[x] = MPS9[x]*0.5
#        error9[x] = error9[x]*0.5

#plt.scatter(k9,MPS9,s=20,marker='v',color='grey')
#plt.errorbar(k9,MPS9,yerr=error9,xerr=[klower9, kupper9],color='grey',linewidth#=2.0,linestyle='None')

####

#for x in range(0, len(k9)):
#        MPS9[x] = MPS9[x]*0.5
#        error9[x] = error9[x]*0.5

#plt.errorbar(k9,MPS9,yerr=error9,color='black',linewidth=3.0,linestyle='None')


####

#for x in range(0, len(k9)):
#        MPS9[x] = MPS9[x]*0.5
#        error9[x] = error9[x]*0.5

#plt.scatter(k9,MPS9,s=20,color='black')
#plt.errorbar(k9,MPS9,error9,color='black',linewidth=2.0,linestyle='None')

####

#plt.text(0.002, 100.0,r'CMB Temperature (Planck)',fontsize=17)
#plt.text(0.002, 50.0,r'CMB Polarization (Planck)',fontsize=17)
#plt.text(0.002, 25.0,r'CMB Lensing (Planck)',fontsize=17)
#plt.text(0.002, 12.5,r'Cosmic Shear (DES)',fontsize=17)
#plt.text(0.002, 6.25,r'Galaxy Clustering (SDSS)',fontsize=17)
#plt.text(0.002, 3.125,r'CMB Lyman-Alpha (SDSS)',fontsize=17)


# Equilibrium Prediction, only valid in low temp limit (boltzmann)
#x = np.linspace(1.0,1000.0,10000)  # GHz
#y = 4.0*(66.6**2/(2.0*3.1415*x))**1.5*np.exp(-1.0*x)
#line11, =plt.plot(x, y, '-',color='blue',linewidth=1.0)
#dashes = [555555555, 5, 5, 5] # 1 points on, 5 off, 10 on, 5 off
#line11.set_dashes(dashes)


###

#line3, =plt.plot(T,Deuterium,'--',color='black',alpha=1.0,linewidth=2.0)
#dashes = [444444444444, 4, 2, 4] # 1 points on, 5 off, 10 on, 5 off
#line3.set_dashes(dashes)

#line4, =plt.plot(T,Tritium,'--',color='black',alpha=1.0,linewidth=2.0)
#dashes = [44444444, 4, 6, 4] # 1 points on, 5 off, 10 on, 5 off
#line4.set_dashes(dashes)

#line5, =plt.plot(T,Helium3,'--',color='black',alpha=1.0,linewidth=2.0)
#dashes = [8, 4, 8, 4] # 1 points on, 5 off, 10 on, 5 off
#line5.set_dashes(dashes)

###


#plt.text(0.7, 2.5,r'$p$',fontsize=17)
#plt.text(0.7, 0.015,r'$n$',fontsize=17)

#plt.text(0.17, 2.5,r'$^4{\rm He}$',fontsize=17)

#plt.text(0.0485, 2.5,r'$^{12}{\rm C}$',fontsize=17)


#plt.text(0.85, 1.0E-13,r'$^2{\rm H}$',fontsize=17)

#plt.text(0.34, 3.0E-19,r'$^3{\rm H}$',fontsize=17)
#plt.text(0.31, 5.0E-21,r'$^3{\rm He}$',fontsize=17)


#plt.text(0.078, 1.0E-21,r'$^{13}{\rm C}$',fontsize=17)

#plt.text(0.07, 1.0E-18,r'$^{14}{\rm C}$',fontsize=17)



#plt.text(0.7, 2.5,r'$p$',fontsize=17)
#plt.text(0.7, 0.015,r'$n$',fontsize=17)

#plt.text(0.17, 2.5,r'$^4{\rm He}$',fontsize=17)

#plt.text(0.0485, 2.5,r'$^{12}{\rm C}$',fontsize=17)


#plt.text(0.85, 1.0E-13,r'$^2{\rm H}$',fontsize=17)

#plt.text(0.34, 3.0E-19,r'$^3{\rm H}$',fontsize=17)
#plt.text(0.31, 5.0E-21,r'$^3{\rm He}$',fontsize=17)


#plt.text(0.078, 1.0E-21,r'$^{13}{\rm C}$',fontsize=17)

#x = np.linspace(0.09,0.15,2)  
#y = x*0.0+0.9*1.1
#line11, =plt.plot(x, y, '-',color='black',linewidth=2.0)
#dashes = [4444444, 4, 8, 4] # 1 points on, 5 off, 10 on, 5 off
#line11.set_dashes(dashes)

#x = np.linspace(0.09,0.15,2)  
#y = x*0.0+0.6*1.1
#line12, =plt.plot(x, y, '-',color='black',linewidth=2.0)
#dashes = [8, 4, 8, 4] # 1 points on, 5 off, 10 on, 5 off
#line12.set_dashes(dashes)



#plt.text(0.17, 0.9,r'${\rm CDM}\,{\rm Only}$',fontsize=17)
#plt.text(0.17, 0.6,r'${\rm CDM+Baryons}$',fontsize=17)

#plt.annotate('', xy=(6.0E6, 1.2), xytext=(1.4E7, 7.0), 
#             arrowprops=dict(facecolor='black', shrink=0.,width=1),
#            )


#plt.annotate('', xy=(4.0E8, 18.0E-3), xytext=(0.95E9, 10.5E-2), 
#             arrowprops=dict(facecolor='black', shrink=0.,width=1),
#            )

#plt.annotate('', xy=(8.0E9, 4.0E-4), xytext=(1.75E10, 2.3E-3), 
#             arrowprops=dict(facecolor='black', shrink=0.,width=1),
#            )


#plt.text(1.6E7, 7.0, r'Knee',rotation=0,color='black',fontsize=17)
#plt.text(1.1E9, 10.5E-2, r'2nd Knee',rotation=0,color='black',fontsize=17)
#plt.text(2.0E10, 2.3E-3, r'Ankle',rotation=0,color='black',fontsize=17)



#

#plt.annotate('', xy=(0.05686, 0.15), xytext=(0.05686, 0.05), 
#             arrowprops=dict(facecolor='black', shrink=0.,width=1),
#            )
#plt.text( 0.05117, 0.0305, r'$\frac{5\pi}{2r_s}$',rotation=0,color='black',fontsize=17)

#

#plt.annotate('', xy=(0.07960, 0.10), xytext=(0.07960, 0.0333), 
#             arrowprops=dict(facecolor='black', shrink=0.,width=1),
#            )
#plt.text( 0.07960, 0.016666, r'$\frac{7\pi}{2r_s}$',rotation=0,color='black',fon#tsize=17)

#

#plt.annotate('', xy=(0.1023, 0.075), xytext=(0.1023, 0.025), 
#             arrowprops=dict(facecolor='black', shrink=0.,width=1),
#            )
#plt.text( 0.1023, 0.0125, r'$\frac{9\pi}{2r_s}$',rotation=0,color='black',fontsize=17)

plt.text(1.6E-4, 8.0E35, r'$\langle N_{\rm MSP} \rangle = 11\, \Gamma_e$',rotation=0,color='black',fontsize=17)



plt.tick_params(which='both',labelsize=14)

plt.xlabel(r'{\rm Stellar}\,{\rm Encounter}\,{\rm Rate}\, $(${\rm Arb.}\,{\rm Units}$)$', fontsize=18) ##set the xlabel for the plot
plt.ylabel(r'$L_{\gamma} \,\, ({\rm erg/s})$', fontsize=18)
#plt.ylabel(r'$E_{\gamma} dN_{\gamma}/d\nu_{\gamma}$ \, $({\rm J}/{\rm cm}^2/{\rm s}/{\rm GHz}/{\rm sr})$', fontsize=19)

plt.axis([1.0E-4, 1.0E1, 1.0E31, 3.0E36])
plt.yscale('log')
plt.xscale('log')

#ax2 = ax1.twiny()  # instantiate a second axes that shares the same x-axis
#####



###
#plt.axes().set_aspect('equal')

#plt.axis([6.0,0.072, 0.0, 6200.0])
#plt.yscale('log')
#plt.xscale('log')

#plt.xlabel(r'Angular Scale (degrees)', fontsize=19) ##set the xlabel for the plot
#plt.ylabel(r'$T^2 \, C_l \, l(l+1)/2\pi$, $(\mu{\rm K}^2)$', fontsize=19)


#plt.tick_params(which='both', width=1.5, length=4,labelsize=14)


#plt.tick_params(which='both',labelsize=14)


#plt.title('J0212.1+5320', fontsize=20)
##plt.plot(xvar, yvar) ##plot a 2D plot of x vs. y

#plt.tight_layout() 

fig.set_tight_layout(True)

#plt.savefig('fig1.pdf') ##save the figure as a png
#plt.show() ##show the figure to screen

fig.savefig('case1-dataplot.pdf')
