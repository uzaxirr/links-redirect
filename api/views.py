from django.shortcuts import redirect

RESUME_URL = "https://drive.google.com/file/d/1PW6qGyz9nnC2FGYwoPXDRIn3a4gcYMMg/view?usp=sharing"
def resume_redirect(request):
    response = redirect(RESUME_URL)
    return response

def root_redirect(request):
    response = redirect("https://uzair.biz/")
    return response

def github_redirect(request):
    response = redirect("https://github.com/uzair-ali10")
    return response

def lkdn_redirect(request):
    response = redirect("https://www.linkedin.com/in/uzair-ali10/")
    return response

def twitter_redirect(request):
    response = redirect("https://twitter.com/UzairAli101")
    return response

def dev_redirect(request):
    response = redirect("https://dev.to/uzairali10/")
    return response

def leetcode_redirect(request):
    response = redirect("https://leetcode.com/uzair-ali10/")
    return response

# def resume_redirect(request):
#     response = FileResponse(open('/home/dark/Dev/personal-redirect/config/resume.pdf', 'rb'), content_type='application/pdf')
#     return response
