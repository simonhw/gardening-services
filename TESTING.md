# The Garden Path - Testing

Deployed program on Heroku: [The Garden Path](https://gardening-services-e596b6371c3f.herokuapp.com/)

![GitHub last commit](https://img.shields.io/github/last-commit/simonhw/gardening-services)
![GitHub contributors](https://img.shields.io/github/contributors/simonhw/gardening-services)

## Contents
- [Form Validation](#form-validation)
    - []()
- [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Full Testing](#full-testing)
    - [Automated Testing](#automated-testing)
- [Bugs](#bugs)
    - [Known Bugs](#known-bugs)
    - [Solved Bugs](#solved-bugs)

## Form Validation
Validating the data to be submitted by the user is done both on the back and front end. 

### Full Testing
The program was deployed on Heroku and tested there on a Windows 10 desktop with a 26" monitor and on a One Plus 9 Pro mobile phone.

The site was tested on Google Chrome, Mozilla Firefox, and Edge on desktop, DuckDuckGo on mobile, and using Chrome Developer Tools for some other screen sizes.

**Feature**|**Expected Outcome**|**Test Performed**|**Results**|**Test Status**
-----|-----|-----|-----|-----
**All Pages**| | | | 
**Home Page**| | | | 
**About Page**| | | | 

### Automated Testing
#### HTML and CSS
The W3C validator sites were used to validate the [HTML](https://validator.w3.org/) and [CSS](https://jigsaw.w3.org/css-validator/) files. [JSHint](https://jshint.com/) was used to validate the JavaScript files.

HTML Page | Passed with no Errors or Warnings? | Comments
:--- | :---: | :---
LOCAL [about.html](static/images/testing/w3c-about.png) | &check; | Trailing slash in self-closing `<img/>` element is flagged as having no effect.
LOCAL [account.html](static/images/testing/w3c-account.png) | &check; |
LOCAL [privacy.html](static/images/testing/w3c-privacy.png) | &check; |
LOCAL [cart.html](static/images/testing/w3c-cart.png) | &check; | Trailing slash in self-closing `<img/>` element is flagged as having no effect.
LOCAL [checkout.html](static/images/testing/w3c-checkout.png) | &check; | Trailing slash in self-closing `<img/>` element is flagged as having no effect.
LOCAL [checkout_success.html](static/images/testing/w3c-checkout-success.png) | &check; |
LOCAL [contact_us.html](static/images/testing/w3c-contact_us.png) | &check;* | This page had one warning and one error, both of which are due to third-party lines of code that are rendered by the reCAPTCHA library. The warning states that having a type attribute in its JavaScript `<script>` tag is unessecary. The error states that the attribute `required` is not allowed on the checkbox div rendered by reCAPTCHA. Attempts were made using JavaScript to remove the attribute on page load, as the field is set as required on the backend already; however, the third-party library still rendered the element with the `required` attribute. Even with this error, the form works as intended with no bugs present. For the purposes of this application, and espcially considering the error is due to third-party code that can't be easily edited, this page is considered as having **passed with no errors**. A trailing slash in a self-closing `<img/>` element is flagged as having no effect.
LOCAL [subscribe.html](static/images/testing/w3c-subscribe.png) | &check; | Trailing slash in self-closing `<img/>` element is flagged as having no effect.
LOCAL [index.html](static/images/testing/w3c-index.png) | &check; | Trailing slash in self-closing `<img/>` element is flagged as having no effect.
LOCAL [create_review.html](static/images/testing/w3c-create_review.png) | &check; | Trailing slash in self-closing `<img/>` element is flagged as having no effect.
LOCAL [reviews.html](static/images/testing/w3c-reviews.png) | &check; | Trailing slash in self-closing `<img/>` element is flagged as having no effect.
LOCAL [unpublished_reviews.html](static/images/testing/w3c-unpublished_reviews.png) | &check; |
LOCAL [service_page.html](static/images/testing/w3c-service_page.png) | &check; | Trailing slash in self-closing `<input/>` element is flagged as having no effect.
LOCAL [services.html](static/images/testing/w3c-services.png) | &check; | Trailing slash in self-closing `<img/>` element is flagged as having no effect.
LOCAL [403.html](static/images/testing/w3c-403.png) | &check; |
| &check; |LOCAL [404.html](static/images/testing/w3c-404.png) | &check; |
NOT TESTED YET!!! [500.html](static/images/testing/w3c-500.png) | | 
Toast messages and Offcanvas | &check; | Toast messages and the Offcanvas element were triggered and validation of the HTML code was done by direct input e.g. a success toast after adding items to the cart.
LOCAL [login.html](static/images/testing/w3c-login.png) | &check; |
LOCAL [signup.html](static/images/testing/w3c-signup.png) | &check; |
LOCAL [logout.html](static/images/testing/w3c-logout.png) | &check; |
[password_reset.html](static/images/testing/w3c-password-reset.png) | &check; | Validated by direct input
[password_reset_done.html](static/images/testing/w3c-password-reset-done.png) | &check; | Validated by direct input
[password_reset_from_key.html](static/images/testing/w3c-password-reset-from-key.png) | &check; | Validated by direct input
[password_reset_from_key_done.html](static/images/testing/w3c-password-reset-from-key-done.png) | &check; | Validated by direct input
[verification_sent.html](static/images/testing/w3c-verification-sent.png) | &check; | Validated by direct input
[email_confirm.html](static/images/testing/w3c-email-confirm.png) | &check; | Validated by direct input

CSS File | Passed with no Errors or Warnings? | Comments
:--- | :---: | :---
LOCAL [style.css](static/images/testing/w3c-css.png) | &check; | ????
LOCAL [accounts.css](static/images/testing/w3c-css-accounts.png) | &check; |
LOCAL [cart.css](static/images/testing/w3c-css-cart.png) | &check; |
LOCAL [checkout.css](static/images/testing/w3c-css-checkout.png) | &check; |
LOCAL [contact.css](static/images/testing/w3c-css-contact.png) | &check; |
LOCAL [reviews.css](static/images/testing/w3c-css-reviews.png) | &check; |

#### JavaScript
JavaScript File | Passed with no Errors or Warnings? | Comments
:--- | :---: | :---
[cart.js](static/images/testing/jshint-cart.png) | &check; |
[cart_numbers.js](static/images/testing/jshint-cart-numbers.png) | &check; |
[cart_preview.js](static/images/testing/jshint-cart-preview.png) | &check; | One variable flagged as undefined: `bootstrap`. This variable is defined in the `bootstrap.bundle.min.js` script which is called before `cart_preview.js` thus allowing the function to work as intended.
[checkout_form.js](static/images/testing/jshint-checkout-form.png) | &check; |
[contact_us.js](static/images/testing/jshint-contact-us.png) | &check; |
[delete_buttons.js](static/images/testing/jshint-delete-buttons.png) | &check; |
[number_inputs.js](static/images/testing/jshint-number-inputs.png) | &check; |
[review_stars.js](static/images/testing/jshint-review-stars.png) | &check; |
[service_form.js](static/images/testing/jshint-service-form.png) | &check; |
[star_ratings.js](static/images/testing/jshint-star-ratings.png) | &check; |
[stripe_elements.js](static/images/testing/jshint-stripe-elements.png) | &check; | One variable flagged as undefined: `Stripe`. This variable is defined in `<script src="https://js.stripe.com/v3/"></script>` which is called before `stripe_elements.js` allowing it to be used correctly.

#### Python
Flake8 was used to check original Python code to ensure compliance with PEP8 standards. This was done by navigating to each Django app in turn and running `python3 -m flake8` in workspace terminal. Any issues were then listed in the terminal along with the filename and location within the file. When no issues remain, the terminal did not print any output.

Flake8 flagged E501 errors in migrations files for lines longer than 79 characters. These files are automatically generated and editing them could result in migration errors. These errors were therefore ignored in this context and no corrections were made to the files.

<details><summary>The Gardening app - Acceptable errors</summary>

There were two different types of errors flagged in the `settings.py` file:
- The first was flagging `env` as being imported but not used. This is because the linter is looking for the word `env` being called elsewhere in the file and not finding it; however, this is an acceptable error as the file is still using the imported data but calling it via `os.environ.get`.
- The second related to lines longer than 79 characters in the `ALLOWED_ORIGINS` and `AUTH_PASSWORD_VALIDATORS` blocks. There was no realistic way of splitting these lines in two and not breaking the functionality of the website; therefore, these errors flagged by the linter were deemed acceptable to have.
    - PEP8 [allows for this](https://peps.python.org/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds):
    "However, know when to be inconsistent – sometimes style guide recommendations just aren't applicable. When in doubt, use your best judgment. Look at other examples and decide what looks best. And don't hesitate to ask! ... ... Some other good reasons to ignore a particular guideline:
    When applying the guideline would make the code less readable, even for someone who is used to reading code that follows this PEP."

![Flake8 command run in the gardening directory](static/images/testing/flake8-gardening.png)

</details>

<details><summary>The About app - No errors</summary>

![Flake8 command run in the about directory](static/images/testing/flake8-about.png)

</details>

<details><summary>The Accounts app - No errors</summary>

![Flake8 command run in the accounts directory](static/images/testing/flake8-about.png)

</details>

<details><summary>The Cart app - No errors</summary>

![Flake8 command run in the cart directory](static/images/testing/flake8-cart.png)

</details>

<details><summary>The Checkout app - No true errors</summary>

In `apps.py`, Flake8 flags `checkout.signals` as being imported but never used. This is due to the linter seeing this file in isolation and not understanding the purpose of the import. It is included so that Django is aware of the signals module and the update listeners contained within.

![Flake8 command run in the checkout directory](static/images/testing/flake8-checkout.png)

</details>

<details><summary>The Reviews app - No errors</summary>

![Flake8 command run in the reviews directory](static/images/testing/flake8-reviews.png)

</details>

#### Accessibility Testing
The WAVE tool was used to assess the website for any errors or issues associated with accessibility. The results and comments for each page are as follows:

##### Index Page
No errors were detected.

![WAVE results for index.html](static/images/testing/wave-index.png)

##### About Page
No errors were detected.

![WAVE results for about.html](static/images/testing/wave-about.png)

#### Lighthouse Testing
##### Home Page

Desktop test:

![Lighthouse test for index.html - desktop](static/images/testing/lighthouse-index-desktop.png)

Mobile test:

![Lighthouse test for index.html - mobile](static/images/testing/lighthouse-index-mobile.png)

##### About Page
Desktop and mobile tests for about.html were all very good with scores ranging from 80 to 100.

Desktop test:

![Lighthouse test for about.html - desktop](static/images/testing/lighthouse-about-desktop.png)

Mobile test:

![Lighthouse test for about.html - mobile](static/images/testing/lighthouse-about-mobile.png)

## Bugs
### Known Bugs
| # | Bug | Image | Plan to Solve |
| --- | --- | --- | --- |

### Solved Bugs
| # | Bug | Image | Solution |
| --- | --- | --- | --- |

<br>

Back to [README.md](/README.md)