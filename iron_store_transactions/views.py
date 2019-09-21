from django.shortcuts import render
from items.models import Item
from django.http import JsonResponse
import json
from . models import IronStoreTransaction , IronStoreTransactionItems, IronStoreTransactionHistory, IronStoreDailyExpenses
import uuid
from datetime import datetime
import datetime as dt
from django.db.models import Sum
from django.views.generic import View
from .render import Render
import math


def add_transaction(request):
    item_list = Item.objects.all()
    return render(request , 'transactions/add_transaction.html',{'items':item_list})

def insert_transaction_to_db(request):
    if request.method == 'POST':
        item_ids = json.loads(request.POST.get('ids'))
        inames = json.loads(request.POST.get('inames'))
        prices = json.loads(request.POST.get('prices'))
        quantities = json.loads(request.POST.get('quantities'))
        totals = json.loads(request.POST.get('totals'))
        cname = request.POST.get('cname')
        phone = request.POST.get('phone')
        discount = request.POST.get('discount')
        totalamount = request.POST.get('totalamount')
        paid = request.POST.get('paid')
        damount = request.POST.get('damount')
        notes = request.POST.get('notes')
        receipt_id = str(uuid.uuid4().fields[-1])[:59]

        irTransation = IronStoreTransaction()
        irTransation.receipt_id = receipt_id
        irTransation.total_amount = totalamount
        irTransation.discount = discount
        irTransation.cname = cname
        irTransation.phone = phone
        irTransation.notes = notes
        irTransation.firt_time_paid = paid
        irTransation.first_time_damount = damount
        irTransation.today_date = dt.date.today()
        irTransation.added_at = datetime.now()
        irTransation.save()


        for i,i_,p,q,t in zip(item_ids,inames,prices,quantities,totals):
            irItems   =  IronStoreTransactionItems()
            irItems.item_name = i_
            irItems.item_quantity = q
            irItems.item_unit_price = p
            irItems.item_total_price = t
            irItems.item_id = i        
            irItems.receipt_id = irTransation
            irItems.added_at = datetime.now()
            irItems.save()

            remaining = 0
            item = Item.objects.filter(id=i).all()
            for it in item:
                stock = float(it.item_quantity)-float(q)
                remaining = stock if stock > 0 else 0
            item.update(item_quantity=remaining) 

        irHistory = IronStoreTransactionHistory()
        irHistory.paid = paid
        irHistory.damount = damount
        irHistory.receipt_id = irTransation
        irHistory.added_at = datetime.now()
        irHistory.today_date = dt.date.today()
        irHistory.save()

        response = {}
        response['obj'] = receipt_id
        return JsonResponse(response)


def view_transactions(request):
    #transactions = IronStoreTransactionHistory.objects.select_related('receipt').filter(damount__gte=-1).values("id","receipt_id",'damount','paid','advance','added_at','receipt__cname','receipt__phone','receipt__total_amount').all()
    
    transactions=IronStoreTransaction.objects.raw('SELECT\
    p1.id,\
    p1.receipt_id,\
    p1.added_at,\
    p1.paid,\
    p1.damount,\
    p1.advance,\
    p2.cname,\
    p2.phone,\
    p2.total_amount\
    FROM\
        iron_store_transactions_ironstoretransactionhistory p1\
    INNER JOIN iron_store_transactions_ironstoretransaction p2 ON\
        p1.receipt_id = p2.receipt_id\
    WHERE\
        p1.added_at =(\
        SELECT\
            MAX(added_at)\
        FROM\
            iron_store_transactions_ironstoretransactionhistory\
        WHERE\
            receipt_id = p1.receipt_id\
        ORDER BY\
            added_at\
        DESC\
    LIMIT 1\
    )')

    
        #print(max(map(itemgetter('id'), list(group))))

    

    #print (transactions.aggregate(Sum('item_quantity'))['item_quantity__sum'])
    #transactions=IronStoreTransaction.objects.values('receipt_id').annotate(item_quantity_sum=Sum('item_quantity')).values_list('receipt_id','item_name')
    """
    transactions=IronStoreTransaction.objects.raw('select * , sum(item_quantity) as sold_quantity from iron_store_transactions_ironstoretransaction group by receipt_id' )
    for t in transactions:
        print(t.receipt_id)
        print(t.sold_quantity)
        print(t.sold_quantity)
    """
    return render(request , 'transactions/view_transactions.html',{'transactions':transactions})
    

def get_damount(request):
    transaction = IronStoreTransactionHistory.objects.filter(receipt_id=request.GET.get('id')).all()
    data = ""
    for o in transaction:
        data = o.damount
    

    response = {}
    response["data"] = data
    return JsonResponse(response)

def edit_due(request):
    if request.method == 'POST':
        receipt_id = request.POST.get('receipt_id')
        damount = request.POST.get('damount')
        paid = request.POST.get('paid')
        advance = request.POST.get('advance')
		
        
		
        remaining_due = float(damount)-float(paid)+float(advance)
        
        
        
        
        try:
            history = IronStoreTransactionHistory()
            history.receipt_id = receipt_id
            history.damount = remaining_due
            history.paid = paid            
            history.advance = advance            
            history.added_at = datetime.now()
            history.save()
            
        except Exception as identifier:
                response = {}
                response['obj'] = 'Something went wrong. Try again!'
                return JsonResponse(response)
        
        
        response = {}
        response['obj'] = 'Due amount updated successfully!'
        return JsonResponse(response)

def get_all_dates(request):
     if request.method == 'GET':
            receipt_id = request.GET.get('id')
            dates = IronStoreTransactionHistory.objects.filter(receipt_id=receipt_id).all()

            data = [{'receipt_id':date.receipt_id,'added_timestamp':str(date.added_at),'added_at': "{}".format(date.added_at.strftime("%B %d, %Y %H:%M:%S"))}
                     for date in dates]
            response = {}
            response['obj'] = data
            return JsonResponse(response)


def get_history(request):
    if request.method == 'GET':
                receipt_id = request.GET.get('id')
                date = request.GET.get('date')

                history = IronStoreTransactionHistory.objects.filter(receipt_id=receipt_id).all()
                transaction = IronStoreTransaction.objects.filter(receipt_id=receipt_id).first()
                for h in history:
                    print("{} =  {}".format(date,str(h.added_at)))
                    if str(h.added_at) is date:
                        print(str(h.added_at))
                data = [{'receipt_id': h.receipt_id,
                        'damount':h.damount,
                        'advance':h.advance,
                        'paid':h.paid,
                        'added_at': "{}".format(h.added_at.strftime("%B %d, %Y %H:%M:%S"))
                        } for h in history if str(h.added_at)==date] 
                data[0]['cname'] = transaction.cname
                response = {}
                response['obj'] = data
                return JsonResponse(response)



def test(request):
    transactions = IronStoreTransactionItems.objects.select_related('receipt').filter(receipt=41340795603834).all()
    return render(request,'transactions/test.html' ,{'transactions':transactions} )


class Pdf(View):

    def get(self, request,receipt):
        transactions = IronStoreTransactionItems.objects.select_related('receipt').filter(receipt=receipt).all()
        trans = IronStoreTransactionHistory.objects.select_related('receipt').filter(damount__gte=0,receipt=receipt).order_by('-added_at').distinct().first()
        receipt_id = 0
        total = 0
        discount = 0
        cname = ''
        phone = ''
        date = ''
        

        for t in transactions:
            receipt_id = t.receipt_id
            total = float(total) + (float(t.item_quantity) * float(t.item_unit_price))
            discount = t.receipt.discount
            cname = t.receipt.cname
            phone = t.receipt.phone 
            dm = t.receipt.first_time_damount   
            pd = t.receipt.firt_time_paid
            date = "{}".format(t.added_at.strftime("%B %d, %Y %H:%M:%S"))




        return Render.render('transactions/test.html', {'transactions':transactions, 'receipt_id':receipt_id , 'total':total,'discount':discount,'damount':dm,'paid':pd,'cname':cname,'phone':phone,'date':date})





class Pdf_history(View):

    def get(self, request,receipt,date):
        history = IronStoreTransactionHistory.objects.filter(receipt_id=receipt).all()
        transaction = IronStoreTransaction.objects.filter(receipt_id=receipt).first()
        print(date)
        cname=transaction.cname
        for h in history:
            print(str(h.added_at))

        data = [{'receipt_id': h.receipt_id,
                'damount':h.damount,
                'advance':h.advance,
                'paid':h.paid,
                'added_at': "{}".format(h.added_at.strftime("%B %d, %Y %H:%M:%S"))
                } for h in history if str(h.added_at)==str(date)] 
        return Render.render('transactions/history.html', {'data':data, 'cname':cname})        

def daily_sale(request):
    date = dt.date.today()
    #transaction = IronStoreTransaction.objects.filter(today_date=date).all()
    transactions=IronStoreTransaction.objects.raw(f'\
    SELECT\
    *\
    FROM\
        iron_store_transactions_ironstoretransactionhistory p1\
    INNER JOIN iron_store_transactions_ironstoretransaction p2 ON\
        p1.receipt_id = p2.receipt_id\
    WHERE\
        p1.today_date = "{date}"\
    ')
    
    return render(request,'transactions/daily_sale.html',{'transactions':transactions})        

def add_expenses(request):
    if request.method == 'POST':
        desc = request.POST.get('description')
        expense = request.POST.get('expense')
        tdate = dt.date.today()
        dlist = desc.split(',')
        elist = expense.split(',')
        
        for d,e in zip(dlist,elist):
            ir = IronStoreDailyExpenses()    
            ir.description = d
            ir.amount = e
            ir.today_date = tdate
            ir.save()
    date = dt.date.today()
    transaction=IronStoreTransaction.objects.raw(f'\
    SELECT\
    *\
    FROM\
        iron_store_transactions_ironstoretransactionhistory p1\
    INNER JOIN iron_store_transactions_ironstoretransaction p2 ON\
        p1.receipt_id = p2.receipt_id\
    WHERE\
        p1.today_date = "{date}"\
    ')
    return render(request,'transactions/daily_sale.html',{'transactions':transaction})                


class Pdf_sale_report(View):
    def get(self,request,date):
        
        transaction=IronStoreTransaction.objects.raw(f'\
            SELECT\
            *\
            FROM\
                iron_store_transactions_ironstoretransactionhistory p1\
            INNER JOIN iron_store_transactions_ironstoretransaction p2 ON\
                p1.receipt_id = p2.receipt_id\
            WHERE\
                p1.today_date = "{date}"\
            ')
        expenses = IronStoreDailyExpenses.objects.filter(today_date=date).all()
        total = 0
        for t in transaction:
            total = total + math.ceil(float(t.paid))

        total_exp = 0
        for e in expenses:
            total_exp = total_exp + math.ceil(float(e.amount))

        today_cash = total - total_exp


        print(expenses)
        return Render.render('transactions/daily_sale_report.html',
        {'transaction':transaction,'expenses':expenses,'date':date,
        'total':total,'total_exp':total_exp,'today_cash':today_cash
        })      