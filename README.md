# The Garden Path

The Garden Path is an e-commerce website for a fictional gardening and landscaping business based in Munster, Ireland. The site offers customers a variety of services ranging from grass cutting and weed removal to arboriculture and tree stump removal. Customer reviews are visible to all site users, and registered users can view their order history and update their details.
This website is responsive and designed to be viewed on a variety of screen sizes. 

![AmIResponsive Layout of Website]()

Deployed program on Heroku: [The Garden Path](https://gardening-services-e596b6371c3f.herokuapp.com/)

![GitHub last commit](https://img.shields.io/github/last-commit/simonhw/gardening-services)
![HTML Static Badge]()
![CSS Static Badge]()
![Python Static Badge]()
![JavaScript Static Badge]()
![GitHub contributors](https://img.shields.io/github/contributors/simonhw/gardening-services)

## Contents
- [User Experience](#user-experience)
    - [Initial Discussion](#initial-discussion)
    - [Agile Planning](#project-planning-with-the-agile-approach)
    - [Business Model](#business-model)
    - [User Stories](#user-stories)
    - [Kanban Board](#kanban-board)
- [Marketing](#marketing)
- [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Wireframes](#wireframes)
    - [ERDs](#entity-relationship-diagrams)
    - [CRUD Functionality](#crud-functionality)
    - [Responsiveness](#responsiveness)
- [Features](#features)
    - [The Homepage](#the-homepage)
    - [The About Page](#the-about-page)
    - [Accounts Pages](#the-signup-page)
    - [The Booking Page](#the-booking-page)
    - [User Bookings](#user-bookings)
    - [Managing Bookings](#managing-bookings)
    - [Error Pages](#error-pages)
    - [Features to be Implemented](#features-to-be-implemented)
- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries, and Programs](#frameworks-libraries-and-programs)
- [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Live Deployment](#live-deployment)
- [Testing](#testing)
- [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code Used](#code-used)
- [Acknowledgements](#acknowledgements)


## User Experience
### Initial Discussion
The Garden Path website offers a number of services to homeowners and businesses in the maintenance and upkeep of their green spaces. The goal of the website is to showcase the services on offer and encourage the site user to choose The Garden Path for their gardening needs. The website allows users to order and pay for various services and stay up to date with speical offers and seasonal promotions via a newsletter signup link. Customers can leave reviews for services they have purchased and edit or delete their own reviews.

### Project Planning with the Agile Approach
Planning and development of The Garden Path e-commerce project was carried out using the Agile method. This involves breaking projects down into smaller manageable sections which allows teams to deliver continuous working releases to the client and end users. These release periods are known as sprints and this project had 4 sprints over 8 weeks.

User Stories were generated and grouped under different Epics to effectively structure the work involved at different stages of the project. These Epics were:
- "Initial Project Setup"
- "Create Models"
- "User Accounts"
- "Website Content"
- "Services and Checkout"
- "Payment System"
- "Reviews"
- "Contact Us"
- "Marketing"
- "Bugs"
- "Writing Documentation"

Each user story was assigned a number of labels to aid in the project workflow. These include:

- `Sprint 1/2/3/4` - To denote in which sprint the user story will be worked on.
- `Story Points: 1/2/3` - To denote how much effort each user story requires.
- `Must-Have` - A user story relating to a feature without which the website will not function correctly. This tag is also used for features which are a requirement for the Code Institute assessment criteria but which would otherwise not impede the site's essential functionality.
- `Should-Have` - A user story relating to a feature that will complement the core website features and enhance the user experience.
- `Could-Have` - A user story relating to a feature that could be of benefit to the user but without which the site will still achieve all its design goals.
- `Site User` - A user story from the perspective of a regular site user.
- `Site Admin` - A user story from the perspective of a site administrator.
- `documentation` - A task related to writing the README or TESTING documents.
- `bug` - Denoting an unsolved bug.
- `Solved Bug` - Denoting a bug that has been resolved.

Using the Agile method allowed this project to be managed well in small chunks. The developer was able to work on specific tasks without losing focus and manage and project the time required for these tasks optimally.

### Business Model
The Garden Path is designed as a Business to Customer (B2C) e-commerce application. Individuals are the main type of customer being targeted for the services being sold, although other businesses can also fall into this category. The deliverables are services; repeat transations are expected based on the positive experience and feedback from customers. A single payment systems is used for The Garden Path, as the services on offer can be seasonal or have extended periods of time before being required again.

### User Stories
Key user stories for the application are outlined below. An exhaustive list can be viewed on its [GitHub Projects page](https://github.com/users/simonhw/projects/4/).

#### EPIC: Initial Project Setup

<details><summary>Show User Stories</summary>

- **Set Up Django Files**: As a **Developer** I can **set up the Django template files** so that I can **begin to write code for the project**.
    - I can install the correct version of Django.
    - I can create a project called **gardening**.
    - I can create an app called **home**.
    - I can display a "Hello world!" string on the webpage.

- **Create PostgreSQL Database**: As a **Developer** I can **create a could-based database** so that I can **store and retrieve data for my website**.
    - I can create a new PostgreSQL instance
    - I can copy the URL in the Details section
    - I can create the env.py file and set DATABASE_URL constant.
    - I can install the relevant packages for database connection.
    - I can run migrations.

- **Deploy Project to Heroku**: As a **Developer** I can **deploy the project to Heroku** so that I can **see that the website displays properly**.
    - I can create a Heroku app with a unique name.
    - I can update the code for deployment with gunicorn.
    - I can deploy the app on Heroku.

- **Deploy Heroku App with Static Files**: As a **Developer** I can **deploy the project with static files** so that **the app will have the same styling as the local version.**.
    - I can create a staticfiles directory and collect the static files.
    - I can deploy the project on Heroku and ensure all styles are applied.

</details>

#### EPIC: Create Models

<details><summary>Show User Stories</summary>

- **Three Custom Models**: As a **Developer** I can **create three custom models** so that I can **satisfy the assessment criteria for the project**.
    - Custom Model 1: Service
    - Custom Model 2: CustomUser
    - Custom Model 3: Reviews
    - Custom Model 4: ContactUs

- **Create Service Model**: As a **Developer** I can **create a custom Services model** so that **I can add services to the website for the user to purchase**.
    - I can create a **services** app.
    - I can create a models file.
    - I can declare the necessary imports.
    - I can create a model with the appropriate fields required.

- **Create Custom User Model**: As a **Developer** I can **create a custom user model** so that I can **customise the user creation process as compared to the default Django model**.
    - I can create an app called **accounts**
    - I can create the CustomUser model in models.py
    - I can update settings.py to use my custom model

- **Create Order Model**: As a **Developer** I can **create an Order model** so that I can **recieve and store customers orders in my database**.
    - I can create an app called **checkout**
    - I can create the Order model in models.py
    - I can add functions to make a unique order number and calculate the total price

- **Create OrderLineIem Model**: As a **Developer** I can **create an OrderLineItem model** so that I can **separate different services into rows on a given order**.
    - I can create the OrderLineIem model in models.py
    - I can add a function to calculate the line subtotal
    
- **Create Reviews Model**: As a **Developer** I can **create a custom Reviews model** so that I can **display customer reviews and store the data in my database**.
    - I can create an app called **reviews**
    - I can create the Review model in models.py
    - I can add functions to calculate an average rating for a service
    
- **Create ContactUs Model**: As a **Developer** I can **create a custom ContactUs model** so that I can **recieve and store customer messages in my database**.
    - I can create an app called **contact**
    - I can create the ContactUs model in models.py

</details>

#### EPIC: User Accounts

<details><summary>Show User Stories</summary>

- **Create an Account**: As a **Site User** I can **create an account** so that I can **view my account details on the website**.
    - When I click the sign-in button, I am prompted to make an account.
    - After registering my details, I can log in and view, create, update, or delete my account details.
    - I can log out and log back in using the password I created.
    - I can reset my password.

- **View Account Page**: As a **Site User** I can **navigate to my account page** so that I can **view or amend my details or delete my account**.
    - When logged in, I can navigate to the My Account page.
    - I can view and amend my details.
    - I can view my past orders

</details>

#### EPIC: Website Content

<details><summary>Show User Stories</summary>

- **Create Base Template**: As a **Developer** I can **create a base template** so that **the similar aspects of the webpages need only be written once and the UX has a consistent appearance across the app**.
    - I can create a base.html file.
    - I can create a header and nav bar for small screens.
    - I can create a footer for small screens.
    - I can create a header and nav bar for larger screens.
    - I can create a footer for larger screens.

- **View Homepage**: As a **Site User** I can **view the homepage**  so that I can **understand the purpose of the website and navigate it successfully**.
    - When a user visits the homepage they can easily understand the purpose of the website
    - The user can navigate to other pages of the website 
    - The user can view a brief "About Us" section
    - The user can see a summary of services offered

- **View Business Information**: As a **Site User** I can **view information about the business** so that I can **make an informed decision about ordering a service**.
    - When I visit the About page, I can read the business information.
    - I can view the locations covered by the business.
    - I can view the products and services offered.

- **Create Error Pages**: As a **Developer** I can **create certain error pages** so that **a site user can understand when something goes wrong viewing a webpage**.
    - I can create a 404 error page.
    - I can create a 403 error page.
    - I can create a 500 error page.

- **View Privacy Policy**: As a **Site User** I can **view the business' privacy policy** so that I can **understand how the business collects and stores my personal data**.
    - I can navigate to the privacy policy page from a link in the footer
    - I can view the privacy policy on a dedicated website page
    - I can understand how to contact the business owners with any inquiries about the policy

</details>

#### EPIC: Services and Checkout

<details><summary>Show User Stories</summary>

- **View Individual Service Details**: As a **Site User** I can **view the Service page** so that I can **see all details related to the service and make an informed decision on my purchase**.
    - When I click on a service I can view its details page.
    - I can see the service description, price, and rating.
    
- **Order a Service**: As a **Site User** I can **select a booking option** so that I can **book a specific service**.
    - I can view the types of services that can be booked.
    - I can select an option to book.
    - I can add the service to my shopping cart.
    
- **View Cart**: As a **Site User** I can **view my cart** so that I can **see what services I am going to order**.
    - When I view my cart, I see a list of services I have selected to order.
    - I can see the individual cost of each service.
    - I can see the total cost of the order.
    - I can click a button to proceed to the online payment stage.
    
- **View Preview of Cart**: As a **Site User** I can **view a preview of the cart when I add a service to it** so that **I can be know the action was successful and confirm what is in the cart without navigating away from the current page**.
    - When I add a service to the cart on smaller screens, I can see a toast preview with the cart details.
    - On desktop screens, when I add a service to the cart, I can see a preview of the cart contents in an offcanvas element.
    
- **Update Services from the Cart Page**: As a **Site User** I can **update or remove services from the cart** so that I can **have an improved experience without navigating back to individual service pages**.
    - I can change the number of a given service and see the subtotal and order total price change.
    - I can remove a service from the cart.
    - When I click remove I can see the order total price change.
    
- **Proceed to Checkout**: As a **Site User** I can **navigate to the checkout page with my order** so that I can **enter my details and place my order**.
    - When I click the checkout button, I can enter my personal and delivery details.
    - I can enter my payment information.
    - I can review my order before submitting.

</details>

#### EPIC: Payment System

<details><summary>Show User Stories</summary>

- **Set Up Stripe**: As a **Developer** I can **set up Stripe in my application** so that I can **handle and process payments securely**.
    - I can install Stripe
    - I can set up a webhook handler
    - I can implement views to process the payment and order data

- **Pay for an Order**: As a **Site User** I can **enter my payment details successfully** so that I can **secure my order**.
    - I can enter my payment details in the checkout process
    - I can be informed of the success or failure of the payment attempt.

- **Receive Confirmation of Orders**: As a **Site User** I can **receive confirmation of my successful order** so that I can **confirm that my order was received and have the details available to me outside of the website**.
    - When I submit an order, I can see a confirmation message on the site with an order number provided.
    - I can view the submitted order details on my account page.
    - I can view the order details in an email confirmation.

</details>

#### EPIC: Reviews

<details><summary>Show User Stories</summary>

- **View Reviews**: As a **Site User** I can **view reviews for a service** so that I can **be more informed about the quality of work carried out by the business**.
    - On a particular service page, I can view all reviews for that service.
    - I can navigate through the reviews via pagination.
    
- **Review a Service**: As a **Site User** I can **review a service that I have ordered** so that I can **leave feedback as a customer and feel like I am interacting with the website and business directly**.
    - I can interact with a "Leave a Review" button
    - I can rate the service out of 5 stars
    - I can write a brief review on my experience with the service
    
- **Edit a Review**: As a **Site User** I can **edit a review that I previously made** so that I can **be in control of content created by me on the website**.
    - For a particular review I have made I can click an edit button
    - I can edit the rating and text content of my reviews and save the changes
    
- **Publish Reviews**: As a **Site Admin** I can **publish pending reviews or unpublish them on the live website** so that I can **ensure only genuine reviews are visible for the business' services**.
    - For a given pending review, I can publish it to the website and make it publicly visible
    - For a given published review, I can unpublish it so that users cannot see it.
    
- **Delete a Review**: As a **Site User** I can **delete a review that I previously made** so that I can **be in control of content created by me on the website**. As a **Site Admin** I can **delete any review** so that I can **be in control of content displayed on the website**.
    - For a particular review I can delete it if I am the author or a staff user.
    - I can confirm or cancel the delete action before it takes effect.

</details>

#### EPIC: Contact Us

<details><summary>Show User Stories</summary>

- **View Contact Us Page**: As a **Site User** I can **send a message to the business** so that I can **make enquiries directly from the website**.
    - I can navigate to the Contact Us page from the main nav bar.
    - I can view the business' contact details.
    - I can send a message to the business using a form.

</details> 

#### EPIC: Marketing

<details><summary>Show User Stories</summary>

- **Subscribe to Newsletters**: As a **Site User** I can **sign up to the website's newsletter** so that I can **be made aware of upcoming offers and information disseminated by the company**.
    - I add my email to the newsletter mailing list.
    - I can receive feedback  confirming that I have been added to the mailing list. 

- **Create Facebook Page**: As a **Developer** I can **create a mock-up Facebook business page** so that I can **demonstrate how social media marketing would be implemented for the business**.
    - I can create a mock-up of a Facebook business page for The Garden Path
    - I can add relevant images
    - I can add posts

- **Search Engine Optimisation**: As a **Developer** I can **implement various SEO features** so that I can **improve the website's performance for search engine indexing**.
    - I can conduct research on and implement keywords.
    - I can create a robots.txt file.
    - I can create a sitemap.xml file.
    - I can employ descriptive meta tags.
    - I can add appropriate `rel` attributes on external links.
    - I can add links to reputable websites related to my business.

</details> 

#### EPIC: Bugs

<details><summary>Show User Stories</summary>

- As a **Developer** I can **detail and keep track of bugs** so that I can **solve them before release or come up with a plan to address them in the future**.
    - For a full list of bugs, please view [TESTING.md](/TESTING.md)

</details> 

#### EPIC: Writing Documentation

<details><summary>Show User Stories</summary>

- As a **Developer** I can **write README, TESTING, and MARKETING files** so that **others can learn about my app and see the work that has gone into preparing it for final release**.

</details> 

### Kanban Board
The GitHub Projects tool was used to manage development progress for this website. A kanban board was used to separate tasks into four columns:
- Todo
- In Progress
- Done
- Future Features

The Epics and labels discussed above were used in conjunction with the board and allowed the developer to manage their time well during development. Below is a screenshot of the final state of the kanban board. The project can be viewed on its [GitHub Projects page](https://github.com/users/simonhw/projects/4/).

![Image of Kanban Board]()

## Marketing
All documentation on the marketing for this e-commerce application can be found in the [MARKETING.md](/MARKETING.md) file.

## Design

### Colour Scheme
A palette of greens gradually becoming lighter was chosen for this website. The different green colours are reflective of the environments in which The Garden Path services are carried out. An off-white colour called Isabelline was added to be able to soften areas of the website and avoid using a complete white shade.

![Coolors colour palette](static/images/readme/the-garden-path-colours.png)

### Typography
The Mate font was chosen from the Google Fonts library as its thin and sharp look evoked thought of garden tools, fencing, and ordered lines. This gives the impression of a professional business and evokes thoughts of neat and careful services carried out by the business.

![Mate Font](static/images/readme/mate.png)

### Imagery
Vibrant and colourful images were chosen for the website to represent the services on offer. Each service image is clear in what it represents with no superfluous information that could mislead the site user. 
The hero image shows a garden path and steps leading to a patio. Red poppies are in focus in the foreground and other plants and trees are in the blurred background. Some pages did not make use of a hero image due to aesthetic design reflecting the pages' purpose. These include but are not limited to the accounts pages, the cart and checkout pages, and the privacy policy page. Individual reasons for this design choice is discussed further in the [Features](#features) section.


### Wireframes
Wireframes were created in Balsamiq for the initial front-end design of the website. The mobile layout was designed first and the tablet and desktop were adapted from this.

**Home Page**

#### Homepage Wireframe - Mobile

![Homepage Wireframe - Mobile](static/images/readme/mobile-wireframe-home.png)

#### Homepage Wireframe - Tablet

![Homepage Wireframe - Tablet](static/images/readme/tablet-wireframe-home.png)

#### Homepage Wireframe - Desktop

![Homepage Wireframe - Desktop](static/images/readme/desktop-wireframe-home.png)


**About Us Page**

<details open><summary>About Us Wireframe - Mobile</summary>

![About Wireframe - Mobile](static/images/readme/mobile-about.png)

</details>

<details><summary>About Us Wireframe - Tablet</summary>

![About Wireframe - Tablet](static/images/readme/tablet-about.png)

</details>

<details><summary>About Us Wireframe - Desktop</summary>

![About Wireframe - Desktop](static/images/readme/desktop-about.png)

</details><br>

**Services Page**

<details open><summary>Services Wireframe - Mobile</summary>

![Services Wireframe - Mobile](static/images/readme/mobile-services.png)

</details>

<details><summary>Services Wireframe - Tablet</summary>

![Services Wireframe - Tablet](static/images/readme/tablet-services.png)

</details>

<details><summary>Services Wireframe - Desktop</summary>

![Services Wireframe - Desktop](static/images/readme/services-desktop.png)

</details>

**Individial Service Pages**

<details open><summary>Individual Service Wireframe - Mobile</summary>

![Individial Service Wireframe - Mobile](static/images/readme/service-mobile.png)

</details>

<details><summary>Individual Service Wireframe - Tablet</summary>

![Individial Service Wireframe - Mobile](static/images/readme/tablet-service-page.png)

</details>

<details><summary>Individual Service Wireframe - Desktop</summary>

![Individial Service Wireframe - Mobile](static/images/readme/service-desktop.png)

</details>

**Basket Page**

<details open><summary>Basket Wireframe - Mobile</summary>

![Basket Wireframe - Mobile](static/images/readme/basket-mobile.png)

</details>

<details><summary>Basket Wireframe - Tablet</summary>

![Basket Wireframe - Mobile](static/images/readme/basket-tablet.png)

</details>

<details><summary>Basket Wireframe - Desktop</summary>

![Basket Wireframe - Mobile](static/images/readme/basket-desktop.png)

</details>

**Checkout Page**

<details open><summary>Checkout Wireframe - Mobile</summary>

![Checkout Wireframe - Mobile](static/images/readme/mobile-checkout.png)

</details>

<details><summary>Checkout Wireframe - Tablet</summary>

![Checkout Wireframe - Mobile](static/images/readme/tablet-checkout.png)

</details>

<details><summary>Checkout Wireframe - Desktop</summary>

![Checkout Wireframe - Mobile](static/images/readme/desktop-checkout.png)

</details>

### Entity Relationship Diagrams
An ERD was created to plan out the models that would be created and used in this project. In total, 8 custom models were written, including some taken from previous Django projects. These are credited below in the [Code Used](#code-used) section and all custom models are explained in the [Custom Models](#custom-models) section.

![ERDs](static/images/readme/erd_the_garden_path.png)

### CRUD Functionality
A key requirement for this project was for users to be able to create, read, update, and/or delete data from the database as appropriate. Users could interact with the database in these ways as follows:

#### Create
* Site users and admin users may **create** by creating a user account.
* Site users may **create** by creating an order, review, or submitting a message.

#### Read
* Site users and admin users may **read** by viewing services, reviews, their account details, and their order history.
* Admin users may also **read** by viewing unpublished reviews.

#### Update
* Site users may **update** by amending their account details or editing their reviews.
* Admin users may **update** by publishing or unpublishing reviews.

#### Delete
* Site users may **delete** by deleting their reviews, or deleting their phone number and address details on their account page.
* Admin users may **delete** by deleting reviews.

<br>


### Responsiveness
Across all pages of the website, Bootstrap's powerful grid system was utilised to control content reponsiveness on a wide variety of screen widths. The design of some key website features on different display sizes is demonstrated below. 

#### Navbar
On small screen sizes the navbar is a dropdown menu accessed on the right hand side of the display. For larger screens the navbar links are displayed in a neat row across the top of the page. This was achieved using the navbar code in the Bootstrap documentation.

<details open><summary>Comparison of navbar on small and large screens</summary>

![Nav bar menu on small screens](static/images/readme/navbar-mobile.gif)
![Nav bar on larger screens](static/images/readme/navbar-desktop.png)

</details>

#### Hero Image
The hero image is shown with its original aspect ratio of ~3:2 on screen sizes up to 768 pixels width. For larger screens, the `<img>` element has a custom CSS stlye of `display: none` applied and its parent div is given a `background-image` of the same picture with a fixed height so that the website content is not completely pushed down out of sight.

<details open><summary>Responsiveness of hero image with differing screen widths</summary>

![Responsiveness of Hero Image](static/images/readme/hero-responsive.gif)

</details>

#### Text Content
Content on small screens is displayed in single column fashion, displaying text and images appropriately as the user scrolls down their device. On larger screens, text and images are displayed side-by-side to make use of the extra horizontal space.

<details open><summary>Comparison on text content layout on small and large screens</summary>

![Content layout on small screens](static/images/readme/content-mobile.gif)
![Content layout on large screens](static/images/readme/content-desktop.png)

</details>

#### Service Page
On the service page, the service images are displayed in columns of 1, 2, 3, and 4 as the screen width increases. The four pricing model cards follow a similar trend underneath.

<details open><summary>Service page on medium screens</summary>

![Service page on small screens](static/images/readme/services-mob.gif)

</details>

<details><summary>Service page on medium screens</summary>

![Service page on medium screens](static/images/readme/services-tablet.gif)

</details>

<details><summary>Service page on large screens</summary>

![Service page on large screens](static/images/readme/services-desktop.gif)

</details>

#### Individual Services
On each service page, the image and service information are displayed either in a single column or in two columns. This is done to maximise the impact of the imagery on wider screen by allowing for a larger image and to make user of the extra space.

<details open><summary>Comparison of service page on mobile and tablet screens</summary>

![Grass Cutting page on mobile screens](static/images/readme/ind-services-mob.gif)
![Grass Cutting page on tablet screens](static/images/readme/ind-services-tablet.png)

</details>

#### Cart
The cart and its features are neatly arranged using the grid system on all screen sizes. The order items and checkout card are displayed in a single column on small screen but are placed side-by-side on wider screens. On large screen sizes the order item list in contained in its own scrollable container, so that the user does not have to scroll away from the checkout card.

<details open><summary>Cart on mobile screens</summary>

![Cart on mobile screens](static/images/readme/cart-mob.gif)

</details>

<details><summary>Cart on desktop screens</summary>

![Cart on desktop screens](static/images/readme/cart-desktop.gif)

</details>

#### Checkout
The site logo, secure checkout text, and progress indicator change position at the top of the screen for different displays to neatly use the extra space provided.

<details open><summary>Comparison of checkout header on small and large screens</summary>

![Checkout header on mobile screens](static/images/readme/checkout-mob.png)
![Checkout header on mobile screens](static/images/readme/checkout-tablet.png)
![Checkout header on mobile screens](static/images/readme/checkout-desktop.png)

</details>

The review order card does not diplay the service images on mobile screen, but on tablets and desktop screens, there is sufficient space to show them.

<details open><summary>Comparison of review order card on small and large screens</summary>

![Checkout order review card on mobile screens](static/images/readme/checkout-review-mob.png)
![Checkout order review card on wider screens](static/images/readme/checkout-review-desktop.png)

</details>

#### Reviews 
Reviews are displayed in different ways depending on how many there are for a service. With at least three, they are arranged in columns of 1, 2, or 3 as screen sizes widen. If there is only one review, a single column is used on all screens, albeit with appropriate offsets to give the review card a set maximum width. Similarly if there are only two reviews, the maximum number of columns used on larger screens is 2. This is to keep reviews centered on the page regardless of how many there are.

<details open><summary>Comparison of user reviews small and large screens</summary>

![User reviews on mobile screens](static/images/readme/reviews-mob.gif)
![User reviews on wider screens](static/images/readme/review-tablet.png)

</details>

#### Contact Us
The Contact Us page displays its form fields in columns of width 10 with an offset of 1 on mobile screens, and columns of width 6 with an offset of 3 on tablet-sized screens and larger. Specific CSS styling had to be applied to the third-party reCAPTCHA container on smaller screens so that it did not extend past the width of the `<html>` element and create a horizonal scroll.

<details open><summary>The Contact Us page on small and large screens</summary>

![Contact Us page on mobile screens](static/images/readme/contact-mob.png)
![Contact Us page on mobile screens](static/images/readme/contact-desktop.png)

</details>

#### Footer
The footer is displayed in a single column on small screens, with a horizontal line separating the different information block. On larger screens, these blocks are arranged in a row that uses the full width of the screen, and the horizontal lines are hidden. 

![Footer on small screens](static/images/readme/footer-mobile.png)
![Footer on larger screens](static/images/readme/footer-desktop.png)

## Features
The website consists of 21 pages with varying levels of accessibility for different types of users:

**Page** | **All Users** | **Authenticated User** | **Staff Users**
:--- | :---: | :---: | :---:
Homepage | &check; |  | 
About Us | &check; |  | 
All Services | &check; |  | 
Individual Services | &check; |  | 
Service Reviews | &check; |  | 
Cart | &check; |  | 
Checkout | &check; |  | 
Confirmation Order page | &check; |  | 
Contact Us | &check; |  | 
Signup and Sign in pages | &check; |  | 
Error pages: 404, 403, and 500 | &check; |  | 
Newsletter page | &check; |  | 
Privacy Policy page | &check; |  | 
My Account |  | &check; | 
Past Order Confirmation pages |  | &check; | 
Leave a Review page |  | &check; | 
Edit a Review page |  | &check; | 
Sign Out page |  | &check; | 
Unpublished Reviews page |  |  | &check;


### All pages on the website have:

**1.** A favicon of a pair of gloves. This icon was chosen to reflect a hands-on and professional business to the customer.  

![Gloves favicon](static/images/readme/gloves-favicon.png)

**2.** A header with a logo and nav bar or menu dropdown for page links (except the checkout page)

![Website Header on mobile](static/images/readme/header-mobile.png)
![Website Header on desktop](static/images/readme/header-desktop.png)

The header contains direct links to the main pages of the website, depending on the authentication status of the site user. The nav link for the page currently being viewed is made distinct with a CSS style of `active` which is represented by a background colour of Sage and text colour of Isabelline when the nav bar is in dropdown form, and a bold font weight with a subtle Isabelline text shadow on larger screens.
- The website logo "The Garden Path" is a link which when clicked will return the user to the `index.html` page.
- "About Us" brings the user to the `about.html` page.
- The "Services" dropdown displays a list of options which include the `services.html` and `service_page` pages.
- "Cart" links to the `cart.html` page.
- "Contact Us" bring the user to `contactus.html`
- "Log In/Sign Up" will direct the user to the `login.html` page which itself contains a link to `signup.html`.

When a user is signed in, the header links change.
- A new link "My Account" brings the user to the `account.html` page.
- "Log In/Sign Up" is hidden and "Log Out" is shown, which will direct the user to the `logout.html` account page.

    ![Website Header on mobile when user is logged in](static/images/readme/header-authenticated-mobile.png)
    ![Website Header on dekstop when user is logged in](static/images/readme/header-authenticated-desktop.png)


**3.** A footer with contact information, social media links, and links to important internal pages and relevant external sites.

- The phone number link opens the device's calling app with the number displayed. The email link similary open the device's email app with the email already entered in the "To:" field.
- The Facebook and Instagram links direct the user to the homepages for those sites, but for a real business these links would point to the business' pages on those platforms.
- Two links are included for SEO reasons and are discussed further in the [MARKETING.md](/MARKETING.md) file.
    - A link to the Associaton of Landscape Contracters in Ireland website
    - A link to the Royal Horticultural Society of Ireland website
- Two other links are for important pages on the website:
    - The privacy policy page
    - The newsletter signup page

![Website Footer](static/images/readme/footer-desktop.png)

### The Homepage
The homepage contains two sections: a general introduction and a services overview. A heading welcomes the user with a smaller muted heading below it communicating that the business is local and specialists in garden care. An image of a smartly-dressed mature man holding a leaf is displayed next to the introduction. This gives the user a sense that the business offers experience and knowledge. The services sub-heading lists the location covered by the business so that the user understands without having to navigate further through the website if they can avail of The Garden Path's services. An image of a man driving a ride-on lawnmower is shown next to the summary of service, and a button which links to the service page is displayed underneath.

![The website' homepage](static/images/readme/content-desktop.png)

### The About Page
Three distinct sections are displayed on the About page.
- The first is a short statement about the business following by a paragraph on the founding of the business by the fictional Dermot Murphy. This history instills a sense of trust and customer care in the user as they think of The Garden Path as one that started as a local business run by someone passionate about their work that has become successful and increased in size. A picture of "Dermot" amongst vegetation reading from a tablet makes the user think of the business as one with good attention to detail.

    ![Our Story section of About Us page](static/images/readme/about-story.png)

- The second section has a different background colour and inset shadow both to seperate it clearly from the other sections and to break up the amount of white on the page. This section contains two different headings which detail the business' mission and the top reasons to patronise The Garden Path. There is a button underneath the "Why Choose Us?" list which brings the customer directly to the Contact Us page if they want to get a quote for the work to be carried out.

    ![Our Mission section of About Us page](static/images/readme/about-mission.png)

- The third section is brief paragraph that speaks directly to the prospective customer. It communicates that the business is dedicated to quality service and delivering exactly what the customer wants. A image of "Dermot" smiling and looking directly at the camera make a connection with the user as if they were speaking in person to a staff member.

    ![Our Mission section of About Us page](static/images/readme/about-committment.png)


### The Service Pages
#### All Services
The All Services page consists of two sections: the list of services and the pricing model.
- Currently offering 6 types of services, the business displays each as a card containing a large vibrant image with a title underneath it. Clicking any of the images or titles will bring the user to the individual service page.

    ![The All Services page services section](static/images/readme/services-section.png)

- The pricing model section outlines the hourly rates for each category of service and, if applicable, the minimum number of hours for the service to be carried out.

    ![The pricing model section](static/images/readme/pricing-section.png)

#### Individual Service Pages
For each individal service, the page is displayed with the hero image, to draw the user's eye to the colours in the image and in the star ratings. A brief description of the service is given, under which sits the star rating. The average rating is displayed as a number of stars out of 5 filled with an orange colour. The decimal value of the rating is listed next to the stars as well as the number of reviews. The number of reviews is a link to the reviews page for the service and is one of the few links on the website outside of the footer where the underline has not been removed for styling reasons. It must be present so that the user understand they can click the link to view the list of reviews.

Underneath the rating are the option(s) for the user to select. These can range from 1-3 options e.g. the size of the area for grass cutting (1 option) or the type of tree service, the size of the tree, and the number of trees (3 options). The price per number of services is shown underneath the options along with two buttons that either allow the user to go back to the list of all services or to add the current service to the user's cart with the selected options.

![An individual service page](static/images/readme/ind-services-tablet.png)

Underneath each service's title are breadcrumb links of the form "All Services > Category > Service". Clicking on the Services breadcrumb takes the user back to the All Services page. Clicking the category breadcrumb (in the above image called "Garden Maintenance") renders the all services page with a category filter so that only services of the current category are shown and with the category name appended to the page's heading. The breadcrumb is shown in bold for the level of page that the user is currently viewing.

![The service category page for Garden Maintenance](static/images/readme/category-page.png)

### The Shopping Cart
When viewing the cart page without any services having been added to it, a message saying "Your cart is empty" is displayed with a button that will bring the user back to the All Services page. The heading indicates the number of services in the cart at any given time.

<details open><summary>Comparison of the cart page when empty and when containing one service</summary>

![Empty Cart page](static/images/readme/cart-empty.png)

![Cart page with one service](static/images/readme/cart-01.png)

</details>

When greater than zero, the total price of the services in the cart is appended after the Cart nabvar link. When the cart has multiple services the list is displayed underneath the checkout card on mobile, and in a fixed height scrollable container on larger screens. For mobile screens, a button that bring the user back to the top of the page is shown when the user scrolls down through the list of services.

<details open><summary>Comparison of the cart page with several services on different screen sizes</summary>

![A cart with many services on small screens](static/images/readme/cart-mob.gif)

![A cart with many services on larger screens](static/images/readme/cart-desktop.gif)

</details>

#### Quantity and Remove buttons
To amend the number of services directly from the cart, the user can click the **-** or **+** buttons to immediatley update the value. The decrement button is disabled when the value is 1 but the user may enter 0 directly into the field in which case the service will be removed from the cart.

![Removing a service from the cart by setting the number to 0](static/images/readme/cart-0-remove.gif)

The remove button is given a prominent size, either as wide as the image or the details container. The `btn-outline-danger` Bootstrap class is used instead of a solid red fill for three different reasons: 
- To keep the association of red with removal or deletion
- To not distract from the colours in the vibrant images
- To avoid clashing with the various green shades used

![Removing an item from the cart with the remove button](static/images/readme/cart-remove-button.gif)

#### The Cart Preview
When adding services to the cart, the user is shown a summary of the current contents of their cart and the total price. This is displayed in the toast message on mobile and tablet screens, and in an offcanvas element on desktop screens. Both types of preview feature a scrollable list for many services and a "View Cart" button to bring the user directly to the cart page.

![Cart preview on smaller screens](static/images/readme/cart-preview-mob.gif)

![Cart preview on desktop screens](static/images/readme/cart-preview-desktop.gif)

### The Checkout Page
When a user proceeds to the checkout page, the navbar is not shown. The site logo is still present, but in the navbar's place is now text saying "Secure Checkout" with a padlock icon, and a custom progress indicator for the checkout process. 

![Checkout Page header](static/images/readme/checkout-mob.png)

#### Progress Indicator
The indicator consists of three filled grey circles connected by grey lines representing the three steps of the checkout process. This is made clear to the user with subheadings under each circle titled "Address", "Payment", and "Review". The circle representing the current step is twice the diameter of the others and has a black colour. When a user moves to the next step, the previous step's circle and the connecting line retain their black colour, but the circle becomes smaller again. This allows the user to understand exactly where they are in the checkout process, what steps they have completed, and how many steps are left.

<details><summary>Demonstration of checkout progress indicator</summary>

![Demonstration of checkout progress indicator](static/images/readme/checkout-progress.gif)

</details>

#### Address Details
The user is first presented with form fields related to their personal details and address. All fields except for "Street Address 2" and "Eircode" are required. The "Continue to Payment" button is disabled until all required input fields contain data. This validation is explained in detail in the [TESTING.md](/TESTING.md) file.

![Checkout address fields and proceed button enable/disable feature](static/images/readme/checkout-address.gif)

#### Payment Details
Continuing to the next stage, the user must enter valid card details into a Stripe input field. The "Review Order" button is disabled until valid details are entered into the field with no errors present.

![Checkout payment input and review order button](static/images/readme/checkout-payment.gif)

#### Review Order
Moving to the final step of the checkout process, an orange text box explains that this is the final step and that user may review their order details below before making the payment. The user's address details are displayed with a "Change" link to go directly back to the address section in case they wish to change any data. The payment details are not explicitly displayed but a message saying that the input was complete is present with a green check box. A change link is also present here in case the user wants to change their card details. Underneath is present a summary of the cart. Only the service name is presented here, as adding the various options affected the presentation poorly. If the user is unsure of the cart contents, there is an "Adjust Cart" button which they can use to navigate back to the cart page. A larger yellow button with the text "Pay and Place Order" draws the eye of the user with its bright colour and padlock icon. This helps the user understand that one they click this button, the checkout process will complete and they can no longer make any adjustments. When clicked, the button text changes to "Processing..." and the padlock turns into a spinner indicating that the payment is being processed. This is especially useful when an unexpected payment or server error occurs. The user will know that the website is in fact attempting to submit the order.

![Checkout submission and success page](static/images/readme/checkout-success.gif)

#### Checkout Success
On successful checkout, a confirmation toast message is shown and informs the user that copy of the order details will be sent to the provided email.

![Checkout success toast message](static/images/readme/checkout-success-toast.png)

The success page itself also confirms this as well as providing the unique order number. A summary of the order details is given with a button allowing the user to navigate back to the website's homepage.

![Checkout success page](static/images/readme/checkout-success.png)

### The Reviews page
A review page exists for each service that The Garden Path offers. Only users who have previously ordered a particular service can write reviews for it. The link to the review page is presented next to the star rating on each service page. When clicked, the user may read the various reviews that have been approved by the site administrators.

![Reviews page](static/images/readme/reviews-mob.gif)

A maximum of 6 reviews are displayed at any one time. If more reviews exists, then pagination controls are shown underneath the reviews as well as an indication of how many pages of reviews there are.

<details><summary>Pagination of reviews</summary>

![Reviews pagination](static/images/readme/reviews-pagination.png)

</details>

#### Writing a Review
If a user has previously ordered a particular service, they will see a Leave a Review button under the page's heading. Clicking it will bring them to the `create_review.html` page. Confirmation of the account under which the review is being made is given above the review form. The user must complete three fields: a title, review content, and rating out of 5. A green Submit button will allow the user to submit their review and a confirmation toast message is displayed stating that the review is pending approval.

<details open><summary>The Leave a Review button</summary>

![Leave a Review button](static/images/readme/review-button.png)

</details>

<details><summary>The review form page</summary>

![The review form page](static/images/readme/review-form.png)

</details>

<details><summary>The review confirmation toast message</summary>

![The review confirmation toast message](static/images/readme/review-toast.png)

</details>

#### Deleting or Editing a Review
When a user in logged in they may edit or delete their published reviews. In these cases, a horizontal line is added to the review card and two distinct Edit and Delete buttons are presented.

<details open><summary>A review with Edit and Delete buttons</summary>

![Review card as seen by its author](static/images/readme/reviews-author.png)

</details>

If the user clicks the Edit button, the review form page is loaded with an amended page title, form heading, and with the form data populated in the fields. Similar to above, a toast message confirms that the review was edited and is not awaiting staff approval. The review can no longer been seen in the list of reviews.

<details><summary>The Edit Review page with amended heading and pre-filled form data</summary>

![Review card as seen by its author](static/images/readme/reviews-edit.png)

</details>

<details><summary>The edit review toast message</summary>

![The review confirmation toast message](static/images/readme/review-edit-toast.png)

</details>

If the user clicks the delete button, a confirmation modal is displayed informing them that the delete action cannot be undone. A cancel button will close the modal without deleting the review.

<details><summary>The Delete Confirmation Modal for reviews.</summary>

![Delete review modal window](static/images/readme/review-modal.png)

</details>

#### Publishing and Unpublishing a Review
Staff users may view a page containing all unpublished reviews and delete or publish them at their discretion. When viewing the main reviews page for a service, they may unpublish or delete any reviews listed, though they do not have the ability to edit any reviews that are not their own. There is no hero image on the unpublished reviews page as only staff users will ever see it and reduces the load on the browser. Staff users can also see the reviewer's contact email address at the bottom of the review card so that they can directly address any concerns the user may have communicated in the review.

<details><summary>Admin view of reviews page</summary>

![Admin view of reviews page](static/images/readme/reviews-admin.png)

</details>

<details><summary>The unpublished reviews page</summary>

![The unpublished reviews page](static/images/readme/reviews-unpublished.png)

</details>

### The Signup Page

### The Sign In Page

### The Sign Out Page

### Error Pages

### Features to be Implemented

## Technologies Used
### Languages
- HTML
- CSS
- Python
- Javascript

Relational database: PostgreSQL.

### Frameworks, Libraries, and Programs
[Am I Responsive?](https://ui.dev/amiresponsive) - To showcase the website on different screen sizes for this README.

Adobe Photoshop 2020 - To resize and crop images.

[Balsamiq](https://balsamiq.com/) - To create the website wireframes.

[Bootstrap](https://getbootstrap.com/) - To build and style content on the website.

[CI Python Linter](https://pep8ci.herokuapp.com/#) - To ensure code meets minimum PEP8 standards.

Chrome Developer Tools - To visualise and test changes to the website code.

[Coolors](https://coolors.co/) - To showcase the colour palette of the website.

[Django](https://www.djangoproject.com/) - A Python framework used to design the website.

[ElephantSQL](https://www.elephantsql.com/) - To create and store the database.

[Favicon.io](https://favicon.io/) - To source the favicon used.

[Free Logo Design](https://freelogodesign.org) - To create a mock logo for the business.

[Git](https://git-scm.com/) - For version control.

[GitHub](https://github.com/) - To save and store files online.

[Gitpod](https://www.gitpod.io/) - The IDE used to write my code.

[Google Fonts](https://fonts.google.com/) - For imported fonts used on the website.

[Heroku](https://www.heroku.com/) - To host the deployed version of the program.

[JSHint](https://jshint.com/) - To validate the JavaScript code.

[LucidChart](https://lucid.app/) - To create Entity Relationship Diagrams

[Pexels.com](https://www.pexels.com/) - To source images used on the website.

[ScreenToGif](https://www.screentogif.com/) - To create GIF files for this README.

[Shields.io](https://shields.io/) - To add badges to this README.

[Shutter Encoder](https://www.shutterencoder.com/) - To convert images to .webp format.

[TinyPNG](https://tinypng.com/) - To compress images.

[W3C Markup Validation Service](https://validator.w3.org/) - To validate the HTML and CSS files.

[W3Schools.com](https://www.w3schools.com/) and [The Python Library](https://docs.python.org/3/library/) - For researching and learning about Python methods and syntax.

## Deployment
The live version of this website was deployed on Heroku.

### Local Deployment
To deploy this program locally on your device, please follow the steps below:

<!-- #### Forking
1. Log in or sign up to [GitHub](https://github.com/).
2. Navigate to the repository for [Lakeview Campsite](https://github.com/simonhw/campsite-bookings).
3. Click the Fork button located in the top right part of the webpage.

#### Cloning
1. Log in or sign up to GitHub.
2. Navigate to the repository for [Lakeview Campsite](https://github.com/simonhw/campsite-bookings).
3. Click on the green Code button, select your preferred option of HTTPS, SSH, or GitHub CLI, and copy the relevant link.
4. Open the terminal in your IDE and navigate to your directory of choice for this new clone.
5. Type `git clone` into the terminal and paste in your copied link. Press enter.

#### Set Up Your Environment
1. In your IDE, navigate to the root directory and run the command `pip3 install -r requirements.txt`. All the necessary packages should now be installed in your workspace.
2. Run the command `python3 manage.py runserver` in your terminal and open the hosted site in your browser.
3. Add the web address to the list of allowed hosts in the `settings.py` file and hard reload your browser. The website should display properly.
4. If it does not, set Debug to True and check for error messages in the webpage displayed.

#### Creating the Database
1. Navigate to the PostgreSQL provider of your choice and create a new instance.
2. Find the database URL and copy it to the clipboard.
3. Create an `env.py` file in your IDE root directory and confirm that it is listed in the `.gitignore` file.
4. Create a secret key yourself or by using a website of your choice such as [Secret Key Generator](https://secretkeygen.vercel.app/).
5. Add the following code to your `env.py` file making sure to replace `enter-copied-url-here` with the URL you copied in step 2 and `your-secret-key` with the one you generated in step 4:
    ```
      import os

      os.environ.setdefault(
          "DATABASE_URL", "<enter-copied-url-here>")
      os.environ.setdefault("SECRET_KEY", "<your-secret-key>")
    ```
6. Run the following command in your IDE terminal to create your database tables: `python3 manage.py migrate`.
7. Create a superuser account by running `python3 manage.py createsuperuser` and enter details as prompted. -->

### Live Deployment
To deploy this project yourself on Heroku, please follow the following additional steps:
<!-- 
1. Log in or sign up to [Heroku](https://www.heroku.com/).
2. Create a new app with a unique name in a region close to you.
3. In the Settings tab under Config Vars, add the key `DATABASE_URL` with a value of the database URL, and the key `SECRET_KEY` with a value of the secret key you created.
4. Confirm that the `Procfile` is present in your directory.
5. Set Debug to False in `settings.py` and commit and push your code to your GitHub repository.
6. In the Deploy tab on Heroku, connect your GitHub repo and manually deploy the **main** branch.
7. Click "View App" to open your deployed website. -->

## Testing
All documentation on the testing of this application can be found in the [TESTING.md](/TESTING.md) file.

## Credits

### Content
ChatGPT was used to generate most of the text content about the campsite and services offered and was edited by Simon Henleywillis. The "description" and "keywords" meta tags were also generated using ChatGPT.

ChatGPT was used to generate a JSON file of users and their respective reviews.

### Media
The business logo was created on [FreeLogoDesign](https://freelogodesign.org). The website states that "[w]hether you use the free or the paid version (high-resolution plan), you are free to use your logo for promotional purposes without having to credit FreeLogoDesign."

All other images used were found on [Pexels](https://www.pexels.com/). The Pexels website states that "*All photos and videos on Pexels can be downloaded and used for free*".
Images were resized and cropped where necessary.

- Hero image: [two-red-flowers-on-stairs](https://www.pexels.com/photo/two-red-flowers-on-stairs-68470/)
- Homepage images: [https://www.pexels.com/photo/a-man-mowing-the-green-lawn-12087398/](https://www.pexels.com/photo/a-man-mowing-the-green-lawn-12087398/), [https://www.pexels.com/photo/man-in-green-jacket-holding-a-green-leaf-3782994/](https://www.pexels.com/photo/man-in-green-jacket-holding-a-green-leaf-3782994/)
- About page images: [https://www.pexels.com/photo/adult-man-wearing-green-jacket-holding-a-tablet-3781932/](https://www.pexels.com/photo/adult-man-wearing-green-jacket-holding-a-tablet-3781932/)
- Grass-cutting Service: [a-person-using-a-lawn-mower](https://www.pexels.com/photo/a-person-using-a-lawn-mower-6728919/)
- Weed Service: [a-group-of-dandelions-in-a-field](https://unsplash.com/photos/a-group-of-dandelions-in-a-field-lYWEUytAj6s)
- Tree service: [https://www.pexels.com/photo/a-firefighter-cutting-a-tree-with-a-chainsaw-7812853/](https://www.pexels.com/photo/a-firefighter-cutting-a-tree-with-a-chainsaw-7812853/)
- Hedge service: [https://www.pexels.com/photo/man-cutting-a-hedge-with-a-trimmer-in-the-garden-24595769/](https://www.pexels.com/photo/man-cutting-a-hedge-with-a-trimmer-in-the-garden-24595769/)
- Flowerbed service: [https://www.pexels.com/photo/photo-of-assorted-color-flowers-at-daytime-1039129/](https://www.pexels.com/photo/photo-of-assorted-color-flowers-at-daytime-1039129/)
- Tree Stump service: [https://www.pexels.com/photo/a-close-up-shot-of-a-tree-stump-10814837/](https://www.pexels.com/photo/a-close-up-shot-of-a-tree-stump-10814837/)


### Code Used
**All code in this project was written entirely by Simon Henleywillis unless otherwise specified below.**
Various Bootstrap classes and components were used in the styling of this website and were learned about from reading the Bootstrap documentation. Chunks of code that were copied or adapted are specifically credited below.

**Feature** | **Source**
--- | ---
Articles used as guidance when creating the CustomUser model | [Learn Django - Django Custom User Model](https://learndjango.com/tutorials/django-custom-user-model) <br> [Medium.com - Custom User Model In Django](https://medium.com/django-unleashed/custom-user-model-in-django-98b9a401a6a2#4826) <br> [Django documentation - Customizing authentication in Django](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#a-full-example)
The Category model | Taken from the Boutique Ado walkthrough
The JavaScript code to control the decrement and increment of the number input field on the service pages | Taken from the Boutique Ado walkthrough
The HTML structure of the toast messages | Adapted from examples in this article: [https://fastbootstrap.com/components/toast/](https://fastbootstrap.com/components/toast/)
Disabling the checkout form buttons dynamically | [StackOverflow - Disabling submit button until all fields have values](https://stackoverflow.com/questions/5614399/disabling-submit-button-until-all-fields-have-values)
Pagination of reviews | Taken from the Django documentation: [https://docs.djangoproject.com/en/5.1/topics/pagination/](https://docs.djangoproject.com/en/5.1/topics/pagination/)
The JavaScript code to control the color of the select field in the Contact Us form | Taken and adapted from the Boutique Ado walkthrough
The HTML, CSS, and JavaScript code for the scroll to top button on the cart page | Taken from this tutorial: [MDB - Scroll back to top button](https://mdbootstrap.com/docs/standard/extended/back-to-top/)
The Offcanvas cart preview | The HTML code was copied from the [Bootsrap documentation](https://getbootstrap.com/docs/5.0/components/offcanvas/)


## Acknowledgements
- [Creating Your First README - Kera Cudmore](https://github.com/kera-cudmore/readme-examples)
- I would like to thank my CI Mentor [Graeme Taylor](https://github.com/G-Taylor) for his support and advice throughout the development phase.
