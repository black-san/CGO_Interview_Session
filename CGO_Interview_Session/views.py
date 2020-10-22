from django.shortcuts import render
from django.http import HttpResponse
from .forms import createForm
from .compute import computeEarliestTime

def frog(response):
    ''' this function is an initialization of the main view
        PARAM:  the response from HTTP
        RETURN: the http response of each condition
    '''
    #   check if there is response which is POST method or there is clicking on compute button
    if response.method == "POST":
            form = createForm( response.POST )

            #   check if inputs in the form is valid
            if form.is_valid():
                x = form.cleaned_data[ "x" ]
                a = form.cleaned_data[ "a" ]
                
                #   split a into array of string
                array_a = a.split( ", " )
                list_a = []

                #   convert each element in an array from string to integer
                for i in array_a:
                    
                    #   check if an element in array is digit
                    if i.isdigit():
                        list_a.append( int( i ) )
                    
                    #   if there is non-digit, return error message
                    else:
                        return HttpResponse( 'Error: "A" is not an array of integer' )
                
                #   call function to compute the earliest time for crossing
                result = computeEarliestTime( x, list_a )
                
                #   check if the result is 1, display the message to tell the earliest time that is 1 second
                if result == 1:
                    return HttpResponse( 'A frog will use at least {} second to cross to the opposite side.'.format( result ) )
                
                #   check if the result is -1, display the message A frog cannot cross to the opposite side
                elif result == -1:
                    return HttpResponse( 'A frog cannot cross to the opposite side.' )
                
                #   check if the result is 1, display the message to tell the earliest time
                else: 
                    return HttpResponse( 'A frog will use at least {} seconds to cross to the opposite side.'.format( result ) )
    
    #   if there is no clicking the button, create the initial form
    else:
        form = createForm()
        return render( response, "frog.html", {"form": form} )