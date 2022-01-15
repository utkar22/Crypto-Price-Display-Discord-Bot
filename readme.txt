This code is to run a Discord Bot that displays the current price of your
cryptocurrency in it's status, and updates it at given intervals of time.

The first step is to create a Discord Bot Account. This is done through
Discord.com Application Portal. Note down the token and the invite link.

The token is the password to the bot. Keep it very securely, and put it in
"token.txt".

Invite the bot to your server(s), and give it permission to access the channels
where you want to show the price.

Put the name of your cryptocurrency in "name.txt"
The time gap is the intervals (in seconds) in which the price displayed is
updated. Put it in "time_gap.txt", according to your need.

Different Cryptos use different APIs for prices; thus you can write the method
specific to your crypto in get_price()

Now, set up is done, and you simply have to run the code.
