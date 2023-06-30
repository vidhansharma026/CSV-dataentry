import io
import csv
from django.shortcuts import render
from . models import Data

# Create your views here.
def index(request):
    return render(request, 'index.html')

def adddata(request):
    if request.method == 'POST':
        rollno = request.POST['rollno']
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        course = request.POST['course']
        fees = request.POST['fees']
        Data.objects.create(
                rollno = rollno,
                name = name,
                email = email,
                mobile = mobile,
                address = address,
                course = course,
                fees = fees,
            )
        return render(request, 'success.html')
    return render(request, 'adddata.html')

def insert_data(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        next(io_string)  # Skip the header row

        for row in csv.reader(io_string, delimiter=','):
            rollno = int(row[0])
            name = str(row[1])
            email = str(row[2])
            mobile = int(row[3])
            address = str(row[4])
            course = str(row[5])
            fees = float(row[6])

            Data.objects.create(
                rollno = rollno,
                name = name,
                email = email,
                mobile = mobile,
                address = address,
                course = course,
                fees = fees,
            )
        return render(request, 'success.html')
    return render(request, 'index.html')

# def stock_list(request):
#     search_query = request.GET.get('search')

#     if search_query:
#         stocks = Data.objects.filter(volume__icontains=search_query)
#     else:
#         stocks = Data.objects.all()

#     return render(request, 'stock_list.html', {'stocks': stocks})
