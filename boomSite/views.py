import chunk
from fileinput import filename
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import NewUserForm
import json
from json import dumps, load, loads
from django.views.decorators.csrf import csrf_exempt
import ast #para diccionario
import sqlite3
from django.contrib.auth.models import User
from .models import Player
from .models import Global
from .models import Plays
from django.contrib.auth.decorators import login_required   
import hashlib
import mimetypes
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import os





def profile(request):
    mydb = sqlite3.connect("db.sqlite3")
    curr = mydb.cursor()

   
   
  
    
    #ATTEMPTS VS LEVELS PLAYED
    h = 'Level'
    v = 'Attempts'
    s = curr.execute("SELECT attempts, level FROM boomSite_plays ")
    success = [[h , v]]
    
    for x in s:
        success.append([x[1], x[0]])
    s = dumps(success)
    
    
    
    
    return render(request,'boomSite/profile.html', { 'success':s })





