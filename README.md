# group-project-readme
Students at UIUC can often feel lost when it comes to involvement with campus life. With IlliniGather, a student can gain recommendations based on the input that they provide on what to do, where to go, and find out what other students are up to that very day.

Functionality:
- Using their net ID, users can enter the webpage. Only users with valid Illinois emails will be allowed to enter the website. 
- Users can input their data/preferences (i.e. number of ppl, weather, what type of activity they want to do, time of day). From these preferences, Illini Gather will generate various itineraries based on what is going on in the area, based on other users’ input.
- Users have the option to “upvote” or “downvote” certain locations, as well as mark if they are at that location. The location, along with the number of votes, will be displayed on the homepage.
- Users can search through study spots, restaurants, parties, community/open RSO events, etc. Different combinations of these types of locations will be generated in the user’s different itineraries.
- Based on user input, our webpage will generate personalized ideas – this could include a list of places to go to or an itinerary based on student’s votes.
- Popularity of locations in each category refreshes once in a certain amount of time. The amount of time it takes to refresh will be based on our algorithm and once we have enough research to decide when the best time to refresh will be.

Backend: 
While writing the backend code, we will use Python with the Flask framework. In order to store our data, we will use MongoDB as a no-SQL database. This would ensure that our data would be organized in a way that is easily traceable and provide seamless real-time updates.
The backend will have the following responsibilities:
Storing user accounts and their subsequent information (MongoDB) -> pymongo
Storing voting and posting data (MongoDB)
Developing the user input tool that finds the ideal places for the user to go
Writing the 2FA authentication code and limiting to UIUC students only (smtplib) with pymongo


Frontend: We will be writing the frontend in HTML and CSS. We can update our UI to make it user-friendly and test out various interactive options for our users to go through once the front-end and back-end is connected. Some CSS libraries we may use could include Bootstrap to help with different themes when building UX.


We chose to separate our application into a frontend and backend instead of relying on one application. Because our project is a webpage, we are using HTML, CSS, and JavaScript on the frontend. The backend, powered by Flask, handles server-side logic, data processing, and API endpoints. This makes interaction between both entities easier. This division also makes it easier to develop our user interface in parallel with our backend: we can develop the interface without needing data provided by the backend first.

Interaction Flow:
User interacts with the frontend via a web browser.
Frontend sends HTTP requests to backend API endpoints.
Flask processes requests, often involving database interactions.
Backend sends JSON responses to the frontend.
Frontend updates the user interface based on the received data.

Installation Instructions:
1. Clone this repo
2. Install Flask and Pymongo via pip (pip install ...)
3. Run main.py
4. Go to local host in web browser

Group roles:

Ryed: Backend, testing, authentication

Rhea: Frontend pages, Top Events, Friends page

Raunak: Frontend pages, Homepage, About page
