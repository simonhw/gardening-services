# The Garden Path

The Garden Path is an e-commerce website for a fictional gardening and landscaping business based in Munster, Ireland. The site offers customers a variety of services ranging from grass cutting and weed removal to arboriculture and tree stump removal. Customer reviews are visible to all site users, and registered users can view their order history and update their details.
This website is responsive and designed to be viewed on a variety of screen sizes. 

![AmIResponsive Layout of Website](docs/images/readme/amiresponsive-gardenpath.png)

Deployed program on Heroku: [The Garden Path](https://gardening-services-e596b6371c3f.herokuapp.com/)

![GitHub last commit](https://img.shields.io/github/last-commit/simonhw/gardening-services)
![HTML Static Badge](https://img.shields.io/badge/HTML5-%20validated%20-%20green?style=flat&logo=HTML5&logoColor=white&labelColor=%23E44D26&color=light%20green)
![CSS Static Badge](https://img.shields.io/badge/CSS%20-%20validated%20-%20green?style=flat&logo=CSS3&logoColor=white&labelColor=%23264de4&color=light%20green)
![Python Static Badge](https://img.shields.io/badge/Python%20-%20validated%20-%20green?style=flat&logo=Python&logoColor=white&labelColor=blue&color=light%20green)
![JavaScript Static Badge](https://img.shields.io/badge/JavaScript%20-%20validated%20-%20green?style=flat&logo=JavaScript&logoColor=white&labelColor=%23e4a125&color=light%20green)
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
    - [Custom Models](#custom-models)
    - [The Homepage](#the-homepage)
    - [The About Page](#the-about-page)
    - [The Service Pages](#the-service-pages)
    - [The Shopping Cart](#the-shopping-cart)
    - [The Checkout Page](#the-checkout-page)
    - [Signup, Login, and Logout](#user-accounts)
    - [My Account Page](#my-account-page)
    - [The Reviews Page](#the-reviews-page)
    - [Contact Us Page](#the-contact-us-page)
    - [Newsletter Page](#the-newsletter-page)
    - [Privacy Policy](#the-privacy-policy-page)
    - [Email Functionality](#email-functionality)
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
The Garden Path is designed as a Business to Customer (B2C) e-commerce application. Individuals are the main type of customer being targeted for the services being sold, although other businesses can also fall into this category. The deliverables are services; repeat transations are expected based on the positive experience and feedback from customers. A single payment system is used for The Garden Path, as the services on offer can be seasonal or have extended periods of time before being required again.

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

- **Create Order Model**: As a **Developer** I can **create an Order model** so that I can **receive and store customers orders in my database**.
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
    
- **Create ContactUs Model**: As a **Developer** I can **create a custom ContactUs model** so that I can **receive and store customer messages in my database**.
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
    - When a user visits the homepage, they can easily understand the purpose of the website
    - The user can navigate to other pages of the website 
    - The user can view a brief "About Us" section
    - The user can see a summary of services offered

- **View Business Information**: As a **Site User**, I can **view information about the business** so that I can **make an informed decision about ordering a service**.
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
    - When I click on a service, I can view its details page.
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
    
- **View Preview of Cart**: As a **Site User** I can **view a preview of the cart when I add a service to it** so that **I can know the action was successful and confirm what is in the cart without navigating away from the current page**.
    - When I add a service to the cart on smaller screens, I can see a toast preview with the cart details.
    - On desktop screens, when I add a service to the cart, I can see a preview of the cart contents in an offcanvas element.
    
- **Update Services from the Cart Page**: As a **Site User**, I can **update or remove services from the cart** so that I can **have an improved experience without navigating back to individual service pages**.
    - I can change the number of a given service and see the subtotal and order total price change.
    - I can remove a service from the cart.
    - When I click remove, I can see the total price change for the order.
    
- **Proceed to Checkout**: As a **Site User**, I can **navigate to the checkout page with my order** so that I can **enter my details and place my order**.
    - When I click the checkout button, I can enter my personal and delivery details.
    - I can enter my payment information.
    - I can review my order before submitting.

</details>

#### EPIC: Payment System

<details><summary>Show User Stories</summary>

- **Set Up Stripe**: As a **Developer** I can **set up Stripe in my application** so that I can **handle and process payments securely**.
    - I can install Stripe.
    - I can set up a webhook handler.
    - I can implement views to process the payment and order data.

- **Pay for an Order**: As a **Site User** I can **enter my payment details successfully** so that I can **secure my order**.
    - I can enter my payment details in the checkout process.
    - I can be informed of the success or failure of the payment attempt.

- **Receive Confirmation of Orders**: As a **Site User** I can **receive confirmation of my successful order** so that I can **confirm that my order was received and have the details available to me outside of the website**.
    - When I submit an order, I can see a confirmation message on the site with an order number provided.
    - I can view the submitted order details on my account page.
    - I can view the order details in an email confirmation.

</details>

#### EPIC: Reviews

<details><summary>Show User Stories</summary>

- **View Reviews**: As a **Site User**, I can **view reviews for a service** so that I can **be more informed about the quality of work carried out by the business**.
    - On a particular service page, I can view all reviews for that service.
    - I can navigate through the reviews via pagination.
    
- **Review a Service**: As a **Site User**, I can **review a service that I have ordered** so that I can **leave feedback as a customer and feel like I am interacting with the website and business directly**.
    - I can interact with a "Leave a Review" button.
    - I can rate the service out of 5 stars.
    - I can write a brief review on my experience with the service.
    
- **Edit a Review**: As a **Site User** I can **edit a review that I previously made** so that I can **be in control of content created by me on the website**.
    - For a particular review I have made, I can click an edit button.
    - I can edit the rating and text content of my reviews and save the changes.
    
- **Publish Reviews**: As a **Site Admin** I can **publish pending reviews or unpublish them on the live website** so that I can **ensure only genuine reviews are visible for the business' services**.
    - For a given pending review, I can publish it to the website and make it publicly visible.
    - For a given published review, I can unpublish it so that users cannot see it.
    
- **Delete a Review**: As a **Site User** I can **delete a review that I previously made** so that I can **be in control of content created by me on the website**. As a **Site Admin** I can **delete any review** so that I can **be in control of content displayed on the website**.
    - For a particular review, I can delete it if I am the author or a staff user.
    - I can confirm or cancel the delete action before it takes effect.

</details>

#### EPIC: Contact Us

<details><summary>Show User Stories</summary>

- **View Contact Us Page**: As a **Site User**, I can **send a message to the business** so that I can **make enquiries directly from the website**.
    - I can navigate to the Contact Us page from the main nav bar.
    - I can send a message to the business using a form.

- **Contact Us Email Confirmation**: As a **Site User** I can **receive an email copy of my enquiry** so that I can **have my own record of the correspondence**.
    - When I send a message via the Contact Us form, I can receive a copy of the message sent to me via email.


- **Pre-filled Contact Us Form**: As a **Site User**, I can **have my account details pre-filled in the Contact Us form** so that I can **avoid typing out data already provided by my user account**.
    - When I am logged in and navigate to the contact us form, I can find my name, email, and phone number pre-filled in the form.

</details> 

#### EPIC: Marketing

<details><summary>Show User Stories</summary>

- **Subscribe to Newsletters**: As a **Site User** I can **sign up to the website's newsletter** so that I can **be made aware of upcoming offers and information disseminated by the company**.
    - I add my email to the newsletter mailing list.
    - I can receive feedback confirming that I have been added to the mailing list. 

- **Create Facebook Page**: As a **Developer** I can **create a mock-up Facebook business page** so that I can **demonstrate how social media marketing would be implemented for the business**.
    - I can create a mock-up of a Facebook business page for The Garden Path.
    - I can add relevant images.
    - I can add posts.

- **Search Engine Optimisation**: As a **Developer** I can **implement various SEO features** so that I can **improve the website's performance for search engine indexing**.
    - I can conduct research on and implement keywords.
    - I can create a robots.txt file.
    - I can create a sitemap.xml file.
    - I can employ descriptive meta tags.
    - I can add `rel` attributes on appropriate external links.
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

![Image of Kanban Board](docs/images/readme/kanban-final.png)

## Marketing
All documentation on the marketing for this e-commerce application can be found in the [MARKETING.md](/MARKETING.md) file.

## Design

### Colour Scheme
A palette of greens gradually becoming lighter was chosen for this website. The different green colours are reflective of the environments in which The Garden Path services are carried out. An off-white colour called Isabelline was added to be able to soften areas of the website and avoid using a complete white shade.

![Coolors colour palette](docs/images/readme/the-garden-path-colours.png)

Some original design choices had to be altered after WAVE Accessibility testing was carried out. Instances of the lighter green colours had to be replaced with the darker shade to resolve contrast errors. The most noticable design change is the colour and background of the review star ratings. A direct comparison is provided in the [WAVE Accessibility Testing](/TESTING.md#accessibility-testing) section of  the TESTING file.

### Typography
The Mate font was chosen from the Google Fonts library as its thin and sharp look evoked thoughts of garden tools, fencing, and ordered lines. This gives the impression of a professional business and makes the user envisage neat and careful services carried out by the business.

![Mate Font](docs/images/readme/mate.png)

### Imagery
Vibrant and colourful images were chosen for the website to represent the services on offer. Each service image is clear in what it represents with no superfluous information that could mislead the site user. 
The hero image shows a garden path and steps leading to a patio. Red poppies are in focus in the foreground, and other plants and trees are in the blurred background. Some pages did not make use of a hero image due to aesthetic design reflecting the pages' purpose. These include but are not limited to the accounts pages, the cart and checkout pages, and the privacy policy page. Individual reasons for this design choice are discussed further in the [Features](#features) section.


### Wireframes
Wireframes were created in Balsamiq for the initial front-end design of the website. The mobile layout was designed first and the tablet and desktop were adapted from this.

**Home Page**

#### Homepage Wireframes

<details open><summary>Homepage Wireframe - Mobile</summary>

![Homepage Wireframe - Mobile](docs/images/readme/mobile-wireframe-home.png)

</details>

<details><summary>Homepage Wireframe - Tablet</summary>

![Homepage Wireframe - Tablet](docs/images/readme/tablet-wireframe-home.png)

</details>

<details><summary>Homepage Wireframe - Desktop</summary>

![Homepage Wireframe - Desktop](docs/images/readme/desktop-wireframe-home.png)

</details>

**About Us Page**

<details open><summary>About Us Wireframe - Mobile</summary>

![About Wireframe - Mobile](docs/images/readme/mobile-about.png)

</details>

<details><summary>About Us Wireframe - Tablet</summary>

![About Wireframe - Tablet](docs/images/readme/tablet-about.png)

</details>

<details><summary>About Us Wireframe - Desktop</summary>

![About Wireframe - Desktop](docs/images/readme/desktop-about.png)

</details><br>

**Services Page**

<details open><summary>Services Wireframe - Mobile</summary>

![Services Wireframe - Mobile](docs/images/readme/mobile-services.png)

</details>

<details><summary>Services Wireframe - Tablet</summary>

![Services Wireframe - Tablet](docs/images/readme/tablet-services.png)

</details>

<details><summary>Services Wireframe - Desktop</summary>

![Services Wireframe - Desktop](docs/images/readme/services-desktop.png)

</details>

**Individial Service Pages**

<details open><summary>Individual Service Wireframe - Mobile</summary>

![Individial Service Wireframe - Mobile](docs/images/readme/service-mobile.png)

</details>

<details><summary>Individual Service Wireframe - Tablet</summary>

![Individial Service Wireframe - Mobile](docs/images/readme/tablet-service-page.png)

</details>

<details><summary>Individual Service Wireframe - Desktop</summary>

![Individial Service Wireframe - Mobile](docs/images/readme/service-desktop.png)

</details>

**Cart Page**

<details open><summary>Cart Wireframe - Mobile</summary>

![Cart Wireframe - Mobile](docs/images/readme/basket-mobile.png)

</details>

<details><summary>Cart Wireframe - Tablet</summary>

![Cart Wireframe - Mobile](docs/images/readme/basket-tablet.png)

</details>

<details><summary>Cart Wireframe - Desktop</summary>

![Cart Wireframe - Mobile](docs/images/readme/basket-desktop.png)

</details>

**Checkout Page**

<details open><summary>Checkout Wireframe - Mobile</summary>

![Checkout Wireframe - Mobile](docs/images/readme/mobile-checkout.png)

</details>

<details><summary>Checkout Wireframe - Tablet</summary>

![Checkout Wireframe - Mobile](docs/images/readme/tablet-checkout.png)

</details>

<details><summary>Checkout Wireframe - Desktop</summary>

![Checkout Wireframe - Mobile](docs/images/readme/desktop-checkout.png)

</details>

### Entity Relationship Diagrams
An ERD was created to plan out the models that would be created and used in this project. Some custom models were written and others were taken from previous Django projects. The latter type are credited below in the [Code Used](#code-used) section, and all custom models are explained in the [Custom Models](#custom-models) section.

![ERDs](docs/images/readme/erd_the_garden_path.png)

### CRUD Functionality
A key requirement for this project was for users to be able to create, read, update, and/or delete data from the database as appropriate. Users could interact with the database in these ways as follows:

#### Create
* Site users and admin users may **create** by creating a user account.
* Site users may **create** by creating an order, reviewing a service, or submitting a message.

#### Read
* Site users and admin users may **read** by viewing services, reviews, their account details, and their order history.
* Admin users may also **read** by viewing unpublished reviews.

#### Update
* Site users may **update** by amending their account details or editing their reviews.
* Admin users may **update** by publishing or unpublishing reviews.

#### Delete
* Site users may **delete** by deleting their reviews or deleting their phone number and address details on their account page.
* Admin users may **delete** by deleting reviews.

<br>


### Responsiveness
Across all pages of the website, Bootstrap's powerful grid system was utilised to control content reponsiveness on a wide variety of screen widths. The design of some key website features on different display sizes is demonstrated below. 

#### Navbar
On small screen sizes the navbar is a dropdown menu accessed on the right hand side of the display. For larger screens the navbar links are displayed in a neat row across the top of the page. This was achieved using the navbar code in the Bootstrap documentation.

<details><summary>Comparison of navbar on small and large screens</summary>

![Nav bar menu on small screens](docs/images/readme/navbar-mobile.gif)
![Nav bar on larger screens](docs/images/readme/navbar-desktop.png)

</details>

#### Hero Image
The hero image is shown with its original aspect ratio of ~3:2 on screen sizes up to 768 pixels width. For larger screens, the `<img>` element has a custom CSS style of `display: none` applied, and its parent div is given a `background-image` of the same picture with a fixed height so that the website content is not completely pushed down out of sight.

<details><summary>Responsiveness of hero image with differing screen widths</summary>

![Responsiveness of Hero Image](docs/images/readme/hero-responsive.gif)

</details>

#### Text Content
Content on small screens is displayed in single column fashion, displaying text and images appropriately as the user scrolls down their device. On larger screens, text and images are displayed side-by-side to make use of the extra horizontal space.

<details><summary>Comparison on text content layout on small and large screens</summary>

![Content layout on small screens](docs/images/readme/content-mobile.gif)
![Content layout on large screens](docs/images/readme/content-desktop.png)

</details>

#### Service Page
On the service page, the service images are displayed in columns of 1, 2, 3, and 4 as the screen width increases. The four pricing model cards follow a similar trend underneath.

<details><summary>Service page on small screens</summary>

![Service page on small screens](docs/images/readme/services-mob.gif)

</details>

<details><summary>Service page on medium screens</summary>

![Service page on medium screens](docs/images/readme/services-tablet.gif)

</details>

<details><summary>Service page on large screens</summary>

![Service page on large screens](docs/images/readme/services-desktop.gif)

</details>

#### Individual Services
On each service page, the image and service information are displayed either in a single column or in two columns. This is done to maximise the impact of the imagery on wider screen by allowing for a larger image and to make user of the extra space.

<details><summary>Comparison of service page on mobile and tablet screens</summary>

![Grass Cutting page on mobile screens](docs/images/readme/ind-services-mob.gif)
![Grass Cutting page on tablet screens](docs/images/readme/ind-services-tablet.png)

</details>

#### Cart
The cart and its features are neatly arranged using the grid system on all screen sizes. The order items and checkout card are displayed in a single column on small screens but are placed side-by-side on wider screens. On large screen sizes the order item list in contained in its own scrollable container, so that the user does not have to scroll away from the checkout card.

<details><summary>Cart on mobile screens</summary>

![Cart on mobile screens](docs/images/readme/cart-mob.gif)

</details>

<details><summary>Cart on desktop screens</summary>

![Cart on desktop screens](docs/images/readme/cart-desktop.gif)

</details>

#### Checkout
The site logo, secure checkout text, and progress indicator change position at the top of the screen for different displays to neatly use the extra space provided.

<details><summary>Comparison of checkout header on small and large screens</summary>

![Checkout header on mobile screens](docs/images/readme/checkout-mob.png)
![Checkout header on mobile screens](docs/images/readme/checkout-tablet.png)
![Checkout header on mobile screens](docs/images/readme/checkout-desktop.png)

</details>

The review order card does not diplay the service images on mobile screen, but on tablets and desktop screens, there is sufficient space to show them.

<details><summary>Comparison of review order card on small and large screens</summary>

![Checkout order review card on mobile screens](docs/images/readme/checkout-review-mob.png)
![Checkout order review card on wider screens](docs/images/readme/checkout-review-desktop.png)

</details>

#### Reviews 
Reviews are displayed in different ways depending on how many there are for a service. With at least three, they are arranged in columns of 1, 2, or 3 as screen sizes widen. If there is only one review, a single column is used on all screens, albeit with appropriate offsets to give the review card a set maximum width. Similarly, if there are only two reviews, the maximum number of columns used on larger screens is 2. This is to keep reviews centred on the page regardless of how many there are.

<details><summary>Comparison of user reviews small and large screens</summary>

![User reviews on mobile screens](docs/images/readme/reviews-mob.gif)
![User reviews on wider screens](docs/images/readme/review-tablet.png)

</details>

#### Contact Us
The Contact Us page displays its form fields in columns of width 10 with an offset of 1 on mobile screens, and columns of width 6 with an offset of 3 on tablet-sized screens and larger. Specific CSS styling had to be applied to the third-party reCAPTCHA container on smaller screens so that it did not extend past the width of the `<html>` element and create a horizontal scroll.

<details><summary>The Contact Us page on small and large screens</summary>

![Contact Us page on mobile screens](docs/images/readme/contact-mob.png)
![Contact Us page on mobile screens](docs/images/readme/contact-desktop.png)

</details>

#### Footer
The footer is displayed in a single column on small screens, with a horizontal line separating the different information blocks. On larger screens, these blocks are arranged in a row that uses the full width of the screen, and the horizontal lines are hidden. 

<details><summary>Comparison of Footer on small and large screens</summary>

![Footer on small screens](docs/images/readme/footer-mobile.png)
![Footer on larger screens](docs/images/readme/footer-desktop.png)

</details>

## Features
The website consists of over 40 pages with varying levels of accessibility for different types of users:

**Page** | **All Users** | **Authenticated User** | **Staff Users**
:--- | :---: | :---: | :---:
Homepage | &check; |  | 
About Us | &check; |  | 
All Services | &check; |  | 
Individual Services (6) | &check; |  | 
Service Reviews (6) | &check; |  | 
Cart | &check; |  | 
Checkout | &check; |  | 
Confirmation Order page | &check; |  | 
Contact Us | &check; |  | 
Signup and Sign in pages | &check; |  | 
Verify Email pages (2)
Password Reset pages (4) | &check; | |
Error pages: 404, 403, and 500 | &check; |  | 
Newsletter page | &check; |  | 
Privacy Policy page | &check; |  | 
My Account |  | &check; | 
Past Order Confirmation pages |  | &check; | 
Leave a Review page |  | &check; | 
Edit a Review page |  | &check; | 
Sign Out page |  | &check; | 
Unpublished Reviews (6) |  |  | &check;

### Custom Models
Original custom models were written for this e-commerce application:
- CustomUser
    - A custom user model to allow logging in using an email address instead of a username. The model explicity sets the login field to use email addresses and sets the first_name and last_name fields as required fields. The CustomUserManager model is set as the model to use when creating
    new CustomUser model instances.
- CustomUserManager
    - For creating user accounts when a site visitor signs up for the first time. A user account is created with the supplied email, password, and first and last name. Superuser creation is also specified and adds the additional Boolean fields of `is_staff`, `is_active`, and `is_superuser` and sets them to `True`.
- Services
    - A custom model for the gardening services on offer. It contains fields for the category type of the service, the name of the service, its price, a full description of the service, a URL for an image representing the service, image alt text for accessibility reasons, the number of published reviews the service has, the average value of all the published review ratings the service has, and Boolean fields denoting whether the service can have the size, acre, tree, or surface attributes.
    - Its `calculate_average_rating` method loops through all approved reviews for the service, sums their ratings, and divides the result by the total number of approved reviews to get an average value.
- Reviews
    - A custom model for service reviews. The model contains fields for a foreign key linked to the authenticated user leaving the review, the service being reviewed, a title, a body of text, the date that the review was originally submitted, the date that the review was last edited or published, the user's rating from 1 to 5, and if the review has been published or not.
- Contact
    - A custom model for submitting a "Contact Us" style inquiry. The model has fields for a foreign key linking the user's message to their UserAccount if they were authenticated, the user's full name, their contact email, their contact number, a specific reason for sending a message, the message content, and the date that the message was submitted.

### All pages on the website have:

**1.** A favicon of a pair of gloves. This icon was chosen to reflect a hands-on and professional business to the customer.  

![Gloves favicon](docs/images/readme/gloves-favicon.png)

**2.** A header with a logo and nav bar or menu dropdown for page links (except the checkout page)

![Website Header on mobile](docs/images/readme/header-mobile.png)
![Website Header on desktop](docs/images/readme/header-desktop.png)

The header contains direct links to the main pages of the website, depending on the authentication status of the site user. The nav link for the page currently being viewed is made distinct with a CSS style of `active` which is represented by a background colour of Sage and text colour of Isabelline when the nav bar is in dropdown form, and a bold font weight with a subtle Isabelline text shadow on larger screens.
- The website logo "The Garden Path" is a link which, when clicked, will return the user to the `index.html` page.
- "About Us" brings the user to the `about.html` page.
- The "Services" dropdown displays a list of options, which include the `services.html` and `service_page` pages.
- "Cart" links to the `cart.html` page.
- "Contact Us" brings the user to `contact.html`.
- "Log In/Sign Up" will direct the user to the `login.html` page which itself contains a link to `signup.html`.

When a user is signed in, the header links change.
- A new link, "My Account", brings the user to the `accounts.html` page.
- "Log In/Sign Up" is hidden, and "Log Out" is shown, which will direct the user to the `logout.html` account page.

    ![Website Header on mobile when user is logged in](docs/images/readme/header-authenticated-mobile.png)
    ![Website Header on dekstop when user is logged in](docs/images/readme/header-authenticated-desktop.png)


**3.** A footer with contact information, social media links, and links to important internal pages and relevant external sites.

- The phone number link opens the device's calling app with the number displayed. The email link similary open the device's email app with the email already entered in the "To:" field.
- The Facebook and Instagram links direct the user to the homepages for those sites, but for a real business these links would point to the business' pages on those platforms.
- Two links are included for SEO reasons and are discussed further in the [MARKETING.md](/MARKETING.md) file.
    - A link to the Associaton of Landscape Contractors in Ireland website
    - A link to the Royal Horticultural Society of Ireland website
- Two other links are for important pages on the website:
    - The privacy policy page
    - The newsletter signup page

![Website Footer](docs/images/readme/footer-desktop.png)

### The Homepage
The homepage contains two sections: a general introduction and a services overview. A heading welcomes the user with a smaller muted heading below it, communicating that the business is local and specialises in garden care. An image of a smartly dressed mature man holding a leaf is displayed next to the introduction. This gives the user a sense that the business offers experience and knowledge. The services sub-heading lists the locations covered by the business so that the user understands if they can avail of The Garden Path's services without having to navigate further through the website. An image of a man driving a ride-on lawnmower is shown next to the summary of services, and a button which links to the services page is displayed underneath.

![The website' homepage](docs/images/readme/content-desktop.png)

### The About Page
Three distinct sections are displayed on the About page.
- The first is a short statement about the business followed by a paragraph on the founding of the business by the fictional Dermot Murphy. This history instills a sense of trust and customer care in the user as they think of The Garden Path as one that started as a local business run by someone passionate about their work that has become successful and increased in size. A picture of "Dermot" amongst vegetation reading from a tablet makes the user think of the business as one with good attention to detail.

    ![Our Story section of About Us page](docs/images/readme/about-story.png)

- The second section has a different background colour and inset shadow both to seperate it clearly from the other sections and to break up the amount of white on the page. This section contains two different headings which detail the business' mission and the top reasons to patronise The Garden Path. There is a button underneath the "Why Choose Us?" list, which brings the customer directly to the Contact Us page if they want to get a quote for the work to be carried out.

    ![Our Mission section of About Us page](docs/images/readme/about-mission.png)

- The third section is brief paragraph that speaks directly to the prospective customer. It communicates that the business is dedicated to quality service and delivering exactly what the customer wants. A image of "Dermot" smiling and looking directly at the camera makes a connection with the user as if they were speaking in person to a staff member.

    ![Our Mission section of About Us page](docs/images/readme/about-committment.png)


### The Service Pages
#### All Services
The All Services page consists of two sections: the list of services and the pricing model.
- Currently offering six types of services, the business displays each as a card containing a large vibrant image with a title underneath it. Clicking any of the images or titles will bring the user to the individual service page.

    ![The All Services page services section](docs/images/readme/services-section.png)

- The pricing model section outlines the hourly rates for each category of service and, if applicable, the minimum number of hours for the service to be carried out.

    ![The pricing model section](docs/images/readme/pricing-section.png)

#### Individual Service Pages
For each individual service, the page is displayed with the hero image to draw the user's eye to the colours in the image and in the star ratings. A brief description of the service is given, under which sits the star rating. The average rating is displayed as a number of stars out of 5 filled with an orange colour. The decimal value of the rating is listed next to the stars, as well as the number of reviews. The number of reviews is a link to the reviews page for the service and is one of the few links on the website outside of the footer where the underline has not been removed for styling reasons. It must be present so that the user understands they can click the link to view the list of reviews.

Underneath the rating are the option(s) for the user to select. These can range from 1-3 options e.g. the size of the area for grass cutting (1 option) or the type of tree service, the size of the tree, and the number of trees (3 options). The price per number of services is shown underneath the options, along with two buttons that either allow the user to go back to the list of all services or add the current service to the user's cart with the selected options.

![An individual service page](docs/images/readme/ind-services-tablet.png)

Underneath each service's title are breadcrumb links of the form "All Services > Category > Service". Clicking on the Services breadcrumb takes the user back to the All Services page. Clicking the category breadcrumb (in the above image called "Garden Maintenance") renders the all services page with a category filter so that only services of the current category are shown and with the category name appended to the page's heading. The breadcrumb is shown in bold for the level of page that the user is currently viewing.

![The service category page for Garden Maintenance](docs/images/readme/category-page.png)

### The Shopping Cart
When viewing the cart page without any services having been added to it, a message saying "Your cart is empty" is displayed with a button that will bring the user back to the All Services page. The heading indicates the number of services in the cart at any given time.

<details open><summary>Comparison of the cart page when empty and when containing one service</summary>

![Empty Cart page](docs/images/readme/cart-empty.png)

![Cart page with one service](docs/images/readme/cart-01.png)

</details>

When greater than zero, the total price of the services in the cart is appended after the Cart navbar link. When the cart has multiple services, the list is displayed underneath the checkout card on mobiles and in a fixed height scrollable container on larger screens. For mobile screens, a button that brings the user back to the top of the page is shown when the user scrolls down through the list of services.

<details><summary>Comparison of the cart page with several services on different screen sizes</summary>

![A cart with many services on small screens](docs/images/readme/cart-mob.gif)

![A cart with many services on larger screens](docs/images/readme/cart-desktop.gif)

</details>

#### Quantity and Remove buttons
To amend the number of services directly from the cart, the user can click the **-** or **+** buttons to immediatley update the value. The decrement button is disabled when the value is 1 but the user may enter 0 directly into the field in which case the service will be removed from the cart.

<details><summary>Removing a service from the cart by setting the number to 0</summary>

![Removing a service from the cart by setting the number to 0](docs/images/readme/cart-0-remove.gif)

</details>

The remove button is given a prominent size, either as wide as the image or the details container. The `btn-outline-danger` Bootstrap class is used instead of a solid red fill for three different reasons: 
- To keep the association of red with removal or deletion
- To not distract from the colours in the vibrant images
- To avoid clashing with the various green shades used

![Removing an item from the cart with the remove button](docs/images/readme/cart-remove-button.gif)

#### The Cart Preview
When adding services to the cart, the user is shown a summary of the current contents of their cart and the total price. This is displayed in the toast message on mobile and tablet screens, and in an offcanvas element on desktop screens. Both types of preview feature a scrollable list for many services and a "View Cart" button to bring the user directly to the cart page.

<details><summary>Toast message cart preview on small screens</summary>

![Cart preview on smaller screens](docs/images/readme/cart-preview-mob.gif)

</details>

<details><summary>Offcanvas cart preview on large screens</summary>

![Cart preview on desktop screens](docs/images/readme/cart-preview-desktop.gif)

</details>

### The Checkout Page
When a user proceeds to the checkout page, the navbar is not shown. The site logo is still present, but in the navbar's place is now text saying "Secure Checkout" with a padlock icon, and a custom progress indicator for the checkout process. 

![Checkout Page header](docs/images/readme/checkout-mob.png)

#### Progress Indicator
The indicator consists of three filled grey circles connected by grey lines representing the three steps of the checkout process. This is made clear to the user with subheadings under each circle titled "Address", "Payment", and "Review". The circle representing the current step is twice the diameter of the others and has a black colour. When a user moves to the next step, the previous step's circle and the connecting line retain their black colour, but the circle becomes smaller again. This allows the user to understand exactly where they are in the checkout process, what steps they have completed, and how many steps are left.

<details><summary>Demonstration of checkout progress indicator</summary>

![Demonstration of checkout progress indicator](docs/images/readme/checkout-progress.gif)

</details>

#### Address Details
The user is first presented with form fields related to their personal details and address. All fields except for "Street Address 2" and "Eircode" are required. The "Continue to Payment" button is disabled until all required input fields contain data. This validation is explained in detail in the [TESTING.md](/TESTING.md) file. An authenticated user can interact with a checkbox that saves the entered details to their user account.

<details><summary>Checkout address fields and proceed button enable/disable feature</summary>

![Checkout address fields and proceed button enable/disable feature](docs/images/readme/checkout-address.gif)

</details>

<details><summary>Save details checkbox in checkout form</summary>

![Save details checkbox in checkout form](docs/images/readme/checkout-save-details.png)

</details>

#### Payment Details
Continuing to the next stage, the user must enter valid card details into a Stripe input field. The "Review Order" button is disabled until valid details are entered into the field with no errors present.

<details><summary>Checkout payment input and review order button</summary>

![Checkout payment input and review order button](docs/images/readme/checkout-payment.gif)

</details>

#### Review Order
Moving to the final step of the checkout process, an orange text box explains that this is the final step and that user may review their order details below before making the payment. The user's address details are displayed with a "Change" link to go directly back to the address section in case they wish to change any data. The payment details are not explicitly displayed, but a message saying that the input was complete is present with a green check box. A change link is also present here in case the user wants to change their card details. Underneath is presented a summary of the cart. Only the service name is presented here, as adding the various options affected the presentation poorly. If the user is unsure of the cart contents, there is an "Adjust Cart" button, which they can use to navigate back to the cart page. A larger yellow button with the text "Pay and Place Order" draws the eye of the user with its bright colour and padlock icon. This helps the user understand that once they click this button, the checkout process will complete, and they can no longer make any adjustments. When clicked, the button text changes to "Processing..." and the padlock turns into a spinner, indicating that the payment is being processed. This is especially useful when an unexpected payment or server error occurs. The user will know that the website is, in fact, attempting to submit the order.

<details><summary>Review Order section and checkout submission</summary>

![Review Order section and checkout submission](docs/images/readme/checkout-success.gif)

</details>

#### Checkout Success
On successful checkout, a confirmation toast message is shown and informs the user that copy of the order details will be sent to the provided email.

![Checkout success toast message](docs/images/readme/checkout-success-toast.png)

The success page itself also confirms this as well as providing the unique order number. A summary of the order is given with a button allowing the user to navigate back to the website's homepage.

![Checkout success page](docs/images/readme/checkout-success.png)

### User Accounts
#### Signing Up
Visitors to the website can register for a user account via a number of links to the Signup Page. The navbar contains the link "Login/Signup", which takes the user to the login page. If the visitor has no account yet, they may use the Sign Up link to navigate to the account creation page. Here, they are presented with a signup form which has required fields of first name, last name, email, confirm email, password, and confirm password. The confirm email field is cruicial here as users do not create usernames but instead use their email addresses to log into their accounts.

<details open><summary>The Sign Up page</summary>

![The Sign Up page](docs/images/readme/signup.png)

</details>

After entering valid details, the user can click the Sign Up button to be brought to the Verify Email Address page. This page informs the user that a confirmation email has been sent to the address they provided, which they must verify before they can log in to the website. If they attempt to log in before verifying their email address, they are redirected to the same page that explains the confirmation email. On successfully verifying their email address, the login page is rendered with an information toast message confirming that the user's email has been verified.

<details><summary>The Signup form being submitted</summary>

![The Sign Up form being submitted](docs/images/readme/verify-email.gif)

</details>

<details><summary>The Verify Email toast message</summary>

![The Verify Email toast message](docs/images/readme/login-toast.png)

</details>

<details><summary>Verifying the email address</summary>

![The verify email page](docs/images/readme/email-confirm.png)

![Toast message after email verification](docs/images/readme/email-confirmed.png)

</details>

#### Logging In
Existing users may log in using their email and password. On the login form, there is a Remember Me checkbox, which, when checked, will keep the user logged in on their current device for seven days as opposed to the default behaviour, which would be until the browser is closed. A password reset link is presented underneath the password field. On successful login, a toast message confirms the account under which the user has just signed in.

<details open><summary>The Sign In page</summary>

![The Sign In page](docs/images/readme/login.png)

</details>

<details><summary>Login toast message</summary>

![The Verify Email toast message](docs/images/readme/login-toast.png)

</details>

#### Password Reset
If a registered user enters a valid email into the reset password form and submits it, a page is rendered informing them to check their email inbox for a password reset link. When the user follows the link, they may change their account password. If the new password is valid, a success page and toast message is rendered confirming that their password was changed. A button underneath the message allows to the user to quickly navigate back to the login page.

<details open><summary>Password Reset page</summary>

![Password Reset page](docs/images/readme/password-reset.png)

</details>

<details><summary>Password Reset information page</summary>

![Password Reset page](docs/images/readme/password-email.png)

</details>

<details><summary>Password Reset form</summary>

![Password Reset page](docs/images/readme/change-password.png)

</details>

<details><summary>Password Reset success page</summary>

![Password Reset page](docs/images/readme/password-changed.png)

</details>

#### Signing Out
A user may sign out when authenticated by clicking the Log Out nav link. They are asked to confirm the action before signing out of their account, and can use the Back button to go back if they change their mind. On successful logout, a toast message is displayed to the user.

<details><summary>Sign Out page</summary>

![Password Reset page](docs/images/readme/logout.png)

</details>

<details><summary>Toast message after signing out</summary>

![Password Reset page](docs/images/readme/logout-toast.png)

</details>

#### My Account Page
An authenticated user may view their account page via a link in the nav bar. On this page, they will see the full name and email that was provided during registration. These two details are read-only. The Default Location Information form contains the user's details if present. These details are rendered herre if the user previously placed an order and clicked the save details checkbox or if they entered the data directly on this page and clicked the Save Changes button.

<details open><summary>My Account page</summary>

![My Account page](docs/images/readme/account.png)

</details>

The user's order history is listed if it exists. The order number, date of purchase, summary of order items, and total price are displayed in a table. The order number is truncated in the table and is itself a link to the past order confirmation page with full details of the past order. Hovering over the link on desktop screens will display the full order number. When the order confirmation page is visited from this link, an information toast message is displayed stating that this order was in the past. If the user has no order history, a statement confirming this is presented instead of an empty table. A "Back to My Account" button allows the user to navigate directly back to their account page.

<details><summary>Toast message and changed button text on past order confirmation page</summary>

![Toast message on past order confirmation page](docs/images/readme/past-order-toast.png)

![Changed button text on past order confirmation page](docs/images/readme/past-order-button.png)

</details>

<details><summary>Order number displayed on mouse hover</summary>

![Order number displayed on mouse hover](docs/images/readme/order-number-hover.png)

</details>

<details><summary>Order history section when user has no order history</summary>

![Order history section when user has no order history](docs/images/readme/account-no-orders.png)

</details>

### The Reviews page
A review page exists for each service that The Garden Path offers. Only users who have previously ordered a particular service can write reviews for it. The link to the reviews page is presented next to the star rating on each service page. When clicked, the user may read the various reviews that have been approved by the site administrators.

![Reviews page](docs/images/readme/reviews-mob.gif)

A maximum of 6 reviews are displayed at any one time. If more reviews exists, then pagination controls are shown underneath the reviews as well as an indication of how many pages of reviews there are.

<details><summary>Pagination of reviews</summary>

![Reviews pagination](docs/images/readme/reviews-pagination.png)

</details>

#### Writing a Review
If a user has previously ordered a particular service, they will see a Leave a Review button under the page's heading. Clicking it will bring them to the `create_review.html` page. Confirmation of the account under which the review is being made is given above the review form. The user must complete three fields: a title, review content, and a rating out of 5. A green Submit button will allow the user to submit their review and a confirmation toast message is displayed stating that the review is pending approval.

<details open><summary>The Leave a Review button</summary>

![Leave a Review button](docs/images/readme/review-button.png)

</details>

<details><summary>The review form page</summary>

![The review form page](docs/images/readme/review-form.png)

</details>

<details><summary>The review confirmation toast message</summary>

![The review confirmation toast message](docs/images/readme/review-toast.png)

</details>

#### Deleting or Editing a Review
When a user in logged in they may edit or delete their published reviews. In these cases, a horizontal line is added to the review card and two distinct Edit and Delete buttons are presented.

<details open><summary>A review with Edit and Delete buttons</summary>

![Review card as seen by its author](docs/images/readme/reviews-author.png)

</details>

If the user clicks the Edit button, the review form page is loaded with an amended page title, form heading, and with the form data populated in the fields. Similar to above, a toast message confirms that the review was edited and is not awaiting staff approval. The review can no longer been seen in the list of reviews.

<details><summary>The Edit Review page with amended heading and pre-filled form data</summary>

![Review card as seen by its author](docs/images/readme/reviews-edit.png)

</details>

<details><summary>The edit review toast message</summary>

![The review confirmation toast message](docs/images/readme/review-edit-toast.png)

</details>

If the user clicks the delete button, a confirmation modal is displayed, informing them that the delete action cannot be undone. A cancel button will close the modal without deleting the review.

<details><summary>The Delete Confirmation Modal for reviews.</summary>

![Delete review modal window](docs/images/readme/review-modal.png)

</details>

#### Publishing and Unpublishing a Review
Staff users may view a page containing all unpublished reviews and delete or publish them at their discretion. When viewing the main reviews page for a service, they may unpublish or delete any reviews listed, though they do not have the ability to edit any reviews that are not their own. There is no hero image on the unpublished reviews page, as only staff users will ever see it, and it reduces the load on the browser. Staff users can also see the reviewer's contact email address at the bottom of the review card so that they can directly address any concerns the user may have communicated in the review.

<details><summary>Admin view of reviews page</summary>

![Admin view of reviews page](docs/images/readme/reviews-admin.png)

</details>

<details><summary>The unpublished reviews page</summary>

![The unpublished reviews page](docs/images/readme/reviews-unpublished.png)

</details>

### The Contact Us Page
The Contact Us form is available for all site visitors to use, regardless of their authentication status. There are 6 form fields, all of which are required:
- Full name
- Contact email
- Phone Number
- Reason for inquiry
- Message content
- Google reCAPTCHA check

If a user is authenticated, the name, email, and phone number fields will already be completed using their user account data. The user must select a reason for contacting the business from a set list of options. Given that the page is publicly accessible to all site visitors, the reCAPTCHA check has been included to combat automated malicious form submissions. When the contact form is submitted successfully, the user is redirected to the homepage, a success toast message is displayed, and a copy of the message details is sent to the email address they provided in the form.

<details><summary>The contact us form</summary>

![The contact us form](docs/images/readme/contact-desktop.png)

</details>

<details><summary>The Contact Us form with user detail fields already completed</summary>

![The contact us form with user detail fields already completed](docs/images/readme/contact-filled.gif)

</details>

<details><summary>The contact us form success toast message</summary>

![The contact us form success toast message](docs/images/readme/contact-toast.png)

</details>

### The Newsletter Page
Users may sign up to a newsletter mailing list by navigating to this page and entering their email address into the MailChimp form. A link to the page is present in the footer of every page on the website.

<details><summary>The newsletter page with MailChimp form</summary>

![The newsletter page with MailChimp form](docs/images/readme/newsletter-page.png)

</details>

### The Privacy Policy Page
The website's privacy policy is presented on its own webpage. Usert may view the policy by following the link provided in the footer on each page. Users are informed that any queries realated to the privacy policy can be sent to the business by using the Contact Us form.

<details><summary>The privacy policy page</summary>

![The privacy policy webpage](docs/images/readme/privacy-policy.png)

![The section of the privacy policy regarding inquiries](docs/images/readme/privacy-contact.png)

</details>

### Error Pages
Custom templates for 403, 404, and 500 error were created for the website. Each page informs the user that something has gone wrong and gives them a navigation option to go back to the main site. The navbar may also be used on each of these pages.

<details><summary>The 403, 404, and 500 errors page</summary>

![The 403 error page](docs/images/readme/403.png)
![The 404 error page](docs/images/readme/404.png)
![The 500 error page](docs/images/readme/500.png)


</details>

### Email Functionality
The Garden Path website utilises a Gmail SMTP Server to send emails to its site users. Users are sent emails in the following situations:
- To verify the email address provided when creating a new user account
- To reset their user account password
- Receiving an order confirmation after successfully paying for and placing an order
- Receiving a summary of a submitted Contact Us form

### Features to be Implemented
Some features could not be implemented in this release of The Garden Path e-commerce website. Below are discussed some of those features that would benefit the site user or help generate more income for the business.

#### Social Media Accounts
Users often create accounts on websites more easily when they have the option to sign in via social media accounts, e.g. Google or Facebook. Offering this feature would potentially increase user engagement and lead to more revenue for The Garden Path. Social media logins could be implemented using the Django allauth package and API credentials generated for the business on those social media platforms.

#### Message History
Allowing users to view their messaging history on their account page would improve the customer experience by keeping their website data accessible from the same secure page.
Staff users would also benefit from being able to view all messages submitted via the contact us form with the ability to reply to users from an admin messages page. As part of this feature, staff users would receive a notification when new messages have been submitted since they last logged in.

#### Responding to Reviews
Adding a feature where staff users can publicy reply to reviews would demonstrate that the business is trustworthy and maintains open communication with its customers. Knowing that The Garden Path has real people behind it who are ready to deal with any issues the customers have could encourage repeat business. Similar to the above, staff users would receive a notification when new reviews have been submitted since they last logged in. This would be very beneficial as staff users must mark reviews as approved before they are published to the main reviews page.

#### Sorting Reviews
Allowing users to sort reviews based on their ratings would benefit them as prospective customers. Seeing the number of 5 stars reviews compared to number of lower star reviews can influence a customer's purchase more than the average rating itself. Since this is a gardening and landscaping website, being able to sort reviews by the season they were written in would help customer's understand how the business performs various services in different conditions.

#### Updating Website Content
Staff users would be able to directly edit website content from the front end. Content models would be created to store the text on the database allowing staff to update the database using forms. Staff would have access to a button in the navbar that toggles an "Editing Mode" for the current page. Edit buttons would be displayed next to blocks of text, which, when clicked, would enable the staff user to update or delete the content. The text would be edited in a form that is displayed in a modal. When submitted successfully, the database would be updated and the new content displayed when the page reloads.

#### Deleting a User Account
Users would have the option to delete their personal data from the database. This would be done via the My Account page and a confirmation modal would ensure the user could not accidentally delete their data by clicking a button once.

## Technologies Used
### Languages
- HTML
- CSS
- Python
- Javascript

Relational database: PostgreSQL

### Frameworks, Libraries, and Programs
[Am I Responsive?](https://ui.dev/amiresponsive) - To showcase the website on different screen sizes for this README.

Adobe Photoshop 2020 - To resize and crop images.

[Balsamiq](https://balsamiq.com/) - To create the website wireframes.

[Bootstrap 5](https://getbootstrap.com/) - To build and style content on the website.

[ChatGPT](https://chatgpt.com/) - To generate text content and sample data for the website.

Chrome Developer Tools - To visualise and test changes to the website code.

Code Institute Postgres Database server - To create and store the database.

[Coolors](https://coolors.co/) - To showcase the colour palette of the website.

[Django](https://www.djangoproject.com/) - A Python framework used to design the website.

[Favicon.io](https://favicon.io/) - To source the favicon used.

[Flake8 Linter](https://flake8.pycqa.org/en/latest/) - To ensure code meets minimum PEP8 standards.

[Free Logo Design](https://freelogodesign.org) - To create a mock logo for the business.

[Git](https://git-scm.com/) - For version control.

[GitHub](https://github.com/) - To save and store files online.

[Gitpod](https://www.gitpod.io/) - The IDE used to write my code.

[Gmail](https://www.gmail.com/) - To send email via an SMTP server.

[Google Fonts](https://fonts.google.com/) - For imported fonts used on the website.

[Google reCAPTCHA](https://www.google.com/recaptcha/about/) - To verify form submissions are genuine and prevent fraud and abuse.

[Heroku](https://www.heroku.com/) - To host the deployed version of the program.

[JSHint](https://jshint.com/) - To validate the JavaScript code.

[JQuery](https://jquery.com/) - A JavaScript library used to simplify event and DOM handling.

[LucidChart](https://lucid.app/) - To create Entity Relationship Diagrams

[Pexels.com](https://www.pexels.com/) - To source images used on the website.

[ScreenToGif](https://www.screentogif.com/) - To create GIF files for this README.

[Shields.io](https://shields.io/) - To add badges to this README.

[Shutter Encoder](https://www.shutterencoder.com/) - To convert images to .webp format.

[Stripe](https://stripe.com/) - To process and manage payments.

[TinyPNG](https://tinypng.com/) - To compress images.

[W3C Markup Validation Service](https://validator.w3.org/) - To validate the HTML and CSS files.

[W3Schools.com](https://www.w3schools.com/), [The Python Library](https://docs.python.org/3/library/), and [jQuery API Documentation](https://api.jquery.com/) - For researching and learning about Python and JavaScript methods and syntax.

## Deployment
The live version of this website was deployed on Heroku.

### Local Deployment
To deploy this program locally on your device, please follow the steps below:

#### Forking
1. Login or sign up to [GitHub](https://github.com/).
2. Navigate to the repository for [The Garden Path](https://github.com/simonhw/gardening-services).
3. Click the **Fork** button located in the top right part of the webpage.

#### Cloning
1. Log in or sign up to GitHub.
2. Navigate to the repository for [The Garden Path](https://github.com/simonhw/gardening-services).
3. Click on the green **Code** button, select your preferred option of HTTPS, SSH, or GitHub CLI, and copy the relevant link.
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
4. Create a secret key yourself or by using a website of your choice, such as [Secret Key Generator](https://secretkeygen.vercel.app/).
5. Add the following code to your `env.py` file, making sure to replace `<enter-copied-url-here>` with the URL you copied in step 2 and `<your-secret-key>` with the one you generated in step 4:
    ```python
      import os

      os.environ['DATABASE_URL'] = '<enter-copied-url-here>'
      os.environ['SECRET_KEY'] = '<your-secret-key>'
    ```
6. Run the following command in your IDE terminal to create your database tables: `python3 manage.py migrate`.
7. Create a superuser account by running `python3 manage.py createsuperuser` and enter details as prompted.

#### Setting up Stripe
1. Login or sign up to [Stripe](https://stripe.com/)
2. Navigate to your Dashboard and click the **Developers** button at the top of the page.
3. Click the **API Keys** heading to reveal your keys.
3. Copy your Publishable key and Secret key and save them in your `env.py` file in the following format:
    ```python
    os.environ['STRIPE_PUBLIC_KEY'] = '<publishable-key>'
    os.environ['STRIPE_SECRET_KEY'] = '<secret-key>'
    ```
    ensuring you replace `<publishable-key>` and `<secret-key>` with the respective keys you copied above.
4. Click the **Webhooks** heading and click **Add Endpoint** on the right-hand side of the screen.
5. Paste in the URL of your local website and append the address with `checkout/wh/`.
6. Under **Select events to listen to**, tick **Select all events**.
7. At the bottom of this list, click **Add Endpoint**.
8. On your new webhook's page, click **Reveal** under Signing secret at the top of the page and copy the key.
9. In `env.py`, add this key using the following format:
    ```python
    os.environ['STRIPE_WH_SECRET'] = '<signing-secret>'
    ```
    where `<signing-secret>` is the key you just copied.
10. Note that you will need to set your local port to public for Stripe to correctly process all webhook events.

#### Setting up reCAPTCHA
1. Navigate to the [reCAPTCHA](https://www.google.com/recaptcha/about/) website and click **Get Started with Enterprise** at the top of the page.
2. Enter a name for your project, click **Get Started**, and wait for the site to set up your account.
3. Click **Cloud Console**, enter a display name for your site, and select "website" as your platform type.
4. Enter your website domain and click done.
5. Click the blue dropdown arrow and enable the **Use checkbox challenge** key.
6. Click **Create Key**.
7. Copy the ID at the top of the page. This is your reCAPTCHA public key.
8. Click **USE LEGACY KEY** on the right-hand side of the page and copy the key. This is your reCAPTCHA private key.
9. Add these keys to your `env.py` file in the following format:
    ```python
    os.environ['RECAPTCHA_PUBLIC_KEY'] = '<public-key>'
    os.environ['RECAPTCHA_PRIVATE_KEY'] = '<private-key>'
    ```
    ensuring you replace `<public-key>` and `<private-key>` with your reCAPTCHA public and private keys respectively.

#### Setting up Email Functionality
1. Login or sign up to [Google](https://accounts.google.com/)
2. Go to your account settings and navigate to the **Security** tab.
3. Enable 2-Step Verification and follow the onscreen instructions.
4. In the search bar at the top of the page, enter "app passwords" and click on the result of the same name.
5. Follow the on-screen instructions until you see the "App name" input field.
6. Enter an appropriate app name and click **Create**.
7. Copy the app password that is shown on your screen.
8. In your `env.py` file, add the following lines:
    ```python
    os.environ['EMAIL_HOST_USER'] = '<your-email>'
    os.environ['EMAIL_HOST_PASS'] = '<your-app-password>'
    ```
    where `<your-email>` is the email address you used and `<your-app-password>` is the password you copied in step 7.

### Live Deployment
To deploy this project yourself on Heroku, please follow the following additional steps:

#### Storing Static files and images.
**Part I**
1. Login or sign up to [Amazon Web Services](https://aws.amazon.com/).
2. Go to the **S3** service and create a new bucket.
3. Enter a bucket name and region and enable ACLS. Tick "Bucket owner preferred" under **Object Ownership**.
4. Click **Create Bucket**.
5. Click the name of your new bucket and navigate to the properties tab.
6. Scroll to the bottom and under **Static website hosting**, tick "Use this bucket to host a website", and click save.
7. On the **Permissions** tab, paste the following code into the CORS section:
    ```json
    [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
    ]
    ```
8. Copy the ARN at the top of the permissions tabs.
9. On the **Bucket Policy** tab, create a new policy with the generator:
    - Type of Policy: S3 Bucket Policy
    - Principal: *
    - Actions: Get Object
    - ARN: paste in the copied ARN from step 8
10. Click **Generate Policy** and copy the result.
11. Paste the code into the bucket policy window and add `/*` at the end of the **Resource** key.
12. Click **Save** and navigate to the **Acess Control List** tab.
13. Click edit and enable **List** for "Everyone (public access), accepting the warning message that appears.

**Part II**
1. Navigate to the IAM service on your Dashboard.
2. Click **Create Group** in the sidebar and give it an appropriate name before clicking **Next Step** until you can see the **Create Group** button. Click **Create Group**.
3. Go to the **Create Policy** page and on the JSON tab, click **Import managed policy**.
4. Find "AmazonS3FullAccess" in the list of options and import it.
5. Update the Resource key in the following format:
    ```json
    "Resource": [
        "<arn-string>",
        "<arn-string>/*"
    ]
    ```
    where `<arn-string>` is the copied ARN from above.
6. Click Review Policy and enter an appropriate name and description before clicking Create Policy.
7. Attach this policy to the Group you created above via the **User Groups** permissions tab.
8. Click **Users** in the sidebar and click **Add User**.
9. Enter an appropriate name and enable programmatic access.
10. Add the user to the user group you created earlier and click next until you are able to click **Create User**.
11. From the Users tabs, click the user you just created and go to the **Security Credentials** tab.
12. Scroll to **Access Keys** and click **Create access key**.
13. Select **Application running outside AWS** and click the next button.
14. Click **Create Access Key** and download the .csv file on the resulting page.

**Part III**
1. In your `settings.py` file, update the values of `AWS_STORAGE_BUCKET_NAME` and `AWS_S3_REGION_NAME` with the values from step 3 in Part I.
2. Download the contents of the `/media/` directory to your computer.
3. Go your S3 Bucket overview tab and click **Create folder**.
4. Name the folder "media" and click save.
5. Select the images to upload, grant public read access, and click upload.

#### Heroku
1. Login or sign up to [Heroku](https://www.heroku.com/).
2. Create a new app with a unique name in a region close to you.
3. In the Settings tab under Config Vars, add the following keys from your `env.py` with their respective values:
    - `DATABASE_URL`
    - `SECRET_KEY`
    - `STRIPE_PUBLIC_KEY`
    - `STRIPE_SECRET_KEY`
    - `EMAIL_HOST_USER`
    - `EMAIL_HOST_PASS`
    - `RECAPTCHA_PUBLIC_KEY`
    - `RECAPTCHA_PRIVATE_KEY`
5. Add the below AWS-related keys in the same way. The access key and secret key are in the .csv file you downloaded in Part II, Step 14.
    - `AWS_ACCESS_KEY_ID`
    - `AWS_SECRET_ACCESS_KEY`
    - `USE_AWS:` with a value of `True`
4. Confirm that the `Procfile` is present in your directory.
5. Set Debug to False in `settings.py` and commit and push your code to your GitHub repository.
6. In the Deploy tab on Heroku, connect your GitHub repo and manually deploy the **main** branch.
7. Add the deployed web address to the list of allowed hosts in your `settings.py` file and commit and push your code.
7. Follow steps 4-8 of [Setting Up Stripe](#setting-up-stripe) to create a new webhook using the domain name of your deployed website.
8. Add the `STRIPE_WH_SECRET` key to your Heroku Config Vars with the new signing secret as its value.
9. Manually deploy your **main** brach again. 
7. Click **View App** to open your deployed website.

## Testing
All documentation on the testing of this application can be found in the [TESTING.md](/TESTING.md) file.

## Credits
### Content
ChatGPT was used to generate most of the text content in the homepage, about page, and service descriptions which was then edited by Simon Henleywillis.

ChatGPT was used to generate large JSON files of users and their reviews to quickly populate the database.

### Media
The business logo was created on [FreeLogoDesign](https://freelogodesign.org). The website states that "[w]hether you use the free or the paid version (high-resolution plan), you are free to use your logo for promotional purposes without having to credit FreeLogoDesign."

All images used were found on [Pexels](https://www.pexels.com/). The Pexels website states that "*All photos and videos on Pexels can be downloaded and used for free*".
Images were resized and cropped where necessary.

- Hero image: [Two Red Flowers on Stairs](https://www.pexels.com/photo/two-red-flowers-on-stairs-68470/)
- Homepage images: [A Man Mowing the Green Lawn](https://www.pexels.com/photo/a-man-mowing-the-green-lawn-12087398/), [Man in green jacket holding a green leaf](https://www.pexels.com/photo/man-in-green-jacket-holding-a-green-leaf-3782994/)
- About page images:  [Man in Green Coat Holding Tablet](https://www.pexels.com/photo/man-in-green-coat-holding-tablet-3781942/), [Adult Man Wearing Green Jacket Holding a Tablet ](https://www.pexels.com/photo/adult-man-wearing-green-jacket-holding-a-tablet-3781932/)
- Grass-cutting Service: [A Person Using a Lawn Mower](https://www.pexels.com/photo/a-person-using-a-lawn-mower-6728919/)
- Weed Service: [A Group of Dandelions in a Field](https://unsplash.com/photos/a-group-of-dandelions-in-a-field-lYWEUytAj6s)
- Tree service: [A Firefighter Cutting a Tree with a Chainsaw](https://www.pexels.com/photo/a-firefighter-cutting-a-tree-with-a-chainsaw-7812853/)
- Hedge service: [Man Cutting a Hedge With a Trimmer in the Garden](https://www.pexels.com/photo/man-cutting-a-hedge-with-a-trimmer-in-the-garden-24595769/)
- Flowerbed service: [Photo of Assorted Color Flowers at Daytime](https://www.pexels.com/photo/photo-of-assorted-color-flowers-at-daytime-1039129/)
- Tree Stump service: [A Close-Up Shot of a Tree Stump](https://www.pexels.com/photo/a-close-up-shot-of-a-tree-stump-10814837/)


### Code Used
**All code in this project was written entirely by Simon Henleywillis unless otherwise specified below.**

Various Bootstrap classes and components were used in the styling of this website and were learned about from reading the Bootstrap documentation. Chunks of code that were copied or adapted are specifically credited below. 

The Boutique Ado walkthrough was used as guidance when creating this project. Where code is directly copied from Boutique Ado without any significant editing or additions on my part, it is credited below.

**Feature** | **Source**
--- | ---
Articles used as guidance when creating the CustomUser model | [Learn Django - Django Custom User Model](https://learndjango.com/tutorials/django-custom-user-model) <br> [Medium.com - Custom User Model In Django](https://medium.com/django-unleashed/custom-user-model-in-django-98b9a401a6a2#4826) <br> [Django documentation - Customizing authentication in Django](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#a-full-example)
The UserAccount model and form | Adapted from the UserProfile model and form in the Boutique Ado walkthrough
The Category model | Taken from the Boutique Ado walkthrough
The Services app's `views.py` file | Taken from the Boutique Ado walkthrough with minor adjustments made.
The Checkout app's `views.py` file | Adapted from the Boutique Ado walkthrough with **major** adjustments.
Service star ratings | The HTML and CSS for the stars were copied from this [Codepen.io workspace](https://codepen.io/mcallaro88/pen/EWQdRX)
The JavaScript code to control the decrement and increment of the number input field on the service pages | Taken from the Boutique Ado walkthrough
The Order model | Adapted from the Boutique Ado walkthrough
The OrderLineItem model | Adapted from the Boutique Ado walkthrough
The Stripe Webhook handler | Adapted from the Boutique Ado walkthrough with major additions made.
The `webhooks.py` file | Taken from the Boutique Ado walkthrough.
The `stripe_elements.js` file | Taken from the Boutique Ado walkthrough and updated with some original code.
The Cart app's `contexts.py` file | Taken from the Boutique Ado walkthrough and adapted to work with my Service model structure.
The HTML, CSS, and JavaScript code for the scroll to top button on the cart page | Taken from this tutorial: [MDB - Scroll back to top button](https://mdbootstrap.com/docs/standard/extended/back-to-top/)
Disabling the checkout form buttons dynamically | [StackOverflow - Disabling submit button until all fields have values](https://stackoverflow.com/questions/5614399/disabling-submit-button-until-all-fields-have-values)
The `checkout.css` file | The contents of this extra CSS file were copied from the Boutique Ado walkthrough
The HTML structure of the toast messages | Adapted from examples in this [Fastbootstrap article](https://fastbootstrap.com/components/toast/).
The Offcanvas cart preview | The HTML code was copied from the [Bootsrap documentation](https://getbootstrap.com/docs/5.0/components/offcanvas/)
Pagination of reviews | Taken from the [Django documentation](https://docs.djangoproject.com/en/5.1/topics/pagination/).
The JavaScript code to control the colour of the select field in the Contact Us form | Taken and adapted from the Boutique Ado walkthrough
Form label for reCAPTCHA field| Line of code copied from a comment on this [GitHub post](https://github.com/google/recaptcha/issues/421)


## Acknowledgements
- [Creating Your First README - Kera Cudmore](https://github.com/kera-cudmore/readme-examples)
- I would like to thank my CI Mentor [Graeme Taylor](https://github.com/G-Taylor), for his encouragement and advice over the last 12 months of this course.
- To my partner Luiza, thank you for encouraging me to face new challenges and supporting me every step of the way. I could not have achieved all that I have without your love and support.