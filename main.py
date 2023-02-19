
import telebot
import datetime
import calendar

# Define the bot token
BOT_TOKEN = '5830959287:AAFgO3OtUUBQembpF8rR0nMgbEocq8DLoag'

# Create the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Define the clockin_work command
clocked_in_employees = {}

@bot.message_handler(commands=['clockin_work'])
def clockin_work_command(message):
    # Get the employee name
    employee_name = message.text.replace("/clockin_work", "").strip()

    if employee_name in clocked_in_employees:
        # Employee has already clocked in
        clock_in_time = clocked_in_employees[employee_name]
        bot.reply_to(message, f"{employee_name} has already clocked in at {clock_in_time.strftime('%H:%M:%S')} today.")
    else:
        # Employee has not clocked in yet
        # Add employee to the list of clocked in employees
        clock_in_time = datetime.datetime.now()
        clocked_in_employees[employee_name] = clock_in_time
        bot.reply_to(message, f"{employee_name} clocks in at {clock_in_time.strftime('%H:%M:%S')} today.")


# Define the after_work command
clocked_out_employees = {}

@bot.message_handler(commands=['after_work'])
def after_work_command(message):
    # Get the employee name
    employee_name = message.text.replace("/after_work", "").strip()

    if employee_name in clocked_out_employees:
        # Employee has already clocked out
        clock_out_time = clocked_out_employees[employee_name]
        bot.reply_to(message, f"{employee_name} has already clocked out at {clock_out_time.strftime('%H:%M:%S')} today.")
    elif employee_name not in clocked_in_employees:
        # Employee has not clocked in
        bot.reply_to(message, f"{employee_name} has not clocked in today.")
    else:
        # Employee has not clocked out yet
        # Add employee to the list of clocked out employees
        clock_out_time = datetime.datetime.now()
        clocked_out_employees[employee_name] = clock_out_time
        bot.reply_to(message, f"{employee_name} closes at {clock_out_time.strftime('%H:%M:%S')} today.")


# Define the month_work_info command
@bot.message_handler(commands=['month_work_info'])
def month_work_info_command(message):
    # Get the employee name
    employee_name = message.text.replace("/month_work_info", "").strip()

    # Get the current month and year
    now = datetime.datetime.now()
    month = now.month
    year = now.year

    # Calculate the number of working days in the current month
    num_working_days = 0
    days_in_month = calendar.monthrange(year, month)[1]
    for day in range(1, days_in_month + 1):
        date = datetime.date(year, month, day)
        if date.weekday() < 5:
            num_working_days += 1

    # Generate a list of the dates that the employee worked
    working_days = []
    for day in range(1, days_in_month + 1):
        date = datetime.date(year, month, day)
        if date.weekday() < 5 and f"{employee_name}_{date}" in clocked_in_employees:
            working_days.append(day)

    # Generate the bot response
    if len(working_days) == 0:
        response = f"{employee_name} did not work any days in the current month."
    else:
        working_days_str = ", ".join(str(day) for day in working_days)
        response = f"{employee_name} worked {len(working_days)} days out of {num_working_days} working days in the current month. Working days: {working_days_str}"

    # Send the response
    bot.reply_to(message, response)

# Start the bot
bot.polling()

