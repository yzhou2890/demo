# -*- coding: utf-8 -*-
"""
extract a num of pages from a pdf
extract multi-single pages from a pdf
combine multi-pdf files into one pdf

module requirement: PyPDF2

Note: for a pdf file read into memory, its page num starts from 0, not 1

"""



import PyPDF2    
#from PyPDF2 import PdfFileReader as pdfReader

def extract_continuous_page( pdfpath="", pdfname="", Fstpg=0, Lstpg=1, pdfname_out="" ):

    # extract a set of continuous pages from a pdf file    
    
    information = [(pdfname, Fstpg, Lstpg)]
    pdfReader   = PyPDF2.PdfFileReader(open(pdfpath+pdfname+".pdf", "rb"))
    for i in range(len(information)):
        pdf_writer = PyPDF2.PdfFileWriter()
        start = information[i][1]
        end = information[i][2]
        while start<=end:
            pdf_writer.addPage(pdfReader.getPage(start-1))
            start+=1
    
        if(0==len(pdfname_out)):
            pdfname_out = '{}_page_{}_to_page_{}.pdf'.format(information[i][0],information[i][1], information[i][2])
        else:
            pdfname_out = pdfname_out
                
        with open( pdfpath + pdfname_out,'wb') as out:
            pdf_writer.write(out)
             

def extract_multi_page( pdfpath="", pdfname="", pagelist=[], pdfname_out="" ):   
    
    # extract a set of specific pages from a pdf file

    pdfReader   = PyPDF2.PdfFileReader(open(pdfpath+pdfname+".pdf", "rb"))

    pdf_writer  = PyPDF2.PdfFileWriter()

    for j in pagelist:
        pdf_writer.addPage(pdfReader.getPage(j-1))      # '-1' is here as page numbers start from 0, not 1

    if(0==len(pdfname_out)):
        pdfname_out = pdfname+"_selection.pdf"
    else:
        pdfname_out = pdfname_out + ".pdf"
            
    with open( pdfpath + pdfname_out,'wb') as out:
        pdf_writer.write(out)
        

def combine_multi_file( pdfpath="", pdfname="", pdfname_out="" ):   
    
    # combine a set of specific files into one single file
    
    pdf_writer  = PyPDF2.PdfFileWriter()
    
    for p in pdfname:

        pdfReader   = PyPDF2.PdfFileReader(open(pdfpath + p + ".pdf", "rb"))            
        pagelist    = list( range(0,(pdfReader.getNumPages()-1), 1) )
    
        for j in pagelist:
            pdf_writer.addPage(pdfReader.getPage(j-1))      # '-1' is here as page numbers start from 0, not 1
    
    
    if(0==len(pdfname_out)):
        pdfname_out = pdfname+"_selection.pdf"
    else:
        pdfname_out = pdfname_out + ".pdf"
            
    with open( pdfpath + pdfname_out,'wb') as out:
        pdf_writer.write(out)


# demo of extracting a continuous num of pages from a pdf file
pdfpath = "N:/My Documents/Teaching/EL3995/201920/interim_report_marks/"                    # file path 
pdfname = "all_marks"               # filenmae - no extension
Fstpg = 15                      # 1st page - inclusive
Lstpg  = 17                     # last page - inclusive

extract_continuous_page(pdfpath, pdfname, Fstpg, Lstpg)


# demo of extracting a set of single pages from a pdf file
pdfname = "all_marks"               # filenmae - no extension
pagelist = [2,4,6,8]
extract_multi_page( pdfpath, pdfname, pagelist, pdfname_out = "multi_pg")


# demo of combining multi-pdf files into a single pdf file
pdfpath = "N:/My Documents/Teaching/EL3995/201920/interim_report_marks/"
pdflist = [ "a", "aa", "a" ]
combine_multi_file(pdfpath, pdflist, pdfname_out = "multi_fl")


