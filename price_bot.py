import asyncio
import discord
import time

client=discord.Client()

name = None #Global Variable

def get_from_file(file_name):
    '''
    This function will get data from the filename given
    The extension has to be provided with the file_name

    Parameters: a string that is the file name
    Returns: a string that contains the data
    '''
    f=open(file_name,"r")
    data = f.read()
    f.close()

    return (data)

def get_token():
    '''
    Store the discord bot token in token.txt
    This function will pull it out of the file
    The token is the password for the bot, so keep it safe.

    Parameters: None
    Returns: a string which is the token
    '''
    token = get_from_file("token.txt")

    return (token)

def get_name():
    '''
    Store the name of the cryptocurrency in name.txt
    This function will pull it out of the file
    The name will also be stored in the global variable

    If the global variable name is None, then the function will pull out the
    name from the file. Otherwise, it will simply return the name in the
    global variable

    Parameters: None
    Returns: a string which is the name
    '''
    global name

    if (not name):
        name = get_from_file("name.txt")

    return (name)


def get_time_gap():
    '''
    Store the time gap in time_gap.txt
    That is the amount of time (in seconds) it will wait before updating the price

    Parameters: None
    Returns: an int which is the time gap
    '''
    time_gap = int(get_from_file("time_gap.txt"))

    return (time_gap)


def get_price():
    '''
    Gets the price from the listing.
    Write the method to get the price for your cryptocurrency here

    Parameters: None
    Returns: a float which is the current price
    '''

    return 0 #Currently returns 0; change this return statement when you write
             #your code fot get_price()




previous_time=0

async def update_status():
    '''
    Checks if the required time has passed. If it has, then it updates the bot
    status with the current price.

    Parameters: None
    Returns: None
    '''
    global previous_time
    
    await client.wait_until_ready()

    while not client.is_closed(): #checks if the bot is online
        required_time_gap=get_time_gap()     #The time (in seconds) after the status should be updated
                                  
        curr_time=time.time()
        curr_time_gap=curr_time-previous_time
        
        if curr_time_gap>required_time_gap: #checks if the required time has passed
            price = get_price()
            name = get_name()

            #Updates the status to "Watching Name: 'Price'"
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{name}: {price}'))
            
            previous_time=curr_time

        await asyncio.sleep(5)


client.loop.create_task(update_status()) #Calls the coroutine update_status 

token=get_token()
client.run(token)
        
