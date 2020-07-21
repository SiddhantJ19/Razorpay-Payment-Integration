from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt

API_URL = 'http://localhost:8000'

@csrf_exempt
def payment(request):
    return render(request, 'payment.html')


def payment_success(request):
    razorpay_payment_id = request.POST.get('razorpay_payment_id')
    headers = {'content-type': 'application/json',
               'authorization': request.session.get('jwt_token')}
    try:
        response = re.post(API_URL + '/user',
                           data={'paymentID': razorpay_payment_id}, headers=headers)
    except:
        return HttpResponse(json.dumps({'status': 500}))
    return redirect('/auth/login')
