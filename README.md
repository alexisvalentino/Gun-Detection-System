<h1>Gun Detection System using OpenCV and Telegram</h1>
<p>This code is a Python script that uses OpenCV, Telegram API, and Pygame to detect guns in a video stream from a camera. The script starts by importing the necessary libraries and setting up the Telegram bot and chat ID.

The script then loads a pre-trained Haar cascade classifier for gun detection and initializes the camera. It also initializes variables to keep track of the first frame, whether a gun is detected, and whether the alarm is active.

Inside the main loop, the script reads a frame from the camera, resizes it, and converts it to grayscale. It then applies the gun detector to the grayscale image and checks if any guns are detected. If a gun is detected, the script sets the 
gun_exist
 variable to 
True
 and draws a rectangle around the gun in the original color image.

If this is the first frame, the script sets it as the reference frame and continues to the next iteration. Otherwise, the script displays the current date and time on the frame and shows it in a window. It also waits for a key press and checks if the 'q' key is pressed to exit the loop.

If a gun is detected, the script increments the 
frames_since_detection
 variable and plays the alarm sound if it's not already active. If the 
frames_since_detection
 variable exceeds a certain threshold (10 frames in this case), the script takes a screenshot of the frame with the gun, sends it to the Telegram chat, and resets the 
frames_since_detection
 variable.

If a gun is not detected, the script resets the 
frames_since_detection
 variable and stops the alarm sound if it's active.

If the 's' key is pressed, the script stops the alarm sound if it's active.

Finally, the script releases the camera, closes the window, and quits Pygame.</p>
<h1>Requirements</h1>
<ul>
<li>Python 3.x</li>
<li>OpenCV</li>
<li>NumPy</li>
<li>imutils</li>
<li>Telegram API</li>
<li>Pygame</li>
</ul>
<h1>Installation</h1>
<ul>
<li>Install Python 3.x on your computer.</li>
<li>Install OpenCV, NumPy, and imutils using pip: <em>'pip install opencv-python numpy imutils'</em></li>
<li>Install Telegram API using pip:  <em>'pip install python-telegram-bot'</em></li>
<li>Install Pygame using pip: <em>'pip install pygame'</em></li>
<li>Download the cascade.xml file and the alarm.wav file and save them in the same directory as the Python script.</li>
</ul>
<h1>Usage</h1>
<ul>
<li>Open the Python script in a text editor or IDE.</li>
<li>Replace the YOUR_BOT_TOKEN and YOUR_CHAT_ID with your own bot token and chat ID.</li>
<li>Run the Python script: <em>' python gun_detection.py</em></li>
<li>The script will start capturing frames from the camera and detecting guns. If guns are detected, an alarm sound will be played, and a message will be sent to the Telegram chat. You can stop the alarm sound by pressing the 's' key, and you can exit the script by pressing the 'q' key.</li>
</ul>
<h1>License</h1>
<p>This project is licensed under the MIT License - see the LICENSE file for details.</p>
<h1>Acknowledgements</h1>
<p>The project was made by Alexis Valentino for the Project Bagsik "Iot powered smart security surveillance system with Threat Detection (Weapons, Anomaly, Behavior Detection), Android Monitoring app and Night Vision capabilities."

