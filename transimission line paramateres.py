from cmath import *
from tkinter import *
from tkinter import messagebox
self = Tk()
self.title("Trn Ln Cal")
self.geometry("8000x8000")
self.configure(bg="#F4F5FF")
models = ["Short series", "Short shunt", "Nominal pi", "Nominal T", "Exact pi", "Exact T", "Hyperbolic model"]
powactypes = ["Leading", "Lagging"]
systemtypes = ["1-phase", "3-phase"]

freq_label = Label(self, text="Freqcy:",font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
freq_entry = Entry(self, bg="#EDF0F9")


leth_label = Label(self, text="Length of T.L:",font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
leth_entry = Entry(self, bg="#EDF0F9",)

resisr_label = Label(self, text="Resistance:",font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
resisr_entry = Entry(self, bg="#EDF0F9")

indtor_label = Label(self, text="Inductance(L):",font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
indtor_entry = Entry(self, bg="#EDF0F9")

shunt_label = Label(self, text="Capictance(C):",font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
shunt_entry = Entry(self, bg="#EDF0F9")

vrline_label = Label(self, text="line voltage at reciving end(Vr):",font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF" )
vrline_entry = Entry(self, bg="#EDF0F9")

acpower_label = Label(self, text="Active Power(P):",font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
acpower_entry = Entry(self, bg="#EDF0F9")

powac_label = Label(self, text="Power Factor(pf):",font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
powac_entry = Entry(self, bg="#EDF0F9")

powactype_label = Label(self, text="Poweype:",font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
powactype_dropdown = OptionMenu(self, StringVar(), *powactypes)

systemtype_label = Label(self, text="System type:",font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
systemtype_dropdown = OptionMenu(self, StringVar(), *systemtypes)

model_label = Label(self, text="Model:",font=("helvetica", 12),fg="#311F6C",bg="#F4F5FF")
model_dropdown = OptionMenu(self, StringVar(), *models)

freq_label.grid(row=0, column=0)
freq_entry.grid(row=0, column=1)

leth_label.grid(row=1, column=0)
leth_entry.grid(row=1, column=1)

resisr_label.grid(row=2, column=0)
resisr_entry.grid(row=2, column=1)

indtor_label.grid(row=3, column=0)
indtor_entry.grid(row=3, column=1)

shunt_label.grid(row=4, column=0)
shunt_entry.grid(row=4, column=1)

vrline_label.grid(row=5, column=0)
vrline_entry.grid(row=5, column=1)

acpower_label.grid(row=6, column=0)
acpower_entry.grid(row=6, column=1)

powac_label.grid(row=7, column=0)
powac_entry.grid(row=7, column=1)

powactype_label.grid(row=8, column=0,pady=7.5)
powactype_dropdown.grid(row=8, column=1,pady=7.5)

systemtype_label.grid(row=9, column=0,pady=7.5)
systemtype_dropdown.grid(row=9, column=1,pady=7.5)

model_label.grid(row=10, column=0,pady=7.5)
model_dropdown.grid(row=10, column=1,pady=7.5)

calculate_button = Button(self,width=15, height=1, text="Calculate",font=("Montserrat ExtraBold", 14,"bold"),fg="#F4F5FF", bg="#673EE6",pady=10)
calculate_button.grid(row=11, column=0,pady=10,padx=50)

A_label = Label(self,font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
B_label = Label(self,font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
C_label = Label(self,font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
perverg_label = Label(self,font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
senvol_label = Label(self,font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
sencuren_label = Label(self,font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
actpowsed_label = Label(self,font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
efncy_label = Label(self,font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
phaveloci_label = Label(self,font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
wagth_label = Label(self,font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
sedpowc_label = Label(self,font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")

infone_label = Label(self,font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
inftow_label = Label(self,font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")

infone_label.config(text="specific standards and guidelines from organizations like " ,font=("helvetica", 12,"bold") ,fg="#311F6C", anchor="w",bg="#F4F5FF")
inftow_label.config(text="IEEE and IEC" ,font=("helvetica", 16,"bold"),fg="#311F6C", anchor="w",bg="#F4F5FF")
infone_label.grid(row=24,column=0)      
inftow_label.grid(row=25,column=0)      



def calculate():
    f = float(freq_entry.get())
    Le = float(leth_entry.get())
    R = float(resisr_entry.get())
    L = float(indtor_entry.get())
    Cap = float(shunt_entry.get())
    vrline = float(vrline_entry.get())
    acpower = float(acpower_entry.get())
    powac = float(powac_entry.get())
    powactype = powactype_dropdown.cget("text").lower()
    systemtype = systemtype_dropdown.cget("text").lower()
    model = model_dropdown.cget("text").lower()

    Y1 = complex(0, 2*pi*f*Cap)
    z = complex(R, 2*pi*f*L)
    Gamma = sqrt(z*Y1)
    beta = Gamma.imag
    lamda = 2*pi/beta
    phasevelo = lamda*f
    if model == "short series":
           A = 1
           B = z
           C = 0
    elif model == "short shunt":
           A = 1
           B = 0
           C = Y1
    elif model == "nominal pi":
        A = 1 + (Y1*z)/2
        B = z
        C = Y1*(1 + (Y1*z)/4)
    elif model == "nominal t":
        A = 1 + (Y1*z)/2
        B =z*(1 + (Y1*z)/4)
        C = Y1
    elif model == "exact pi":
       Zc = sqrt(z/Y1)
       zdash=Zc*sinh(Gamma)
       ydash=Y1*tanh(Gamma/2)/(Gamma/2)
       A = 1+(ydash*zdash)/2
       B = zdash
       C = ydash*(1+(ydash*zdash)/4)
    elif model == "exact t":
        Zc = sqrt(z/Y1)
        zdash=Zc*tanh(Gamma/2)/(Gamma/2)
        ydash=sinh(Gamma)/Zc
        A = 1+(ydash*zdash)/2
        B = zdash*(1+(ydash*zdash)/4)
        C = ydash
    elif model == "hyperbolic model":
        Zc = sqrt(z/Y1)
        A = cosh(Gamma)
        B = Zc*sinh(Gamma)
        C =sinh(Gamma)/Zc
    
    ra,theta_A=polar(A)
    rb,theta_B=polar(B)
    rc,theta_C=polar(C)

    if powactype == "leading":
        m=1
    elif powactype == "lagging":
        m=-1

    if systemtype == "1-phase":
        n=1
        vr=complex(vrline,0)
    elif systemtype == "3-phase":
        n=3
        vr=complex(vrline/sqrt(3),0)

    Ir=complex(acpower/(n*vr),m*acpower*sqrt(1 - powac**2)/(n*vr*powac))
    vs=A*vr + B*Ir
    Is=C*vr + A*Ir
    k,angv=polar(vs)
    t,angi=polar(Is)
    phis=angv-angi
    Ps=n*k*t*cos(phis)
    etap=acpower*100/Ps.real
    pervregu=100*((k/ra)-vr.real)/vr.real

    A_label.config(text=f"Polar form of A  = {ra:.5f}∠{theta_A:.5f}°")
    A_label.grid(row=12,column=0)

    B_label.config(text=f"Polar form of B  = {rb:.5f}∠{theta_B:.5f}°")
    B_label.grid(row=13,column=0)

    C_label.config(text=f"Polar form of C  = {rc:.5f}∠{theta_C:.5f}°")
    C_label.grid(row=14,column=0)

    perverg_label.config(text=f"Percentage voltage regulation  = {pervregu.real:.5f}%")
    perverg_label.grid(row=15,column=0)

    senvol_label.config(text=f"Sending end voltage  ={k:.5f}∠{angv*180/pi:.5f}°")
    senvol_label.grid(row=16,column=0)

    sencuren_label.config(text=f"Sending end current  ={t:.5f}∠{angi*180/pi:.5f}°")
    sencuren_label.grid(row=17,column=0)

    actpowsed_label.config(text=f"Active power at the sending end  = {Ps.real:.5f}")
    actpowsed_label.grid(row=18,column=0)

    efncy_label.config(text=f"Efficiency of the line  = {etap:.5f}%")
    efncy_label.grid(row=19,column=0)

    phaveloci_label.config(text=f"Phase velocity  = {phasevelo:.5f}")
    phaveloci_label.grid(row=20,column=0)

    wagth_label.config(text=f"Wave length  = {lamda:.5f} ")
    wagth_label.grid(row=21,column=0)

    sedpowc_label.config(text=f"Sending end power factor  = {cos(phis).real:.5f}")
    sedpowc_label.grid(row=22,column=0)

#these codes are for making a cable calculations    
# def cabling():      
#     response = messagebox.askyesno("Show Other Page", "Do you want to do cable sizing?")
#     if response:
#              #Create and show the other page
#             root = Toplevel(self)
#             root.configure(bg="#F4F5FF")
#             root.title("Here are your cable sizing results")
#             root.geometry("400x300")
#             root_label = Label(root, text="Hello to the new page!")
#             root_label.pack(pady=20)
#             Area_label = Label(root,font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
#             info_label = Label(root,font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
#             Area_label.config(text=f"Cross-Sectional Area (A):  = 5")
#             Area_label.grid(row=23,column=0)

#             currentdesnity_label = Label(root, text="Current Desnity:",font=("helvetica", 12),fg="#311F6C", anchor="w",bg="#F4F5FF")
#             currentdesnity_entry = Entry(root, bg="#EDF0F9")
#             currentdesnity_label.grid(row=0, column=0)
#             currentdesnity_entry.grid(row=0, column=1)
#     root.mainloop()

#     # Implement the cabling function here


calculate_button.config(command=lambda: (calculate()))
self.mainloop()
