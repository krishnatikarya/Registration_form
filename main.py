from tkinter import*
root = Tk()
root.geometry("500x300")
# Krishna
def getsvals():
    print("Accepted")

# heading
Label(root, text="Python Registration Form", font="ar 15 bold").grid(row=0, column = 3)


#field name
name = Label(root, text="Name")
phoneno =Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
Paymentmode = Label(root, text="Paymentmode")


# packing fields
name.grid(row=1,column=2)
phoneno.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
Paymentmode.grid(row=5,column=2)



# variable for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue =StringVar
Paymentmodevalue =StringVar
checkvalue =IntVar

#creating entry field
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=Paymentmodevalue)


#packing entry feild
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)


#creating checkbox
checkbtn = Checkbutton(text="remember me?", variable= checkvalue) 
checkbtn.grid(row=6, column = 3)

root.mainloop()
from tkinter import*
root = Tk()
root.geometry("500x300")

def getsvals():
    print("Accepted")

# heading
Label(root, text="Python Registration Form", font="ar 15 bold").grid(row=0, column = 3)


#field name
name = Label(root, text="Name")
phoneno =Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
Paymentmode = Label(root, text="Paymentmode")


# packing fields
name.grid(row=1,column=2)
phoneno.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
Paymentmode.grid(row=5,column=2)



# variable for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue =StringVar
Paymentmodevalue =StringVar
checkvalue =IntVar

#creating entry field
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=Paymentmodevalue)


#packing entry feild
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)


#creating checkbox
checkbtn = Checkbutton(text="remember me?", variable= checkvalue) 
checkbtn.grid(row=6, column = 3)

#submit button
Button(text="submit", command=getsvals).grid(row=7, column=3)

root.mainloop()