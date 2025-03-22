# from flask import Flask,request,jsonify
# from flask_mail import Mail, Message
# import os
# import time 

# app = Flask(__name__)

# app.config['MAIL_SERVER'] = 'smtp.gmail.com' 
# app.config['MAIL_PORT'] = 587                
# app.config['MAIL_USERNAME'] = ''  
# app.config['MAIL_PASSWORD'] = '' 
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False

# mail = Mail(app)

# def send_email(to_email,to_name,text_body,pdf_path=None,image_path=None):
#     html_body = f"""\
#    <html>
#   <body>
#     <p>Dear {to_name},</p>

#     <p>It was an absolute honor to have you with us at the Gen AI Summit 2025. Your presence and active participation added immense value to the discussions and collaborations throughout the event. We are truly grateful for your contribution to making the summit a remarkable success.</p>

#     <p>We are delighted to share the moments we captured during the summit. Please find the photo gallery here:</p>
#     <p><a href="https://drive.google.com/drive/folders/1o3wKbJIsDJbTS1mttQrG2yzUiQN_gSFo" target="_blank">https://drive.google.com/drive/folders/1o3wKbJIsDJbTS1mttQrG2yzUiQN_gSFo</a></p>

#     <p>Thank you once again for being a part of this incredible journey to shape the future of Generative AI. We look forward to staying connected and welcoming you to future editions of the summit.</p>

#     <p>Warm regards,<br>Team<br>Gen AI Summit 2025</p>
#     <p>Connect : +91 6230356822</p>
#     <p>Website : <a href="www.genaisummit.in" target="_blank">www.genaisummit.in</a></p>
#   </body>
# </html>
#     """
#     # HTML part
# #     html_body = f"""\
# #    <html>
# #   <body>
# #     <p>Greetings sir/madam,</p>

# #     <p>We are delighted to invite you to join us at <strong>The GenAI Summit 2025</strong>. This summit is a distinctive platform that brings together government leaders, tech innovators, investors, and entrepreneurs to shape the future of Generative AI.</p>

# #     <p><strong>Date:</strong> 11th January 2025</p>
# #     <p><strong>Venue:</strong> Eros Hotel, New Delhi</p>
# #     <p><strong>Website:</strong> <a href="https://genaisummit.in/" target="_blank">https://genaisummit.in/</a></p>

# #     <h3>Social Media Handles:</h3>
# #     <ul>
# #       <li><a href="https://www.instagram.com/genaisummit01/" target="_blank">Insta - @genaisummit01</a></li>
# #       <li><a href="https://www.linkedin.com/company/genaisummit2025" target="_blank">LinkedIn - GenAI Summit 2025</a></li>
# #     </ul>

# #     <h3>Speakers Lineup:</h3>
# #     <ul>
# #       <li><strong>MBA Chai Wala - Prafull Billore</strong></li>
# #       <li><strong>Rameesh Kailasam</strong> - CEO, IndiaTech</li>
# #       <li><strong>Sunil Dhaiya</strong> - Executive Vice President-Skilling, Wadhwani Foundation</li>
# #       <li><strong>Rishikesh Patankar</strong> - Vice President, National Skill Development Corporation</li>
# #       <li><strong>Pankaj Rai</strong> - Group Chief Data and Analytics Officer, Aditya Birla Group</li>
# #       <li><strong>Kumar Anurag Pratap</strong> - Vice President, Digital Inclusion & Sustainability Leader, Capgemini</li>
# #       <li><strong>Geetha Adinarayan</strong> - IBM Distinguished Engineer, CTO, Product Engineering, APAC</li>
# #       <li><strong>Richa Mukherjee</strong> - Senior Director – PayU</li>
# #       <li><strong>Atul Gohad</strong> - Head, Generative AI, Bosch Global Software Technologies</li>
# #       <li><strong>Sahhil Kumar</strong> - CEO, Quick Pay</li>
# #       <li><strong>Dr N. Panigrahi</strong> - Outstanding Scientist, Centre for AI & Robotics, DRDO</li>
# #       <li><strong>Kanishka Agiwal</strong> – Head, Service Lines, India & South Asia at Amazon Web Services (AWS)</li>
# #       <li><strong>Nikhil Bhushan</strong> - CTO, Starbucks</li>
# #       <li><strong>Abhinav Sharma</strong> - CTO & Director, Artificial Intelligence and Automation Leader, Cisco Systems</li>
# #       <li><strong>Gaurav Anand</strong> - Head of Data & Analytics, DIAGEO, India</li>
# #       <li><strong>Nikhil Malhotra</strong> - Chief Innovation Officer, Global Head of AI and Emerging Technologies, Tech Mahindra</li>
# #       <li><strong>Amit Verma</strong> - Chief Technology Officer, Hindustan Times Digital</li>
# #       <li><strong>Rajnish Virmani</strong> - CIO Advisor - India, Zoom</li>
# #       <li><strong>Harneet Singh</strong> - Founder & Chief AI Officer, Rabbitt AI</li>
# #       <li><strong>Anand Vijay Jha</strong> - Vice President, Visa</li>
# #       <li><strong>Kamesh Sanghi</strong> - Dy. Country Director, American India Foundation</li>
# #       <li><strong>Abhishek Lal</strong> – Chief Digital Officer, Marks & Spencer</li>
# #     </ul>

# #     <p>We look forward to connecting with you!</p>

# #     <p>Warm regards,<br><strong>Delegate Team</strong></p>

# #     <h3>For further queries, contact us at:</h3>
# #     <p><strong>Email ID:</strong> <a href="mailto:connect@genaisummit.in">connect@genaisummit.in</a></p>
# #     <p><strong>Contact Number:</strong> +91 62303 56822</p></b><br>
# #         <embed src="cid:embedded_pdf" width="600" height="400" type="application/pdf"><br><br>
# #          <img src="cid:embedded_image" alt="" width="300"><br><br>
# #   </body>
# # </html>

# #     """
# #     html_body = f"""\
# #    <html>
# #   <body>
# #     <p>Respected Sir/Ma'am,</p>

# #     <p>We are thrilled to announce the Gen AI Summit 2025, a premier event dedicated to exploring the transformative potential of Generative AI. Scheduled for January 11, 2025, at the Eros Hotel, New Delhi, this one-day summit will feature a stellar lineup of 25+ expert speakers and an audience of visionaries, innovators, and industry leaders.</p>

# #     <p>This prestigious event offers a unique opportunity for collaboration, and we are reaching out to invite your esteemed organization to partner with us as a sponsor. By supporting the Gen AI Summit 2025, you can:</p>

# #     <ul>
# #       <li>Showcase your brand as a leader in the rapidly evolving AI landscape.</li>
# #       <li>Connect with industry experts, innovators, and decision-makers.</li>
# #         <li>Gain unparalleled visibility and networking opportunities.</li>
# #     </ul>

# #         <p>We also request you to kindly fill out a short Google Form with your contact details to express your interest in collaborating with us for this transformative event. This will help us tailor a partnership package that aligns with your organizational goals and values.</p>

# #         <p>👉 <a href="https://forms.gle/ccEpagyt2kzkGaK38" target="_blank">Google Form Link</a></p>

# #         <p>Your support will contribute significantly to the success of this landmark event, and we believe this collaboration will be mutually rewarding.</p>

# #         <p>For further details about sponsorship packages or any other inquiries, please feel free to contact me directly at <a href="mailto:Gauranshi@genaisummit.in">Gauranshi@genaisummit.in</a> or +91 6230356822.</p>

# #         <p>We look forward to the opportunity of partnering with you to redefine the future of Generative AI.</p>

# #     <p>Warm regards,<br>Gauranshi Gupta<br>Gen AI Summit 2025</p>
# #     <p>📞 Helpline: +91 6230356822</p>
# #     <p>🌐 Website: <a href="www.genaisummit.in" target="_blank">www.genaisummit.in</a></p>
# #     <p>📱 Instagram: <a href="https://www.instagram.com/genaisummit01/" target="_blank">@genaisummit01</a></p>
# #     <p>💼 LinkedIn: <a href="https://www.linkedin.com/company/genaisummit2025" target="_blank">Gen AI Summit 2025</a></p>
    
# #     <br>
# #         <embed src="cid:embedded_pdf" width="600" height="400" type="application/pdf"><br><br>
# #          <img src="cid:embedded_image" alt="" width="300"><br><br>
# #   </body>
# # </html>
# #     """



#     # msg = Message(
#     #     subject="Get ready to meet the industry's Best at the GenAI Summit - 11th January 2025,New Delhi",
#     #     sender='"GenAI Summit" <Anant@genaisummit.in>',
#     #     recipients=[to_email]

#     # )
#     msg = Message(
#         subject="Biggest Gen AI Summit 2025 | Sponsorship Opportunity",
#         sender='"GenAI Summit" <Anant@genaisummit.in>',
#         recipients=[to_email]

#     )
#     # msg.body=text_body
#     msg.html=html_body

#     # if pdf_path:
#     #     with app.open_resource(pdf_path) as pdf:
#     #         msg.attach(
#     #             os.path.basename(pdf_path),
#     #             'application/pdf',
#     #             pdf.read(),
#     #             headers={'Content-ID': '<embedded_pdf>'}  # Dictionary format
#     #         )

#     # # Attach Image with correct headers format
#     # if image_path:
#     #     with app.open_resource(image_path) as image:
#     #         msg.attach(
#     #             os.path.basename(image_path),
#     #             'image/jpeg',
#     #             image.read(),
#     #             headers={'Content-ID': '<embedded_image>'}  # Dictionary format
#     #         )

#     # Send email
#     with app.app_context():
#         mail.send(msg)

#     print(f"Email sent to {to_name} at {to_email}")

# @app.route('/sendemails', methods=['POST'])
# def send_bulk_emails_route():
#     try:
#         # Parse JSON data
#         data = request.get_json()
#         if not isinstance(data, dict):
#             return jsonify({"error": "Invalid JSON structure. Expected a JSON object."}), 400

#         # Validate 'recipients' field
#         recipient_list = data.get('recipients', [])
#         if not isinstance(recipient_list, list):
#             return jsonify({"error": "'recipients' must be a list."}), 400

#         # Validate 'text_body'
#         text_body_template = data.get('text_body')

#         # Validate 'pdf_path'
#         pdf_path = data.get('pdf_path')
#         # if not pdf_path or not os.path.exists(pdf_path):
#         #     return jsonify({"error": f"Invalid or missing 'pdf_path': {pdf_path}"}), 400

#         # Optional image path
#         image_path = data.get('image_path')
#         # if image_path and not os.path.exists(image_path):
#         #     return jsonify({"error": f"Invalid or missing 'image_path': {image_path}"}), 400

#         # Process each recipient
#         for recipient in recipient_list:
#             if not isinstance(recipient, dict):
#                 return jsonify({"error": "Each recipient must be a dictionary."}), 400

#             to_email = recipient.get('email')
#             to_name = recipient.get('name')

#             if not to_email or not to_name:
#                 return jsonify({"error": "Each recipient must include 'email' and 'name'."}), 400

#             # Format the text body
#             text_body = text_body_template.format(to_name=to_name)

#             try:
#                 send_email(to_email, to_name, text_body, pdf_path, image_path)
#             except Exception as e:
#                 print(f"Failed to send email to {to_email}: {e}")

#         return jsonify({"status": "Emails sent successfully"}), 200

#     except Exception as e:
#         print(f"Error: {e}")
#         return jsonify({"error": "An unexpected error occurred."}), 500

# # Example Usage
# if __name__ == "__main__":
    
#     app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)), debug=False)


from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os
import pandas as pd
import json

app = Flask(__name__)


def extract_emails_in_batches(folder_path, email_column_name, name_column_name):
    email_entries = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(('.csv', '.xls', '.xlsx')):
            file_path = os.path.join(folder_path, file_name)
            try:
                if file_name.endswith('.csv'):
                    df = pd.read_csv(file_path)
                else:  # Handle .xls and .xlsx
                    df = pd.read_excel(file_path)

                if email_column_name in df.columns and name_column_name in df.columns:
                    for index, row in df.loc[:, [email_column_name, name_column_name]].dropna().iterrows():
                        email = row[email_column_name]
                        name = row[name_column_name]
                        if email not in ["No email", "vanshikaaggarwal@igdtuw.ac.in", "shivani.chopra@hp.com"]:
                            email_entries.append({"email": email, "name": name})
                else:
                    print(f"Column '{email_column_name}' or '{name_column_name}' not found in file {file_name}")
            except Exception as e:
                print(f"Error processing file {file_name}: {e}")

    return email_entries

def send_email(sender_email, sender_password, to_email, to_name, subject, text_body, pdf_file=None, image_file=None):
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = sender_email
    app.config['MAIL_PASSWORD'] = sender_password
    mail = Mail(app)

    msg = Message(
        subject=subject,
        sender=sender_email,
        recipients=[to_email]
    )
    msg.body = f"Dear {to_name},\n\n{text_body}"

    if pdf_file:
        msg.attach(
            pdf_file.filename,
            'application/pdf',
            pdf_file.read(),
            headers={'Content-ID': '<embedded_pdf>'}
        )

    if image_file:
        msg.attach(
            image_file.filename,
            'image/jpeg',
            image_file.read(),
            headers={'Content-ID': '<embedded_image>'}
        )

    with app.app_context():
        mail.send(msg)

    print(f"Email sent to {to_name} at {to_email}")

@app.route('/sendemails', methods=['POST'])
def send_bulk_emails_route():
    try:
        sender_email = request.form.get('sender_email')
        sender_password = request.form.get('sender_password')
        subject = request.form.get('subject')
        text_body_template = request.form.get('text_body')
        csv_folder_path = request.form.get('csv_folder_path')
        email_column_name = request.form.get('email_column_name')
        name_column_name = request.form.get('name_column_name')

        pdf_file = request.files.get('pdf_file')
        image_file = request.files.get('image_file')

        if not all([sender_email, sender_password, subject, text_body_template, csv_folder_path, email_column_name, name_column_name]):
            return jsonify({"error": "Missing required parameters"}), 400

        recipient_list = extract_emails_in_batches(csv_folder_path, email_column_name, name_column_name)

        for recipient in recipient_list:
            to_email = recipient['email']
            to_name = recipient['name']
            text_body = text_body_template.format(to_name=to_name)

            try:
                send_email(sender_email, sender_password, to_email, to_name, subject, text_body, pdf_file, image_file)
            except Exception as e:
                print(f"Failed to send email to {to_email}: {e}")

        return jsonify({"status": "Emails sent successfully"}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)), debug=False)
