# council/views.py
from django.shortcuts import render, get_object_or_404
from .models import Deputy, CouncilDecision

# --- Представления для Депутатов ---
def deputy_list(request):
    """Отображает список всех активных депутатов."""
    deputies = Deputy.objects.filter(is_active=True).order_by('order', 'full_name')
    context = {
        'deputies': deputies
    }
    return render(request, 'council/deputy_list.html', context)

def deputy_detail(request, pk):
    """Отображает детальную страницу одного депутата."""
    deputy = get_object_or_404(Deputy, pk=pk)
    context = {
        'deputy': deputy
    }
    return render(request, 'council/deputy_detail.html', context)

# --- Представления для Решений Кенеша ---
def decision_list(request):
    """Отображает список всех опубликованных решений Кенеша."""
    decisions = CouncilDecision.objects.filter(is_published=True).order_by('-decision_date', '-decision_number')
    context = {
        'decisions': decisions
    }
    return render(request, 'council/decision_list.html', context)

def decision_detail(request, slug):
    """Отображает детальную страницу одного решения Кенеша."""
    decision = get_object_or_404(CouncilDecision, slug=slug, is_published=True)
    context = {
        'decision': decision
    }
    return render(request, 'council/decision_detail.html', context)