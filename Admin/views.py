from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import *
from Account.views import registration
from django.contrib import messages

def homepage(request):
    context = {
        'user_list' : User.objects.all()
    }
    return render(request, 'index1.html', context)

def chart(request):
    context = {
        
    }
    return render(request, 'apex_chart.html', context)

def basicElements(request):
    context = {
        
    }
    return render(request, 'Basic_Elements.html', context)

def bootTable(request):
    context = {
        
    }
    return render(request, 'bootstrap_table.html', context)

def calender(request):
    context = {
        
    }
    return render(request, 'calender.html', context)

def dataTable(request):
    context = {
        
    }
    return render(request, 'data_table.html', context)

def dropdown(request):
    context = {
        
    }
    return render(request, 'dropdown.html', context)

def forgotPass(request):
    context = {
        
    }
    return render(request, 'forgot_pass.html', context)

def invoice(request):
    context = {
        
    }
    return render(request, 'invoice.html', context)

def layouts(request):
    context = {
        
    }
    return render(request, 'Layouts.html', context)

# def login(request):
#     context = {
        
#     }
#     return render(request, 'login.html', context)

# def register(request):
#     context = {
        
#     }
#     return render(request, 'register.html', context)

# Admin
def newAdmin(request):
    form = createAdmin(request.POST or None)
    if form.is_valid():
        form.save()
        form = createAdmin()
    context = {
        'formAdmin':form
    }
    return render(request, 'add_new_admin.html', context)

def adminList(request):
    context = {
        'admin_list' : MainAdmin.objects.all()
    }
    return render(request, 'admin_list.html', context)

def deleteAdmin(request, id):
    deleteadmin = get_object_or_404(MainAdmin, pk=id)
    context = {'deleteadmin': deleteadmin}    
    
    if request.method == 'GET':
        return render(request, 'delete_admin.html',context)
    elif request.method == 'POST':
        deleteadmin.delete()
        messages.success(request,  'The list has been deleted successfully.')
        return redirect('adminList')
    
def editAdmin(request, id):
    editadmin = get_object_or_404(MainAdmin, id=id)

    if request.method == 'GET':
        context = {'form': createAdmin(instance=editadmin), 'id': id}
        return render(request,'edit_admin.html',context)
    
    elif request.method == 'POST':
        form = createAdmin(request.POST, instance=editadmin)
        if form.is_valid():
            form.save()
            messages.success(request, 'The list has been updated successfully.')
            return redirect('adminList')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'edit_admin.html',{'form':form})


# User
def newUser(request):
    form = createUser1(request.POST or None)
    if form.is_valid():
        form.save()
        form = createUser1()
    context = {
        'formUser1':form
    }
    return render(request, 'add_new_user.html', context)

def userList(request):
    context = {
        'user_list' : User.objects.all()
    }
    return render(request, 'user_list.html', context)

def deleteUser(request, id):
    deleteuser = get_object_or_404(User, pk=id)
    context = {'deleteuser': deleteuser}    
    
    if request.method == 'GET':
        return render(request, 'delete_user.html',context)
    elif request.method == 'POST':
        deleteuser.delete()
        messages.success(request,  'The list has been deleted successfully.')
        return redirect('userList')
    
def editUser(request, id):
    editleague = get_object_or_404(User, id=id)

    if request.method == 'GET':
        context = {'form': addLeague(instance=editleague), 'id': id}
        return render(request,'edit_user.html',context)
    
    elif request.method == 'POST':
        form = createUser1(request.POST, instance=editleague)
        if form.is_valid():
            form.save()
            messages.success(request, 'The list has been updated successfully.')
            return redirect('userList')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'edit_user.html',{'form':form})

# League
def LeagueForm(request):
    form = addLeague(request.POST or None)
    if form.is_valid():
        form.save()
        form = addLeague()
    context = {
        'addLeague':form
    }
    return render(request, 'add_league.html', context)

def leagueList(request):
    context = {
        'league_list' : League.objects.all()
    }
    return render(request, 'league_list.html', context)

def deleteLeague(request, id):
    deleteleague = get_object_or_404(League, pk=id)
    context = {'deleteleague': deleteleague}    
    
    if request.method == 'GET':
        return render(request, 'delete_league.html',context)
    elif request.method == 'POST':
        deleteleague.delete()
        messages.success(request,  'The list has been deleted successfully.')
        return redirect('leagueList')
    
def editLeague(request, id):
    editleague = get_object_or_404(League, id=id)

    if request.method == 'GET':
        context = {'form': addLeague(instance=editleague), 'id': id}
        return render(request,'edit_league.html',context)
    
    elif request.method == 'POST':
        form = addLeague(request.POST, instance=editleague)
        if form.is_valid():
            form.save()
            messages.success(request, 'The list has been updated successfully.')
            return redirect('leagueList')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'edit_league.html',{'form':form})

# Club
def ClubForm(request):
    form = addClub(request.POST or None)
    if form.is_valid():
        form.save()
        form = addClub()
    context = {
        'addClub':form
    }
    return render(request, 'add_club.html', context)

def clubList(request):
    context = {
        'club_list' : Club.objects.all()
    }
    return render(request, 'club_list.html', context)

def deleteClub(request, id):
    deleteclub = get_object_or_404(Club, pk=id)
    context = {'deleteclub': deleteclub}    
    
    if request.method == 'GET':
        return render(request, 'delete_club.html',context)
    elif request.method == 'POST':
        deleteclub.delete()
        messages.success(request,  'The list has been deleted successfully.')
        return redirect('clubList')
    
def editClub(request, id):
    editclub = get_object_or_404(Club, id=id)

    if request.method == 'GET':
        context = {'form': addClub(instance=editclub), 'id': id}
        return render(request,'edit_club.html',context)
    
    elif request.method == 'POST':
        form = addClub(request.POST, instance=editclub)
        if form.is_valid():
            form.save()
            messages.success(request, 'The list has been updated successfully.')
            return redirect('clubList')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'edit_club.html',{'form':form})

# TopMatch
def top_match_create(request):
    if request.method == 'POST':
        form = TopMatchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('top_match_create')
    else:
        form = TopMatchForm()
    return render(request, 'top_matches.html', {'form': form})

def topMatchList(request):
    context = {
        'top_match_list' : TopMatch.objects.all()
    }
    return render(request, 'top_matches_list.html', context)

def deleteTopMatch(request, id):
    deletetopmatch = get_object_or_404(TopMatch, pk=id)
    context = {'deletetopmatch': deletetopmatch}    
    
    if request.method == 'GET':
        return render(request, 'delete_top_match.html',context)
    elif request.method == 'POST':
        deletetopmatch.delete()
        messages.success(request,  'The list has been deleted successfully.')
        return redirect('topMatchList')
    
def editTopMatch(request, id):
    edittopmatch = get_object_or_404(TopMatch, id=id)

    if request.method == 'GET':
        context = {'form': TopMatchForm(instance=edittopmatch), 'id': id}
        return render(request,'edit_top_match.html',context)
    
    elif request.method == 'POST':
        form = TopMatchForm(request.POST, instance=edittopmatch)
        if form.is_valid():
            form.save()
            messages.success(request, 'The list has been updated successfully.')
            return redirect('topMatchList')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'edit_top_match.html',{'form':form})

# NextToGo
def NextToGoForm(request):
    form = createNextToGo(request.POST or None)
    if form.is_valid():
        form.save()
        form = createNextToGo()
    context = {
        'formNextToGo':form
    }
    return render(request, 'next_to_go.html', context)

def nextToGoList(request):
    context = {
        'next_to_go_list' : NextToGo.objects.all()
    }
    return render(request, 'next_to_go_list.html', context)

def deleteNextToGo(request, id):
    deletenexttogo = get_object_or_404(NextToGo, pk=id)
    context = {'deletenexttogo': deletenexttogo}    
    
    if request.method == 'GET':
        return render(request, 'delete_next_to_go.html',context)
    elif request.method == 'POST':
        deletenexttogo.delete()
        messages.success(request,  'The list has been deleted successfully.')
        return redirect('nextToGoList')
    
def editNextToGo(request, id):
    editnexttogo = get_object_or_404(NextToGo, id=id)

    if request.method == 'GET':
        context = {'form': createNextToGo(instance=editnexttogo), 'id': id}
        return render(request,'edit_next_to_go.html',context)
    
    elif request.method == 'POST':
        form = createNextToGo(request.POST, instance=editnexttogo)
        if form.is_valid():
            form.save()
            messages.success(request, 'The list has been updated successfully.')
            return redirect('nextToGoList')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'edit_next_to_go.html',{'form':form})
        
# Trending
def TrendingForm(request):
    form = createTrending(request.POST or None)
    if form.is_valid():
        form.save()
        form = createTrending()
    context = {
        'formTrending':form
    }
    return render(request, 'trending.html', context)

def trendingList(request):
    context = {
        'trending_list' : Trending.objects.all()
    }
    return render(request, 'trending_list.html', context)

def deleteTrending(request, id):
    deletetrending = get_object_or_404(Trending, pk=id)
    context = {'deletetrending': deletetrending}    
    
    if request.method == 'GET':
        return render(request, 'delete_trending.html',context)
    elif request.method == 'POST':
        deletetrending.delete()
        messages.success(request,  'The list has been deleted successfully.')
        return redirect('trendingList')
    
def editTrending(request, id):
    editnexttogo = get_object_or_404(Trending, id=id)

    if request.method == 'GET':
        context = {'form': createTrending(instance=editnexttogo), 'id': id}
        return render(request,'edit_trending.html',context)
    
    elif request.method == 'POST':
        form = createTrending(request.POST, instance=editnexttogo)
        if form.is_valid():
            form.save()
            messages.success(request, 'The list has been updated successfully.')
            return redirect('trendingList')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'edit_trending.html',{'form':form})
        
def betSlip(request, id):
    print(id)
    betslip = get_object_or_404(NextToGo, id=id)

    context = {
        'bet_slip' : NextToGo.objects.all(), 'id':id,
    }
    return render(request, 'bet_slip.html', context)

    # betslip = get_object_or_404(NextToGo, id=id)
    # if request.method == 'GET':
    #     context = {'form': createNextToGo(instance=betslip), 'id': id}
    #     return render(request,'bet_slip.html',context)