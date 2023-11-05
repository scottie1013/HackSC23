from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')


def recurrence(request):
    return render(request, 'recurrence.html')

def pred(request):
    return render(request, 'pred.html')

def test(request):
    return render(request, 'test.html')


# # views.py
# import your_model  # Import your trained model module

# def display_data(request):
#     # Load the trained model
#     model = your_model.load_model()

#     # Process data if necessary
#     input_data = ...

#     # Get predictions from the model
#     predictions = model.predict(input_data)

#     # Pass predictions as context to the template
#     context = {'predictions': predictions}
#     return render(request, 'your_template.html', context)
