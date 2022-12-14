from tkinter import *
from PIL import ImageTk,Image
import math, random
from twilio.rest import Client
from tkinter import messagebox as mb
import tkinter as tk
import os
import customtkinter
import mysql.connector
import pandas as pd
from tabulate import tabulate
from mysql.connector import Error
root=Tk()
mobile=StringVar()
password=StringVar()
rgst_name=StringVar()
rgst_mobile=StringVar()
rgst_pwd=StringVar()
rgst_mail=StringVar()
rgst_otp=StringVar()

root.geometry("870x560")
root.configure(background="#FFFFFF")
#===============main=====================
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#EDEDED"
        title = Label(self.root, text="Billing Software", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg="#EDEDED", fg="Black", relief=GROOVE)
        title.pack(fill=X)
    # ================variables=======================
        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
        self.syrup = IntVar()
        self.cream = IntVar()
        self.thermal_gun = IntVar()
    # ============grocery==============================
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.spices = IntVar()
        self.flour = IntVar()
        self.maggi = IntVar()
        #=============coldDrinks=============================
        self.sprite = IntVar()
        self.mineral = IntVar()
        self.juice = IntVar()
        self.coke = IntVar()
        self.lassi = IntVar()
        self.mountain_duo = IntVar()
    # ==============Total product price================
        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()
    # ==============Customer==========================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
    # ===============Tax================================
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()
    # =============customer retail details======================
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#EDEDED")
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name:", bg=bg_color, font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg="#EDEDED", font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg="#EDEDED", font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

    # ===================Medical====================================
        F2 = LabelFrame(self.root, text="Medical Purpose", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#EDEDED")
        F2.place(x=5, y=180, width=325, height=380)

        sanitizer_lbl = Label(F2, text="Sanitizer", font=('times new roman', 16, 'bold'), bg="#EDEDED", fg="black")
        sanitizer_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sanitizer_txt = Entry(F2, width=10, textvariable=self.sanitizer, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sanitizer_txt.grid(row=0, column=1, padx=10, pady=10)

        mask_lbl = Label(F2, text="Mask", font=('times new roman', 16, 'bold'), bg="#EDEDED", fg="black")
        mask_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        mask_txt = Entry(F2, width=10, textvariable=self.mask, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mask_txt.grid(row=1, column=1, padx=10, pady=10)

        hand_gloves_lbl = Label(F2, text="Hand Gloves", font=('times new roman', 16, 'bold'), bg="#EDEDED", fg="black")
        hand_gloves_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        hand_gloves_txt = Entry(F2, width=10, textvariable=self.hand_gloves, font=('times new roman', 16, 'bold'), bd=5, relief =GROOVE)
        hand_gloves_txt.grid(row=2, column=1, padx=10, pady=10)

        syrup_lbl = Label(F2, text="Syrup", font=('times new roman', 16, 'bold'), bg="#EDEDED", fg="black")
        syrup_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        syrup_txt = Entry(F2, width=10, textvariable=self.syrup, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        syrup_txt.grid(row=3, column=1, padx=10, pady=10)

        cream_lbl = Label(F2, text="Cream", font=('times new roman', 16, 'bold'), bg = "#EDEDED", fg = "black")
        cream_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        cream_txt = Entry(F2, width=10, textvariable=self.cream, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        cream_txt.grid(row=4, column=1, padx=10, pady=10)

        thermal_gun_lbl = Label(F2, text="Thermal Gun", font=('times new roman', 16, 'bold'), bg="#EDEDED", fg="black")
        thermal_gun_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        thermal_gun_txt = Entry(F2, width=10, textvariable=self.thermal_gun, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        thermal_gun_txt.grid(row=5, column=1, padx=10, pady=10)

    # ==========GroceryItems=========================
        F3 = LabelFrame(self.root, text="Grocery Items", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#EDEDED")
        F3.place(x=340, y=180, width=325, height=380)

        rice_lbl = Label(F3, text="Rice", font=('times new roman', 16, 'bold'), bg="#EDEDED", fg="black")
        rice_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        rice_txt = Entry(F3, width=10, textvariable=self.rice, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        rice_txt.grid(row=0, column=1, padx=10, pady=10)

        food_oil_lbl = Label(F3, text="Food Oil", font=('times new roman', 16, 'bold'), bg="#EDEDED", fg="black")
        food_oil_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        food_oil_txt = Entry(F3, width=10, textvariable=self.food_oil, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        food_oil_txt.grid(row=1, column=1, padx=10, pady=10)

        wheat_lbl = Label(F3, text="Wheat", font=('times new roman', 16, 'bold'), bg="#EDEDED", fg="black")
        wheat_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        wheat_txt = Entry(F3, width=10, textvariable=self.wheat, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        wheat_txt.grid(row=2, column=1, padx=10, pady=10)

        spices_lbl = Label(F3, text="Spices", font=('times new roman', 16, 'bold'), bg="#EDEDED", fg="black")
        spices_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        spices_txt = Entry(F3, width=10, textvariable=self.spices, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        spices_txt.grid(row=3, column=1, padx=10, pady=10)

        flour_lbl = Label(F3, text="Flour", font=('times new roman', 16, 'bold'), bg="#EDEDED", fg="black")
        flour_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        flour_txt = Entry(F3, width=10, textvariable=self.flour, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        flour_txt.grid(row=4, column=1, padx=10, pady=10)

        maggi_lbl = Label(F3, text="Maggi", font=('times new roman', 16, 'bold'), bg="#EDEDED", fg="black")
        maggi_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        maggi_txt = Entry(F3, width=10, textvariable=self.maggi, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        maggi_txt.grid(row=5, column=1, padx=10, pady=10)

    # ===========ColdDrinks================================
        F4 = LabelFrame(self.root, text="Cold Drinks", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#EDEDED")
        F4.place(x=670, y=180, width=325, height=380)

        sprite_lbl = Label(F4, text="Sprite", font=('times new roman', 16, 'bold'), bg="#EDEDED", fg="black")
        sprite_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sprite_txt = Entry(F4, width=10, textvariable=self.sprite, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sprite_txt.grid(row=0, column=1, padx=10, pady=10)

        mineral_lbl = Label(F4, text="Mineral Water", font=('times new roman', 16, 'bold'), bg="#EDEDED", fg="black")
        mineral_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        mineral_txt = Entry(F4, width=10, textvariable=self.mineral, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mineral_txt.grid(row=1, column=1, padx=10, pady=10)

        juice_lbl = Label(F4, text="Juice", font=('times new roman', 16, 'bold'), bg="#EDEDED", fg="black")
        juice_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        juice_txt = Entry(F4, width=10, textvariable=self.juice, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        juice_txt.grid(row=2, column=1, padx=10, pady=10)

        coke_lbl = Label(F4, text="Coke", font=('times new roman', 16, 'bold'), bg="#EDEDED", fg="black")
        coke_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        coke_txt = Entry(F4, width=10, textvariable=self.coke, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        coke_txt.grid(row=3, column=1, padx=10, pady=10)

        lassi_lbl = Label(F4, text="Lassi", font=('times new roman', 16, 'bold'), bg="#EDEDED", fg="black")
        lassi_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        lassi_txt = Entry(F4, width=10, textvariable=self.lassi, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        lassi_txt.grid(row=4, column=1, padx=10, pady=10)

        mountain_duo_lbl = Label(F4, text="Mountain Duo", font=('times new roman', 16, 'bold'), bg="#EDEDED", fg="black")
        mountain_duo_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        mountain_duo_txt = Entry(F4, width=10, textvariable=self.mountain_duo, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mountain_duo_txt.grid(row=5, column=1, padx=10, pady=10)

    # =================BillArea======================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)

        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

    # =======================ButtonFrame=============
        F6 = LabelFrame(self.root, text="Bill Area", font=('times new roman', 14, 'bold'), bd=10, fg="Black", bg="#EDEDED")
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Medical Price", font=('times new roman', 14, 'bold'), bg="#EDEDED", fg="black")
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='W')
        m1_txt = Entry(F6, width=18, textvariable=self.medical_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m1_txt.grid(row=0, column=1, padx=18, pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", font=('times new roman', 14, 'bold'), bg="#EDEDED", fg="black")
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=18, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", font=('times new roman', 14, 'bold'), bg="#EDEDED", fg="black")
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='W')
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drinks_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m3_txt.grid(row=2, column=1, padx=18, pady=1)

        m4_lbl = Label(F6, text="Medical Tax", font=('times new roman', 14, 'bold'), bg="#EDEDED", fg="black")
        m4_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='W')
        m4_txt = Entry(F6, width=18, textvariable=self.medical_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m4_txt.grid(row=0, column=3, padx=18, pady=1)

        m5_lbl = Label(F6, text="Grocery Tax", font=('times new roman', 14, 'bold'), bg="#EDEDED", fg="black")
        m5_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='W')
        m5_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m5_txt.grid(row=1, column=3, padx=18, pady=1)

        m6_lbl = Label(F6, text="Cold Drinks Tax", font=('times new roman', 14, 'bold'), bg="#EDEDED", fg="black")
        m6_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='W')
        m6_txt = Entry(F6, width=18, textvariable=self.cold_drinks_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m6_txt.grid(row=2, column=3, padx=18, pady=1)

    # =======Buttons-======================================
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=760, width=580, height=105)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generateBill_btn = Button(btn_f, command=self.bill_area, text="Generate Bill", bd=2, bg="#535C68", fg="white", pady=12, width=12, font='arial 13 bold')
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", bd=2, bg="#535C68", fg="white", pady=15, width=12, font='arial 13 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()


    def total(self):
        self.m_h_g_p = self.hand_gloves.get()*12
        self.m_sa_p = self.sanitizer.get()*5
        self.m_m_p = self.mask.get()*5
        self.m_s_p = self.syrup.get()*30
        self.m_c_p = self.cream.get()*5
        self.m_t_g_p = self.thermal_gun.get()*15
        self.total_medical_price = float(self.m_m_p + self.m_h_g_p + self.m_sa_p + self.m_c_p + self.m_t_g_p + self.m_s_p )

        self.medical_price.set("Rs. "+str(self.total_medical_price))
        self.c_tax = round((self.total_medical_price*0.05), 2)
        self.medical_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p = self.rice.get()*10
        self.g_f_o_p = self.food_oil.get()*10
        self.g_w_p = self.wheat.get()*10
        self.g_s_p = self.spices.get()*6
        self.g_f_p = self.flour.get()*8
        self.g_m_p = self.maggi.get()*5
        self.total_grocery_price = float(self.g_r_p+self.g_f_o_p+self.g_w_p+self.g_s_p+self.g_f_p+self.g_m_p)

        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*5), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.c_d_s_p = self.sprite.get()*10
        self.c_d_w_p = self.mineral.get()*10
        self.c_d_j_p = self.juice.get()*10
        self.c_d_c_p = self.coke.get()*10
        self.c_d_l_p = self.lassi.get()*10
        self.c_m_d = self.mountain_duo.get()*10
        self.total_cold_drinks_price = float(self.c_d_s_p+self.c_d_w_p+self.c_d_j_p+self.c_d_c_p+self.c_d_l_p+self.c_m_d)

        self.cold_drinks_price.set("Rs. "+str(self.total_cold_drinks_price))
        self.c_d_tax = round((self.total_cold_drinks_price * 0.1), 2)
        self.cold_drinks_tax.set("Rs. "+str(self.c_d_tax))

        self.total_bill = float(self.total_medical_price+self.total_grocery_price+self.total_cold_drinks_price+self.c_tax+self.g_tax+self.c_d_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome Grocery Retail")
        self.txtarea.insert(END, f"\nBill Number: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n================================")
        self.txtarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            mb.showerror("Error", "Customer Details Are Must")
        elif self.medical_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drinks_price.get()=="Rs. 0.0":
            mb.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
    # ============medical===========================
        if self.sanitizer.get() != 0:
            self.txtarea.insert(END, f"\n Sanitizer\t\t{self.sanitizer.get()}\t\t{self.m_sa_p}")
        if self.mask.get() != 0:
            self.txtarea.insert(END, f"\n Mask\t\t{self.mask.get()}\t\t{self.m_m_p}")
        if self.hand_gloves.get() != 0:
            self.txtarea.insert(END, f"\n Hand Gloves\t\t{self.hand_gloves.get()}\t\t{self.m_h_g_p}")
        if self.syrup.get() != 0:
            self.txtarea.insert(END, f"\n Syrup\t\t{self.syrup.get()}\t\t{self.m_s_p}")
        if self.cream.get() != 0:
            self.txtarea.insert(END, f"\n Cream\t\t{self.cream.get()}\t\t{self.m_c_p}")
        if self.thermal_gun.get() != 0:
            self.txtarea.insert(END, f"\n Thermal Gun\t\t{self.sanitizer.get()}\t\t{self.m_t_g_p}")
    # ==============Grocery============================
        if self.rice.get() != 0:
            self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
        if self.food_oil.get() != 0:
            self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_o_p}")
        if self.wheat.get() != 0:
            self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
        if self.spices.get() != 0:
            self.txtarea.insert(END, f"\n Spices\t\t{self.spices.get()}\t\t{self.g_s_p}")
        if self.flour.get() != 0:
            self.txtarea.insert(END, f"\n Flour\t\t{self.flour.get()}\t\t{self.g_f_p}")
        if self.maggi.get() != 0:
            self.txtarea.insert(END, f"\n Maggi\t\t{self.maggi.get()}\t\t{self.g_m_p}")
        #================ColdDrinks==========================
        if self.sprite.get() != 0:
            self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.c_d_s_p}")
        if self.mineral.get() != 0:
            self.txtarea.insert(END, f"\n Mineral\t\t{self.mineral.get()}\t\t{self.c_d_w_p}")
        if self.juice.get() != 0:
            self.txtarea.insert(END, f"\n Juice\t\t{self.juice.get()}\t\t{self.c_d_j_p}")
        if self.coke.get() != 0:
            self.txtarea.insert(END, f"\n Coke\t\t{self.coke.get()}\t\t{self.c_d_c_p}")
        if self.lassi.get() != 0:
            self.txtarea.insert(END, f"\n Lassi\t\t{self.cream.get()}\t\t{self.c_d_l_p}")
        if self.mountain_duo.get() != 0:
            self.txtarea.insert(END, f"\n Mountain Duo\t\t{self.sanitizer.get()}\t\t{self.c_m_d}")
            self.txtarea.insert(END, f"\n--------------------------------")
    # ===============taxes==============================
        if self.medical_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Medical Tax\t\t\t{self.medical_tax.get()}")
        if self.grocery_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
        if self.cold_drinks_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Cold Drinks Tax\t\t\t{self.cold_drinks_tax.get()}")

        self.txtarea.insert(END, f"\n Total Bil:\t\t\t Rs.{self.total_bill}")
        self.txtarea.insert(END, f"\n--------------------------------")
        self.save_bill()

    def save_bill(self):
        op = mb.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            mb.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
           return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                present = "yes"
        if present == "no":
            mb.showerror("Error", "Invalid Bill No")

    def clear_data(self):
        op = mb.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.sanitizer.set(0)
            self.mask.set(0)
            self.hand_gloves.set(0)
            self.syrup.set(0)
            self.cream.set(0)
            self.thermal_gun.set(0)
    # ============grocery==============================
            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.spices.set(0)
            self.flour.set(0)
            self.maggi.set(0)
    # =============coldDrinks=============================
            self.sprite.set(0)
            self.mineral.set(0)
            self.juice.set(0)
            self.coke.set(0)
            self.lassi.set(0)
            self.mountain_duo.set(0)
    # ====================taxes================================
            self.medical_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            self.medical_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def exit_app(self):
        op = mb.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()
def page():
    f1.destroy()
    obj = Bill_App(root)
def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP
def sendotp():
    global msg
    mobile=int(e_mob.get())
    account_sid ="ACc647ef10d7a5108db8ef1aa643c4e98e"
    auth_token ="d8a1ca4b15291a06b1870388fa2b303c"
    client = Client(account_sid, auth_token)
    msg=generateOTP()
    message = client.messages \
                    .create(
                         body=f"{msg} is your OTP for verification and valid for 10 minutes.",
                         from_='+15135863924',
                         to=f"+91{mobile}"
                     )
    res=mb.showinfo("otp","otp sent successfully!")
def nextentrybox(event):
    event.widget.tk_focusNext().focus()
def custom(hostname,username,password,dbname):
    try:
        conn=None
        conn=mysql.connector.connect(
        host=hostname,
        user=username,
        password=password,
        db=dbname
        )
        return conn
    except Error as f:
        print(f"Error occured: {f}")

def fetchdb(conn,query):
    cur1=conn.cursor()
    result = None
    try:
        cur1.execute(query)
        result = cur1.fetchall()
        return result
    except Error as f:
        print(f"Error : {f}")
        
def insert_data(conn,query):
    try:
        cur1=conn.cursor()
        cur1.execute(query)
        conn.commit()
        conn.close()
    except Error as f:
        print(f"Error : {f}")
        
def registration():
    conn1=custom("localhost","root","Shubham@1712","verified_no")
    mob=e_mob.get()
    name=e_name.get()
    pwd=e_pwd.get()
    email=e_mail.get()
    q=f"""insert into memebers values("{name}",{mob},"{pwd}","{email}");"""
    insert_data(conn1,q)
    n=mb.showinfo("success","Successfully Registered")
    login()
    
def verification():
        verification=int(msg)
        enter=int(e_otp.get())
        if enter == verification:
            s=mb.showinfo("Success","OTP Verification Successfull")
        else:
            s=mb.showwarning("Abort","Verification Failed!!")
    
def show():
    mobile=e1.get()
    password=e2.get()
    conn=custom('localhost', 'root', 'Shubham@1712','verified_no')
    q=f"""select mobile,m_password from memebers where m_password="{password}" and mobile="{mobile}";"""
    result=fetchdb(conn,q)

    if mobile==result[0][0] and password==result[0][1]:
        resp=mb.showinfo("Success","Login Successful")
        #callling 2nd window
        page()
    elif mobile!=result[0][0]:
        resp=mb.showwarning("Abort",f"Invalid user or password")
    else:
        resp=mb.showwarning("failure","wrong info")
    
def signup():
#     f2.destroy()
    global sf2
    sf2=Frame(f1,width=400,height=270,bg="#FFFFFF")
    sf2.place(relx=0.05,rely=0.35)
    name=Label(sf2,text="Name:",bg="#FFFFFF")
    name.place(relx=0.15,rely=0.1)
    global e_name
    e_name=customtkinter.CTkEntry(sf2,width=200,text_font=("Brute Sans Regular",14),fg_color="#fff",
                 bg_color="#FFFFFF",text_color="black",corner_radius=10,textvariable=rgst_name)
    e_name.place(relx=0.35,rely=0.1)
    mobile=Label(sf2,text="Mobile no.:",bg="#FFFFFF")
    mobile.place(relx=0.15,rely=0.22)
    global e_mob
    e_mob=customtkinter.CTkEntry(sf2,width=200,text_font=("Brute Sans Regular",14),fg_color="#fff",
                 bg_color="#FFFFFF",text_color="black",corner_radius=10,textvariable=rgst_mobile)
    e_mob.place(relx=0.35,rely=0.22)
    pwd=Label(sf2,text="Password:",bg="#FFFFFF")
    pwd.place(relx=0.15,rely=0.34)
    global e_pwd
    e_pwd=customtkinter.CTkEntry(sf2,width=200,text_font=("Brute Sans Regular",14),fg_color="#fff",
                 bg_color="#FFFFFF",text_color="black",corner_radius=10,textvariable=rgst_pwd)
    e_pwd.place(relx=0.35,rely=0.34)
    mail=Label(sf2,text="E-mail:",bg="#FFFFFF")
    mail.place(relx=0.15,rely=0.46)
    global e_mail
    e_mail=customtkinter.CTkEntry(sf2,width=200,text_font=("Brute Sans Regular",14),fg_color="#fff",
                 bg_color="#FFFFFF",text_color="black",corner_radius=10,textvariable=rgst_mail)
    e_mail.place(relx=0.35,rely=0.46)
    #submit button
    smt=customtkinter.CTkButton(sf2,width=60,height=20,border_width=0,corner_radius=15,text="Submit",text_color="white",bg_color="#fff",
                                              fg_color="#8F00FF",hover_color="pink",state=NORMAL,command=sendotp)
    smt.place(relx=0.45,rely=0.57)
    otp=Label(sf2,text="OTP:",bg="#FFFFFF")
    otp.place(relx=0.15,rely=0.66)
    global e_otp
    e_otp=customtkinter.CTkEntry(sf2,width=200,text_font=("Brute Sans Regular",14),fg_color="#fff",
                 bg_color="#FFFFFF",text_color="black",corner_radius=10,textvariable=rgst_otp)
    e_otp.place(relx=0.35,rely=0.66)
    #verification button
    verify=customtkinter.CTkButton(sf2,width=60,height=20,border_width=0,corner_radius=15,text="Verify",text_color="white",bg_color="#fff",
                                              fg_color="#8F00FF",hover_color="pink",state=NORMAL,command=verification)
    verify.place(relx=0.45,rely=0.78)
    #registration button
    rgstr=customtkinter.CTkButton(sf2,width=60,height=20,border_width=0,corner_radius=15,text="Register",text_color="white",bg_color="#fff",
                                              fg_color="#8F00FF",hover_color="pink",state=NORMAL,command=registration)
    rgstr.place(relx=0.45,rely=0.9)

def login():

    global f2
    f2=Frame(f1,width=450,height=250,bg="#FFFFFF")
    f2.place(relx=0,rely=0.4)
    l1=Label(f2,text="Mobile no.:",bg="#FFFFFF")
    l1.place(relx=0.2,rely=0.06)
    l2=Label(f2,text="Password:",bg="#FFFFFF")
    l2.place(relx=0.2,rely=0.21)
    global e1
    e1=customtkinter.CTkEntry(f2,width=200,text_font=("Dosis",14,"italic"),fg_color="#fff",
                bg_color="white",text_color="black",corner_radius=10,textvariable=mobile)
    e1.place(relx=0.36,rely=0.05)
    global e2

    e2=customtkinter.CTkEntry(f2,width=200,text_font=("Brute Sans Regular",14),fg_color="#fff",
                 bg_color="#FFFFFF",text_color="black",show="*",corner_radius=10,textvariable=password)
    e2.place(relx=0.36,rely=0.2)
    button1 =customtkinter.CTkButton(f2,width=50,height=20,border_width=0,corner_radius=15,text="Log In",text_color="white",bg_color="#fff",
                                              fg_color="#8F00FF",hover_color="pink",state=NORMAL,command=show)                                 
    button1.place(relx=0.63, rely=0.4)
    frgt=customtkinter.CTkButton(f2,width=50,height=20,corner_radius=10,text="Forgot?",fg_color="#8F00FF",state=NORMAL)
    frgt.place(relx=0.3,rely=0.4)

    
f1=Frame(root,width=850,height=550,bg="#FFFFFF")
f1.place(relx=0.5,rely=0.5,anchor=CENTER)
img1=Image.open(r"C:\Users\Shubham\Desktop\billing system\login pAGE.png")
img=ImageTk.PhotoImage(img1)
l1=Label(f1,image=img)
l1.place(relx=0.5,rely=0.5,anchor=CENTER)
log = customtkinter.CTkButton(f1,width=100,height=30,border_width=0,corner_radius=15,text="Log In",text_color="grey",bg_color="#fff",
                                             fg_color="#FFFFFF",hover_color="blue",state=NORMAL,command=login)                                 
log.place(relx=0.15, rely=0.29)
sign = customtkinter.CTkButton(f1,width=100,height=30,border_width=0,corner_radius=15,text="Sign Up",text_color="grey",bg_color="#fff",
                                             fg_color="#FFFFFF",hover_color="blue",state=NORMAL,command=signup)                                 
sign.place(relx=0.3, rely=0.29)

# f2=Frame(f1,width=450,height=250,bg="#FFFFFF")
# f2.place(x=30,y=125)


login()
root.mainloop()
