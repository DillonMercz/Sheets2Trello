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
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Google Forms/Google Sheets To Trello</h3>

  <p align="center">
    Google forms/sheets and customer data all in one, organized place
    <br />
    <a href="https://github.com/GaelKBertrand/googlesheet2trello"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/GaelKBertrand/googlesheet2trello">View Demo</a>
    ·
    <a href="https://github.com/GaelKBertrand/googlesheet2trello/issues">Report Bug</a>
    ·
    <a href="https://github.com/GaelKBertrand/googlesheet2trello/issues">Request Feature</a>
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

[![Product Name Screen Shot][product-screenshot]](https://example.com) product screenshot 

For many businesses and organizations, their online platforms require users to make requests which can be worked on later by the adminstrators. One prominent example of this situation takes place during online shopping or on freelance websites. customers make requests that need to be addressed by freelancers or developers. It tends to take a huge amount of time for develpers to under go  a process of accesding their databases, collect those requests and them strategically to their 'to-do lists' managment process. 

This repository aims at reducing this time taken and optimize the process of scheduling tasks and other necessary information collected from google forms and google sheet directly into Trello. 

### Functionality 

After filling out a form, the responses are saved to a Google sheet and then organized in a Trello Board. This can be used to keep track of orders, organizing spreadsheet data into lists based on keywords, and virtually anything that deals with giving tasks to or organizing Google form responses and spreadsheet data. The problems that this solves are innumerable. This is a hack that doesn't require a database to collect orders and does not need complicated scripts to get the orders to a well-organized place.

### Building process

The script that makes the API calls was built in Python. It uses IFTTT for the new row trigger in Google spreadsheets and sends an email stating the number of the new row in the subject of the email. The script extracts the row number from the email and using the Google Sheets API, it will start off by checking the responses of certain cells to determine which list to put the data in, and which cells to grab the data from. After the data is fetched, it is split into variables which can then be sent to Trello. To actually build the cards accurately every time, there is a lot of work involved. So the program starts off by sending a request to Trello via the API to create a new card. The JSON response is then split into a list, then into variables to get the Card ID and the List ID. with this info, checklists can then be created on the card to define what exactly the customer wants. We make another POST request and create a checklist, we then split the JSON response to get the checklist ID, and then we make more POST requests to populate the checklist with the customer's contact information, as well as the information about the order. The information that populates the checklist comes from the variables collected earlier from the Google spreadsheet. After testing it out on google forms, we built an HTML form and connected the google backend so that the responses from the custom HTML form, could be saved into the spreadsheet along with the google forms equivalent responses.

### Built With

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [IFTTT] (add website)
* [Python] (add website)
* [Google API] (add website)
* [HTML] (add website)


<!-- GETTING STARTED -->
## Getting Started

This is how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is the list of things you need to use the software and how to install them.


### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Put in the steps below 


<!-- USAGE EXAMPLES -->
## Usage and applications

1. Medical Field
2. Engineering Field
3. Data Science
4. Education Systems
5. Companies (Large, Medium, and Small)
6. Freelancers
7. Government
8. Online Event Booking
9. Custom Order Systems
10. When Combined with a payment, this could be the frontend of a consulting Business.
11. Accounting
12. Construction
13. Organizing Information about organizations, events, and more.
14. Storing information without having to build or set up a database.

_For more examples, please refer to the [Documentation](https://example.com)_




<!-- Accomplishments -->

## Accomplishments that we're proud of

We are proud of the system that we have made. It is reliable, can solve many problems, and can be implemented to work with more systems other than google forms. We all know now how to build APIs, and we learned not only how to use postman, but how to use it effectively. This was a big win for the startup team and this will help us to expand our business and stay organized at the same time.


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
