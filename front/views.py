from django.shortcuts import render, HttpResponse

from datetime import datetime

def home(req):
  return render(req, 'home.html')

def api(req):
  now = datetime.now()
  t = now.strftime("%d-%m-%Y * %H:%M:%S")
  return HttpResponse(f'''
<h4>HELLO from API</h4>
<p>Current time: {t}</p>
''')