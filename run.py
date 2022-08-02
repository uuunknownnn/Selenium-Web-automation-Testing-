from booking.booking import Booking

#once this method finishes all inside commends
#it runs __exit__() method from the class (Booking())
with Booking(teardown=False) as bot:   #context manager
    bot.land_first_page()
    bot.choose_your_currency('USD')  #pass your favoriate currency or leave empty for USD
    bot.choose_your_destination('new york')
    bot.select_dates(checkin_date='2022-08-08', checkout_date='2022-08-20')
    bot.how_many_adults(8)
    bot.apply_Filtrations()
