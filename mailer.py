from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Flask Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'Anant@genaisummit.in'
app.config['MAIL_PASSWORD'] = 'fxgi hoqz umlg ikej'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

# Function to send email
def send_email(to_email, to_name, text_body, pdf_path=None, image_path=None, html_body=None):
    msg = Message(
        subject="Personalized Email with Embedded Attachments",
        sender='mridulmittal2003@gmail.com',
        recipients=[to_email]
    )
    
    # Set the plain text body
    if text_body:
        msg.body = text_body
    
    # Set the HTML body if provided
    if html_body:
        msg.html = html_body

    # Attach PDF if provided
    if pdf_path:
        with app.open_resource(pdf_path) as pdf:
            msg.attach(
                os.path.basename(pdf_path),
                'application/pdf',
                pdf.read(),
                headers={'Content-ID': '<embedded_pdf>'}
            )

    # Attach image if provided
    if image_path:
        with app.open_resource(image_path) as image:
            msg.attach(
                os.path.basename(image_path),
                'image/jpeg',
                image.read(),
                headers={'Content-ID': '<embedded_image>'}
            )

    # Send email
    with app.app_context():
        mail.send(msg)

    print(f"Email sent to {to_name} at {to_email}")

# Route to send bulk emails
@app.route('/sendemails', methods=['POST'])
def send_bulk_emails_route():
    try:
        # Parse JSON data
        data = request.get_json()
        if not isinstance(data, dict):
            return jsonify({"error": "Invalid JSON structure. Expected a JSON object."}), 400

        # Validate 'recipients' field
        recipient_list = data.get('recipients', [])
        if not isinstance(recipient_list, list):
            return jsonify({"error": "'recipients' must be a list."}), 400

        # Validate 'text_body'
        text_body_template = data.get('text_body')
        if not text_body_template:
            return jsonify({"error": "'text_body' is required."}), 400

        # Validate 'html_body' (optional)
        html_body_template = data.get('html_body', None)
        if not html_body_template:
            # Use the default HTML template if not provided
            html_body_template = """<html>
                                      <body>
                                        <p>Greetings sir/madam,</p>
                                        <p>We are delighted to invite you to join us at The GenAI Summit 2025.</p>
                                        <p>We look forward to connecting with you!</p>
                                        <p>Best regards,<br><strong>Delegate Team</strong></p>
                                      </body>
                                    </html>"""

        # Validate 'pdf_path' (optional)
        pdf_path = data.get('pdf_path')
        # Optional: You can validate pdf_path if required

        # Validate 'image_path' (optional)
        image_path = data.get('image_path')
        # Optional: You can validate image_path if required

        # Process each recipient
        for recipient in recipient_list:
            if not isinstance(recipient, dict):
                return jsonify({"error": "Each recipient must be a dictionary."}), 400

            to_email = recipient.get('email')
            to_name = recipient.get('name')

            if not to_email or not to_name:
                return jsonify({"error": "Each recipient must include 'email' and 'name'."}), 400

            # Format the text and html body with recipient's name
            text_body = text_body_template.format(to_name=to_name)
            html_body = html_body_template.format(to_name=to_name)

            try:
                send_email(to_email, to_name, text_body, pdf_path, image_path, html_body)
            except Exception as e:
                print(f"Failed to send email to {to_email}: {e}")

        return jsonify({"status": "Emails sent successfully"}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500

# Example Usage
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)), debug=False)
