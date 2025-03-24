from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 


"""
The DefaultRouter in Django REST Framework automatically generates a set of standard URL patterns for a viewset. When you register a viewset with a DefaultRouter, it creates the following default routes:
Default Routes Created by DefaultRouter

Assuming you have a viewset called UserViewSet registered with the router under the prefix users, the following routes will be created:
1. List Users
    URL: /users/
    Method: GET
    Description: Retrieve a list of all users.
2. Create User
    URL: /users/
    Method: POST
    Description: Create a new user.
3. Retrieve User
    URL: /users/{id}/
    Method: GET
    Description: Retrieve a specific user by ID.
4. Update User
    URL: /users/{id}/
    Method: PUT
    Description: Update a specific user by ID (replace the entire user).
5. Partial Update User
    URL: /users/{id}/
    Method: PATCH
    Description: Partially update a specific user by ID (update only the fields provided).
6. Delete User
    URL: /users/{id}/
    Method: DELETE
    Description: Delete a specific user by ID.


"""