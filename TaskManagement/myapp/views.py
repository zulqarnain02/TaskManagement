from django.shortcuts import render
from .models import Task
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.timezone import now

def home(request):
    tasks = Task.objects.all()  # Fetch all tasks
    return render(request, 'home.html', {'tasks': tasks})

def Details(request):
    return render(request, 'Details.html')


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        assignto = request.POST.get('assignto')
        duedate = request.POST.get('duedate')
        description = request.POST.get('description')
        
        try:
            Task.objects.create(
                title=title,
                assignto=assignto,
                startdate=now(),
                duedate=duedate,
                description=description,
                status='Pending'  # You can set the default status or get from form
            )
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


def modify_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('id')
        title = request.POST.get('title')
        assignto = request.POST.get('assignto')
        duedate = request.POST.get('duedate')
        description = request.POST.get('description')
        status = request.POST.get('status')
        
        try:
            task = Task.objects.get(taskid=task_id)
            task.title = title
            task.assignto = assignto
            task.duedate = duedate
            task.description = description
            task.status = status
            task.save()
            return JsonResponse({'success': True})
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Task not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


def delete_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('id')
        
        try:
            task = Task.objects.get(taskid=task_id)
            task.delete()
            return JsonResponse({'success': True})
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Task not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


def Details(request, task_id):
    try:
        task = Task.objects.get(taskid=task_id)
        return render(request, 'Details.html', {'task': task})
    except Task.DoesNotExist:
        return render(request, 'error.html', {'message': 'Task not found'})
