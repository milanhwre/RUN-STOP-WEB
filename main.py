from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime
app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)


    return '''
<!DOCTYPE html> 
<html lang="en" x-data="{ ping: 'Calculating...', time: 'Loading...' }">
 <head> 
  <meta charset="UTF-8"> 
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
  <title>𝗔𝗡𝗜𝗦𝗛-𝐗𝐃-𝐖𝐄𝐁</title> 
  <meta name="description" content="A web application to check Facebook tokens and manage profile guard settings. Secure your Facebook profile with ease."> 
  <meta property="og:title" content="Koja-XD WEB - This Tools allows you to check facebook tokens and manage profile guard settings. And getting your Access Token and Cookie and you can spam react on fb using the tools below."> 
  <meta property="og:description" content="A web application to check Facebook tokens and manage profile guard settings. Secure your Facebook profile with ease and access token and cookie."> 
  <meta property="og:image" content="https://i.ibb.co/PFwnZ5C/IMG-20240610-WA0044.jpg"> 
  <meta property="og:url" content="https://kojaxd.onine"> 
  <link href="css/tailwind.min.css" rel="stylesheet"> 
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet"> 
  <style>
        body {
            font-family: 'Poppins', sans-serif;
            scroll-behavior: smooth;
            transition: background-color 0.5s, color 0.5s;
            background-color: #1a202c;
            color: white;
        }

        .card {
            transition: transform 0.3s, box-shadow 0.3s, opacity 0.3s;
            opacity: 1;
            transform: translateY(0);
            border: 1px solid #4a5568;
            background-color: #2d3748;
            color: #f9f9f9;
            position: relative;
        }

        .card:hover {
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.4);
        }

        .status {
            position: absolute;
            top: 10px;
            right: 10px;
            background-color: #1a202c;
            padding: 5px 10px;
            border-radius: 5px;
            display: flex;
            align-items: center;
            font-size: 14px;
            color: #a0aec0;
        }

        .status .dot {
            height: 10px;
            width: 10px;
            background-color: #48bb78;
            border-radius: 50%;
            display: inline-block;
            margin-right: 5px;
        }

        .hidden {
            opacity: 0;
            transform: scale(0.95);
            pointer-events: none;
        }

        .text-yellow-500:hover {
            color: #eab308;
        }

        .header-button:hover {
            background-color: #eab308;
        }

        .fixed-header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
            background-color: #2d3748;
            transition: background-color 0.3s;
        }

        .header-shadow {
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.3);
        }

        .header-spacing {
            margin-top: 80px;
        }

        .focus\:outline-none:focus {
            outline: 2px solid #eab308;
            outline-offset: 4px;
        }

        .fade-in {
            animation: fadeIn 0.5s ease-in-out;
        }

        @keyframes fadeIn {
            0% {
                opacity: 0;
                transform: translateY(20px);
            }

            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .bubble-button {
            background: linear-gradient(135deg, #ffcc33, #ff66cc);
            color: white;
            padding: 10px 20px;
            border-radius: 50px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .bubble-button:hover {
            transform: scale(1.1);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
        }

        .loading-spinner {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 200px;
        }

        .loading-spinner div {
            width: 40px;
            height: 40px;
            border: 4px solid #eab308;
            border-radius: 50%;
            border-top-color: transparent;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            0% {
                transform: rotate(0deg);
            }

            100% {
                transform: rotate(360deg);
            }
        }

        footer {
            background-color: #2d3748;
            color: white;
            padding: 20px;
            text-align: center;
            margin-top: 20px;
        }

        .footer-links {
            margin-top: 10px;
        }

        .footer-links a {
            color: #ffcc33;
            margin: 0 10px;
            transition: color 0.2s;
        }

        .footer-links a:hover {
            color: #ff9900;
        }

        .footer-social {
            margin-top: 15px;
        }

        .footer-social a {
            color: white;
            margin: 0 5px;
            transition: color 0.2s;
        }

        .footer-social a:hover {
            color: #ffcc33;
        }

        .search-bar {
            position: relative;
            width: 100%;
            max-width: 400px;
        }

        .search-bar input {
            width: 100%;
            padding: 10px 15px 10px 40px;
            border-radius: 25px;
            background-color: #2d3748;
            color: white;
            border: 1px solid #4a5568;
            transition: border-color 0.2s;
        }

        .search-bar input:focus {
            border-color: #eab308;
            outline: none;
        }

        .search-bar i {
            position: absolute;
            top: 50%;
            left: 15px;
            transform: translateY(-50%);
            color: #eab308;
        }

        .search-bar i:hover {
            color: #ff9900;
        }

        .iframe-container {
            position: relative;
            overflow: hidden;
            padding-top: 56.25%; /* 16:9 aspect ratio (divide 9 by 16 = 0.5625) */
        }

        .iframe-container iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
        }
    </style> 
 </head> 
 <body> 
  <div class="fixed-header p-4 rounded-b-lg flex justify-between items-center shadow-lg header-shadow header-content"> 
   <h1 class="text-3xl font-bold header-title">𝗔𝗡𝗜𝗦𝗛-𝐗𝐃-𝐖𝐄𝐁</h1> 
   <div> 
    <p>ms: <span id="pingValue">Calculating...</span></p> 
    <p>TIME: <span id="timeValue">Loading...</span></p> 
   </div> 
  </div> 
  <div class="container mx-auto p-4 header-spacing"> 
   <div> 
    <h2 class="text-2xl font-bold mb-2"><i class="fas fa-project-diagram mr-2 animated-icon"></i>Welcome To Abhi-XD</h2> 
    <p class="text-gray-300 mb-6">Explore our diverse range of tools designed to enhance your Facebook experience, automate tasks, and improve your overall productivity.</p> 
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6"> 
     <!-- Card 1 --> 
     <div class="card p-4 rounded-lg project-card shadow-lg fade-in" data-category="Facebook Tool"> 
      <img src="https://i.ibb.co/vxknQ6Y/20241109-211542.jpg" alt="KOJA Tools Logo" style="width: 100%; height: 50%;"> 
      <div class="status"> 
       <span class="dot"></span> Up 
      </div> 
      <h3 class="text-lg font-bold mb-1">Tool 1</h3> 
      <p class="text-gray-400 mb-2">E - Fighter's Tool</p> 
      <p class="text-gray-300 mb-4">Convo tool which helps to Send Msg using Token </p> 
      <a href="/convo" target="_blank" class="bubble-button focus:outline-none"><i class="fas fa-external-link-alt mr-2"></i>Check it now!</a> 
     </div> 
     <p class="text-gray-300 mb-6"></p> 
     <!-- Card 2 --> 
     <div class="card p-4 rounded-lg project-card shadow-lg fade-in" data-category="Facebook Tool"> 
      <img src="https://i.ibb.co/D8PvMYg/20241109-211521.jpg" alt="KOJA Tools Logo" style="width: 100%; height: 50%;"> 
      <div class="status"> 
       <span class="dot"></span> Up 
      </div> 
      <h3 class="text-lg font-bold mb-1">Tool 2</h3> 
      <p class="text-gray-400 mb-2">Get Post UID</p> 
      <p class="text-gray-300 mb-4">Here You Just Paste Your Post Link And Get Uid Without Login</p> 
      <a href="/getuid" target="_blank" class="bubble-button focus:outline-none"><i class="fas fa-external-link-alt mr-2"></i>Check it now!</a> 
     </div> 
     <p class="text-gray-300 mb-6"></p> 
     <!-- Card 3 --> 
     <div class="card p-4 rounded-lg project-card shadow-lg fade-in" data-category="Facebook Tool"> 
      <img src="https://i.ibb.co/dbGZbQW/20241109-211447.jpg" alt="KOJA Tools Logo" style="width: 100%; height: 50%;"> 
      <div class="status"> 
       <span class="dot"></span> Up 
      </div> 
      <h3 class="text-lg font-bold mb-1">Tool 3</h3> 
      <p class="text-gray-400 mb-2">Get Messenger Group UID</p> 
      <p class="text-gray-300 mb-4">Here You Just Paste Your Token And Get All Messenger Groups UID With Name </p> 
      <a href="/group" target="_blank" class="bubble-button focus:outline-none"><i class="fas fa-external-link-alt mr-2"></i>Check it now!</a> 
     </div> 
     <p class="text-gray-300 mb-6"></p> 
     <!-- Card 4 --> 
     <div class="card p-4 rounded-lg project-card shadow-lg fade-in" data-category="Facebook Tool"> 
      <img src="https://i.ibb.co/4Jr9zfS/20241109-211408.jpg" alt="KOJA Tools Logo" style="width: 100%; height: 50%;"> 
      <div class="status"> 
       <span class="dot"></span> Up 
      </div> 
      <h3 class="text-lg font-bold mb-1">Tool 4</h3> 
      <p class="text-gray-400 mb-2">Check Facebook Token</p> 
      <p class="text-gray-300 mb-4">Here You Just Paste Your Token And Check If It's Valid or Not</p> 
      <a href="/tokken" target="_blank" class="bubble-button focus:outline-none"><i class="fas fa-external-link-alt mr-2"></i>Check it now!</a> 
     </div> 
     <p class="text-gray-300 mb-6"></p> 
     <!-- Card 5 --> 
     <div class="card p-4 rounded-lg project-card shadow-lg fade-in" data-category="Facebook Tool"> 
      <img src="https://i.ibb.co/6rg9NR7/Screenshot-20240708-042131.png" alt="KOJA Tools Logo" style="width: 100%; height: 50%;"> 
      <div class="status"> 
       <span class="dot"></span> Up 
      </div> 
      <h3 class="text-lg font-bold mb-1">Tool 5</h3> 
      <p class="text-gray-400 mb-2">Termux Offline Tool</p> 
      <p class="text-gray-300 mb-4">Convo tool which helps to Send Msg using Token </p> 
      <a href="https://github.com/K0J4/Termux-Offline" target="_blank" class="bubble-button focus:outline-none"><i class="fas fa-external-link-alt mr-2"></i>Check it now!</a> 
     </div> 
     <p class="text-gray-300 mb-6"></p> 
     <div class="card p-4 rounded-lg project-card shadow-lg fade-in" data-category="Facebook Tool"> 
      <img src="https://i.ibb.co/cJVFz8z/20241109-211340.jpg" alt="KOJA Tools Logo" style="width: 100%; height: 50%;"> 
      <div class="status"> 
       <span class="dot"></span> Up 
      </div> 
      <h3 class="text-lg font-bold mb-1">Tool 6</h3> 
      <p class="text-gray-400 mb-2">Get Token with Cookie</p> 
      <p class="text-gray-300 mb-4">Here You Get Facebook Token For Convo/Post</p> 
      <a href="/get_token" target="_blank" class="bubble-button focus:outline-none"><i class="fas fa-external-link-alt mr-2"></i>Check it now!</a> 
     </div> 
     <p class="text-gray-300 mb-6"></p> 
     <div class="card p-4 rounded-lg project-card shadow-lg fade-in" data-category="Facebook Tool"> 
      <img src="https://i.ibb.co/t2hmyMQ/20241015-140049.jpg" alt="KOJA Tools Logo" style="width: 100%; height: 50%;"> 
      <div class="status"> 
       <span class="dot"></span> Up 
      </div> 
      <h3 class="text-lg font-bold mb-1">Tool 7</h3> 
      <p class="text-gray-400 mb-2">Free Server Convo </p> 
      <p class="text-gray-300 mb-4">Convo tool which helps to Send Msg using Token</p> 
      <a href="http://152.42.220.111:25670" target="_blank" class="bubble-button focus:outline-none"><i class="fas fa-external-link-alt mr-2"></i>Check it now!</a> 
     </div> 
     <p class="text-gray-300 mb-6"></p> 
     <div class="card p-4 rounded-lg project-card shadow-lg fade-in" data-category="Facebook Tool"> 
      <img src="https://i.ibb.co/JnZczzX/20241015-140220.jpg" alt="KOJA Tools Logo" style="width: 100%; height: 50%;"> 
      <div class="status"> 
       <span class="dot"></span> Up 
      </div> 
      <h3 class="text-lg font-bold mb-1">Tool 8</h3> 
      <p class="text-gray-400 mb-2">POST SERVER </p> 
      <p class="text-gray-300 mb-4">Wall Server Send Coment with Tokens</p> 
      <a href="http://172.81.128.14:21508/" target="_blank" class="bubble-button focus:outline-none"><i class="fas fa-external-link-alt mr-2"></i>Check it now!</a> 
     </div> 
    </div> 
   </div> 
  </div> 
  <footer> 
   <div>
    © 2024 Technical Anish2M. All rights reserved.
   </div> 
   <div class="footer-social"> 
    <a href="https://www.facebook.com/profile.php?id=100010503540373"><i class="fab fa-facebook-f"></i></a> 
    <a href="https://wa.me/923218638257"><i class="fab fa-whatsapp"></i></a> 
   </div> 
  </footer> 
  <script>
        // Function to calculate live ping
        function calculateLivePing() {
            var startTime = new Date().getTime();
            fetch('https://www.google.com', { mode: 'no-cors' })
                .then(function(response) {
                    var endTime = new Date().getTime();
                    var pingTime = endTime - startTime;
                    document.getElementById('pingValue').textContent = pingTime + ' ms';
                })
                .catch(function(err) {
                    console.error('Fetch error: ', err);
                    document.getElementById('pingValue').textContent = 'Error';
                });
        }

        // Function to update live time in Asia/karanchi
        function updateLiveTimeInKarachi() {
            var options = { timeZone: 'Asia/Karachi', hour12: false, hour: 'numeric', minute: 'numeric', second: 'numeric' };
            var formatter = new Intl.DateTimeFormat('en-US', options);
            var timeString = formatter.format(new Date());
            document.getElementById('timeValue').textContent = timeString;
        }

        // Update live ping and time every second
        setInterval(function() {
            calculateLivePing();
            updateLiveTimeInKarachi();
        }, 1000); // Update every 1 second
    </script> 
 </body>
</html>
'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
