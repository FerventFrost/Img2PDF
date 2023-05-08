import os
from PIL import Image

def ReadDirList(ImageFolder):
    """Read the directory list of the image folder and sort it"""
    DirList = os.listdir(ImageFolder)
    DirList.sort()
    return DirList

def Img2PDF(ImageFolder, PDFName):
    """Convert images in the image folder to PDF
    ImageFolder: Image folder path
    PDFName: PDF file name"""
    image = [ Image.open(f"{ImageFolder}/" + str(f)) for f in ReadDirList(ImageFolder)]
    image[0].save(f"{PDFName}.pdf", "PDF",resolution=100.0, save_all=True, append_images=image[1:])


if __name__ == "__main__":
    ImageFolder = "Image"
    PDFName = "Kratos.pdf"
    Img2PDF(ImageFolder, PDFName)