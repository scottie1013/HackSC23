from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')


def prediction_form(request):
    return render(request, 'prediction_form.html')

def prediction_result(request):
    return render(request, 'prediction_result.html')

def test(request):
    return render(request, 'test.html')

# def test1(request):
#     return render(request, 'test1.html')


# # views.py
# import your_model  # Import your trained model module

# views.py
import joblib  # Import joblib for loading the model

def test1(request):
    # Load the model from the .pkl file
    model_path = 'my_django_app/models/your_model.pkl'
    model = joblib.load('C:/Users/Aditee/OneDrive/Documents/GitHub/HackSC23/hacksc/svm.pkl')

    # Process data if necessary
    input_data = ...

    # Get predictions from the model
    predictions = model.predict(input_data)

    # Pass predictions as context to the template
    context = {'predictions': predictions}
    return render(request, 'test1.html', context)

# def predict_recurrence(request):
#     if request.method == 'POST':
#         age = request.POST.get('age')
#         menopause = request.POST.get('menopause')
#         tumor_size = request.POST.get('tumor_size')
#         inv_nodes = request.POST.get('inv_nodes')
#         node_caps = request.POST.get('node_caps')
#         irradiate = request.POST.get('irradiate')

#         # Load the trained model
#         # model = joblib.load('C:/Users/Aditee/OneDrive/Documents/GitHub/HackSC23/hacksc/svm.pkl')
#         # try:
#         #     model = joblib.load(r'C:/Users/Aditee/OneDrive/Documents/GitHub/HackSC23/hacksc/svm.pkl')
#         # except Exception as e:
#         #     print(f"Error loading the model: {e}")

#         # Prepare the input data in the format expected by the model
#         input_data = [age, menopause, tumor_size, inv_nodes, node_caps, irradiate]
        
#         try:
#             model = joblib.load('C:/Users/Aditee/OneDrive/Documents/GitHub/HackSC23/hacksc/svm.pkl')
#         except Exception as e:
#             print(f"Error loading the model: {e}")

#         # Make a prediction
#         prediction = model.predict([input_data])

#         # Pass the prediction to the template
#         context = {'prediction': prediction}
#         return render(request, 'prediction_result.html', context)

#     return render(request, 'prediction_form.html')


# import pickle

# # Load the trained model
# with open('svm.pkl', 'rb') as f:
#     model = pickle.load(f)

# def predict_recurrence(request):
#     if request.method == 'POST':
#         age = request.POST.get('age')
#         menopause = request.POST.get('menopause')
#         tumor_size = request.POST.get('tumor_size')
#         inv_nodes = request.POST.get('inv_nodes')
#         node_caps = request.POST.get('node_caps')
#         irradiate = request.POST.get('irradiate')

#         # Convert categorical inputs to numerical values
#         categorical_values = {
#             'lt40': 0,
#             'ge40': 1,
#             'premeno': 2,
#             'yes': 1,
#             'no': 0,
#         }

#         age = int(age)
#         menopause = categorical_values[menopause]
#         tumor_size = int(tumor_size)
#         inv_nodes = int(inv_nodes)
#         node_caps = categorical_values[node_caps]
#         irradiate = categorical_values[irradiate]

#         # Create the input data for the model
#         input_data = [age, menopause, tumor_size, inv_nodes, node_caps, irradiate]

#         # Make predictions using the model
#         prediction = model.predict(input_data)

#         # Create the context dictionary
#         context = {
#             # 'age': age,
#             # 'menopause': menopause,
#             # 'tumor_size': tumor_size,
#             # 'inv_nodes': inv_nodes,
#             # 'node_caps': node_caps,
#             # 'irradiate': irradiate,
#             'prediction': prediction[0]
#         }

#         # Render the HTML template with the context
#         return render(request, 'prediction_result.html', context)



from django.shortcuts import render
from . forms import PredictCreateForm
from .models import PredictCancer
import pickle
from django.views.generic.list import ListView
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin


def PredictCreate(request):
    form = PredictCreateForm()

    # collect input from client
    context = {'prediction': ""}
    if request.method == 'POST':
        age = request.POST.get('age')
        menopause = request.POST.get('menopause')
        tumor_size = request.POST.get('tumor_size')
        inv_nodes = request.POST.get('inv_nodes')
        node_caps = request.POST.get('node_caps')
        irradiate = request.POST.get('irradiate')

        #umpickle save labels from the LabelEncoder
        # age_p = pickle.load(open('svm.pkl', 'rb'))
        # meno = pickle.load(open('svm.pkl', 'rb'))
        # tumor = pickle.load(open('svm.pkl', 'rb'))
        # nodes = pickle.load(open('svm.pkl', 'rb'))
        # caps = pickle.load(open('svm.pkl', 'rb'))
        # radd = pickle.load(open('svm.pkl', 'rb'))
        # with open('svm.pkl', 'rb') as f:
        #     model = pickle.load(f)

        # #get value of selected variable
        # age_val = age_p.transform([age])
        # meno_val = meno.transform([menopause])
        # tumor_val = tumor.transform([tumor_size])
        # nodes_val = nodes.transform([inv_nodes])
        # caps_val = caps.transform([node_caps])
        # radd_val = radd.transform([irradiate])

        #make predictions
        # scaled= pickle.load(open('scaling.pkl', 'rb'))
        model = joblib.load(open('svm.pkl', 'rb'))

        # classification = model.predict(model.transform([[age_val, meno_val, tumor_val, nodes_val, caps_val, radd_val]]))
        input_data = [age, menopause, tumor_size, inv_nodes, node_caps, irradiate]

        # Make predictions using the model
        prediction = model.predict(input_data)

        #saving prediction in database
        result = prediction[0]
        if result == 0:
            context['prediction'] =  "No Recurrence Events"
        elif result == 1:
            context['prediction'] =  "Recurrence Events"
        else:
            return 'error'
        
        PredictCancer.objects.create(age=age, menopause=menopause, tumor_size=tumor_size, inv_nodes=inv_nodes,
                 node_caps=node_caps,  irradiate=irradiate, classification=context['prediction'])
        
        return render(request, "prediction_result.html", context)

    return render(request, 'prediction_form.html', {'form':form})