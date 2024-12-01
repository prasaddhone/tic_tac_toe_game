from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import User
from django.contrib.auth.decorators import login_required

# Home page view
def home(request):
    return render(request, 'home.html')

# Register view
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            return redirect('login')
        else:
            return HttpResponse("Username already taken.")
    return render(request, 'register.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('game')
        else:
            return HttpResponse("Invalid login credentials.")
    return render(request, 'login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def game_view(request):
    if request.method == "POST":
        # Here you would handle the game logic and determine the result
        # For now, assume 'X' is the user and 'O' is the CPU.
        result = "win"  # Assume win for now; you can implement logic for loss or draw
        
        # Update user stats based on the result
        user = request.user
        if result == "win":
            user.wins += 1
        elif result == "lose":
            user.losses += 1
        elif result == "draw":
            user.draws += 1
        
        user.save()

        # Redirect to the result page
        return redirect('result', result=result)
    
    return render(request, 'game.html')

@login_required
def result_view(request, result):
    user = request.user
    
    # Increment score based on result
    if result == 'win':
        user.wins += 1
    elif result == 'lose':
        user.losses += 1
    elif result == 'draw':
        user.draws += 1
    
    # Save the updated user info
    user.save()

    return render(request, 'result.html', {
        'result': result,
        'user': user,  # Pass the user to display their info
    })

def game_view(request):
    # Fetch top 10 players sorted by wins
    top_players = User.objects.all().order_by('-wins')[:10]  # Fetch top 10 players by wins

    return render(request, 'game.html', {
        'top_players': top_players,  # Pass the top 10 players to the template
    })

# Game result view
def result(request, result):
    # Save result logic
    return render(request, 'result.html', {'result': result})
