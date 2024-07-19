from tkinter import *
import random
from datetime import date
from tkinter import messagebox as tmsg
import time
from time import strftime
#--------------------------------Initialization---------------
win=Tk()
#Title of the window is that
win.title("Enterprise Billing Solution")
win.geometry("1340x780")
backcolour="#4D0039"

#-------------------------------Data Storage-----------------
billno=[]
repository={'Oil':107,'Salt':35,'Sugar':50,'Ghee':500,'Atta':70,'Rice':56,'Garam Masala':80}
repository1={'Oil':100,'Salt':20,'Sugar':20,'Ghee':20,'Atta':12,'Rice':200,'Garam Masala':25}
global listingprice
listingprice=[]
#----------------Default text--------------------------------
def Welcometxt():
    text_area.delete(1.0,END)
    text_area.insert(END,"\t\t     Welcome To ABC Retails")
    text_area.insert(END,f"\n=================================================")
    text_area.insert(END,f"\n Bill_Number:\t\t{bill_no.get()}")
    text_area.insert(END,f"\nCustomer Name:\t\t{cust_name_input.get()}")
    text_area.insert(END,f"\nContact:\t\t{cust_ph_input.get()}")
    text_area.insert(END,f"\n=================================================")
    text_area.insert(END,"\n Product\t\t Quantity\t\t Price\t     Total Price")
    text_area.insert(END,f"\n=================================================\n")

#place holders of F2
def additem(*args):
    #if cust_name_in.get()=='':
    #    tmsg.showerror("Data pending","Fill Customer name to continue.")
    #    return
    #if cust_ph_in.get()==''or len(str(cust_ph_in.get()))!=0:
    #    tmsg.showerror("Data pending","Fill Proper Customer Phone number")
    #    return
    if cust_name_input.get()=='':
        tmsg.showerror("Unfilled Data","Enter Customer Name to generate bill.")
        return
    elif cust_ph_input.get()==0 or len(str(cust_ph_input.get()))!=10:
        tmsg.showerror("Unfilled Data","Enter a proper phone number to generate bill.")
        return
    else:
        cust_name_input.config(text=cust_name_input.get())
    if prd_1.get()=='':
        tmsg.showerror("Unfilled Data","Enter atleast one item to generate bill.")
        return
    if prd_quantity_1.get()=='':
        tmsg.showerror("Unfilled Data","Minimum One quantity is required to generate bill.")
        return
    else:
        if repository.get(prd_1.get())==None:
            tmsg.showerror("error","This item is out of stock.")
            return
        elif repository1.get(prd_1.get())<prd_quantity_1.get():
            tmsg.showerror("error","This item is out of stock.")
            return
        else:
            prc=repository.get(prd_1.get())
            qt1=repository1.get(prd_1.get())
            global qt
            qt=prd_quantity_1.get()
            global remqt1
            remqt=qt1-qt
            remqt1="Remaining Quantity:  "+str(remqt)
            ttprice=prc*qt
            text_area.insert(END,f'{prd_1.get()}\t\t{prd_quantity_1.get()}\t\t{prc}\t\t{ttprice}\n')
        prd_rem.config(text=remqt1)
        repository1[prd_1.get()]=remqt
        listingprice.append(ttprice)

def rem_quant():
    rq=repository1.get(prd_1.get())
    rq1="Remaining Quantity:  "+str(rq)
    prd_rem.config(text=rq1)

def update_time():
    global string_time
    string_time=strftime('%H:%M:%S %p')
    tmreal.config(text=string_time)
    tmreal.after(1000,update_time)

def grandbill():
    if cust_name_input.get()=='':
        tmsg.showerror("Unfilled Data","Enter Customer Name to generate bill.")
        return
    elif cust_ph_input.get()==0 or len(str(cust_ph_input.get()))!=10:
        tmsg.showerror("Unfilled Data","Enter a proper phone number to generate bill.")
        return
    else:
        cust_name_input.config(text=cust_name_input.get())
    if prd_1.get()=='':
        tmsg.showerror("Unfilled Data","Enter atleast one item to generate bill.")
        return
    text_area.insert(END,f"\n=================================================")
    text_area.insert(END,f"Total Payable Amount :\t\t\t\t\t\t{sum(listingprice)}")
    text_area.insert(END,f"\n=================================================")
    text_area.insert(END,f"\n\t\tThank you, Visit Again.")

def savebill():
    op=tmsg.askyesno('Save Bill','Do you want to save this bill')
    if op>0:
        bill_details=text_area.get(1.0,END)
        f1=open("C:/Users/Adity/Desktop/New folder (2)/bills/"+str(bill_no.get())+".txt",'x')
        f1.write(bill_details)
        f1.close()
        tmsg.showinfo('Saved',f"Bill has been saved with bill number {bill_no}")
    
def clr():
    if cust_name_input.get()=='':
        tmsg.showerror("Unfilled Data","Enter Customer Name to generate bill.")
        return
    elif cust_ph_input.get()==0 or len(str(cust_ph_input.get()))!=10:
        tmsg.showerror("Unfilled Data","Enter a proper phone number to generate bill.")
        return
    else:
        cust_name_input.config(text=cust_name_input.get())
    if prd_1.get()=='':
        tmsg.showerror("Unfilled Data","Enter atleast one item to generate bill.")
        return
    Welcometxt()
    tmsg.showwarning("ALert!","Customer Data Added")

def save_text():
    text = text_area.get("1.0", END)  # Get all text from the Text widget
    with open(f"{bill_no}.txt", "w") as file:
        file.write(text)
        file.close()
        tmsg.showinfo(f"Bill has been saved with bill number {bill_no}")

def search_bill():
    text_area.delete(1.0,END)
    f = open("C:/Users/Adity/Desktop/New folder (2)/bills/"+sch1_inp.get()+".txt", "r")
    text_area.insert(1.0,f.read()) 

def check_stock_report():
    text_area.delete(1.0,END)
    text_area.insert(END,f"\t\t\tStock")
    text_area.insert(END,f"\n=================================================\n")
    text_area.insert(END,f"Item\t\t\tQuantity\t\t\tPrice")
    text_area.insert(END,f"\n=================================================")
    for i in repository:
        text_area.insert(END,f"\n{i}\t\t\t{repository1.get(i)}\t\t\t{repository.get(i)}")

#=================Variables=================================
cust_name_in=StringVar()
cust_ph_in=IntVar(value='')
bill_no=StringVar()
x=str(random.randint(100,99999))
x1=str(random.getrandbits(10))
y=str(date.today())
z=y+"_"+x+"_"+x1
billno.append(z)
bill_no.set(str(z))
prd_1=StringVar()
prd_quantity_1=IntVar(value='')
#t=time.asctime()
sch_inp=StringVar()

#=================Top Title==================================
title=Label(win,text="Billing Solutions",bg=backcolour,fg="white",font=("timesnewroman",25,"bold"),relief="solid")
title.pack(fill=X)
#================Customer Details============================
F1=LabelFrame(win,text="  Customer Details:",bg=backcolour,fg="#FFDB58",font=("timesnewroman",20,"bold"),relief="solid")
F1.place(x=0,y=80,relwidth=1)
cust_name=Label(F1,text="Customer Name:",bg=backcolour,fg="white",font=("timesnewroman",20,"bold"),relief="raised")
cust_name.grid(row=0,column=0,padx=10,pady=5)
cust_name_input=Entry(F1,width=15,font='arial 20 bold',relief="ridge")
cust_name_input.grid(row=0,column=1,padx=10,pady=5)
cust_ph=Label(F1,text="Contact Number:",bg=backcolour,fg="white",font=("timesnewroman",20,"bold"),relief="raised",width=15,foreground="white")
cust_ph.grid(row=0,column=2,padx=10,pady=5)
cust_ph_input=Entry(F1,width=12,font='arial 20 bold',relief="ridge",textvariable=cust_ph_in)
cust_ph_input.grid(row=0,column=4,padx=10,pady=5)
tm=Label(F1,text="Now :",bg=backcolour,font='Timesnewroman 20 bold',fg="white",relief="raised")
tm.grid(row=0,column=5)
tmreal=Label(F1,text='',width=15,bg=backcolour,fg="white",font="timesnewroman 20 italic")
tmreal.grid(row=0,column=6)
#======================Product List==========================
F2=LabelFrame(win,text="Product Details",bg=backcolour,fg="#FFDB58",font=("timesnewroman",20,"bold"),relief="solid")
F2.place(x=20,y=180,width=630,height=550)
prd=Label(F2,text="Product Name:",bg=backcolour,fg="lightgreen",font=("timesnewroman",20,"bold"))
prd.grid(row=0,column=0,padx=30,pady=20)
prd_input=Entry(F2,width=20,font='arial 15 italic',textvariable=prd_1)
prd_input.grid(row=0,column=1,padx=30,pady=20)

prd_quantity=Label(F2,text="Product Quantity:",bg=backcolour,fg="lightgreen",font=("timesnewroman",20,"bold"))
prd_quantity.grid(row=1,column=0,padx=30,pady=20)
prd_rem=Label(F2,text="Remaining quantity:",width=25,font='arial 15 italic',bg=backcolour,fg="white")
prd_rem.grid(row=2,column=0)
prd_quantity_input=Entry(F2,width=20,font='arial 15 italic',textvariable=prd_quantity_1)
prd_quantity_input.grid(row=1,column=1,padx=30,pady=20)
#======================Search bill==========================
F4=LabelFrame(win,text="-----Add-ons",bg=backcolour,fg="#FFDB58",font=("timesnewroman",20,"bold"))
F4.place(x=1290,y=180,width=230,height=550)
sch1=Label(F4,text="Search Bill:",width=23,bg=backcolour,fg="white",font=("timesnewroman",12,"bold"))
sch1.grid(row=1,column=0)
sch1_inp=Entry(F4,width=15,font=("timesnewroman",12,"bold"),textvariable=sch_inp)
sch1_inp.grid(row=2,column=0)
sch1_src=Button(F4,text="Search",font="arial 15 bold",width=11,command=search_bill,height=3)
sch1_src.grid(row=4,column=0,pady=12)
check_stock=Button(F4,text="Check Stock",command=check_stock_report,font="arial 15 bold",width=11,height=3)
check_stock.grid(row=5,column=0,pady=12)

#===================button==================================
btn1=Button(F2,text="Add item",font="arial 15 bold",width=15,command=additem)
btn1.grid(row=3,column=0,padx=10,pady=30)
btn2=Button(F2,text="Generate Bill",font="arial 15 bold",width=15,command=grandbill)
btn2.grid(row=3,column=1,padx=10,pady=30)
btn3=Button(F2,text="Add \n Customer Details",font="arial 15 bold",width=15,command=clr)
btn3.grid(row=4,column=0,padx=10,pady=30)
btn4=Button(F2,text="Find \nRemaining quantity",font="arial 15 bold",command=rem_quant,width=15,height=2)
btn4.grid(row=4,column=1,padx=10,pady=30)
btn5=Button(F2,text="Print Bill",font="arial 15 bold",width=15,height=2,command=savebill)
btn5.grid(row=5,column=0,padx=10,pady=30)
btn6=Button(F2,text="Exit",font="arial 15 bold",command=quit,width=15,height=2)
btn6.grid(row=5,column=1,padx=10,pady=30)

#=====================billing area===============================
F3=LabelFrame(win,text='Bill Generation Slot',relief=GROOVE,bd=10,font="arial 20 italic",labelanchor=N)
F3.place(x=700,y=180,width=630,height=550)
bill_title=Label(F3,text="INVOICE",font="arial 20 bold",bd=5)
bill_title.pack(fill=X)
#======================Scroll the index=========================
scroll_y=Scrollbar(F3,orient="vertical")
text_area=Text(F3,yscrollcommand=scroll_y,font="timesnewroman 15 italic")
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=text_area.yview)
text_area.pack()
Welcometxt()
update_time()
#full screen
win.attributes('-fullscreen',True)

#Closes app with Escape key
win.bind('<Escape>',quit)
win.mainloop()