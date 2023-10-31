from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from .models import *
from django.contrib.gis.geoip2 import GeoIP2
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from urllib.parse import urlencode
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User

import mpu
from django.views.decorators.cache import never_cache

# Create your views here.

# 
def getProds(request,tenderId):
    tender = Tender.objects.get(id=tenderId)
    tenderDetails = TenderDetails.objects.filter(tenderId=tender)
    print(tenderDetails,request)
    return render(request,"pages/viewprods.html",{"tenderDetails":tenderDetails})
def loginuser(request):
    return render(request,'auth/login.html')

def afterLogin(request):
    print(request)
    return render(request,"auth/login.html")

def startScreen(request):
    if request.user.is_authenticated:
        c=Customer.objects.filter(userId=request.user)
        s=Supplier.objects.filter(userId=request.user)
        if len(c)>0:
            return redirect('customerPage')
        elif len(s)>0:
            return redirect('getTender')
        else:
            return render(request,'auth/startscreen.html')
    return render(request,'auth/startscreen.html')

def customerPage(request):
    return render(request,'pages/customer.html')

def loadLocation(request):
    userObj=User.objects.get(username=request.user)
    if request.method == 'POST':
        lat=request.POST.get('lat')
        longi=request.POST.get('long')
        print(lat,longi)
        try:
            addressObj = Address.objects.get(userId=userObj)
            addressObj.lat = lat
            addressObj.long = longi
            addressObj.save()
        except Exception as e:
            addressObj = Address()
            addressObj.lat = lat
            addressObj.long = longi
            addressObj.userId = userObj
            addressObj.save()
    return render(request,'pages/customer.html')
@never_cache
def placetender(request):
    if request.method == "POST":
        proName = request.POST.getlist("proName")
        proQty = request.POST.getlist("proQty")
        kmRange = request.POST.get("kmRange")
        prodCat= request.POST.get("procat")
        print(f"The Range :{kmRange}")
        customer = Customer.objects.get(userId=request.user)
        print(customer)
        tender =Tender()
        tender.catId=category.objects.get(id=prodCat)
        tender.customerId = customer
        tender.save()
        supplierObj = Supplier.objects.all()
        nearBySupplier = []
        print(supplierObj)
        if(len(proName)==1):
            tenderDetails = TenderDetails()
            tenderDetails.tenderId = tender
            tenderDetails.productName = proName[0]
            tenderDetails.qty = proQty[0]
            tenderDetails.save()
        else:
            for i in range(0,len(proName)):
                tenderDetails = TenderDetails()
                tenderDetails.tenderId = tender
                tenderDetails.productName = proName[i]
                tenderDetails.qty = proQty[i]
                tenderDetails.save()
        try:
            userLocation = Address.objects.get(userId=customer.userId)
            lat1 = userLocation.lat 
            lon1 = userLocation.long
        except Exception as e:
            print(e)
        if(kmRange == "1"):
            for s in supplierObj:
                location = Address.objects.get(userId=s.userId)
                nearBySupplier.append({"name":s.userId.username,"latitude":location.lat,"longitude":location.long})
            for data in nearBySupplier:
                print(data)
        else:
            for supplier in supplierObj:
                location = Address.objects.get(userId=supplier.userId)
                # Point two
                lat2 = location.lat
                lon2 = location.long
                dist = mpu.haversine_distance((lat1, lon1), (lat2, lon2))
                print(f"the disatnce is {dist:.2f}")
                if(int(dist)<=int(kmRange)):
                    nearBySupplier.append({"name":supplier.userId.username,"latitude":location.lat,"longitude":location.long})
            for data in nearBySupplier:
                print(data)
        print(f"the near by supplier is {nearBySupplier}")
        # send nearby supplier to the template for showing in map
        return render(request,"pages/nearBySup.html",{"nearBySupplier":nearBySupplier})
    customer = Customer.objects.filter(userId=request.user)
    if len(customer) == 0 :
        customer = Customer()
        customer.userId = request.user
        customer.role = 0
        customer.save()
    cat=category.objects.all()
    return render(request,"auth/tender.html",{"category":cat})

def vendorshop(request):
    return render(request,"pages/vendorshop.html")

def nearByDealer(request):
    
    return render(request,"pages/nearBySup.html",{"nearBySupplier":nearBySupplier})
class AddressView(CreateView):
    model = Address 
    fields = ['address']
    template_name = 'auth/map.html'
    success_url = '/getMe'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data  (**kwargs)
        context['mapbox_access_token'] = 'pk.eyJ1IjoiZXN3YXJpdHNtZSIsImEiOiJja2lvZ3YycDAxYXMzMnFsYnAybDBlZXhvIn0.XLS1ZaIb5mwh43r8ElL_5A'
        context['addresses'] = Address.objects.all()
        return context


def grtCord(request):
    if request.method=="POST":
        print(request.POST.get("Lat"))
        print(request.POST.get('Long'))
        userObj = User.objects.get(username=request.user)
        supplier = Supplier.objects.get(userId=userObj)
        addresObj = Address()
        addresObj.lat = float(request.POST.get('Lat'))
        addresObj.long = float(request.POST.get('Long'))
        addresObj.address = supplier.shopName
        addresObj.userId = userObj
        
        addresObj.save()
        print(request.POST.get('Lat'))
        return redirect('mapMain')  

    return render(request,"auth/getCord.html")

def vendorOnboarding(request):
    userObj = User.objects.get(username=request.user)
    if request.method == "POST":
        sname = request.POST.get("sname")
        simg = request.FILES.get("simg")
        contact = request.POST.get("contact")
        gstNo = request.POST.get("gstNo")
        gimg = request.FILES.get("gimg")
        cat = request.POST.get("category")
        lat = request.POST.get("lat")
        longi = request.POST.get("long")
        supplier = Supplier()
        supplier.gstNo = gstNo
        supplier.gstImg = gimg
        supplier.mobileNo = contact
        supplier.shopName = sname
        supplier.shopImg = simg
        supplier.userId = userObj
        supplier.catId = category.objects.get(id=cat)
        supplier.save()
        addressObj = Address()
        addressObj.lat = lat
        addressObj.long = longi
        addressObj.userId = userObj
        addressObj.save()
        return redirect("getTender")
    print(userObj)
    supplierObj = Supplier.objects.filter(userId =userObj)
    print(len(supplierObj))
    if len(supplierObj)>0:
        return redirect('getTender')
    else:
        cat = category.objects.all()
        return render(request,"pages/vendorOnboarding.html",{"cat":cat})

def getTender(request):
    tenders = Tender.objects.filter(fullFilled=False)
    return render(request,"pages/displayTender.html",{"tenders":tenders})

def viewTenders(request):
    if request.method == "POST":
        if request.POST.get("viewProd"):
            tenderId = request.POST.get("viewProd")
            print(tenderId)
            return getProds(request,tenderId)
        elif request.POST.get("delTen"):
            delTen=request.POST.get("delTen")
            tender = Tender.objects.get(id=delTen)
            tender.delete()
            return redirect("viewTenders")
        elif request.POST.get("viewQuat"):
            viewQuat = request.POST.get("viewQuat")
            tender = Tender.objects.get(id=viewQuat)
            print(tender)
            Penquotations = Quotation.objects.filter(tender=tender,tender__fullFilled=False,quotation_status=False)
            comQuatations = Quotation.objects.filter(tender=tender,tender__fullFilled=True,quotation_status=True)
            return render(request,"pages/showQuat.html",{"Penquotations":Penquotations,"comQuatations":comQuatations})
  
    tenders=Tender.objects.all()
    quotList=[]
    for t in tenders:
        quotObj=Quotation.objects.filter(tender=t,quotation_status=True)
        quotList.append(len(quotObj))
    data=zip(tenders,quotList)
    return render(request,"pages/viewTenders.html",{"data":data})
    
def giveQuat(request, id):
    tender = get_object_or_404(Tender, id=id)
    if request.method == "POST":
        price = request.POST.getlist("qprice")
        total_price = 0

        supplier = Supplier.objects.get(userId=request.user)
        qObj=Quotation()
        qObj.tender = tender
        qObj.supplier = supplier   
        for i in range(0, len(price)):
            qObj.pricePerQty = price[i]
            total_price += int(price[i])
        qObj.totalPrice = total_price
        qObj.save()
        return redirect("getTender")

    ten_det = TenderDetails.objects.filter(tenderId=tender)
    return render(request, "pages/giveQuatation.html", {"tenDet": ten_det, "tender": tender})

def pendingQuat(request):
    if request.method == "POST":
        if request.POST.get("viewProd"):
            tenderId = request.POST.get("viewProd")
            print(tenderId)
            return getProds(request,tenderId)
        elif request.POST.get("accept"):
            quat = request.POST.get("accept")
            # quat will have two values comma saparated
            quat = quat.split(",")
            
            t = Tender.objects.get(id=quat[0])
            t.fullFilled=True
            t.save()
            quatObj = Quotation.objects.get(id=quat[1])
            quatObj.quotation_status=True
            quatObj.save()
        elif request.POST.get("reject"):
            quat = request.POST.get("reject")
            quat = quat.split(",")

            quatObj = Quotation.objects.get(id=quat[1])
            
            quatObj.delete()
    return redirect("viewTenders")

def logoutUser(request):
    logout(request)
    return redirect("startscreen")