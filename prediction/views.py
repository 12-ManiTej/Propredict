# Create your views here.

from django.shortcuts import render,redirect
from  django.contrib.auth.models import User,auth
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Home_Details
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import math


# def sighnup(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         email=request.POST['email']
#         password1=request.POST['password1']
#         password2=request.POST['password2']
#         if password1==password2:
#             if User.objects.filter(email=email).exists():
#                 messages.info(request,'email already exists')
#             if User.objects.info(username=username).exists():
#                 messages.info(request,'username already exists')
#             user=User.objects.create_user(username=username,email=email,password=password1)
#             user.save()
#             return redirect('login.html')
#         else:
#             messages.info(request,'password dont match')
#         return render(request,'sighnup.html')
#     else:
#         return render(request,'sighnup.html')
# def login(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password1']
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(user)
#             return redirect('index')
#         else:
#             messages.info(request,'user dont exist')
#         return render(request,'login.html')

@login_required(login_url='login')
def predict(request):
    return render(request,'predict.html')

def index(request):
    return render(request,'index.html')

@login_required(login_url='login')
def home(request):
    dest1 = Home_Details.objects.all()
    return render(request,'home.html',{"dest1":dest1})

def home_details(request,pk):
    dest2=Home_Details.objects.get(id=pk)
    current_building = Home_Details.objects.get(id=pk)
    other_buildings = Home_Details.objects.exclude(id=pk)

    similarities = []
    for building in other_buildings:
        price_building1 = current_building.price
        price_building2 = building.price
        city_building1 = current_building.city
        city_building2 = building.city


        # Calculate the squared difference between the sqft values
        price_difference = (price_building1 - price_building2) ** 2
        city_difference = 0 if city_building1 == city_building2 else 1
        # Calculate the similarity score based on Euclidean distance
        price_weight = 0.4
        city_weight=0.3

        similarity_score = math.sqrt(price_weight*price_difference+city_weight*city_difference)
        similarities.append((building, similarity_score))

    sorted_buildings = sorted(similarities, key=lambda x: x[1], reverse=True)

    top_n = 3
    recommendations = [building for building, _ in sorted_buildings[:top_n]]

    return render(request, 'home_details.html', {'current_building': current_building, 'recommendations': recommendations,'dest2':dest2})
    # dest2 = Home_Details.objects.get(id=pk)
    # return render(request,"home_details.html",{"dest2":dest2})

# def recommend_building(request, building_id):
#     current_building = Home_Details.objects.get(id=building_id)
#     other_buildings = Home_Details.objects.exclude(id=building_id)

#     similarities = []
#     for building in other_buildings:
#         similarity_score = calculate_similarity(current_building, building)
#         similarities.append((building, similarity_score))

#     sorted_buildings = sorted(similarities, key=lambda x: x[1], reverse=True)

#     top_n = 5
#     recommendations = [building for building, _ in sorted_buildings[:top_n]]

#     return render(request, 'home_details.html', {'recommendations': recommendations})

# def calculate_similarity(building1,building2):
#     sqft_building1 = building1.sqft
#     sqft_building2 = building2.sqft

#     # Calculate the squared difference between the sqft values
#     sqft_difference = (sqft_building1 - sqft_building2) ** 2

#     # Calculate the similarity score based on Euclidean distance
#     similarity_score = math.sqrt(sqft_difference)

#     return similarity_score

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
            # Process the signup form data and create the account
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            # Create the user account
            user = User.objects.create_user(username=username, email=email, password=password)
            # messages.success(request,"Account created successfully !")
            # Redirect to the login page
            return redirect('login')
        
        elif 'login' in request.POST:
            # Process the login form data and handle the login
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Authenticate and log in the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

# def login(request):
#     return render(request,'login.html')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
        
#          # Authenticate user credentials
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#              # Log in the user
#             login(request, user)
            
#              # Redirect to a success page or desired URL
#             return redirect('index.html')
#         else:
#              # Display an error message for invalid credentials
#             error_message = "Invalid username or password."
#             return render(request, 'login.html')
    
#     return render(request, 'login.html')

# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         email = request.POST['email']
        
#         # Create a new user
#         user = User.objects.create_user(username=username, password=password, email=email)
        
#         # Log in the user after registration
#         login(request, user)
        
#         # Redirect to a success page or desired URL
#         return redirect('index.html')
    
#     return render(request, 'login.html')



# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
        
#         # Authenticate user credentials
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             # Log in the user
#             login(request, user)
            
#             # Redirect to a success page or desired URL
#             return redirect('index')  # Update to the desired URL name or path, e.g., 'home' or '/'
#         else:
#             # Display an error message for invalid credentials
#             error_message = "Invalid username or password."
#             return render(request, 'login.html', {'error_message': error_message})
    
#     return render(request, 'login.html')

# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         email = request.POST['email']
        
#         # Create a new user
#         user = User.objects.create_user(username=username, password=password, email=email)
        
#         # Log in the user after registration
#         login(request, user)
        
#         # Redirect to a success page or desired URL
#         return redirect('index')  # Update to the desired URL name or path, e.g., 'home' or '/'
    
#     return render(request, 'login.html')


def result(request):
    # data=pd.read_csv(r"C:/Users/jilla/Downloads/USA_housing.csv")
    # data=data.drop(['Address'],axis=1)
    # X=data.drop('Price',axis=1)
    # Y=data['Price']
    # X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=30)
    # model=LinearRegression()
    # model.fit(X_train,Y_train)
    # var1=float(request.GET['n1'])
    # var2=float(request.GET['n2'])
    # var3=float(request.GET['n3'])
    # var4=float(request.GET['n4'])
    # var5=float(request.GET['n5'])
    # pred=model.predict(np.array([var1,var2,var3,var4,var5]).reshape(1,-1))
    # pred=round(pred[0])

    data=pd.read_csv(r"C:/Users/jilla/Downloads/USA_housing.csv")
    # Drop the 'Address' column
    data = data.drop(['Address'], axis=1)

# Split the data into features (X) and target variable (Y)
    X = data.drop('Price', axis=1)
    Y = data['Price']

# Split the data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Create a Random Forest regression model
    model = RandomForestRegressor()

# Train the model
    model.fit(X_train, Y_train)
    var1=float(request.GET['n1'])
    var2=float(request.GET['n2'])
    var3=float(request.GET['n3'])
    var4=float(request.GET['n4'])
    var5=float(request.GET['n5'])
    pred = model.predict(np.array([var1, var2, var3, var4, var5]).reshape(1, -1))
    pred = round(pred[0])
    price="Predicted price is "+str(pred)
    return render(request,'predict.html',{"result2":price})