# <p align="center"> The Dog Shop: Milestone Project 4

![Responsive Designs](static/images/readme_images/readme-image-main.png)

### <p align="center">The image above is a visual of the site displayed on different devices using [I Am Responsive](http://ami.responsivedesign.is/#)

### <p align="center">You can view the live site here: [www.the-dog-shop.com](https://the-dog-shop.herokuapp.com//)

--- 

# <p align="center"> Introduction

Welcome to The Dog Shop - a dedicated store for site users to purchase dog related products. The site also has a dedicated blog section where our dog experts post relevant articles related to dog’s health and wellbeing. Site users can interact with blog posts by adding comments on posts and interacting with other site users. The store is of course fictional and for educational purposes only. 

I built this e-commerce site for my 4th and final milestone project he Code Institutes Full Stack Software Development Course. The overall goal of the project was to design, build and launch a full stack django based software app, that allows users to create an account, be authenticated, store and manipulate data, and purchase products using the stripe payment platform. Due to the nature of the site, additional authentication and validation protocols have been used to prevent unintended use of the site.  

--- 

# Contents

- [**User Experience (UX)**](#ux)
  - [User Stories](#user-stories)
  - [Strategy](#strategy)
    - [_External user’s goal_](#external-user’s-goal)
    - [_Site owner's goal_](#external-user’s-goal)
  - [Scope](#scope)
    - [_Scope In_](#scope-in)
    - [_Scope Out_](#scope-out)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
    - [_Wireframes_](#mobile-wireframes)
  - [Surface](#surface)
    - [_Design_](#design)
    - [_Colour_](#colour)
    - [_Typography_](#typography)
- [**Data Set Up**](#data-set-up)
    - [_Database Design_](#cdata-base-design)
- [**Features**](#features)
  - [_Existing Features_](#existing-features)
  - [_Features Left to Implement_](#features-left-to-implement)
- [**Technologies Used**](#technologies-used)
  - [_Languages_](#languages)
  - [_Frameworks & Libraries_](#frameworks-and-libraries)
- [**Testing**](#testing)
- [**Version Control Management**](#version-control-management)
- [**Deployment**](#deployment)
  - [_Deployment Steps_](#deployment-steps)
  - [_How To run this Project Locally_](#how-to-run-this-project-locally)
- [**Credits**](#credits)
  - [_Content_](#content)
  - [_Media_](#media)
  - [_Code_](#code)
- [**Resources**](#resources)
- [**Acknowledgements**](#acknowledgements)

---

# <p align="center"> UX

### User Stories

|   As A       |  I want to be able to...                                |   So that I can...                                       |
| :----------  | :-------------------------------------------------------|----------------------------------------------------------|
| Site User    | Navigate through the site easily                        | Purchase quickly and efficiently                         |
| Site User    | View individual products details                        | Decide if the product is what I need                     |
| Site User    | Search for products on the site                         | Find what I need quickly                                 |
| Site User    | Understand why I need to create and account             | Make a decision on where to share my personal details    |
| Site User    | Make a purchase without having to create an account     | Do not need to share my personal details                 |
| Site User    | Create an account                                       | Save my personal information                             |
| Site User    | Create an account                                       | Comment on and share opinions on recent blog posts       |
| Site User    | Receive email confirmation when creating an account     | Have confirmation that it was successful                 |
| Site User    | Reset my password                                       | Access my account if I forget my password                |
| Site User    | Have a personal profile page                            | View my order history                                    |
| Site User    | Select quantity of individual products                  | Purchase the right quantity I require                    |
| Site User    | Be able to delete any personal comments posted          | Full control over my content                             |
| Site User    | Be notified when I add a product to my shopping bag     | I can easily see what I am buying                        |
| Site User    | See the total cost of my purchase before paying         | Know how my will be charged to be debit/credit card      |
| Site User    | See a payment success or failure message                | Verify that my purchase has been successful              |
| Site User    | Receive a confirmation email after making a purchase    | Have a receipt and record of my purchase                 |
| Site Owner   | Add products to the store from the front end            | Quickly add new products to the site                     |
| Site Owner   | Edit products on the front end                          | Update products details on the site                      |
| Site Owner   | Delete products from the front end                      | Remove products from the site                            |
| Site Owner   | Add blog posts to the site                              | Share relevant information and engage with the site user |
| Site Owner   | Edit blog posts on the site                             | Update the content easily                                |
| Site Owner   | Save draft blog posts in my profile                     | Access and finish at a later time before posting to the site |
| Site Owner   | View all saved draft blog posts in my admin profile     | Easily see all unpublished blog posts                    |
| Site Owner   | Delete blog posts from site                             | Remove content from the site                             |
| Site Owner   | Delete site user comments                               | So that I can remove comments that are not appropriate   |

--- 

## Strategy

### External user’s goal

> - Easily navigate a consumer website to find the products that I’m interested in. 
> - Creating an account should be seamless and not require too much personal information or questions. 
> - Checking out should be simple and easy to understand, I should know exactly what is in my basket and how much I am going to pay. 
> - Adding comments and interacting with blog posts should be simple, and I should have control over my content by being able to delete posts whenever I decide to do so. 


### Site owner's goal

> - Create a site that provides specific information to a targeted audience. 
> - Create a site that allows site users to easily navigate products, having the ability to search and sort different product types and view individual product details - price, ratings etc. 
> - Create a site that allows users to create an account, enabling them to store their information for quicker checkout. 
> - reate a site that is user friendly and visually indicates when the user has actioned a specific event - like a pop up when adding a product to their shopping bag.
> - Share content to engage site users. Allows users to read and interact with relevant content (Blog Posts) by having the ability to post comments / share opinions on individual articles. 
> -  Create a business revenue stream by targeting a specific market with relevant products.


## Scope

### Scope In

- A homepage that instantly and visually demonstrates what the site’s overall purpose is.
- A one page home page that provides a link to the site product page.
- A nav bar that provides easy navigation to different product ranges. 
- A search bar within the navbar throughout the site to allow users to quickly find relevant products. 
- Product page that visually shows price, ratings and an image. 
- Product details page that shows individual product information with quantity selector. 
- Sorting functionality to allow the site user to sort by price, rating, name or category. 
- Shopping bag icon in the navbar throughout the site, with visual indication of the users total spend. 
- My account section that allows customers to create an account, as well as logging in and out of existing accounts. 
- Dedicate profile page where site users can save their delivery information and view their order history. 
- Active email receipts for account creation verification, password reset, and purchase receipts. 
- Dedicated Blog Page that allows the site owner to post, edit and delete content. 
- Comments structure that allows site users to comment on individual blog posts when signed into their account.
- Site owner ability to add, edit and remove products from the store.
- Site owner admin privileges to remove site user comments.
- Site owner only ability to add, edit and delete blog posts.
- Site owner ability to save draft blog posts in their user profile.
- Stripe payments integration.

### Scope out

- Ability to create an account or sign in using social media accounts.
- Ability to add ratings to products.
- Ability for site users to add blog posts (Only Site Owner's can past blogs).
- Mandatory account creation - account creation only required to save personal information, shopping bag items between sessions or post comments to published blog posts. 
- Site user ability to reply directly to other site user comments. 
- Ability to like, up, or downvote other site user comments. 
- Ability for users to Edit comments (future feature).
- Ability to save payment information. 
- Ability to use google, android or alternative payment payment methods. 
- Requirement for site owners to approve site users comments before being published. 

--- 

## Structure

The structure of the site will be a simplistic flow that navigates the user through the site easily, with the intended purpose of purchasing products. Product information will be displayed clearly with just the right amount of information to allow the user to continue moving forward through the user flow. Account creation and sign in/out will be quick and effortless. 

### Home Page
> - The main page of the site will visually demonstrate the site's purpose so that when a user lands on the home page, there is no confusion as to what the site is. 
> - A link will be placed directly in the middle of the page with a clear call to action of ‘SHOP NOW’, allowing the customer to go straight to the products page. 

### Search Bar
> - Allows the user to search for products, enabling quicker identification of specific requirements. 

### My Account
> - A drop down nav bar that allows the site user to register or sign into their account, access their personalised profile page or log out of their account. 
> - When in a non-logged state, only a Register and Login link will display. 
> - When logged in and authenticated, a ‘Profile and Logout link will display. 
> - If the site user is a superuser or admin user, additional links will appear to that user group privileges which will be a Product Admin link and a Blog Admin Link.

### Shopping bag
> - A shopping bag icon will be present in the navbar which will add up the value of any products added to the user's bag throughout their shopping journey. This allows the users to visually see the total spend as the shop.

### Navigation links
> - Several product specific navigational links will be displayed to allow the user to navigate quickly to specific product ranges. 

### Call to action banner
> - Underneath the main navigation link, a call to action banner will be displayed to encourage the user to increase their spend, currently this will be free delivery, but in future could also be used for initiatives like discount codes or shipping information. 

### Main Products page
> - All products displayed on this page. Users will be able to sort by Price, Rating, Name or Category. 

### Individual Products page
> - Page specific to a product a user clicked on. This page will display the product details, including Price, Category and Rating. 
> - A quantity selector allows the user to increase or decrease the quantity of the product they wish to buy. 
> - If the product comes in a range of sizes, a size selector drop down will appear. 
> - A Continue Shopping button will allow the user to return to the product page. 
> - An Add to bag button will allow the user to add the product to their shopping bag. 

### Shopping bag toast pop up:
When an item is added to the Shopping Bag, a pop up appears to visually show the user their shopping bag details. This includes:
> - Success message
> - Total items in Shopping Bag
> - Total cost inc/exc delivery
> - Amount of additional spend required to obtain free delivery. 
> - Secure Checkout Button

### Shopping Bag
When the ‘Secure Checkout’ button is clicked, the user will be navigated to their shopping bag. This page will contain:
> - Product info and image
> - Total Price of each individual product
> - Quantity selector to allow users to update the quantity of each item in their bag. 
> - Total cost
> - Delivery Cost
> - Grand Total Cost
> - If a user has not spent enough to qualify for free shopping, a message will display advising how much additional spend is required.
> - A ‘Continue Shopping’ button to allow users to go back to the main products page. 
> - A ‘Secure Checkout’ button which will take the user to the main Check Out Page. 

### Check Out Page
> - A simple checkout page where the user will see their order summary and a checkout form for entering their delivery details. 
> - A call to action will be displayed to encourage the user to create and account or sign in to save their information. 
> - If a user is logged in, and information has been saved previously, the delivery details stored will be pre filled, allowing the user to checkout quicker. 
> - A payment section, allowing the user to add their payment method.
> - A message will appear to demonstrate once again how much the user will be charged.

### Checkout Success Page
> - When payment is successful, a checkout success page will display, showing the user their order confirmation number, order summary and delivery information. 
> - A link to allow the user to return to the main products page. 
> - Upon successful completion of an order, the user will be sent a confirmation e-mail containing their order number and order details. 

### User Profile Page
> - Personalised profile page where users can store their delivery information. 
> - If a user is logged in when making a purchase, their order details will be stored and displayed in their profile page order history section - this contains order number and summary of items purchased. 
> - If the user is a superuser or Admin (Site Owner), their profile page will also contain any unpublished blogs. These blogs can be edited and posted live on the site from within this page.
 
### Blog Management
> - Allows Site Owners to create draft blog posts and either post directly onto the site or save for later. 
> - Draft (unpublished) blog posts will be saved to the Site Owners profile page. 

### Product Management
> - Allows Site Owners to add products directly to the store. 
> - Store owners will also be able to edit and delete products on the main products page and the individual product page. 


### Blog Page
> - Dedicated blog page which will be used for presenting market specific content. 
> - Users can access blogs and information on this page. 

### Comments Section 
> - A comments section will be contained within individual blog post pages, allowing the user to add comments and opinions to posted blog posts. 
> - Users will be able post and delete their own comments. 
> - Superusers (Site Owners) will be able to delete all comments without restriction.

### Footer 
> - A simple fixed footer that contains links to the company social media accounts. The footer will only be present on larger screens and will not be visible on mobile devices to improve the mobile shopping experience.  

--- 

## Skeleton

- The website has been designed to allow the user to navigate through the journey effortlessly. 
- The My Account section within the nav bar is designed to display relevant to whether the user is logged into the site or not. 
- The user will flow through the shopping journey from product selection through to payment. 
- The user will be able to create an account easily so that they can save/update their information and review order history in a dedicated profile page.
- Once logged in, the user will also be able to comment on blog posts. They will have the ability to delete comments, but not edit. 
- If user logs out, they will be asked to confirm before being navigated to the home page. 
- If the user logs out, their shopping bag session will end and bag contents set to zero. 

### Wireframes

All wireframes were created using [Balsamic](https://balsamiq.com/).

The wireframes for both mobil and desktop can be found below.

- [Mobile Wireframes](https://github.com/scotty-james/the-dog-shop--MS4/blob/main/static/docs/wireframes_mobile.pdf)
- [Desktop Wireframes](https://github.com/scotty-james/the-dog-shop--MS4/blob/main/static/docs/wireframes_desktop.pdf)

--- 

## Surface

### Design

The website’s primary purpose in an ecommerce site and as such the the design of the store has been simplistic without any distraction. The main page has only one call to action which is a SHOP NOW button. 

The product page is dedicated to products and relevant product information. Customers can navigate back and forth from their shopping bag however the main goal is to seamlessly navigate the customer through to the checkout page in as little clicks as possible. The footer is simple and provides links to the site's social media platforms. 

A dedicated blog page provides relevant content and allows the user to interact by being able to post comments to individual blog posts. The blog section is accessed via a link in the nav bar, but otherwise is not promoted throughout the customer journey. 

### Colour

The color scheme is very simple in nature to align with the crisp design of the site, three colours have been used throughout - white, blue & yellow. 
- #0b2f47
- #4ba5cd
- #f2cc59

![Colour Palette](static/images/readme_images/colour-palette.png)

### Typography

In line with the website's simple and clean design, Only one font has been used throughout - Montserrat! 

![Google Fonts](static/images/readme_images/readme-googlefont.png)

--- 

# <p align="center"> Features

## Existing Features

- My Account link that only displays links to sing in or register when in a non logged in state. 
- A shopping bag in the navbar that displays total spend as the user adds products to their bag. Total spend increase/decreases as the user adds/removes products from their bag. 
- One clear CTA on the main page. 
- A sign up page that allows new users to create an account, which will allow the user to interact with the site
- A sign in page that will allow existing members to sign into their account in order to interact with the site
- Clear messaging to warn the user of specific actions - for example, advising the customer that a user name already exists if they try to create an account using a username that has already been taken.
- Clear messaging to warn the customer when they enter the wrong username and/or password when signing in
- Clear messaging to advise the customer that they have successfully created an account, logged out or logged in. 
User authentication. 
- Email verification requirements to ensure user and site security. Users are sent a link to their email address to verify identity. 
- Ability to reset password. 
All forms have validation to ensure the user enters the required parameters in each form throughout the site.
- A quantity selector button to allow users to increase or decrease products before adding to their shopping bag. 
- A quantity selector in the shopping bag page to allow users to adjust and update the items in their bag. 
- Sort selector in the products page, allowing users to sort products. 
- Search bar in the navbar to allow users quick access to their required products. 
- Pop up Modal when a user adds an item to their bag, providing visual indication of event along with the product added, total items currently in bag and total spend so far. 
- Free delivery messaging within the pop up modal with exact amount of spend required to qualify for free delivery - if shopping spend currently has not reached free delivery threshold. 
Order summary including product image displayed on checkout page. 
- Ability for users to create an account or sign in when on the checkout page - in order to save their information. 
- Messaging underneath the payment section showing total cost being charged to the card. 
- Personalised checkout success page showing order number, confirmation and order summary. 
- Email receipt of order sent to users e-mail address, containing order number, confirmation and order summary. 
- Personalised profile page showing full order history - if user purchases while logged in. 
- Privilege level user group access, including super user only access to Product Management and Blog Management of the site. 
- Site user ability to add comments to individual blog posts when logged into their account. 
- Site user ability to delete their own individual comments when signed into their account. 
- Site user ability to add and update their personal information within their personalised profile page. 
- Superuser ability to add, edit and delete products on the site. 
- Superuser ability to add, edit and delete blog posts on the site. 
- Superuser ability to save unpublished blog posts to their profile section, enabling them to edit and publish at a later date. 
- Ability to add images to products and blog posts.
- Superuser ability to delete all user comments. 
- Defensive programming techniques used to prevent unintended actions - for example, any features that can be deleted will trigger a warning modal asking the user to reconfirm their intent. 
- Superuser privilege only actions locked down to improve security and avoid malicious activity - for example, any user attempting to by manually navigate to a superuser only page will be displayed with a warning message that they do not have the required access. 

## Features Left to Implement

- Adding site user comments history to their personal profile page. 
- Ability for users to edit their comments. 
- Ability for users to reply directly to other site user comments to increase interactivity. 
- Ability for users to up/down vote other users' comments and site owner blog posts. 
- Dedicated contact page for users to contact the site owner through additional methods outside the current social media links.  
- A like / helpful button which will allow users to like blog posts. 
- Ability for users to sign up to email newsletters. 
- Admin functionality that will allow admin to moderate comments as the site grows.
- Additional payment methods - like google pay, paypal etc. 
- Ability to save payment information. 
- Stripe discount functionality to enable discount codes. 
- Ability for users to sign in using their social media accounts to allow for a more seamless user experience when signing in or creating accounts. 

--- 

# <p align="center"> Technologies Used

## Languages
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [Python](https://www.python.org/)
* [JQuery](https://jquery.com/)


## Frameworks and Libraries

- [Django](https://www.djangoproject.com/) - was used as the core  web framwork for the site.
- [SQLite 3](https://www.sqlite.org/index.html) - was used for the webapp's databases.
- [Postgres](https://www.postgresql.org/) - was used for database management.
- [Allauth](https://django-allauth.readthedocs.io/en/latest/) - was used for account authentification, registration and management.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - was used for the form redering on the site.
- [Pip3](https://pip.pypa.io/) - was used to install the required packages to run python.
- [DJ Database](https://pypi.org/project/dj-database-url/) - was used for DATABASE_URL management.
- [Stripe](https://stripe.com) - was used for site's payment handling.
- [Heroku](https://www.heroku.com/) - was used to deploy the webapp. 
- [Gunicorn](https://gunicorn.org/) - was used for the python server implementation.
- [Psycopg2](https://pypi.org/project/psycopg2/) - was used as a Postgres python database adapter.
- [django-storages](https://django-storages.readthedocs.io/en/latest/) - used for backend custom storages.
- [RandomKeygen](https://randomkeygen.com/) - Used to generate a random number which was used as the web app's SECRET_KEY.
- [Pillow](https://pillow.readthedocs.io/en/stable/) - was used for image processing on the site.
- [AWS S3](https://aws.amazon.com/s3/) - was used to store static and media files.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - was used to manage the AWS services.
- [Bootstrap4](https://getbootstrap.com/) - was used to build core components of the website, inc the footer and the model structure.
- [Google Fonts](https://fonts.google.com/) - was used to select the text font to be used throughout the site.
- [Font Awesome](https://fontawesome.com/) - was used to display icons throughout the website.
- [Gitpod](https://gitpod.io/) - was used as my IDE.
- [Git](https://git-scm.com/) - was used for version control via VS code by providing regular commits to Git, and pushing to GitHub.
- [GitHub](https://github.com/) - for my Git repository.
- [Balsamic](https://balsamiq.com/) - was used to create the website wireframes.
- [Tinyjpg](https://tinyjpg.com/) - was used for image resizing.
- [Favicon Generator](https://favicon.io/favicon-converter/) - was used for generating the site favicon.
- [PEP8](http://pep8online.com/) - was used to validate the code for the website. 
- [JS Hint](https://jshint.com/) - was used to validate the javascript code within the website. 
- [Jigsaw](https://jigsaw.w3.org/css-validator/) - was used to vaidate all CSS code. 
- [W3C Markup Validation](https://validator.w3.org/#validate_by_input) - was used to validate the HTML within the code base. 
 
--- 

# <p align="center">Testing

### W3C Validation

The following pages were passed through the official W3C validation site with no errors returning:

- index.html: No errors or warnings to show.
- products.html: No errors or warnings to show.
- product_detail.html: No errors or warnings to show.
- checkout.html: No errors or warnings to show.
- checkout-success.html: No errors or warnings to show.
- blog.html: No errors or warnings to show.
- blog_detail.html: No errors or warnings to show.

![HTML Validator Results](static/images/readme_images/html_validator.png)

- base.css: Congratulations! No Error Found.

![Duplicate ID Error](static/images/readme_images/css_validator.png)

Blog and Product editing pages:
- Edit-post.html
- Edit_product.html

Site validation on both these pages failed due to a Duplicate ID error:  

![Duplicate ID Error](static/images/readme_images/dup-id-image-error.png)

This is explained more in the Fixed Bugs section.

- Bag.html: 

Site validation failed on this page also due a different Duplicate ID error: 

![Duplicate ID Error](static/images/readme_images/dup-id-error-bag.png)

Resolution details contained in the fixed bugs section.


### JSHint

The following files were passed through JSHint with no warnings detected.

- blog_elements.js
- product_elemets.js
- strip_elements.js

stripe_elements.js threw up some errors which were resolved by adding `/*jshint esversion: 6 */` to the top of the file. One additional error remained which was a missing semi collon. 

![JShint Results](static/images/readme_images/js-hint.png)

### PEP8 Python Validator

PEP8 was used to ensure that all Python code meets PEP8 requirements. All .py files in this project were passed through the PEP8 Python Validator successfully. 

### Browser Validation
- In addition to testing on google chrome, I tested the game fully on the Safari and Firefox browsers.
- Firefox: All tests successful.
- Safari: All tests successful.

### Manual Device Check:

I checked the site manually on the following devices - all pages check checked separately.
- Samsung S10
- Iphone X
- Macbook Pro 
- Dell Laptop
- Ipad Pro
- Samasung Tablet
- Monitor Screen 

#### Link And Hover Validation
I went through each page individually to manually check that all links & hover styling worked as intended. This test was performed on both mobile and desktop devices. 

index.html: 
> - First call to action link on the hero image.
> - Nav Bar: All product links.
> - My account when not logged in state: 
>   - Register, 
>   - Log in. 
> - My Account when logged in state: 
>   - Product Admin, 
>   - Blog Admin, 
>   - My Profile, 
>   - Log Out.

Products.html
> - Product image link 
> - Edit product link
> - Delete product modal

Product_detail.html
>  - Quantity selector
>  - Continue shopping link
>  - Add to bag link
>  - Bag Toast Pop Up
>  - Secure checkout link 

Bag.html
>  - Quantity selector
>  - Continue shopping link
>  - Secure checkout link

Checkout.html
> - Adjust bag link 
> - Complete order link 
> - Checkout_success.html: back to store link

Blog.html
> - Readmore link 

Blog_detail.html
> - Edit blog button
> - Delete blog button
> - Submit comment
> - Delete comment 

Product Admin
> - Add Product and image

Blog Admin
> - Add blog and image
> - Save blog and image

### Form Validation

- Sign in form: 
    - Checked on both mobile, ipad and desktop devices. 
    - Submit form without username added to ensure input field ‘required’ attribute was working correctly and alert displayed prompted customer to add input. 
    - Submit form without password added to ensure input field ‘required’ attribute was working correctly and alert displayed prompted customer to add input.

- Sign up form 
    - Checked on both mobile, ipad and desktop devices. 
    - Submit form without email address added to ensure input field ‘required’ attribute was working correctly and alert displayed prompted customer to input email address. 
    - Submit form without name added to ensure input field ‘required’ attribute was working correctly and alert displayed prompted customer to input email address.

- Add Product Form: 
    - Submitted fully filled in product and reviewed on main products page to ensure review displayed as intended. 
    - Tested adding images.
    - Checked Django Admin to ensure data captured correctly

- Add Blog Form: 
    - Submitted fully filled in blog post and reviewed on blog page to ensure new blog displayed as intended. 
    - Checked Django Admin to ensure data captured correctly
    - Tested adding images.

- Edit Product Form: 
    - Submitted fully filled in product edit and reviewed on product page to ensure new product displayed as intended. 
    - Tested adding new images.
    - Checked Django Admin to ensure data captured correctly

- Edit blog Form: 
    - Submitted fully filled in blog edit and reviewed on blog page to ensure new updated blog displayed as intended. 
    - Tested adding new images.
    - Checked Django Admin to ensure data captured correctly

- Delete Modal: 
  - Fully tested delete model for both product, blog and comments items to ensure modal pop up was presented as intended, and that product/blog/comment was deleted on confirmation. 
  - Checked Django Admin to ensure product/blog removed.

### Additional Manual Testing:
Super user/admin user has access to the:
- Access to the django admin panel.
- Ability to add and edit products on the main products and individual products pages.
- Product admin page to add products directly to store.
- Superuser only profile page which shows unpublished blogs.
- Blog admin page to add blogs directly to store, or create drafts with ability to save for later. 
- Ability to delete all user comments on blog posts

Toast pop ups display when:
- a site user creates and account, signs in or logs out of their account
- a user adds a product to their bag
- a user updates a product in their bag.
- A user updates information in their profile
- A user makes a purchase
- A user adds or deletes a comment
- An Admin edits or deletes a product 
- An Admin edits or deletes a blog post
- A user attempts to access or use an site owner only page
- An Admin deletes a blog post or comment

### Email Validation

Email verification sent succesfull when account created with link tested:

![email verification](static/images/readme_images/email-verification.png)

Email order confirmation sent succesfully after payment succesful with link tested:

![order confirmation email](static/images/readme_images/email-subject.png)

![order confirmation email](static/images/readme_images/email-body.png)

### Image Validation

-   I went through each page to ensure all images displayed correctly. 
-   I went through each file to ensure all Alt Text had been applied correctly to each image url to validate accessibility requirements.
- the image rendered on the edit product/blog form was squashed. I will look to improve this in a future release as this is not displayed on the customer facing part of the site, so less of a priority.

### Site Performance Validation

#### First Test

![Lighthouse Report](static/images/readme_images/lighthouse_image-1.png)

The first report from lighthouse returned poor scores for best practice. Reasons outlined below. 

- Best Practices: Failing elements where:
  - Content Best PracticesFormat your HTML in a way that enables crawlers to better understand your app’s content.
  - Document does not have a meta description

To reseove this I added a meta description tag: `<meta name="description" content="Animal products and services - The Dog Shop"/>`

#### Second Test

With this issues fixed, the site now returns a stronger lighthouse performance score across all key measures:

![Lighthouse Report](static/images/readme_images/lighthouse_image-2.png)

lighthouse perfromance testing was then carried out on all othersite pages. 

### Stripe Testing

I tested Stripe payments by sending test webhooks: All tests successful.

![Stripe Tests](static/images/readme_images/stripe-wh.png)

### User Story Testing

## <p align="center"> AS A SITE USER


> I WANT TO BE ABLE TO: Navigate through the site easily<br>
SO THAT I CAN: Purchase quickly and efficiently<br>

![User-story-1](static/images/readme_images/user-story-1.png)

> I WANT TO BE ABLE TO: View individual products details<br>
SO THAT I CAN: Decide if the product is what I need<br>

![User-story-2](static/images/readme_images/user-story-2.png)

> I WANT TO BE ABLE TO: Search for products on the site <br>
SO THAT I CAN: Find what I need quickly <br>

![User-story-3](static/images/readme_images/user-story-3.png)

> I WANT TO BE ABLE TO: Understand why I need to create and account <br>
SO THAT I CAN: Make a decision on where to share my personal details <br>

> I WANT TO BE ABLE TO: Make a purchase without having to create an account <br>
SO THAT I CAN: Do not need to share my personal details <br>

![User-story-4](static/images/readme_images/user-story-4.png)

> I WANT TO BE ABLE TO: Create an account <br>
SO THAT I CAN: Save my personal information<br>

![User-story-5](static/images/readme_images/user-story-5.png)

> I WANT TO BE ABLE TO: Create an account <br>
SO THAT I CAN: Comment on and share opinions on recent blog posts<br>

![User-story-6](static/images/readme_images/user-story-6.png)

> I WANT TO BE ABLE TO: Receive email confirmation when creating an account <br>
SO THAT I CAN: Have confirmation that it was successful<br>

![email verification](static/images/readme_images/email-verification.png)

> I WANT TO BE ABLE TO: Reset my password <br>
SO THAT I CAN: Access my account if I forget my password<br>

![User-story-7](static/images/readme_images/user-story-7.png)

> I WANT TO BE ABLE TO: Have a personal profile page <br>
SO THAT I CAN: View my order history <br>

![User-story-8](static/images/readme_images/user-story-8.png)

> I WANT TO BE ABLE TO: Select quantity of individual products <br>
SO THAT I CAN: Purchase the right quantity I require <br>

![User-story-9](static/images/readme_images/user-story-9.png)

> I WANT TO BE ABLE TO: Be able to delete any personal comments posted <br>
SO THAT I CAN: Full control over my content <br>

![User-story-10](static/images/readme_images/user-story-10.png)

> I WANT TO BE ABLE TO: Be notified when I add a product to my shopping bag <br>
SO THAT I CAN: I can easily see what I am buying<br>

![User-story-12](static/images/readme_images/user-story-12.png)

> I WANT TO BE ABLE TO: See the total cost of my purchase before paying <br>
SO THAT I CAN: Know how my will be charged to be debit/credit card<br>

![User-story-13.1](static/images/readme_images/user-story-13.1.png)
![User-story-13](static/images/readme_images/user-story-13.png)

> I WANT TO BE ABLE TO: See a payment success or failure message<br>
SO THAT I CAN: Verify that my purchase has been successful<br>

![User-story-14](static/images/readme_images/user-story-14.png)

> I WANT TO BE ABLE TO: Receive a confirmation email after making a purchase<br>
SO THAT I CAN: Have a receipt and record of my purchase<br>

![order confirmation email](static/images/readme_images/email-subject.png)

![order confirmation email](static/images/readme_images/email-body.png)

## <p align="center"> AS A SITE OWNER

> I WANT TO BE ABLE TO: Add products to the store from the front end <br>
SO THAT I CAN: Quickly add new products to the site <br>

![User-story-15](static/images/readme_images/user-story-15.png)

> I WANT TO BE ABLE TO: Edit products on the front end <br>
SO THAT I CAN: Update products details on the site <br>

![User-story-16](static/images/readme_images/user-story-16.png)

> I WANT TO BE ABLE TO: Delete products from the front end <br>
SO THAT I CAN: Remove products from the site <br>

![User-story-17](static/images/readme_images/user-story-18.1.png)

> I WANT TO BE ABLE TO: Add blog posts to the site <br>
SO THAT I CAN: Share relevant information with the site user <br>

![User-story-19](static/images/readme_images/user-story-17.png)

> I WANT TO BE ABLE TO: Edit blog posts on the site <br>
SO THAT I CAN: Update the content easily <br>

![User-story-20](static/images/readme_images/user-story-18.png)

> I WANT TO BE ABLE TO: Save draft blog posts in my profile <br>
SO THAT I CAN: Access and finish at a later time before posting to the site <br>

> I WANT TO BE ABLE TO: View all saved draft blog posts in my admin profile <br>
SO THAT I CAN: Easily see all unpublished blog posts<br>

![User-story-4](static/images/readme_images/user-story-19.1.png)
![User-story-4](static/images/readme_images/user-story-19.png)

> I WANT TO BE ABLE TO: Delete blog posts from site<br>
SO THAT I CAN: Remove content from the site <br>

![User-story-4](static/images/readme_images/user-story-20.png)


<br>

## Fixed Bugs
 
### Blog and Product editing pages:
- Edit-post.html
- Edit_product.html

Site validation on both these pages failed due to a Duplicate ID error:  

![Duplicate ID Error](static/images/readme_images/dup-id-image-error.png)

I found this a fairly difficult error to trace back, but after a lot of searching and reading previous comments in the group slack channel, I noticed that the first error was attributed to the fact I had created 2 separate customer_clearable_file_input.html files - one each for the Blog and Product Apps. 

![Duplicate ID Error](static/images/readme_images/custom-file-error.png)

Steps taken to fix:

- Delete the customer widgets template from the blog app - including the customer_clearable_file_input.html file. 
- Delete the widgets.py file from the blog app.
- In the blog app forms.py, import CustomerClearableFileInput from product.widgets.
- This continued to throw the same error. I then changed the file ID name to match the duplicate ID error I was getting to see if this would fix the issue - `new-image` to `id_image`. 
- I changed this in the custom clearable file input file and also the associated JS code. 

This seemed to fix the issue, but another issue was now present where the file input was now displayed as an Input field on the front end. 

![Duplicate Id Error](static/images/readme_images/dup-id-image-error-2.png)

![Duplicate Id Error](static/images/readme_images/dup-id-image-error-2.1.png)

To resolve this, I changed the input type from `id_image` to `‘file’` in the customer clearable input file (`Select Image <input type="file"`) and retested. This then finally resolved the issue and all both edit product and edit post files passed through validation successfully.

![Duplicate Id Error Fix](static/images/readme_images/dup-id-image-fix.png)

### Duplicate ID error on the Shopping Bag Page:

- bag.html

This was another error that really took a bit of time to investigate and understand. The error was coming from the quantity form increment/decrement functionality. The original code for this was taken from the course walk through project ‘Ado Boutique’. The code was originally used in the product details page and adapted for the shopping car to enhance the mobile experience. However, this resulted in the same ID’s being used for different functions. 

Steps taken to fix:
- Created a new include file within the Bag App called quantity_input_script.html 
- Added the code from the same named file (quantity_input_script.html) in the Product App. 
- Analysed the files associated with the script to obtain all ID’s causing the issue, in this case they were:
  - `id="decrement-qty_{{ item.item_id }}`
  - `id="increment-qty_{{ item.item_id }}`
  - `id_qty_{{ item.item_id }}`
  - `id="remove_{{ item.item_id }}`
- Changed these ID’s to Classes and removed the ID attribute. 
Updated the bag/includes/quantity_input_script.html file by changing the itemID attribute to ‘Class’. 
- Changed name of includes directory file to point towards the the Bag App file, rather than the Products App file. 
- This resolved the issu. Passing the page through site validation then returned a successful validation.

![Duplicate Id Error Fix](static/images/readme_images/dup-id-image-fix.png)







