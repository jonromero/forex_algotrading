# Forex-algotrading
This is the code for the Forex algotrading platform I am building on http://jon.io.
Go there and read the posts!

Feel free to pull and submit any patches you like

# Installation

Open runner.py and put your own OANDA_ACCESS_TOKEN and OANDA_ACCOUNT_ID. Read http://jon.io/forex-brokers.html on how to get those or the documentation in Oanda.

Now let's create a virtualevn in order to install any dependancies:

> virtualenv /tmp/falgo

Let's activate the env
> source /tmp/falgo/bin/activate

Switch to the directory
> cd falgo

Install dependencies
> pip install -r requirements.txt

Start it up!
> python runner.py


For any questions, ping me on twitter @jonromero or http://jon.io