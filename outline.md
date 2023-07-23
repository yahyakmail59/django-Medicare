Home page:
    slider:
        - image
        - title
        - sub-title

    BOOK APPOITMENT: 
        - name
        - phone_number
        - email
        - Appointment booking time
        - note

        opening our (edit in frontend)

                
list BOOK APPOITMENT Page:
    - table return all data in DB from BOOK APPOITMENT

    DEPARTMENT:
        - image
        - name
        - description
        - Gallary
    - TREATMENTS
        - name
        - price
        - image
        - descriptions
        - QUANTITY
        - category (forign from shop)
        - Gallary


        reviews:
            - writer review
            - title
            - review content

            ADD YOUR REVIEW:
                - title
                - message
            
            RELATED PRODUCTS


    

Doctor:
    - image
    - name
    - DEPARTMENT Image (forign key)
    - DEPARTMENT (category)
    - Degrees
    - day_of_week (VARCHAR): Represents the day of the week (e.g., "Monday," "Tuesday," etc.)
    - opening_time (TIME): Represents the opening time of the day
    - closing_time (TIME): Represents the closing time of the day
    - description
    - CONTACT
        - Address
        - phone_number
        - email

      DOCTOR DETAILS page
slider_doctor:
    - image
    - name
    - DEPARTMENT Image (forign key)
    - DEPARTMENT

SERVICES:
    - name
    - DEPARTMENT Image (forign key)
    - description
    - Doctor image (forign)


    SERVICES-detail page
    scroll infinite

review:  (same TESTIMONIALS)
    - Review writer
    - disease name
    - description

slider review:
    - Review writer
    - disease name
    - description

FAQ'S: # fronend edit

blog:
    - post image
    - published at
    - title
    - auther
    - content
    - category
    - TAGS


    BLOG LIST Page
    BLOG GRID page
    SINGLE POST page
        - ADD YOUR COMMENT Form [comment, writer_name, email, website]

    post comment
    prevous post and next post
    search
    LATEST POSTS
    comment counter
    filters [CATEGORY, RECENT POSTS, Time, TAGS]

CONTACT US:
    - name
    - phone_number
    - email
    - note

GALLERY:
    - DEPARTMENT (forign)
    - images
    filter DEPARTMENT Gallary by DEPARTMENT

shop:
    - CATEGORIES
    - TREATMENTS
        - name
        - price
        - image
        - descriptions
        - QUANTITY
        - category
        - Gallary

    search
    filters [CATEGORIES, PRICE, BEST SELLERS, ]
    add to cart


cart:
    - PRODUCT
    - product image
    - price
    - QUANTITY
    - TOTAL
    - cart total
        - Subtotal
        - total
        
        proceed to checkout

    add coupon
    remove from cart

CHECK OUT:
    - user


    BILLING DETAILS Form
        - First name
        - last name
        - phone
        - email
        - Company name
        - Country
        - Address
        - Town/City
        - Postcode/zip
        - Order Notes


        create account
        PAYMENT METHOD
        place order
        

    home app:
        slider:
            - image
            - title
            - sub-title
           
        BOOK APPOITMENT form: 
            - name
            - phone_number
            - email
            - Appointment booking Date
            - note

        DEPARTMENT:
            - image
            - name
            - description

        Doctor:
            - image
            - name
            - DEPARTMENT Image (forign key)
            - DEPARTMENT (category)

        SERVICES:
            - name
            - DEPARTMENT Image (forign key)
            - description

        slider CUSTOMERS SAY:
            - Review writer
            - disease name
            - description
            - petiont image

        LATEST POSTS:
            - title
            - published at
            - image
