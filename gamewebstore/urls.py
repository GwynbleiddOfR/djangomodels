from django.urls import include, path
from .views import index, adminGames, administrador, carrito, deleteGame, deleteUser, descriptionGame, editarPerfil, forgetPassword, gatoRandom, login, msgVerificarEmail, register, suspendUser, userProfile, vistaCompras, vistaVender, vistaVentas

urlpatterns = [
    path('', index, name='index'),
    path('adminGames/', adminGames, name='adminGames'),
    path('administrador/', administrador, name='administrador'),
    path('carrito/', carrito, name='carrito'),
    path('deleteGame/', deleteGame, name='deleteGame'),
    path('deleteUser/', deleteUser, name='deleteUser'),
    path('descriptionGame/', descriptionGame, name='descriptionGame'),
    path('editarPerfil', editarPerfil, name='editarPerfil'),
    path('forgetPassword', forgetPassword, name='forgetPassword'),
    path('gatoRandom', gatoRandom, name='gatoRandom'),
    path('login', login, name='login'),
    path('msgVerificarEmail', msgVerificarEmail, name='msgVerificarEmail'),
    path('register', register, name='register'),
    path('suspendUser', suspendUser, name='suspendUser'),
    path('userProfile', userProfile, name='userProfile'),
    path('vistaCompras', vistaCompras, name='vistaCompras'),
    path('vistaVender', vistaVender, name='vistaVender'),
    path('vistaVentas', vistaVentas, name='vistaVentas'),
]