from Tkinter import *
from tkMessageBox import *
import random
import time
import datetime
root1=Tk()
root1.geometry("650x650+0+0")
root1.title("Project")
root1.attributes("-fullscreen",True)
def enter():
    root=Toplevel(root1)
    #root.attributes("-fullscreen",True)
    root.geometry("1350x950+0+0")
    root.title("Billing System")
    root.configure(background="powder blue")

    Tops=Frame(root,width=1350,height=100,bd=12,relief="groove")
    Tops.pack(side=TOP)

    f1=Frame(root,width=990,height=650,bd=8,relief="groove")
    f1.pack(side=LEFT)


    f2=Frame(root,width=440,height=650,bd=8,relief="groove")
    f2.pack(side=RIGHT)

    f1a=Frame(f1,width=440,height=330,bd=8,relief="groove")
    f1a.pack(side=TOP)

    f2a=Frame(f1,width=900,height=330,bd=6,relief="groove")
    f2a.pack(side=BOTTOM)

    ft2=Frame(f2,width=440,height=650,bd=12,relief="groove")
    ft2.pack(side=TOP)
    fb2=Frame(f2,width=440,height=50,bd=16,relief="groove")
    fb2.pack(side=BOTTOM)

    f1aa=Frame(f1a,width=400,height=330,bd=16,relief="groove")
    f1aa.pack(side=LEFT)
    f1ab=Frame(f1a,width=400,height=330,bd=16,relief="groove")
    f1ab.pack(side=RIGHT)

    f2aa=Frame(f2a,width=450,height=330,bd=14,relief="groove")
    f2aa.pack(side=LEFT)

    f2ab=Frame(f2a,width=450,height=330,bd=14,relief="groove")
    f2ab.pack(side=RIGHT)

    Tops.configure(background="powder blue")
    f1.configure(background="powder blue")
    f2.configure(background="powder blue")
    var1=IntVar()
    var2=IntVar()
    var3=IntVar()
    var4=IntVar()
    var5=IntVar()
    var6=IntVar()
    var7=IntVar()
    var8=IntVar()
    var9=IntVar()
    var10=IntVar()
    var11=IntVar()
    var12=IntVar()
    var13=IntVar()
    var14=IntVar()
    var15=IntVar()
    var16=IntVar()

    DateofOrder=StringVar()
    Receipt_Ref=StringVar()
    PaidTax=StringVar()
    SubTotal=StringVar()
    TotalCost=StringVar()
    CostofCakes=StringVar()
    CostofDrinks=StringVar()
    ServiceCharge=StringVar()

    E_Devils_Own=StringVar()
    E_Assam_Tea=StringVar()
    E_Darjeeling_Tea=StringVar()
    E_Masala_Chai=StringVar()
    E_Aztec=StringVar()
    E_Strawberry_Lemonade=StringVar()
    E_Green_Tea=StringVar()
    E_Green_Apple_Tea=StringVar()

    E_Coffee_cake=StringVar()
    E_Red_Velvet_Cake=StringVar()
    E_Apple_Cake=StringVar()
    E_Banana_Cake=StringVar()
    E_Bear_Cake=StringVar()
    E_Bara_birth=StringVar()
    E_Carrot_Cake=StringVar()
    E_Chocolate_Cake=StringVar()

    E_Devils_Own.set("0")
    E_Assam_Tea.set("0")
    E_Darjeeling_Tea.set("0")
    E_Masala_Chai.set("0")
    E_Aztec.set("0")
    E_Strawberry_Lemonade.set("0")
    E_Green_Tea.set("0")
    E_Green_Apple_Tea.set("0")

    E_Coffee_cake.set("0")
    E_Red_Velvet_Cake.set("0")
    E_Apple_Cake.set("0")
    E_Banana_Cake.set("0")
    E_Bear_Cake.set("0")
    E_Bara_birth.set("0")
    E_Carrot_Cake.set("0")
    E_Chocolate_Cake.set("0")
    


    DateofOrder.set(time.strftime("%d/%m/%Y"))
    def Reset():
        PaidTax.set("")
        SubTotal.set("")
        TotalCost.set("")
        CostofDrinks.set("")
        CostofCakes.set("")
        ServiceCharge.set("")
        txtReceipt.delete("1.0",END)

    
        E_Devils_Own.set("0")
        E_Assam_Tea.set("0")
        E_Darjeeling_Tea.set("0")
        E_Masala_Chai.set("0")
        E_Aztec.set("0")
        E_Strawberry_Lemonade.set("0")
        E_Green_Tea.set("0")
        E_Green_Apple_Tea.set("0")

    

        E_Coffee_cake.set("0")
        E_Red_Velvet_Cake.set("0")
        E_Apple_Cake.set("0")
        E_Banana_Cake.set("0")
        E_Bear_Cake.set("0")
        E_Bara_birth.set("0")
        E_Carrot_Cake.set("0")
        E_Chocolate_Cake.set("0")
        
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)

    
        txtDevils_Own.configure(state=DISABLED)
        txtAssam_Tea.configure(state=DISABLED)
        txtDarjeeling_Tea.configure(state=DISABLED)
        txtMasala_Chai.configure(state=DISABLED)
        txtAztec.configure(state=DISABLED)
        txtStrawberry_Lemonade.configure(state=DISABLED)
        txtGreen_Tea.configure(state=DISABLED)
        txtGreen_Apple_Tea.configure(state=DISABLED)
        txtCoffee_cake.configure(state=DISABLED)
        txtRed_Velvet_Cake.configure(state=DISABLED)
        txtApple_Cake.configure(state=DISABLED)
        txtBanana_Cake.configure(state=DISABLED)
        txtBear_Cake.configure(state=DISABLED)
        txtBara_birth.configure(state=DISABLED)
        txtCarrot_Cake.configure(state=DISABLED)
        txtChocolate_Cake.configure(state=DISABLED)

    def chkbutton_value():
        if(var1.get() == 1):
            txtDevils_Own.configure(state=NORMAL)
        elif var1.get()== 0:
            txtDevils_Own.configure(state=DISABLED)
            E_Devils_Own.set("0")
         
        if(var2.get() == 1):
            txtAssam_Tea.configure(state=NORMAL)
        elif var2.get()== 0:
            txtAssam_Tea.configure(state=DISABLED)
            E_Assam_Tea.set("0")

        if(var3.get() == 1):
            txtDarjeeling_Tea.configure(state=NORMAL)
        elif var3.get()== 0:
            txtDarjeeling_Tea.configure(state=DISABLED)
            E_Darjeeling_Tea.set("0")

        if(var4.get() == 1):
            txtMasala_Chai.configure(state=NORMAL)
        elif var4.get()== 0:
            txtMasala_Chai.configure(state=DISABLED)
            E_Masala_Chai.set("0")

        if(var5.get() == 1):
            txtAztec.configure(state=NORMAL)
        elif var5.get()== 0:
            txtAztec.configure(state=DISABLED)
            E_Aztec.set("0")

        if(var6.get() == 1):
            txtStrawberry_Lemonade.configure(state=NORMAL)
        elif var6.get()== 0:
            txtStrawberry_Lemonade.configure(state=DISABLED)
            E_Strawberry_Lemonade.set("0")

        if(var7.get() == 1):
            txtGreen_Tea.configure(state=NORMAL)
        elif var7.get()== 0:
            txtGreen_Tea.configure(state=DISABLED)
            E_Green_Tea.set("0")

        if(var8.get() == 1):
            txtGreen_Apple_Tea.configure(state=NORMAL)
        elif var8.get()== 0:
            txtGreen_Apple_Tea.configure(state=DISABLED)
            E_Green_Apple_Tea.set("0")

        if(var9.get() == 1):
            txtCoffee_cake.configure(state=NORMAL)
        elif var9.get()== 0:
            txtCoffee_cake.configure(state=DISABLED)
            E_Coffee_cake.set("0")

        if(var10.get() == 1):
            txtRed_Velvet_Cake.configure(state=NORMAL)
        elif var10.get()== 0:
            txtRed_Velvet_Cake.configure(state=DISABLED)
            E_Red_Velvet_Cake.set("0")

        if(var11.get() == 1):
            txtApple_Cake.configure(state=NORMAL)
        elif var11.get()== 0:
            txtApple_Cake.configure(state=DISABLED)
            E_Apple_Cake.set("0")

        if(var12.get() == 1):
            txtBanana_Cake.configure(state=NORMAL)
        elif var12.get()== 0:
            txtBanana_Cake.configure(state=DISABLED)
            E_Banana_Cake.set("0")

        if(var13.get() == 1):
            txtBear_Cake.configure(state=NORMAL)
        elif var13.get()== 0:
            txtBear_Cake.configure(state=DISABLED)
            E_Bear_Cake.set("0")

        if(var14.get() == 1):
            txtBara_birth.configure(state=NORMAL)
        elif var14.get()== 0:
            txtBara_birth.configure(state=DISABLED)
            E_Bara_birth.set("0")

        if(var15.get() == 1):
            txtCarrot_Cake.configure(state=NORMAL)
        elif var15.get()== 0:
            txtCarrot_Cake.configure(state=DISABLED)
            E_Carrot_Cake.set("0")

         
        if(var16.get() == 1):
            txtChocolate_Cake.configure(state=NORMAL)
        elif var16.get()== 0:
            txtChocolate_Cake.configure(state=DISABLED)
            E_Chocolate_Cake.set("0")
        
    
    def Receipt():
        txtReceipt.delete("1.0",END)
        x = random.randint(10908, 500876)
        randomRef = str(x)
        Receipt_Ref.set("BILL"+randomRef)

        txtReceipt.insert(END,"Receipt_Ref:\t\t\t"+Receipt_Ref.get()+"\t\t"+DateofOrder.get()+"\n")
        txtReceipt.insert(END,"Items\t\t\t\t\t"+"Cost of Items \n\n")
        txtReceipt.insert(END,"Devils Own: \t\t\t\t\t\t"+ E_Devils_Own.get()+"\n")
        txtReceipt.insert(END,"Assam Tea:\t\t\t\t\t\t"+E_Assam_Tea.get()+"\n")
        txtReceipt.insert(END,"Darjeeling Tea:\t\t\t\t\t\t"+E_Darjeeling_Tea.get()+"\n")
        txtReceipt.insert(END,"Masala Chai:\t\t\t\t\t\t"+E_Masala_Chai.get()+"\n")
        txtReceipt.insert(END,"Aztec:\t\t\t\t\t\t"+E_Aztec.get()+"\n")
        txtReceipt.insert(END,"Strawberry Lemonade:\t\t\t\t\t\t"+ E_Strawberry_Lemonade.get()+"\n")
        txtReceipt.insert(END,"Green Tea:\t\t\t\t\t\t"+E_Green_Tea.get()+"\n")
        txtReceipt.insert(END,"Green Apple Tea:\t\t\t\t\t\t"+ E_Green_Apple_Tea.get()+"\n")
        txtReceipt.insert(END,"Coffee cake:\t\t\t\t\t\t"+E_Coffee_cake.get()+"\n")
        txtReceipt.insert(END,"Red Velvet Cake:\t\t\t\t\t\t"+E_Red_Velvet_Cake.get()+"\n")
        txtReceipt.insert(END,"Apple Cake:\t\t\t\t\t\t"+E_Apple_Cake.get()+"\n")
        txtReceipt.insert(END,"Banana Cake:\t\t\t\t\t\t"+E_Banana_Cake.get()+"\n")
        txtReceipt.insert(END,"Bear Cake:\t\t\t\t\t\t"+E_Bear_Cake.get()+"\n")
        txtReceipt.insert(END,"Bara birth:\t\t\t\t\t\t"+E_Bara_birth.get()+"\n")
        txtReceipt.insert(END,"Carrot Cake:\t\t\t\t\t\t"+E_Carrot_Cake.get()+"\n")
        txtReceipt.insert(END,"Chocolate Cake:\t\t\t\t\t\t"+E_Chocolate_Cake.get()+"\n")
        txtReceipt.insert(END,"Cost of Drinks:\t\t"+CostofDrinks.get()+"\tTax Paid:\t\t"+PaidTax.get()+"\n")
        txtReceipt.insert(END,"Cost of Cakes:\t\t"+CostofCakes.get()+"\tSubTotal:\t\t"+SubTotal.get()+"\n")
        txtReceipt.insert(END,"Service Charge:\t\t"+ServiceCharge.get()+"\tTotal Cost:\t\t"+TotalCost.get()+"\n")

    lblInfo=Label(Tops,font=("ariala",70,"bold"),text="   Cafe Management System   ",bd=10,background="turquoise2")
    lblInfo.grid(row=0,column=0)

    def CostofItem():
        Item1=float(E_Devils_Own.get())
        Item2=float(E_Assam_Tea.get())
        Item3=float(E_Darjeeling_Tea.get())
        Item4=float(E_Masala_Chai.get())
        Item5=float(E_Aztec.get())
        Item6=float(E_Strawberry_Lemonade.get())
        Item7=float(E_Green_Tea.get())
        Item8=float( E_Green_Apple_Tea.get())

        Item9=float(E_Coffee_cake.get())
        Item10=float(E_Red_Velvet_Cake.get())
        Item11=float(E_Apple_Cake.get())
        Item12=float(E_Banana_Cake.get())
        Item13=float(E_Bear_Cake.get())
        Item14=float(E_Bara_birth.get())
        Item15=float( E_Carrot_Cake.get())
        Item16=float( E_Chocolate_Cake.get())

        PriceofDrinks =(Item1 * 75.0) + (Item2 * 50.0) + (Item3 * 90.0)\
                        + (Item4 * 30.0) + (Item5 *  200.0) + (Item6 * 150.0) + (Item7 * 25.0) + (Item8 * 65.0)
                                                                          
        PriceofCakes =(Item9 * 400.0) + (Item10 * 500.0) + (Item11 * 300.0)\
                       + (Item12 * 150.0) + (Item13 * 600.0) + (Item14 * 550.0) + (Item15 * 250.0) + (Item16 * 450.0)
        DrinksPrice="Rs",str("%.2f"%(PriceofDrinks))
        CakesPrice="Rs",str("%.2f"%(PriceofCakes))
        CostofCakes.set(CakesPrice)
        CostofDrinks.set(DrinksPrice)                                                                      
        SC="Rs",str("%.2f"%(20.5))
        ServiceCharge.set(SC)

        SubTotalofITEMS="Rs",str("%.2f"%(PriceofDrinks + PriceofCakes + 20.5))
        SubTotal.set(SubTotalofITEMS)                                                                      

        Tax="Rs",str("%.2f"%((PriceofDrinks + PriceofCakes + 20.5)*0.15))                                                                     
        PaidTax.set(Tax)
        TT=((PriceofDrinks + PriceofCakes + 20.5)*0.15)                                                                      
        TC="Rs",str("%.2f"%(PriceofDrinks + PriceofCakes + 20.5 + TT)) 
        TotalCost.set(TC)

    def qExit():
        qExit=askyesno("Quit System","Do you want to quit?")
        if qExit > 0:
            root.destroy()
            return

    


          
   

    

   
#===============================================================================
    Devils_Own=Checkbutton(f1aa,text="Devils Own\t",variable=var1,onvalue=1,offvalue=0,
                      font=("arial",18,"bold"),command=chkbutton_value).grid(row=0,sticky=W)
    Assam_Tea=Checkbutton(f1aa,text="Assam Tea\t",variable=var2,onvalue=1,offvalue=0,
                         font=("arial",18,"bold"),command=chkbutton_value).grid(row=1,sticky=W)
    Darjeeling_Tea=Checkbutton(f1aa,text="Darjeeling Tea\t",variable=var3,onvalue=1,offvalue=0,
                           font=("arial",18,"bold"),command=chkbutton_value).grid(row=2,sticky=W)
    Masala_Chai=Checkbutton(f1aa,text="Masala Chai\t",variable=var4,onvalue=1,offvalue=0,
                            font=("arial",18,"bold"),command=chkbutton_value).grid(row=3,sticky=W)
    Aztec=Checkbutton(f1aa,text="Aztec\t",variable=var5,onvalue=1,offvalue=0,
                           font=("arial",18,"bold"),command=chkbutton_value).grid(row=4,sticky=W)
    Strawberry_Lemonade=Checkbutton(f1aa,text="Strawberry Lemonade\t",variable=var6,onvalue=1,offvalue=0,
                               font=("arial",18,"bold"),command=chkbutton_value).grid(row=5,sticky=W)
    Green_Tea=Checkbutton(f1aa,text="Green Tea\t",variable=var7,onvalue=1,offvalue=0,
                                font=("arial",18,"bold"),command=chkbutton_value).grid(row=6,sticky=W)
    Green_Apple_Tea=Checkbutton(f1aa,text="Green Apple Tea\t",variable=var8,onvalue=1,offvalue=0,
                                font=("arial",18,"bold"),command=chkbutton_value).grid(row=7,sticky=W)
#================================================================================

    Coffee_cake=Checkbutton(f1ab,text="Coffee cake\t\t\t",variable=var9,onvalue=1,offvalue=0,
                            font=("arial",18,"bold"),command=chkbutton_value).grid(row=0,sticky=W)
    Red_Velvet_Cake=Checkbutton(f1ab,text="Red Velvet Cake\t\t\t",variable=var10,onvalue=1,offvalue=0,
                                font=("arial",18,"bold"),command=chkbutton_value).grid(row=1,sticky=W)
    Apple_Cake=Checkbutton(f1ab,text="Apple Cake\t\t\t",variable=var11,onvalue=1,offvalue=0,
                                  font=("arial",18,"bold"),command=chkbutton_value).grid(row=2,sticky=W)
    Banana_Cake=Checkbutton(f1ab,text="Banana Cake\t\t\t",variable=var12,onvalue=1,offvalue=0,
                                  font=("arial",18,"bold"),command=chkbutton_value).grid(row=3,sticky=W)
    Bear_Cake=Checkbutton(f1ab,text="Bear Cake\t\t\t",variable=var13,onvalue=1,offvalue=0,
                                     font=("arial",18,"bold"),command=chkbutton_value).grid(row=4,sticky=W)
    Bara_birth=Checkbutton(f1ab,text="Bara birth\t\t\t",variable=var14,onvalue=1,offvalue=0,
                                        font=("arial",18,"bold"),command=chkbutton_value).grid(row=5,sticky=W)
    Carrot_Cake=Checkbutton(f1ab,text="Carrot Cake\t\t\t",variable=var15,onvalue=1,offvalue=0,
                                  font=("arial",18,"bold"),command=chkbutton_value).grid(row=6,sticky=W)
    Chocolate_Cake=Checkbutton(f1ab,text="Chocolate Cake\t\t\t",variable=var16,onvalue=1,offvalue=0,
                                font=("arial",18,"bold"),command=chkbutton_value).grid(row=7,sticky=W)
#============================================================================
    txtDevils_Own=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Devils_Own,state=DISABLED,background="turquoise2")
    txtDevils_Own.grid(row=0,column=1)
    txtAssam_Tea=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Assam_Tea,state=DISABLED,background="cyan")
    txtAssam_Tea.grid(row=1,column=1)
    txtDarjeeling_Tea=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Darjeeling_Tea,state=DISABLED,background="deep pink")
    txtDarjeeling_Tea.grid(row=2,column=1)
    txtMasala_Chai=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Masala_Chai,state=DISABLED,background="red")
    txtMasala_Chai.grid(row=3,column=1)
    txtAztec=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Aztec,state=DISABLED,background="turquoise1")
    txtAztec.grid(row=4,column=1)
    txtStrawberry_Lemonade=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Strawberry_Lemonade,state=DISABLED,background="chocolate1")
    txtStrawberry_Lemonade.grid(row=5,column=1)
    txtGreen_Tea=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Green_Tea,state=DISABLED,background="turquoise3")
    txtGreen_Tea.grid(row=6,column=1)
    txtGreen_Apple_Tea=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Green_Apple_Tea,state=DISABLED,background="tan1")
    txtGreen_Apple_Tea.grid(row=7,column=1)
#===============================================================================
    txtCoffee_cake=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Coffee_cake,state=DISABLED,background="orchid2")
    txtCoffee_cake.grid(row=0,column=1)
    txtRed_Velvet_Cake=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Red_Velvet_Cake,state=DISABLED,background="firebrick1")
    txtRed_Velvet_Cake.grid(row=1,column=1)
    txtApple_Cake=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Apple_Cake,state=DISABLED,background="turquoise2")
    txtApple_Cake.grid(row=2,column=1)
    txtBanana_Cake=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Banana_Cake,state=DISABLED,background="mediumpurple1")
    txtBanana_Cake.grid(row=3,column=1)
    txtBear_Cake=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Bear_Cake,state=DISABLED,background="wheat")
    txtBear_Cake.grid(row=4,column=1)
    txtBara_birth=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Bara_birth,state=DISABLED,background="lightblue1")
    txtBara_birth.grid(row=5,column=1)
    txtCarrot_Cake=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Carrot_Cake,state=DISABLED,background="maroon1")
    txtCarrot_Cake.grid(row=6,column=1)
    txtChocolate_Cake=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Chocolate_Cake,state=DISABLED,background="pale green")
    txtChocolate_Cake.grid(row=7,column=1)
#===============================================================================
    lblReceipt=Label(ft2,font=("arial",12,"bold"),text="Receipt",bd=2,anchor="w")
    lblReceipt.grid(row=0,column=0,sticky=W)
    txtReceipt=Text(ft2,width=59,height=22,bg="white",bd=8,font=("arial",11,"bold"),background="turquoise2")
    txtReceipt.grid(row=1,column=0)
#==========================================================================
    lblCostofDrinks=Label(f2aa,font=("arial",16,"bold"),text="Cost of Drinks",bd=8)
    lblCostofDrinks.grid(row=0,column=0,sticky=W)
    txtCostofDrinks=Entry(f2aa,font=("arial",17,"bold"),bd=8,insertwidth=2,justify="left",textvariable= CostofDrinks,background="turquoise2")
    txtCostofDrinks.grid(row=0,column=1)

    lblCostofCakes=Label(f2aa,font=("arial",16,"bold"),text="Cost of Cakes",bd=8)
    lblCostofCakes.grid(row=1,column=0,sticky=W)
    txtCostofCakes=Entry(f2aa,font=("arial",17,"bold"),bd=8,insertwidth=2,justify="left",textvariable=CostofCakes,background="turquoise2")
    txtCostofCakes.grid(row=1,column=1)

    lblServiceCharge=Label(f2aa,font=("arial",16,"bold"),text="Service Charge ",bd=8)
    lblServiceCharge.grid(row=2,column=0,sticky=W)
    txtServiceCharge=Entry(f2aa,font=("arial",17,"bold"),bd=8,insertwidth=2,justify="left",textvariable=ServiceCharge,background="turquoise2")
    txtServiceCharge.grid(row=2,column=1)
#===============================================================================
    lblPaidTax=Label(f2ab,font=("arial",16,"bold"),text="Paid Tax",bd=8)
    lblPaidTax.grid(row=0,column=0,sticky=W)
    txtPaidTax=Entry(f2ab,font=("arial",16,"bold"),bd=8,insertwidth=3,justify="left",textvariable=PaidTax,background="turquoise2")
    txtPaidTax.grid(row=0,column=1)

    lblSubTotal=Label(f2ab,font=("arial",16,"bold"),text="Sub Total",bd=8)
    lblSubTotal.grid(row=1,column=0,sticky=W)
    txtSubTotal=Entry(f2ab,font=("arial",16,"bold"),bd=8,insertwidth=3,justify="left",textvariable=SubTotal,background="turquoise2")
    txtSubTotal.grid(row=1,column=1)

    lblTotalCost=Label(f2ab,font=("arial",16,"bold"),text="Total cost",bd=8)
    lblTotalCost.grid(row=2,column=0,sticky=W)
    txtTotalCost=Entry(f2ab,font=("arial",16,"bold"),bd=8,insertwidth=3,justify="left",textvariable= TotalCost,background="turquoise2")
    txtTotalCost.grid(row=2,column=1)
#================================================================================
    btnTotal=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),background="turquoise2",width=6,
                    text="Total",command=CostofItem).grid(row=0,column=0)

    btnReceipt=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),background="turquoise2",width=4,
                      text="Receipt",command=Receipt).grid(row=0,column=1)

    btnReset=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),background="turquoise2",width=4,
                    text="Reset",command=Reset).grid(row=0,column=2)

    btnExit=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=("arial",16,"bold"),background="turquoise2",width=3,
                   text="Exit",command=qExit).grid(row=0,column=3)

   
shortcutbar = Frame(root1, height=60, bg='orange')
toolbar = Label(shortcutbar, text='PYTHON PROJECT',bg='palegreen1',fg='black',height=2,font='times 12 bold ',relief="raise")
toolbar.pack(side=TOP,fill=X,expand=YES)
shortcutbar.pack(expand=NO, fill=X)
shortcutbar2 = Frame(root1, height=60, bg="orange")
toolbar = Label(shortcutbar2, text="Welcome To Cafe Management System ",bg='palegreen1',fg='turquoise3',height=2,font='times 16 bold',relief="raise")
toolbar.pack(side=TOP,fill=X,expand=YES)
shortcutbar2.pack(expand=NO, fill=X)
toolbar = Label(shortcutbar, text='',bg='palegreen1',fg='black',height=2,font='arial 12 bold',relief="raise")
toolbar.pack(side=TOP,fill=X,expand=YES)
shortcutbar.pack(expand=NO, fill=X)
shortcutbar2 = Frame(root1, height=60, bg='orange')
toolbar = Label(shortcutbar2, text="",bg='palegreen1',fg='black',height=2,font='CalibriLight 12 bold',relief="raise")
toolbar.pack(side=TOP,fill=X,expand=YES)
shortcutbar2.pack(expand=NO, fill=X)

a=PhotoImage(file="b.gif",width=1250,height=450)
b=Label(root1,image=a,relief="groove")
b.pack()

def aboutus():
    master=Tk()
    master.attributes("-fullscreen",True)    
    master.title("Student Details")
    master.geometry("1350x650+0+0")   
    shortcutbar = Frame(master, height=30, bg='cyan2')
    toolbar = Label(shortcutbar, text='PYTHON PROJECT',bg='cyan2',fg='purple',height=2,font='CalibriLight 12 bold')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)
    Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(master, text='\n\n\nCafe Management System\n\n\nThe project is designed by',fg='turquoise2',font='Times 20 bold').pack(side=TOP,anchor=CENTER)
    Label(master, text='Ashish Agrawal (151257)',fg='turquoise2',font='Times 25 bold').pack(side=TOP,anchor=CENTER)
    Label(master, text='Batch-B2',fg='turquoise2',font='Times 25 bold').pack(side=TOP,anchor=CENTER)
    Label(master, text='Email-id-ashishbyn@gmail.com',fg='turquoise2',font='Times 25 bold').pack(side=TOP,anchor=CENTER)
    Label(master, text='Mobile No-7240915586',fg='turquoise2',font='Times 25 bold').pack(side=TOP,anchor=CENTER)
    Label(master, text='Submitted To',fg='turquoise2',font='Times 20 bold').pack(side=TOP,anchor=CENTER)
    Label(master, text='Dr. Mahesh Kumar',fg='turquoise2',font='Times 25 bold').pack(side=TOP,anchor=CENTER)
    
    def sbmt():
        master.destroy()
        page2()
    s = Frame(master, height=30, bg='light green')
    Button(s, text='EXIT',width=16,height=1,bg='cyan2',fg='black',font='Times 12 bold',command=master.destroy,relief="groove").pack(side=BOTTOM,fill=X ,anchor=SW)
    s.pack(side=BOTTOM,fill=X,anchor=SW)
def submit():
    submit=askyesno("Quit System","Do you want to quit?")
    if submit > 0:
        root1.destroy()
        return   
s = Frame(root1, height=30, bg='light green')
Button(s, text='EXIT',width=16,height=1,bg='light blue',fg='black',font='Times 14 bold',command=submit,background="turquoise2",relief="groove").pack(side=BOTTOM,fill=X,anchor=SW)
s.pack(side=BOTTOM,expand=NO, fill=X)    
Button(padx=16,pady=1,bd=4,fg="black",font=("arial",14,"bold"),background="turquoise2",width=4,
           text="About us",command=aboutus,relief="groove").pack(side=BOTTOM,fill=X,anchor=SW)

Button(padx=16,pady=1,bd=4,fg="black",font=("arial",14,"bold"),background="turquoise2",width=4,
                text="Enter",command=enter,relief="groove").pack(side=BOTTOM,fill=X,anchor=SW)
root1.mainloop()

