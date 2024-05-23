from django.shortcuts import render, redirect  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from recipes.forms import UserRegistrationForm

#define a function view called login_view that takes a request from user
def login_view(request):
  #initialize:
  #error_message to None
  error_message = None
  # create Form object with username and password fields
  form = AuthenticationForm()

  # when user hits "login" button, then POST request is generated
  if request.method == 'POST':
    #read the data sent by the form via POST request
    form = AuthenticationForm(data=request.POST)

    #check if form is valid
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')

      #use Django authenticate function to validate the user
      user = authenticate(username=username, password=password)
      if user is not None:
        #if user is authenticated then use pre-defined Django function to login
        login(request, user)
        #& send the user to desired page
        return redirect('recipes:list')
    #in case of error
    else: error_message = 'Unable to login, check username and password and retry.' #print error message
  
  #prepare data to send from view to template
  context = {
    'form': form, #send the form data
    'error_message': error_message #and the error message
  }
  #load the login page using "context" information
  return render(request, 'auth/login.html', context)

# define a view to handle user registration
def register(request):
  if request.method == 'POST':
    registration_form = UserRegistrationForm(request.POST)
    if registration_form.is_valid():
      user = registration_form.save()
      login(request, user)
      return redirect('recipes:list')
    else:
      for error in registration_form.errors.values():
        messages.error(request, error)
        print('error:' + error)
  else:
    registration_form = UserRegistrationForm()
  return render(request, 'auth/register.html', {'registration_form': registration_form})
    

#define a function view called logout_view that takes a request from user
def logout_view(request):
  #use the pre-defined Django function to logout
  logout(request)
  #after logging out go to login form
  return render(request, 'auth/success.html')