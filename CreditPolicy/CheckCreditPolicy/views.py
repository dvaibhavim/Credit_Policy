from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def CheckCreditPolicy(request):
	response_data = {}
    headers = {'content_type':'application/json'}
    data = request.POST.get('data') 
    Policy = json.loads(data)
    msg = reason = ""
    try:
    	cust_debt = 0.50*Policy['customer_income']
    	if Policy['customer_income']<500:
    		msg  = "REJECT"
    		reason = "LOW_INCOME"
    	#if multiple reject messages are present in input, appending it to the reason rather than returning one message
    	elif Policy['customer_debt']>cust_debt:
    		msg = "REJECT"
    		reason +="HIGH_DEBT_FOR_INCOME"
    	elif Policy['payment_remarks_12m']>0:
    		msg = "REJECT"
    		reason +="PAYMENT_REMARKS_12M"
    	elif Policy['payment_remarks']>1:
    		msg = "REJECT"
    		reason +="PAYMENT_REMARKS"
    	elif Policy['customer_age']<18:
    		msg = "REJECT"
    		reason +="UNDERAGE"
    	else:
    		msg = "ACCEPT"
    except Exception as e:
    	msg +="Error!!! " + str(e)
    response_data['message'] = msg
    response_data['reason'] = reason
    return HttpResponse(json.dumps(response_data), content_type="application/json")

