from flask import Flask,request,jsonify
from flask_mail import Mail, Message
import os
import time 

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com' 
app.config['MAIL_PORT'] = 587                
app.config['MAIL_USERNAME'] = 'Anant@genaisummit.in'  
app.config['MAIL_PASSWORD'] = 'fxgi hoqz umlg ikej'          
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

def send_email(to_email,to_name,text_body,pdf_path=None,image_path=None):
    html_body = f"""\
    <html>
      <body>
        <p>Hi {to_name},<br><br>
        <br>
           <b>Embedded PDF:</b><br>
           <embed src="cid:embedded_pdf" width="600" height="400" type="application/pdf"><br><br>
           <b>Embedded Image:</b><br>
           <img src="cid:embedded_image" alt="Embedded Image" width="300"><br><br>
           Visit our <a href="https://www.yourwebsite.com">website</a>.<br><br>
           Best regards,<br>
           Your Name
        </p>
      </body>
    </html>
    """
    msg = Message(
        subject="Personalized Email with Embedded Attachments",
        sender='mridulmittal2003@gmail.com',
        recipients=[to_email]

    )
    msg.body=text_body
    msg.html=html_body

    if pdf_path:
        with app.open_resource(pdf_path) as pdf:
            msg.attach(
                os.path.basename(pdf_path),
                'application/pdf',
                pdf.read(),
                headers={'Content-ID': '<embedded_pdf>'}  # Dictionary format
            )

    # Attach Image with correct headers format
    if image_path:
        with app.open_resource(image_path) as image:
            msg.attach(
                os.path.basename(image_path),
                'image/jpeg',
                image.read(),
                headers={'Content-ID': '<embedded_image>'}  # Dictionary format
            )

    # Send email
    with app.app_context():
        mail.send(msg)

    print(f"Email sent to {to_name} at {to_email}")

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

        # Validate 'pdf_path'
        pdf_path = data.get('pdf_path')
        # if not pdf_path or not os.path.exists(pdf_path):
        #     return jsonify({"error": f"Invalid or missing 'pdf_path': {pdf_path}"}), 400

        # Optional image path
        image_path = data.get('image_path')
        # if image_path and not os.path.exists(image_path):
        #     return jsonify({"error": f"Invalid or missing 'image_path': {image_path}"}), 400

        # Process each recipient
        for recipient in recipient_list:
            if not isinstance(recipient, dict):
                return jsonify({"error": "Each recipient must be a dictionary."}), 400

            to_email = recipient.get('email')
            to_name = recipient.get('name')

            if not to_email or not to_name:
                return jsonify({"error": "Each recipient must include 'email' and 'name'."}), 400

            # Format the text body
            text_body = text_body_template.format(to_name=to_name)

            try:
                send_email(to_email, to_name, text_body, pdf_path, image_path)
            except Exception as e:
                print(f"Failed to send email to {to_email}: {e}")

        return jsonify({"status": "Emails sent successfully"}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500

# Example Usage
if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)), debug=False)




