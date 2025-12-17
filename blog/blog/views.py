from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .models import Post
from django.urls import reverse_lazy
from django.shortcuts import render

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogTextView(ListView):
    model = Post
    template_name = "text.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]
    
class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]
    
class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
    
def cv_view(request):
    context = {
        "person": {
            "name": "Shrimp Shrimpson",
            "position": "Ocean Engineer",
            "profile": "Lorem ipsum dolor sit amet, consectetur adipiscing elit..."
        },
        "contact": {
            "phone": "+000 123 456 789",
            "email": "Shrimpson@gmail.com",
            "address": "Baltic Sea"
        },
        "education": [
            {
                "period": "2025 – 2025",
                "degree": "BSc in Ocean Engineering",
                "university": "University of Marine Life"
            },
        ],
        "languages": [
            {"name": "English"},
            {"name": "French"},
            {"name": "Spanish"},
        ],
        "experience": [
        {
            "period": "2025 – Present",
            "position": "Senior Ocean Engineer",
            "description": (
                "Design and maintenance of underwater tunnels and coral-safe platforms. "
                "Led a team of crustaceans in high-pressure deep-sea environments."
            )
        },
        ],
        "skills": [
            {"name": "Underwater Construction"},
            {"name": "Coral-Safe Design"},
            {"name": "Shell Structural Analysis"},
            {"name": "Deep-Sea Navigation"},
            {"name": "Kelp Energy Systems"},
            {"name": "Team Leadership"}
        ]
    }
    return render(request, "cv.html", context)