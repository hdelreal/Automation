Steps for running TestExercises:

I used Selenium with Python, in which I followed this next rules:
    - I created methods to do specific jobs.
        -TestExercise1.py: Web page is open. Web browser is in full screen.
            TO RUN: Uncomment last code line. Open a command line in
            directory in which this file is stored and type python TestExercise1.py

        -TestExercise2.py: Uses some functions to add items to shopping cart 
        Also, searches for items to add to shopping cart.
            TO RUN: Uncomment last code line. Open a command line in
            directory in which this file is stored, comment last code line of the previous Test
            and type python TestExercise2.py (this test calls TestExercise1 to run)

        -TestExercise3: Looks at shopping cart and check items are added to
        it. Also takes a screenshot to visualize shopping cart
            TO RUN: Uncomment last code line. Open a command line in
            directory in which this file is stored, comment last code line of the previous Tests
            and type python TestExercise3.py  (this test calls previous TestExercises)

        -TestExercise4: Deletes an item from shopping cart and takes a screenshot.
            TO RUN: Uncomment last code line. Open a command line in
            directory in which this file is stored, comment last code line of the previous Tests
            and type python TestExercise4.py (this test calls previous TestExercises)

I used methods in python as libraries because if we need to call a specific task
it is needed just to call the method

These methods are commented to let know every step taken in the process.

I used selectors like:
    - WebDriver: Firefox WebDriver was used to make this tasks possible
    - Find_element_by...: in which we can locate specific fields in HTML field
    - Pyautogui library: To move mouse pointer
    - Time library: to make some delays in the tasks process

Selenium with python is an easy language to use. We don't need to specify every step
in code. But, might be a disadvantage because it is no compiled
