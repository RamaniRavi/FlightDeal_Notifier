<h1 align="center">FlightDeal Notifier</h1>
<h3 align="center">A Python application to track and notify flight deals based on user-defined budgets.</h3>
<h3 align="left">Project Overview:</h3>
<p align="left"> FlightDeal Notifier is a Python application that continuously monitors flight prices and alerts users
    when prices fall below their specified budget. The project utilizes Python for development, PythonAnywhere for
    deployment, Google Sheets for data management, and various flight APIs to fetch flight information. </p>
<h3 align="left">Features:</h3>
<ul>
    <li>Price Tracking: Continuously monitors flight prices against user-defined budgets.</li>
    <li>Notifications: Alerts users when flight prices drop below their set budget.</li>
    <li>Search Engine: Executes every minute to ensure up-to-date flight deals.</li>
    <li>Google Sheets Integration: Manages user data and preferences.</li>
    <li>Flight API Integration: Retrieves flight information and prices.</li>
</ul>
<h3 align="left">Technologies Used:</h3>
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img
            src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"
            alt="python" width="40" height="40" /> </a> <a href="https://www.pythonanywhere.com/" target="_blank"
        rel="noreferrer"> <img
            src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/PythonAnywhere_logo.svg/1200px-PythonAnywhere_logo.svg.png"
            alt="pythonanywhere" width="40" height="40" /> </a> <a href="https://developers.google.com/sheets"
        target="_blank" rel="noreferrer"> <img
            src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Google_Sheets_logo.png/1200px-Google_Sheets_logo.png"
            alt="googlesheets" width="40" height="40" /> </a> <a href="https://www.flightapi.com/" target="_blank"
        rel="noreferrer"> <img src="https://example.com/flight-api-logo.png" alt="flightapi" width="40" height="40" />
    </a> </p>
<h3 align="left">Installation:</h3>
<ol>
    <li>Clone the Repository:
        <pre><code>git clone https://github.com/yourusername/FlightDeal-Notifier.git</code></pre>
    </li>
    <li>Navigate to the Project Directory:
        <pre><code>cd FlightDeal-Notifier</code></pre>
    </li>
    <li>Install Required Packages:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Configure the Application: <ul>
            <li>Create a Google Sheets document for user data and preferences.</li>
            <li>Set up flight API keys and configure API endpoints.</li>
            <li>Update configuration settings in `config.py` with your API keys and Google Sheets details.</li>
        </ul>
    </li>
</ol>
<h3 align="left">Usage:</h3>
<ol>
    <li>Run the Application:
        <pre><code>python main.py</code></pre>
    </li>
    <li>The application will continuously check for flight price drops and notify users accordingly.</li>
</ol>
<h3 align="left">Deployment:</h3>
<ol>
    <li>Create an Account: Sign up on <a href="https://www.pythonanywhere.com/" target="_blank"
            rel="noreferrer">PythonAnywhere</a>.</li>
    <li>Upload Files: Use the PythonAnywhere dashboard to upload your project files.</li>
    <li>Set Up a Scheduled Task: Configure a scheduled task to run your script every minute.</li>
</ol>
<h3 align="left">Contributing:</h3>
<p align="left"> If you would like to contribute to the development of FlightDeal Notifier, please follow these steps:
<ol>
    <li>Fork the repository.</li>
    <li>Create a new branch for your feature or bug fix.</li>
    <li>Make your changes and commit them with descriptive messages.</li>
    <li>Push your changes to your forked repository.</li>
    <li>Create a pull request to the original repository.</li>
</ol>
</p>
<h3 align="left">Acknowledgments:</h3>
<p align="left"> - Thanks to <a href="https://www.flightapi.com/" target="_blank" rel="noreferrer">Flight APIs</a> for
    providing flight data.<br> - Special thanks to <a href="https://www.pythonanywhere.com/" target="_blank"
        rel="noreferrer">PythonAnywhere</a> for hosting. </p>
