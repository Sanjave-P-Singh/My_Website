import smtplib


def send_email(message):
    # Your email sending logic here
    try:
        # Create an SMTP server instance
        server = smtplib.SMTP('your_smtp_server_address', 587)  # Update with your SMTP server details

        # Start TLS encryption
        server.starttls()

        # Log in to the SMTP server with your credentials
        server.login('sanjave_singh25@gmail.com', 'your_password')

        # Send the email
        sender = 'sanjave_singh25@gmail.com' 
        receiver = 'recipient@example.com'  # Update with the recipient's email address
        server.sendmail(sender, receiver, message)

        # Close the SMTP server connection
        server.quit()

    except smtplib.SMTPResponseException as e:
        print(f"SMTP Error: {e.smtp_code} - {e.smtp_error}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Call the send_email function with your message content
send_email("Your email message content here")
