from django.shortcuts import render
import stripe

stripe.api_key = "sk_test_51JcPSlFTOXGpyrVRGifT9KJPhZ0RegN3qgU8EVsjZNfvE1TNzeTQdlUuGmKhYEawshRKtlOq2MNKehLRFZ7lTqQt00nLhq3VjA"


def index(request):

    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(request.POST["amount"])
        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['name'],
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount * 100,
            currency='usd',
            description='Donation'
        )
        
        
    resp = 'OKEY'
    context = {
        'response': resp
    }
    return render(request, 'index.html', context)