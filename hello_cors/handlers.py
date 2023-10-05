from corsheaders.signals import check_request_enabled

def cors_allow_mysites(sender, request, **kwargs):
  allowed = ['http://craft.localhost:3000']
  origin = request.META.get("HTTP_ORIGIN")
  if origin in allowed:
    return True
  return False

check_request_enabled.connect(cors_allow_mysites)