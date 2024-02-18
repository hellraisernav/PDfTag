from PyPDF2 import PdfFileReader

def get_info(path):
    with open(path,'rb') as f:
        pdf=PdfFileReader(f)
        info= pdf.getDocumentInfo()
        number_of_pages=pdf.getNumPages()


    print(info)

    author=info.author
    creator=info.creator
    producer=info.producer
    subject=info.subject
    title=info.title
    keywords=info.keywords
    tag=info.tag

if __name__=='__main__':
    path='FCFR.pdf'
    get_info(path)