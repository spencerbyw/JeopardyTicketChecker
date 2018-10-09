# JeopardyTicketChecker
Checks the Jeopardy website for live ticket availability.

## Installation
- Written for Python 3, so make sure that's available
- The only dependencies are found in the `examples` folder, so if you want those you will need the `sendgrid` package. So you can do `pip install sendgrid` or `pip install -r requirements.txt` (use `pip3` if you have both versions of Python installed)
- If you are just modifying the base `jeopardy_ticket_checker.py` script, then the only dependencies you'd have to worry about are those you add yourself :)

## Usage
`jeopardy_ticket_checker.py` contains the core functionality, so it can be run with `python jeopardy_ticket_checker.py` (use `python3` if both versions are installed)

The base script is meant to be modified to allow you to fire an action when tickets are/aren't available. Inside the `examples` folder are some demonstrations of how this is done. For instance, when tickets are available, you can send an email via the Sendgrid API. This could be routinely run with a `cron` job to be automatically notified when tickets are available.
