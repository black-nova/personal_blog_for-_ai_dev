#from basic_app.pdf_user import cool_ok
#from basic_app.pdf_delete import rem_pas
def handle_uploaded_file(f):  
    with open('basic_app/pdf/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)
    #cool_ok(f.name)
    #rem_pas(f.name)
  