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
    # HTML part
    html_body = f"""\
   <html>
  <body>
    <p>Greetings sir/madam,</p>

    <p>We are delighted to invite you to join us at <strong>The GenAI Summit 2025</strong>. This summit is a distinctive platform that brings together government leaders, tech innovators, investors, and entrepreneurs to shape the future of Generative AI.</p>

    <p><strong>Date:</strong> 11th January 2025</p>
    <p><strong>Venue:</strong> Eros Hotel, New Delhi</p>
    <p><strong>Website:</strong> <a href="https://genaisummit.in/" target="_blank">https://genaisummit.in/</a></p>

    <h3>Social Media Handles:</h3>
    <ul>
      <li><a href="https://www.instagram.com/genaisummit01/" target="_blank">Insta - @genaisummit01</a></li>
      <li><a href="https://www.linkedin.com/company/genaisummit2025" target="_blank">LinkedIn - GenAI Summit 2025</a></li>
    </ul>

    <h3>Speakers Lineup:</h3>
    <ul>
      <li><strong>MBA Chai Wala - Prafull Billore</strong></li>
      <li><strong>Rameesh Kailasam</strong> - CEO, IndiaTech</li>
      <li><strong>Sunil Dhaiya</strong> - Executive Vice President-Skilling, Wadhwani Foundation</li>
      <li><strong>Rishikesh Patankar</strong> - Vice President, National Skill Development Corporation</li>
      <li><strong>Pankaj Rai</strong> - Group Chief Data and Analytics Officer, Aditya Birla Group</li>
      <li><strong>Kumar Anurag Pratap</strong> - Vice President, Digital Inclusion & Sustainability Leader, Capgemini</li>
      <li><strong>Geetha Adinarayan</strong> - IBM Distinguished Engineer, CTO, Product Engineering, APAC</li>
      <li><strong>Richa Mukherjee</strong> - Senior Director – PayU</li>
      <li><strong>Atul Gohad</strong> - Head, Generative AI, Bosch Global Software Technologies</li>
      <li><strong>Sahhil Kumar</strong> - CEO, Quick Pay</li>
      <li><strong>Dr N. Panigrahi</strong> - Outstanding Scientist, Centre for AI & Robotics, DRDO</li>
      <li><strong>Kanishka Agiwal</strong> – Head, Service Lines, India & South Asia at Amazon Web Services (AWS)</li>
      <li><strong>Nikhil Bhushan</strong> - CTO, Starbucks</li>
      <li><strong>Abhinav Sharma</strong> - CTO & Director, Artificial Intelligence and Automation Leader, Cisco Systems</li>
      <li><strong>Gaurav Anand</strong> - Head of Data & Analytics, DIAGEO, India</li>
      <li><strong>Nikhil Malhotra</strong> - Chief Innovation Officer, Global Head of AI and Emerging Technologies, Tech Mahindra</li>
      <li><strong>Amit Verma</strong> - Chief Technology Officer, Hindustan Times Digital</li>
      <li><strong>Rajnish Virmani</strong> - CIO Advisor - India, Zoom</li>
      <li><strong>Harneet Singh</strong> - Founder & Chief AI Officer, Rabbitt AI</li>
      <li><strong>Anand Vijay Jha</strong> - Vice President, Visa</li>
      <li><strong>Kamesh Sanghi</strong> - Dy. Country Director, American India Foundation</li>
      <li><strong>Abhishek Lal</strong> – Chief Digital Officer, Marks & Spencer</li>
    </ul>

    <p>We look forward to connecting with you!</p>

    <p>Warm regards,<br><strong>Delegate Team</strong></p>

    <h3>For further queries, contact us at:</h3>
    <p><strong>Email ID:</strong> <a href="mailto:connect@genaisummit.in">connect@genaisummit.in</a></p>
    <p><strong>Contact Number:</strong> +91 62303 56822</p>
    <b>PDF:</b><br>
        <embed src="cid:embedded_pdf" width="600" height="400" type="application/pdf"><br><br>
         <img src="cid:embedded_image" alt="Embedded Image" width="300"><br><br>
        Visit our <a href="https://www.yourwebsite.com">website</a>.<br><br>
  </body>
</html>

    """

    msg = Message(
        subject="Get ready to meet the industry's Best at the GenAI Summit - 11th January 2025,New Delhi",
        sender='"Gen AI-Summit" <Anant@genaisummit.in>',
        recipients=[to_email]

    )
    # msg.body=text_body
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
