# Brick-Fitness
This is My final Project For The Code Institute curriculum.

I got the idea for this project as i was trying to become a lot healthier as I had terrible eating habits and I wasn't doing any exercise
 I wanted to build this project as a place for people to start a new journey of fitness and health, as I struggled to find the resources
 to get started as you tend to find a lot of conflicting information online.

## Disclaimer Please Do not use any real cards with stripe, PLease use the USA test card
### Card number 4242 4242 4242 4242 and random expiry and cvc code will be accepted
 
## UX
 
My design philosophy for this project was to keep everything simple for the user side of the site. 
I wanted people to visit the site and discover new meals/workout inspiration some elements of the UI are incomplete.

Further updartes to be pushed in the coming weeks


[Wireframes / Mockups!](https://github.com/danielclements/brick-fitness/blob/master/README/brick.pdf)

## Features

### Existing Features
- Authentication
    - User registration allows a user to create an account and buying merch and adding plans
    - User login allows a user to login, when logged in a session is started 
    - User logout will stop the current user's session
    - User Profile is created on user creation

- Purchase merch from the merch store
    - user adds a product to the basket
    - users clicks the cart
    - user clicks checkout
    - user fills out checkout forms
    - redirect to Stripe
    - captures payment intent allowing the purchase to complete
- subscribe to Premium and free  Plans
     - User Navigates to either meal or workout plans view
     - user clicks Activate plan
     - redirect to Profile page showing currently active plan
- Profile page that displays if the User has subscriber to a premium Account
- Ability to Upgrade a user profile to Premium, uses Stripe
- Secure payments with stripe

-The merch store is based on the boutique ado project by code institute
    - Back end code handling
    -some front end pages
    -comments added to pages to annotate code from this project



### Features Left to Implement

- improved UI
- Orders to be displayed in Profile page
- premium users to be able to save progress on plans
- Premium users to be able to upload a custom Profile Picture
- Social Media Like Feed to show off your progress free for all users
- Calorie Tracking Implementation

## Technologies Used

- [HTML 5](https://en.wikipedia.org/wiki/HTML5)
    - The project uses **HTML 5** to write the front end of the website.

- [CSS 3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - This project uses **CSS 3** to style the front end of the website.

- [Javascript](https://www.javascript.com/)
    - Used within bootstrap elements.

- [Python](https://www.python.org/)
    - Python handles all backend code for this site

- [Bootstrap 4](https://getbootstrap.com)
    - This project uses **Bootstrap** to improve scaling to mobile and to add the contact form.

- [Sketch](https://www.sketch.com/)
    - This project uses **Sketch** to create mockups / wireframes, also used to create the background for the Contact page.

### Frameworks Used
- [Django](https://www.djangoproject.com/)
    - Django is a powerful frame work for developers in a hurry

### CDNs Used
- [Google Font](https://fonts.google.com/)

- [Font Awesome](https://fontawesome.com/)

### Python modeules
- [Stripe](https://stripe.com/gb?utm_campaign=paid_brand-UK_en_Search_Brand_Stripe-2032860449&utm_medium=cpc&utm_source=google&ad_content=355351450259&utm_term=stripe&utm_matchtype=e&utm_adposition=&utm_device=c&gclid=Cj0KCQiAzZL-BRDnARIsAPCJs72jjT43ATuUFxfkh3Ful3lgsRWyn6r9NMeaHrOmNWgiWwr1tTcTUQIaArAuEALw_wcB)
- Pillow
- Gunicorn
- Dj_database_url
## Database Schema

![DB Schema](https://raw.githubusercontent.com/danielclements/brick-fitness/master/README/Brick_fitness.png)

### Browsers used for testing:

- [Google Chrome](https://www.google.com/chrome/)
- [Firefox](https://www.mozilla.org/en-GB/firefox/new/)
- [Safari](https://www.apple.com/uk/safari/)
- [Microsoft Edge](https://www.microsoft.com/en-gb/windows/microsoft-edge)

### Devices used for testing:

- MacBook Pro 13"
- Office PC with 28" monitor 
- Office PC with 24" monitor 
- Iphone 11
- Google Chrome dev tools using multiple view ports

### Bugs:
- Mobile views are not fully implemented, as a result some pages only display properly on desktop, this is due to running out of time on the submission date
- User can subscribe to premium plans even if they are not currently a active subscriber
- mealplans sometime fails to render the mail names dropdown box
- google email client doesnt dispay the correct sender name


## Deployment

This project is hosted on heroku [Brick-Fitness](https://brick-fitness.herokuapp.com/)

This python project is dependent on a few packages.

First these need to be installed, we can achieve this with the following command: pip install -r requirements.txt

This project is hosted on heroku, I achieved this by:

1. Going to the heroku dashboard and creating a new app.
2. Then the 'Deploy' section and down to 'deployment method' select github and link heroku to this repository.
3. Create a 'config vars' under the 'setttings' and add the relevent config_vars see below
4. Back to the 'Deploy' tab, continuing down to 'manual deploy' and pressing 'deploy branch'.
5. Link with github to auto deploy on each new git push

The follow config_vars are defined in heroku
  - AWS_ACCESS_KEY_ID
  - AWS_SECRET_ACCESS_KEY
  - DATABASE_URL
  - EMAIL_HOST_PASS
  - EMAIL_HOST_USER
  - SECRET_KEY
  - STRIPE_PUBLIC_KEY
  - STRIPE_SECRET_KEY
  - USE_AWS


### Running Code locally:


1. Using Download:
    1. Navigate to `https://github.com/danielclements/brick-fitness`.
    2. Click the green button that says "Clone or Download".
    3. Click download zip.
    4. Extract zip file.
    5. Import in to preferred IDE.

2. Using Git Clone:
    1. Open terminal in preferred IDE.
    2. Type "git clone https://github.com/danielclements/game_score.gg"
    3. This command will install the dependencies for this project: pip install -r requirements.txt
    4. In the terminal write 'python app.py' to run the application.
    
If running this project locally you will need to add a file call 'env.py', with the following values:
  - DATABASE_URL
  - SECRET_KEY
  - STRIPE_PUBLIC_KEY
  - STRIPE_SECRET_KEY
  - EMAIL_HOST_USER




## Credits


### Media

- Main Background for the section was provided by [Pexels](https://www.pexels.com/)


### Acknowledgements

- Illustrations [undraw](https://undraw.co/illustrations) 

- Background gradients by [Gradient Magic](https://www.gradientmagic.com/)

- Mcolor changing Navbar[StackOverflow](https://stackoverflow.com/questions/23706003/changing-nav-bar-color-after-scrolling)

- Original Locin Page Design[sefyudem](https://github.com/sefyudem/Responsive-Login-Form )

- Message flashing tutorial by []()

- Help with extending user profile and Send/Receive signals [SimpleIsBetter](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)

- Stripe Payment intent creation [Alex Ford](http://www.fordsdevelopment.co.uk/)

- Database Model Queries [Dennis Ivy](https://www.youtube.com/watch?v=PD3YnPSHC-c&t=335s)

