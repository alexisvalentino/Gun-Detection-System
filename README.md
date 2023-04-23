<h1>Gun Detection using OpenCV, Pygame, and Email</h1>
<p>This Python script uses OpenCV, Pygame, and email to detect guns in a video stream from a camera. If guns are detected, an alarm sound is played, and an email with a message and screenshot is sent to a recipient email address. This script can be used for security purposes to detect guns in public places or restricted areas.</p>
<h1>Prerequisites</h1>
<p>You will need to have the following libraries and tools installed on your system:</p>
<ul>
<li>Python 3.x</li>
<li>OpenCV 2 or 3</li>
<li>Pygame</li>
<li>smtplib</li>
<li>email.mime.multipart</li>
<li>email.mime.text</li>
<li>email.mime.image</li>
</ul>
<p>You will also need to have a gun cascade classifier file (e.g., cascade.xml) in the same directory as the script. You can download a pre-trained classifier from a source such as GitHub.
<h1>Getting Started</h1>
<ol>
<li>Clone the repository or download the script and the required files to your system.</li>
<li>Install the required libraries and tools.</li>
<li>Replace the FROM_EMAIL and FROM_PASSWORD variables in the script with your own email address and password, respectively.</li>
<li>Replace the TO_EMAIL variable in the script with the email address of the recipient.</li>
<li>Run the script using the command python gun_detection.py.</li>
</ol>
<h1>Usage</h1>
<ul>
<li>Press q to quit the script.</li>
<li>Press s to stop the alarm sound.</li>
<li>If guns are detected, an email with a message and screenshot will be sent to the recipient email address.</li>
</ul>
<h1>License</h1>
<p>This project is licensed under the MIT License - see the LICENSE file for details.</p>
<h1>Acknowledgements</h1>
<p>The project was made by Alexis Valentino</p>

