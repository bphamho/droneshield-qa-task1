### BUG 1: Locked Out User
**Priority:** High

**Severirty:** Major

- **Environment:** Mac OS Sonoma
- **Browser:** Chrome
- **Application Version:** 130.0.6723.117

**Steps to Reproduce:**
1. Attempt to log into account using user locked_out_user and password secret_sauce

**Expected Result:**
The user should be able to log in.

**Actual Result:**
An error message appears saying the user has been locked out.

### BUG 2: Add to cart/Remove from cart functionality not working correctly for some users
**Priority:** High

**Severirty:** Major

- **Environment:** Mac OS Sonoma
- **Browser:** Chrome
- **Application Version:** 130.0.6723.117

**Steps to Reproduce:**
1. Log in with account problem_user or error_user
2. Attempt to add items to cart
3. Attempt to remove items from cart

**Expected Result:**
Items should be added to cart

**Actual Result:**
Some "Add to Cart" and "Remove" buttons do not function properly and remain the same.

### BUG 3: Add to cart functionality not working correctly for some users
**Priority:** High

**Severirty:** Major

- **Environment:** Mac OS Sonoma
- **Browser:** Chrome
- **Application Version:** 130.0.6723.117

**Steps to Reproduce:**
1. Log in with account problem_user or error_user
2. Attemp to add items to cart

**Expected Result:**
Items should be added to cart

**Actual Result:**
Some "Add to Cart" buttons do not function properly and remain the same.

### BUG 4: Empty cart checkout

**Priority:** High

**Severirty:** Major

- **Environment:** Mac OS Sonoma
- **Browser:** Chrome
- **Application Version:** 130.0.6723.117

**Steps to Reproduce:**
1. Log into account
2. Navigate to cart (with no items in cart)
3. Press checkout
4. Enter in details
5. Press Continue
6. Press Finish

**Expected Result:**
The user should not be able to checkout with an empty cart.

**Actual Result:**
The user is able to reach the order confirmation screen even though no items was added to the cart.

### BUG 5: Checkout Information Page not functioning correctly
**Priority:** High

**Severirty:** Major

- **Environment:** Mac OS Sonoma
- **Browser:** Chrome
- **Application Version:** 130.0.6723.117

**Steps to Reproduce:**
1. Log in with account problem_user or error_user
2. Add items to cart
3. Go to cart
4. Press Checkout
5. Enter in details

**Expected Result:**
The First Name, Last Name and Zip/Post Code text fields should be populated when text is entered in.

**Actual Result:**
The Last Name text field does not populate when entering in text.

### BUG 6: Sorting by name
**Priority:** High

**Severirty:** Major

- **Environment:** Mac OS Sonoma
- **Browser:** Chrome
- **Application Version:** 130.0.6723.117

**Steps to Reproduce:**
1. Log in with account problem_user, error_user or visual_user
2. Use sorting functionality

**Expected Result:**
Sorting should work as described i.e. sort produces alphabetically when selecting Name (A to Z).

**Actual Result:**

problem_user:
The sorting functionality does nothing when an option is selected.

error_user:
The browser produces an error that "Sorting is broken!".

visual_user:
When sorting by price, the prices aren't sorted in the correct order (due to a bug that will be described in BUG 7)

### BUG 7: Visual bugs
**Priority:** High

**Severirty:** Major

- **Environment:** Mac OS Sonoma
- **Browser:** Chrome
- **Application Version:** 130.0.6723.117

**Steps to Reproduce:**
1. Log in with account visual_error or problem_user
2. Observe pricing and image visuals

**Expected Result:**
The price should be correct and the images should be correct.

**Actual Result:**

problem_user: The images displayed for all products are that of a dog instead of the actual items

visual_user: 
1. The prices for each item change on page reload but when in the cart/checkout the prices are correct. 
2. The incorrect image is used for the Backpack
3. The "Add to cart" button for the last product is misalligned
4. The cart button on the top right is misalligned
5. When in the cart, the "Checkout" button is misalligned

### BUG 8: Perforamnce Issues
**Priority:** High

**Severirty:** Major

- **Environment:** Mac OS Sonoma
- **Browser:** Chrome
- **Application Version:** 130.0.6723.117

**Steps to Reproduce:**
1. Log in with account performance_user
2. Interact with web application and observe load times

**Expected Result:**
When adding to cart it should be instant and loading pages should also be near instant.

**Actual Result:**
There is lag/latency when interacting with elements of the web application.