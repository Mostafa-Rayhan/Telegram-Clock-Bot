#
# import telebot
# import datetime
#
# # Define the bot token
# BOT_TOKEN = '5830959287:AAFgO3OtUUBQembpF8rR0nMgbEocq8DLoag'
#
# # Create the bot
# bot = telebot.TeleBot(BOT_TOKEN)
#
# # Define the time command
# # @bot.message_handler(commands=['time'])
# # def time_command(message):
# #     # Get the current time
# #     now = datetime.datetime.now()
# #     # Format the time as a string
# #     time_str = now.strftime('%H:%M:%S')
# #     # Send the time to the chat
# #     bot.reply_to(message, f"The current time is {time_str}.")
#
# # Define the clockin_work command
# clocked_in_employees = {}
#
# @bot.message_handler(commands=['clockin_work'])
# def clockin_work_command(message):
#     # Get the employee name
#     employee_name = message.text.replace("/clockin_work", "").strip()
#
#     if employee_name in clocked_in_employees:
#         # Employee has already clocked in
#         clock_in_time = clocked_in_employees[employee_name]
#         bot.reply_to(message, f"{employee_name} has already clocked in at {clock_in_time.strftime('%H:%M:%S')} today.")
#     else:
#         # Employee has not clocked in yet
#         # Add employee to the list of clocked in employees
#         clock_in_time = datetime.datetime.now()
#         clocked_in_employees[employee_name] = clock_in_time
#         bot.reply_to(message, f"{employee_name} clocks in at {clock_in_time.strftime('%H:%M:%S')} today.")
#
#
# # Start the bot
# bot.polling()
#
#
#



# import telebot
# import time
# import datetime
#
# # Define the bot token and the chat ID
# BOT_TOKEN = '5830959287:AAFgO3OtUUBQembpF8rR0nMgbEocq8DLoag'
# CHAT_ID = '26715376'
#
# # Create the bot
# bot = telebot.TeleBot(BOT_TOKEN)
#
# # Define the start command
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(CHAT_ID, 'Bot started. Send /stop to stop real-time updates.')
#     # Start sending updates every second
#     while True:
#         send_update()
#         time.sleep(1)
#
# # Define the stop command
# @bot.message_handler(commands=['stop'])
# def stop(message):
#     bot.send_message(CHAT_ID, 'Bot stopped.')
#     # Stop sending updates
#
# # Define the send_update function
# def send_update():
#     # Get the current time
#     now = datetime.datetime.now()
#     # Format the time as a string
#     time_str = now.strftime('%H:%M:%S')
#     # Send the time to the chat
#     bot.send_message(CHAT_ID, f"The current time is {time_str}.")
#
# # Start the bot
# bot.polling()

#
# import telebot
# import time
# import datetime
#
# # Define the bot token
# BOT_TOKEN = '5830959287:AAFgO3OtUUBQembpF8rR0nMgbEocq8DLoag'
#
# # Create the bot
# bot = telebot.TeleBot(BOT_TOKEN)
#
# # Define the start command
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.reply_to(message, 'Bot started. Send /stop to stop real-time updates.')
#     # Start sending updates every second
#     while True:
#         send_update(bot, message.chat.id)
#         time.sleep(1)
#
# # Define the stop command
# @bot.message_handler(commands=['stop'])
# def stop(message):
#     bot.reply_to(message, 'Bot stopped.')
#     # Stop sending updates
#
# # Define the send_update function
# def send_update(bot, chat_id):
#     # Get the current time
#     now = datetime.datetime.now()
#     # Format the time as a string
#     time_str = now.strftime('%H:%M:%S')
#     # Send the time to the chat
#     bot.send_message(chat_id, f"The current time is {time_str}.")
#
# # Start the bot
# bot.polling()


