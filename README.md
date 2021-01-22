<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License MIT][license-shield]][license-url]
[![Website][website-shield]][website-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/DillonMercz/Sheets2Trello/blob/main/">
    <img src="Logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Google Forms/Google Sheets To Trello</h3>

  <p align="center">
    Google forms/sheets and customer data all in one, organized place in Trello
    <br />
    <a href="https://github.com/DillonMercz/Sheets2Trello"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/DillonMercz/Sheets2Trello">View Demo</a>
    ·
    <a href="https://github.com/DillonMercz/Sheets2Trello/issues">Report Bug</a>
    ·
    <a href="https://github.com/DillonMercz/Sheets2Trello/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#postman-workspace">Postman Workspace</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/DillonMercz/Sheets2Trello/blob/main/trello%20splur.png) 

For many organizations, the online platforms require users to submit requests that are handled by administrators later. One prominent example of this occurs during online shopping or on freelance websites. Customers contact freelancers and expect them to solve their problems. Here At Splurket, we Know firsthand that it is hard to stay organized as a developer. Which is why we made it easy! Developers usually spend a lot of time on accessing databases, collecting requests from various sources such as google forms and google sheets, and strategizing how to organize them into their ‘to-do list’ management platforms, such as Trello. This project proves that it is very easy to accomplish this daunting task through automation using APIs. 
 
This repository allows you to schedule tasks and other necessary information collected through google forms and google sheet directly into Trello. 

Our startup team was looking for a way to take customer requests and put them into Trello, a company that makes tasks planning and organization easy. Therefore, all customer orders and tasks can be listed in one place, and we can stay well organized within the company. This is an excellent tool that provides solutions to a wide range of problems relating to business, industry, and personal aspects of life.

### Functionality 

The information is organized in a Trello Board in lists after filling out a google form or google spreadsheet. This is achieved by conditional logical assigning the cards to the correct list so that the data is very organized. This can be used to keep track of orders, organize spreadsheet data into lists based on keywords, sort on the fly based on search results, and pretty much anything that has to do with assigning tasks or organizing spreadsheet responses and Google form responses. The problems that this solves are innumerable. This hack does not rely on a database to take orders, nor does it require complicated scripts to get orders in a well-structured place. 
*Optional* In Our Postman Workspace, we have examples for the stripe API to handle Payments and Payouts. Perfect for Ecommerce solutions, as well as Freelance developer solutions.

### Building process

1. The script that calls APIs was written in Python. It uses IFTTT to trigger a new row in Google spreadsheets and sends an email with the number of the new row in the subject line. The script extracts the row number from the email and using the Google Sheets API, it will check the responses to certain cells to determine which list and which cells to pull data from.

2. After the data is fetched, it is split into variables which can then be sent to Trello. It takes a lot of time and work to actually create the cards correctly every time. The program starts off by requesting a new card from Trello via the API. The JSON response is then split into a list, then into variables to get the Card ID and the List ID. With this information, checklists can be created on the card to determine the exact needs of the customer. Therefore, we make another POST request and create a checklist and then split the JSON response to get the checklist ID.

3. Then we make more POST requests to populate the checklist with the customer's contact information, as well as the information about the order. The information that populates the checklist comes from the variables collected earlier using the Google spreadsheet.

4. After testing it out on google forms, we built an HTML form and connected the google back-end, so that the responses from the custom HTML form could be saved into the spreadsheet along with the google forms equivalent responses.


### Built With

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [IFTTT] https://Ifttt.com
* [Python] https://https://www.python.org/
* [Google Sheets API] https://developers.google.com/sheets/api
* [Google Sheets API- Getting Started] https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
* [Google Mail API] https://developers.google.com/gmail/api
* [Trello API] https://developer.atlassian.com/cloud/trello/rest/
* [Stripe API] https://stripe.com/docs/api
* [Spyder IDE- From Anaconda] https://www.anaconda.com/products/individual
* [Postman] https://www.postman.com/
* add more pluggins and tools 


<!-- GETTING STARTED -->
## Getting Started
To Get Started Please Refer to the Instructions Below:

### Prerequisites
* Python (3 works the best)
* Gspread Library
* Oauth2client Library
* Requests Library
* Imap 
* A Google Email (With less Secure Apps Allowed)
* Trello API Key and Token
* Trello Board
* A Form
* Google Sheets API Credentials
* Server For Hosting The Script and keeping it on (Only Expense You should need to pay, there are free alternatives)


### Installation

1. Get a free API Key at [https://trello.com](https://trello.com/app-key)
2. Copy the API Key To a Secure Place
3. Generate an API Token by clicking the "Token" Link.
4. Don't give them away!
5. Get Your Google Sheets API client_secret.json
6. Using the new email provided from the newly generated google API, invite that email to your google sheets document.
7. Put the Client_secret.json in the same directory as your project.
8. Fill in all the Information needed to sign in to the desired Email.
9. Search "Trello API Key" in the demo.py document and Fill in the variable with your Trello API key
10. Search "Trello API Token" in the demo.py document and fill in the variable with you Trello API Token
11. Search "List ID" in the Demo.py and fill in the corresponding variables. (List Ids Can be generated by making a new ist in trello, then a new card. After that click "share on the right-hand side of the card, and get the "Idlist" value from the JSON data. Mozilla Forefox Prints the JSON Data So that you can easily find it)
12. Define what cells you want to collect, and assign variables to them
13. Modify The Trello APIs to use your variables collected from the Google Sheet.
14. Pip install -r requirements.txt
15. Run and troubleshoot any problems/ Modify to your content
16. If Problems Persist, Open A New Issue, or reach out to us.


### Postman Workspace

<img src="https://github.com/DillonMercz/Sheets2Trello/blob/main/postman.png" alt="Postman workspace screenshot">

Below are short instructions on how to use our Postman Workspace.

Postman is an easy to use IDE for Web Services and APIs. Postman will take the API request that you make in one language and turn it into all the other languages via its API. You can use Postman to connect many web services together using their API. Software developers will find this feature useful for adding API functionality to different aspects of what they develop. More recently, Postman added some really useful features that allow developers to work together in one location. In Postman, you can not only use APIs, but you can also build your own! This IDE provides everything you need to build, test, and deploy your API.

These are the steps to set up Trello so that it can be used with our scripts. You will need to acquire Trello API credentials and add them to Postman as variables before you start this. 

1. Use the create board request in our “Create Board” collection to start off. The parameters for the board are https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-post.

2. Create a list using the BoardID acquired from a JSON response after sending a POST request to make a board. Creating a list is easy, and the parameters can be found at https://developer.atlassian.com/cloud/trello/rest/api-group-lists/#api-lists-post

3. Using the ListId Acquired from the JSON response, make a card, and specify which list by creating a parameter called “idList” and adding the list id acquired from the JSON response. For a full list of the parameters used to create a list refer to https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post

4. After creating the card, the checklist needs to be made, and the Card ID you receive in the JSON request can now be used to create a checklist on the card you just created. For a full list of parameters to add a card refer to https://developer.atlassian.com/cloud/trello/rest/api-group-checklists/#api-checklists-post

5. After the checklist is made, copy the checklist ID from the JSON response, and then send a response to add fields to the checklist. 
  The format you should follow is ‘Field Name Field Value’. For example if your name is John, you use the “name” parameter and write ‘Name: John Doe’. 
  If you want to use an email address, you use the “name” parameter and write: ‘Email: Johndoe@x.com’. For a full list of params, refer to https://developer.atlassian.com/cloud/trello/rest/api-group-checklists/#api-checklists-id-checkitems-post

In the Postman workspace we also added Stripe API requests to show that a business can use these to collect payments from customers using the stripe API, this system can then be used to move money around or automatically send payments, arrange customers on Trello lists, or even arrange sales. The Stripe APi gives this workspace high business value.

**Tip IF you need JSON information, just export a card as JSON in Firefox, and the JSON data is well organized and the variables are easy to find.**


<!-- USAGE EXAMPLES -->
## Usage and applications

1. Software Development
2. Freelance
3. Medical Field
4. Engineering Field
5. Data Science
6. Education Systems
7. Companies (Large, Medium, and Small)
8. Freelancers
9. Government
10. Online Event Booking
11. Custom Order Systems
12. When Combined with a payment, this could be the frontend of a consulting Business.
13. Accounting
14. Construction
15. Organizing Information about organizations, events, and more.
16. Storing information without having to build or set up a database.
17. Sales



_For more examples, please refer to the [Devpost Documentation](https://devpost.com/software/google-forms-google-sheets-to-trello)_


<!-- Accomplishments -->

## Accomplishments that we're proud of

We were able to create a working system that can help teams of online vendors, Developers, Businesses freelancers, and many more to get organized, save time, and allocate it to other useful activities. The sheer amount that it took a person to create Trello lists and organize them depending on their google form data or google sheet data is nonexistent now because it is an automated process.

We are proud of the system that we have made which can be implemented to work with more systems other than google forms. We learned a lot on how to build APIs by using Postman effectively. This was a big win for the startup team and this will help us to expand our business and stay organized at the same time. This system was Built by Developers, For Developers looking to stay organized.


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Dylan Clayton - [@Dillon_marks](https://twitter.com/dillon_marks) - dylanclayton3@gmail.com

Gael K. Bertrand - [Discord: BeeKay Koozie#6769](https://discord.com)

Project Link: [https://github.com/DillonMercz/Sheets2Trello](https://github.com/DillonMercz/Sheets2Trello)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/DillonMercz/Sheets2Trello.svg?style=for-the-badge
[contributors-url]: https://github.com/DillonMercz/Sheets2Trello/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/DillonMercz/Sheets2Trello.svg?style=for-the-badge
[forks-url]: https://github.com/DillonMercz/Sheets2Trello/network/members
[stars-shield]: https://img.shields.io/github/stars/DillonMercz/Sheets2Trello.svg?style=for-the-badge
[stars-url]: https://github.com/DillonMercz/Sheets2Trello/stargazers
[issues-shield]: https://img.shields.io/github/issues/DillonMercz/Sheets2Trello.svg?style=for-the-badge
[issues-url]: https://github.com/DillonMercz/Sheets2Trello/issues
[license-shield]: https://img.shields.io/github/license/DillonMercz/Sheets2Trello.svg?style=for-the-badge
[license-url]: https://github.com/DillonMercz/Sheets2Trello/blob/main/LICENSE
[website-shield]: https://img.shields.io/website?down_color=lightgrey&down_message=offline&up_color=blue&up_message=online&url=https%3A%2F%2Fshields.io
[website-url]: https://splurket.com
[product-screenshot]: https://github.com/DillonMercz/Sheets2Trello/blob/main/trello%20splur.png

