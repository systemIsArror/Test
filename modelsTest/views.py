#encoding:utf-8
from django.db.models import *
from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
	# p = Publisher.pub.exclude(pub_city='北京')
	# p = Publisher.pub.order_by('-pub_name')
	# p = Publisher.pub.only('pub_city')
	# p = Publisher.pub.values(u'pub_name',u'pub_city')
	# p = Publisher.pub.values_list(u'pub_name',u'pub_city')s
	# p = Publisher.pub.all().annotate(Min('pub_price'))
	# p = Publisher.pub.filter(pub_name__contains=u"清华").extra(where=['id=1'])
	p = Publisher.pub.raw('select * from publisher')
	# print p.query

	print p
	context = {'list':p}
	return render(request,'modelsTest/index.html',context)
