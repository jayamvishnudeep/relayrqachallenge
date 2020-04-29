# relayrqachallenge

## Overview
API Tests for Zomato public api & Reqres API (https://reqres.in/) with pytest as a framework

I have used below mentioned public API's

<ul>
  <li><b>Zomato Public API</b> - Only GET request method is exposed to Public and I used <b>GET Cities</b> api request. The API key must be given to the request headers and I haven't removed it from the Code as it's Public! You can find about the API deatils here https://developers.zomato.com/documentation#!/common/cities</li>
 
  <li><b>Reqres.in Public API</b> - All the CRUD request methods are exposed to public without any authentication and so I used it to perform api tests. You can find about the API deatils here https://reqres.in/ </li> 
</ul>

## Technologies/Frameworks used:

<ul>
  <li>Python</li>
  <li>Pytest</li>
</ul>

## Libraries used:
<ul>
  <li>Requests</li>
</ul>


## Requirements:

<ul>
  <li>Python version - 3.8</li>
  <li>Eclipse or Pycharm IDE</li>
</ul>

## How to run?
Clone this git repository and then go to the IDE terminal and use ``` pytest api-testing``` command and all the api tests will run