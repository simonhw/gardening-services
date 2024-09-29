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
- LOCAL [about.html](static/images/readme/w3c-about.png) - Passed with no errors or warnings. Trailing slash in self-closing `<img/>` element is flagged as having no effect.
- LOCAL [account.html](static/images/readme/w3c-account.png) - Passed with no errors or warnings.
- LOCAL [privacy.html](static/images/readme/w3c-privacy.png) - Passed with no errors or warnings.
- LOCAL [cart.html](static/images/readme/w3c-cart.png) - Passed with no errors or warnings. Trailing slash in self-closing `<img/>` element is flagged as having no effect.
- LOCAL [checkout.html](static/images/readme/w3c-checkout.png) - Passed with no errors or warnings. Trailing slash in self-closing `<img/>` element is flagged as having no effect.
- LOCAL [checkout_success.html](static/images/readme/w3c-checkout-success.png) - Passed with no errors or warnings.
- LOCAL [contact_us.html](static/images/readme/w3c-contact_us.png) - This page had one warning and one error, both of which are due to third-party lines of code that are rendered by the reCAPTCHA library. The warning states that having a type attribute in its JavaScript `<script>` tag is unessecary. The error states that the attribute `required` is not allowed on the checkbox div rendered by reCAPTCHA. Attempts were made using JavaScript to remove the attribute on page load, as the field is set as required on the backend already; however, the third-party library still rendered the element with the `required` attribute. Even with this error, the form works as intended with no bugs present. For the purposes of this application, and espcially considering the error is due to third-party code that can't be easily edited, this page is considered as having **passed with no errors**. A trailing slash in a self-closing `<img/>` element is flagged as having no effect.
- LOCAL [subscribe.html](static/images/readme/w3c-subscribe.png) - Passed with no errors or warnings. Trailing slash in self-closing `<img/>` element is flagged as having no effect.
- LOCAL [index.html](static/images/readme/w3c-index.png) - Passed with no errors or warnings. Trailing slash in self-closing `<img/>` element is flagged as having no effect.
- LOCAL [create_review.html](static/images/readme/w3c-create_review.png) - Passed with no errors or warnings. Trailing slash in self-closing `<img/>` element is flagged as having no effect.


- [style.css](static/images/readme/w3c-css.png) - No errors found.

#### JavaScript
<!-- - [booking.js](static/images/readme/jshint-booking.png) - No warnings found. -->
<!-- - [user_booking.js](static/images/readme/jshint-userbookings.png) - No warnings found. -->

#### Python
<details><summary>.py - No errors</summary>

![](static/images/readme)

</details>

#### Accessibility Testing
The WAVE tool was used to assess the website for any errors or issues associated with accessibility. The results and comments for each page are as follows:

##### Index Page
No errors were detected.

![WAVE results for index.html](static/images/readme/wave-index.png)

##### About Page
No errors were detected.

![WAVE results for about.html](static/images/readme/wave-about.png)

#### Lighthouse Testing
##### Home Page

Desktop test:

![Lighthouse test for index.html - desktop](static/images/readme/lighthouse-index-desktop.png)

Mobile test:

![Lighthouse test for index.html - mobile](static/images/readme/lighthouse-index-mobile.png)

##### About Page
Desktop and mobile tests for about.html were all very good with scores ranging from 80 to 100.

Desktop test:

![Lighthouse test for about.html - desktop](static/images/readme/lighthouse-about-desktop.png)

Mobile test:

![Lighthouse test for about.html - mobile](static/images/readme/lighthouse-about-mobile.png)

## Bugs
### Known Bugs
| # | Bug | Image | Plan to Solve |
| --- | --- | --- | --- |

### Solved Bugs
| # | Bug | Image | Solution |
| --- | --- | --- | --- |

<br>

Back to [README.md](/README.md)