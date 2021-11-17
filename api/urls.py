from django.urls import path, include
from .views import root_redirect, github_redirect, lkdn_redirect, twitter_redirect, resume_redirect, dev_redirect, leetcode_redirect

urlpatterns = [
    path('', root_redirect),
    path('resume',resume_redirect),
    path('github', github_redirect),
    path('lkdn', lkdn_redirect),
    path('linkedin', lkdn_redirect),
    path('twitter', twitter_redirect),
    path('dev', dev_redirect),
    path('leetcode', leetcode_redirect),
]
