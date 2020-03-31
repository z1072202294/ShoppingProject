# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path,include

# =============================================================

# from TTL.baseApps import ttl_user
# urlpatterns = [
#     path('resigter/',include(ttl_user.urls)),
#     path('ttl/v1',)
# ]