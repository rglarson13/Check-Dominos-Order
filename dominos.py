# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 17:45:50 2018

@author: Bob Larson
"""

from bs4 import BeautifulSoup
import urllib

# put as many 10-digit phone numbers as you want into the dictionary
numbers = {'Jenny':'5558675309'}

def OrderStatus(phone):
'''
This function grabs the XML page with your order status
and peels a few key details out of it, then returns
a dictionary with those details.

The `phone` parameter is the phone number you used when
you placed your order -- Dominos tracks orders by phone 
number.
'''

    url = 'https://order.dominos.com/orderstorage/GetTrackerData?Phone={}'.format(phone)
    xmldoc = urllib.request.urlopen(url)
    
    soup = BeautifulSoup(xmldoc, 'xml')
    
    os = str(soup.find('OrderStatuses').text)
    
	# if you care to grab other details from the XML file, just add 'em
	# by name to order_dict
    order_dict = {
        'OrderDescription':'',
        'StartTime':'',
        'OvenTime':'',
        'RackTime':''  
    }
    
    if len(os) > 0:
        for key in order_dict:
            order_dict[key] = str(soup.find(key).text)

        order_dict['Phone'] = phone
        
        return order_dict
    
    else:
        return 'No order found for {}'.format(phone)


while True:
    for name in numbers:
        phone = numbers[name]
        
        os = OrderStatus(phone)
        
        if isinstance(os, dict):
            for key in os:
                print('{}: {}'.format(key, os[key]))
        
        else:
            print(os)
	
	# check for status updates twice a minute
    sleep(30)