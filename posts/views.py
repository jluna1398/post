from django.shortcuts import render
from django.views.generic import ListView, DetailView
import pandas as pd 
import numbers 
import collections
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import Normalizer, StandardScaler
# Create your views here.
from .models import Post


def LDA(f, array_des, step) -> int:
    # Take some parameters here and update. 
    return array_des * step




class HomePageView(ListView):
    model = Post
    template_name = "home.html"


def LinearRegression( data, model, steps):
    data = pd.read_csv(data, delimeter='*')
    data.head()
    # selects what type of pipelines you want to create
    # Create a standar Scaler here to make the data
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    model = LinearRegression()
    model.fit(data_scaled)
    return model
    
    
