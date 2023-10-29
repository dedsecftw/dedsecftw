from telegram.ext.updater import Updater
from telegram.ext.commandhandler import CommandHandler

telegram_token = "6553957180:AAGMS2yfjRu4IjCEmw7dIyG_68Dfz8eXf44"
#creating objects to perform a task
updater = Updater("6553957180:AAGMS2yfjRu4IjCEmw7dIyG_68Dfz8eXf44", use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
  update.message.reply_text('Hello! Welcome to BriansClub BOT.')
  update.message.reply_text('Type /help for bot commands.')
def help(update, context):
  update.message.reply_text(
      """
🟩BOT COMMANDS🟩

 ├ /start -> Start the bot
 ├ /help -> To get bot commands
 ├ /link -> To get shop links
 ├ /contact -> Contact Info
 ├ /vendors -> List of verified vendors in the group chat
 ├ /promo -> To advertise here
      """)

def link(update, context):
  update.message.reply_text(
      """
🟢These are only active shop links, any other link is 100% scam.🟢
🟡If one of the link is down, use another:

☑️https://bclub.cm
☑️https://bclub.mp
☑️https://bclub.tk

⭕Onion link, can only be accessed using Tor browser
☑️http://briansclcfyc5oe34hgxnn3akr4hzshy3edpwxsilvbsojp2gwxr57qd.onion
☑️http://pmd5wavy5j4vyyzlgth7nbeoojsbevdydcovejjxgydqzusm6jij2jad.onion

🟢Reserve domains :
☑️️https://briansclub.cm
☑️https://briansclub.mx
☑️https://briancrabs.de
☑️https://briancrabs.cm
☑️https://briancrabs.mx
      """
  )

def contact(update, context):
  update.message.reply_text('t.me/thomasKGB')

def promo(update, context):
  update.message.reply_text('https://t.me/briansclubcmcc/12')

def vendors(update, context):
  update.message.reply_text(
      """
🟢List of vendors:

(Verified, but we don't take guarantee of anyone on telegram, use escrow. All of them will accept escrow, if not let us know)

├@zodiacFTW -- Spammed cards/Phishing accounts/Escrower
├@Ninjago4L --  Escrower
├@tgrstandartnuy -- @TGRTEAMLINKS -- Lookup
├@staydan49 -- @SS3CXMember_Bot
├@ScamsandGrams174 -- ID/Scans
├@cerberuxsupport1 -- Cerberux Official Admin (CC Shop)
├@Scamgodz753 -- CPNs / TRADELINES

      """
  )

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('link',link))
updater.dispatcher.add_handler(CommandHandler('contact',contact))
updater.dispatcher.add_handler(CommandHandler('promo',promo))
updater.dispatcher.add_handler(CommandHandler('vendors', vendors))

updater.start_polling()  # Start the bot
updater.idle() # Wait for the script to be stopped; this will stop the bot