Step by step instruction to create API through viewsets and router:
1. Create Project
2. Create App (In our case book_app)
   1. Create folder api inside your app
      1. Create serializers.py
      2. Create Viewsets.py
3. Create router.py file at project level
    from app.api(folder).viewsets import yorviewsset
    from rest_framework import routers
   1. create router
   2. register your viewset with created router
4. In project level urls.py set path for your API
    path('bookapi/',include(router.urls)),

Flow:
1. urls.py(project level)------Will look for registered router
2. router.py(project level)----- will look for given viewset
3. Viewsets.py(App level)------ Look for serializer
4. serializers.py------- Look for model
5. model.py-------- Actual Model present here



_**Steps for Authentication and permissions:**_

1. Go to settings and paste below lines
     REST_FRAMEWORK={
    'DEFAULT_PERMISSION_CLASSES':('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.TokenAuthentication',),}
2. Add rest_framework.authtoken in installed apps

3. set project level URl for generating token
    from rest_framework.authtoken import views
    path('app-token-auth/',views.obtain_auth_token,name='app-token-auth')

4. open terminal and runserver 
5. open another terminal 
   1. first pip install httpie
   2. http POST http://localhost:8000/bookapi-token-auth/ username="admin" password="admin" 
   3. http http://localhost:8000/bookapi/book_app/ "Authorization: Token 1719ff2ecdee155492af0d4b132dc2df51563f35"
   
6. Successful!!!!

Note:Instead of writing DEFAULT_PERMISSION_CLASSES and DEFAULT_AUTH_CLASSES in setting you can write it in 
viewsets.
   

_**Steps for Filtering_** 
1. pip install django-filter
2. add in installed apps----- 'django_filters'
3. settings.py
   REST_FRAMEWORK={
    'DEFAULT_FILTER_BACKENDS':('django_filters.rest_framework.DjangoFilterBackend',)}
4. In viewsets
   1. create bookfilter(filters.FilterSet):
   2. Include fields of filter
5. In BookViewSet , set filterset_class=bookfilter