import tkMessageBox
import tkSimpleDialog

from tkinter import *
import xml.etree.ElementTree as ET


class UpdateLink:
    def __init__(self, body):
        self.link = Entry(body,
                         font="Verdana 12",
                          width=50)
        self.link.grid(row = 1, column = 2)

        title = Label(body, text="Picture link", font="Arial 12")
        title.grid(row = 1, column = 1)

        but = Button(body,
                            text="Update",
                            width=6, height=1,
                            bg="red", fg="black")

        but.bind("<Button-1>", self.updatePLink)
        but.grid(row = 1, column = 3)

    def updatePLink(self, event):
        doc = ET.parse('pictureLink.xml')
        root = doc.getroot()
        django = doc.find('link')
        django.text = self.link.get()

        doc.write('pictureLink.xml', encoding="utf-8", xml_declaration=True)
        tkMessageBox.showinfo(
            "Updated",
            "Picture link is updated"
        )




