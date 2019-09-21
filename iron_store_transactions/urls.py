from django.urls import path
from . import views
from .views import Pdf
from .views import Pdf_history,Pdf_sale_report
urlpatterns = [
    path('', views.add_transaction , name="add_transaction"),
    path('insert_transaction_to_db', views.insert_transaction_to_db , name="insert_transaction_to_db"),
    path('view_transactions', views.view_transactions , name="view_transactions"),
    path('get_damount', views.get_damount , name="get_damount"),
    path('edit_due', views.edit_due , name="edit_due"),
    path('get_all_dates', views.get_all_dates , name="get_all_dates"),
    path('get_history', views.get_history , name="get_history"),
    path('pdf/<int:receipt>', Pdf.as_view()),
    path('test', views.test , name="test"),
    path('history_pdf/<int:receipt>/<str:date>', Pdf_history.as_view()),   
    path('daily_sale', views.daily_sale , name="daily_sale"),
    path('add_expenses', views.add_expenses , name="add_expenses"),
    path('daily_sales_report/<str:date>', Pdf_sale_report.as_view()),   
]