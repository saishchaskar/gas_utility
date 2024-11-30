from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate , login as loginUser , logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
# Create your views here.
from services.forms import ServiceRequestForm,SignUpForm
from services.models import ServiceRequest
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = ServiceRequestForm()
        todos = ServiceRequest.objects.filter(user = user).order_by('submitted_at')
        return render(request , 'index.html' , context={'form' : form , 'todos' : todos})

@login_required(login_url='login')
def requests_list(request):
    if request.user.is_authenticated:
        user = request.user
        form = ServiceRequestForm()
        todos = ServiceRequest.objects.filter(user = user).order_by('submitted_at')
        return render(request , 'service_requests.html' , context={'form' : form , 'todos' : todos})

def login(request):
    if request.method == 'GET':
        # Display an empty form for GET requests
        form = AuthenticationForm()
        context = {
            "form": form
        }
        return render(request, 'login.html', context=context)
    else:
        # Process the login form for POST requests
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Get the cleaned data from the form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user is not None:
                # Log in the user
                loginUser(request, user)
                return redirect('home')  # Replace 'home' with your actual homepage URL name
        # If the form is invalid, re-render the page with error messages
        context = {
            "form": form
        }
        return render(request, 'login.html', context=context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Save the user and redirect to the login page
            form.save()
            return redirect('login')  # Update 'login' to your actual login URL name
    else:
        # Instantiate an empty form for GET requests
        form = SignUpForm()

    context = {"form": form}
    return render(request, 'signup.html', context)




@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = ServiceRequestForm(request.POST, request.FILES)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = user
                todo.save()
                return redirect("requests")
        else:
            form = ServiceRequestForm()
            # Fetch choices for request type from ServiceRequest model
            request_type_choices = ServiceRequest.REQUEST_TYPE_CHOICES
            # Pass choices to the form context
            form.fields['request_type'].choices = request_type_choices
        return render(request, 'index.html', context={'form': form})



def delete_todo(request , id ):
    print(id)
    ServiceRequest.objects.get(pk = id).delete()
    return redirect('home')

def change_todo(request , id  , status):
    todo = ServiceRequest.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')

def show_details(request, id):
    # Retrieve the ServiceRequest object for the given ID
    todo = get_object_or_404(ServiceRequest, pk=id)
    
    # Render the template with the ServiceRequest object
    return render(request, 'service_details.html', context={"todo": todo})

def signout(request):
    logout(request)
    return redirect('login')

def profile(request):
    if request.method == 'GET':
        user = request.user
        print(user)
        # print("form\n",form)
        context={
            # "form":form,
            "first_name":user.first_name,
            "last_name":user.last_name,
            "name":(user.first_name).upper()+" "+(user.last_name).upper(),
            "id":user.id,
            "email":user.email,
            "member_from":(user.date_joined).strftime('%Y-%m-%d %H:%M:%S'),
            # "m":user.date_joined,
            "username":user.username
                }
        # t=context['m']
        # print("m=",t,"\n",t.strftime('%Y-%m-%d %H:%M:%S'))
        return render(request , 'user_profile.html' , context=context)
    else:
        print("form=",request.POST)
        form = (request.POST)  
        print("first name=",form['first_name'])
        # user = {
        #     "form" : form
        # }
        
        user=request.user
        user.first_name=form['first_name']
        user.last_name=form['last_name']
        user.email=form['email']
        user.username=form['username']
        print("user in profile:",user)
        user.save()
        if user is not None:
            return redirect('profile')
        
def edit_profile(request):
    if request.method == 'POST':
        print("form=",request.POST)
        form = (request.POST)  
        print("first name=",form['first_name'])
        # user = {
        #     "form" : form
        # }
        
        user=request.user
        user.first_name=form['first_name']
        user.last_name=form['last_name']
        user.email=form['email']
        user.username=form['username']
        print("user in profile:",user)
        user.save()
        # if user is not None:
        return redirect('profile')
    else:
        print("in get edit profile")
        user = request.user
        print(user)
        # print("form\n",form)
        context={
            # "form":form,
            "first_name":user.first_name,
            "last_name":user.last_name,
            "name":(user.first_name).upper()+" "+(user.last_name).upper(),
            "id":user.id,
            "email":user.email,
            "member_from":(user.date_joined).strftime('%Y-%m-%d %H:%M:%S'),
            # "m":user.date_joined,
            "username":user.username
                }
        return render(request , 'profile_edit.html' , context=context)





    