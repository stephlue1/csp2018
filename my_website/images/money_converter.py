def Currency_exchange():
    print ''
    print 'this is a currency exchange program.'
    print 'Here are the option for exchange. do not worry there are more coming '
    print '1. USD To EUROS'
    print '2. EUROS To USD'
    print '3. USD To CAD'
    print '4. CAD To USD'
    print '5. USD To SWISS FRANC'
    print '6. SWISS FRANC To USD'
    print '7. USD To JPY'
    print '8. JPY To USD'
    print '9. USD To AUD'
    print '10. AUD To USD'
    print '11. USD To Israeli New Shekel'
    print '12. Israeli New Shekel To USD'
    print '13. USD To IRR'
    print '14. IRR To USD'
    print '15. USD To BMD'
    print '16. BMD To USD'
    print '17. USD To KRW'
    print '18. KRW To USD'
    print '19. USD To EGP'
    print '20. EGP To USD'
    print '21. USD To PESO'
    print '22. PESO To USD'
    option = raw_input('to begin the exchange, type the number that corresponds with the exchange ')
    if option == '1':
        amount = int(raw_input('type the amount here '))
        print amount * .81, 'EUROS'
    elif option == '2':
        amount = int(raw_input('type the amount here '))
        print amount * 1.23, 'USD'
    elif option == '3':
        amount = int(raw_input('type the amount here '))
        print amount * 1.29, 'CAD'
    elif option == '4':
        amount = int(raw_input('type the amount here '))
        print amount * .78, 'USD'
    elif option == '5':
        amount = int(raw_input('type the amount here '))
        print amount * .95, 'FRANCS'
    elif option == '6':
        amount = int(raw_input('type the amount here '))
        print amount * 1.05, 'USD'
    elif option == '7':
        amount = int(raw_input('type the amount here '))
        print amount * 106.35, 'JPY'
    elif option == '8':
        amount = int(raw_input('type the amount here '))
        print amount * .0094, 'USD'
    elif option == '9':
        amount = int(raw_input('type the amount here '))
        print amount * 1.30, 'AUD'
    elif option == '10':
        amount = int(raw_input('type the amount here '))
        print amount * .77, 'USD'
    elif option == '11':
        amount = int(raw_input('type the amount here '))
        print amount * 3.5, 'SHEKELS'
    elif option == '12':
        amount = int(raw_input('type the amount here '))
        print amount * .29, 'USD'
    elif option == '13':
        amount = int(raw_input('type the amount here '))
        print amount * 377450, 'IRR'
    elif option == '14':
        amount = int(raw_input('type the amount here '))
        print amount * .000030, 'USD'
    elif option == '15':
        amount = int(raw_input('type the amount here '))
        print amount * 1, 'BMD'
    elif option == '16':
        amount = int(raw_input('type the amount here '))
        print amount * 1, 'USD'
    elif option == '17':
        amount = int(raw_input('type the amount here '))
        print amount * 1058.81, 'KRW'
    elif option == '18':
        amount = int(raw_input('type the amount here '))
        print amount * .00094, 'USD'
    elif option == '19':
        amount = int(raw_input('type the amount here '))
        print amount * 17.67, 'EGP'
    elif option == '20':
        amount = int(raw_input('type the amount here '))
        print amount * .057, 'USD'
    elif option == '21':
        amount = int(raw_input('type the amount here '))
        print amount * 18.31, 'PESO'
    elif option == '22':
        amount = int(raw_input('type the amount here '))
        print amount * 0.055, 'USD'
    else:
        print "whoops... wrong input, try again."
        Currency_exchange()
    
