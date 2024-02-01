from django.shortcuts import render, redirect, get_object_or_404

from .models import AllUsers01  # Import the new model

def homef(request):
    return render(request, "homeH.html")

def viewAllf(request):
    users=AllUsers01.objects.all()                #retrieve all instances of the AllUsers01 model.
    return render(request, "viewAllH.html",{'users':users})

def addf(request):
    if request.method == "POST":
        # Fetch data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        amount = request.POST.get('amount')

        # Create an AllUsers01 object and save it to the database
        user = AllUsers01(name=name, email=email, dob=dob, amount=amount)
        user.save()

        print("Data has been added to the database")
        return redirect("viewAllUP/")

    return render(request, "addH.html")


def deletef(request, user_id):
    user = get_object_or_404(AllUsers01, pk=user_id)
    user.delete()
    return redirect("viewAllUP/")

def update_userf(request, user_id):
    user = get_object_or_404(AllUsers01, pk=user_id)
    return render(request, "updateH.html", {'user': user})

def do_update_userf(request, user_id):
    if request.method == 'POST':
        user_name = request.POST.get("user_name")
        user_email = request.POST.get("user_email")
        user_dob = request.POST.get("user_dob")
        user_amount = request.POST.get("user_amount")

        user = AllUsers01.objects.get(pk=user_id)
        user.name = user_name
        user.email = user_email
        user.dob = user_dob
        user.amount = user_amount

        user.save()
    return redirect("viewAllUP/")



def depositf(request):
    if request.method == 'POST':
        user_email = request.POST.get("user_email")
        deposit_amount = int(request.POST.get("deposit_amount", 0))  # Convert to integer, default to 0 if not provided

        user = get_object_or_404(AllUsers01, email=user_email)
        user.amount += deposit_amount
        user.save()

    return render(request, "depositeH.html")


def withdrawf(request):
    insufficient_balance = False

    if request.method == 'POST':
        user_email = request.POST.get("user_email")
        withdraw_amount = int(
            request.POST.get("withdraw_amount", 0))  # Convert to integer, default to 0 if not provided

        user = get_object_or_404(AllUsers01, email=user_email)

        if withdraw_amount <= user.amount:
            user.amount -= withdraw_amount
            user.save()
        else:
            insufficient_balance = True

    return render(request, "withdrawH.html", {'insufficient_balance': insufficient_balance})


def transferf(request):
    if request.method == 'POST':
        sender_email = request.POST.get("sender_email")
        recipient_email = request.POST.get("recipient_email")
        transfer_amount = int(request.POST.get("transfer_amount", 0))  # Convert to integer, default to 0 if not provided

        sender = get_object_or_404(AllUsers01, email=sender_email)
        recipient = get_object_or_404(AllUsers01, email=recipient_email)

        if transfer_amount <= sender.amount:
            sender.amount -= transfer_amount
            recipient.amount += transfer_amount
            sender.save()
            recipient.save()
        else:
            print("Insufficient balance for the transfer.")

    return render(request, "transferH.html")


def viewonef(request):
    user = None

    if request.method == 'POST':
        user_email = request.POST.get("user_email")
        user = get_object_or_404(AllUsers01, email=user_email)
    else:
        user = None  # Clear the user variable if the form is not submitted

    return render(request, "viewoneH.html", {'user': user})

