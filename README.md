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

[![Product Name Screen Shot][product-screenshot]](https://github.com/DillonMercz/Sheets2Trello/blob/main/trello%20splur.png) product screenshot 

For many organizations, the online platforms require users to submit requests that are handled by administrators later. One prominent example of this occurs during online shopping or on freelance websites. Customers contact freelancers and expect them to solve their problems. Developers usually spend a lot of time on accessing databases, collecting requests from various sources such as google forms and google sheets, and strategizing how to organize them into their ‘to-do list’ management platforms, such as Trello.  
 
This repository allows you to schedule tasks and other necessary information collected through google forms and google sheet directly into Trello. 

Our startup team was looking for a way to take customer requests and put them into Trello, a company that makes tasks planning and organization easy. Therefore, all customer orders and tasks can be listed in one place, and we can stay well organized within the company. This is an excellent tool that provides solutions to a wide range of problems relating to business, industry, and personal aspects of life. 

### Functionality 

The information is organized in a Trello Board in lists after filling out a google form or google spreadsheet. This can be used to keep track of orders, organize spreadsheet data into lists based on keywords, sort on the fly based on search results, and pretty much anything that has to do with assigning tasks or organizing spreadsheet responses and Google form responses. The problems that this solves are innumerable. This hack does not rely on a database to take orders, nor does it require complicated scripts to get orders in a well-structured place.

### Building process

1. The script that calls APIs was written in Python. It uses IFTTT to trigger a new row in Google spreadsheets and sends an email with the number of the new row in the subject line. The script extracts the row number from the email and using the Google Sheets API, it will check the responses to certain cells to determine which list and which cells to pull data from.

2. After the data is fetched, it is split into variables which can then be sent to Trello. It takes a lot of time and work to actually create the cards correctly every time. The program starts off by requesting a new card from Trello via the API. The JSON response is then split into a list, then into variables to get the Card ID and the List ID. With this information, checklists can be created on the card to determine the exact needs of the customer. Therefore, we make another POST request and create a checklist and then split the JSON response to get the checklist ID.

3. Then we make more POST requests to populate the checklist with the customer's contact information, as well as the information about the order. The information that populates the checklist comes from the variables collected earlier using the Google spreadsheet.

4. After testing it out on google forms, we built an HTML form and connected the google back-end, so that the responses from the custom HTML form could be saved into the spreadsheet along with the google forms equivalent responses.

### Built With

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [IFTTT] (add website)
* [Python] (add website)
* [Google API] (add website)
* [HTML] (add website)
* add more pluggins and tools 


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

We were able to create a working system that can help teams of online vendors and freelancers to get organized, save time, and allocate it to other useful activities. The sheer amount that it took a person to create Trello lists and organize them depending on their google form data is nonexistent now because it is an automated process.

We are proud of the system that we have made which can be implemented to work with more systems other than google forms. We learned a lot on how to build APIs by using Postman effectively. This was a big win for the startup team and this will help us to expand our business and stay organized at the same time.


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
[contributors-url]: https://github.com/DillonMercz/Sheets2Trello/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/DillonMercz/Sheets2Trello/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/DillonMercz/Sheets2Trello/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/DillonMercz/Sheets2Trello/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/DillonMercz/Sheets2Trello/blob/master/LICENSE.txt
[website-shield]: https://img.shields.io/website?down_color=lightgrey&down_message=offline&up_color=blue&up_message=online&url=https%3A%2F%2Fshields.io
[website-url]: https://splurket.com
[product-screenshot]: images/screenshot.png
