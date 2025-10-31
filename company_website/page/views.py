from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home_page_view(request):
    context = {
        "inventory_list":["chocolate","cadbury","bournville"],
        "greeting":"thank You For VisIting"
    }
    return render(request,"home.html", context)

class AboutpageView(TemplateView):
    template_name = "about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = "9999999999"
        context["address"] = "123, Main Street, City"
        return context