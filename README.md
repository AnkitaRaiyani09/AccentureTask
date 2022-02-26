# AccentureTask

This project includes 4 test cases.

I have used python unit test cause it's feasible for small number of test case and with python one can easily 
create test case without much worrying about syntax.

Scenario 1 : test_1broken_image
https://the-internet.herokuapp.com/broken_images
Evaluate the broken images out of all images and assert the result.

Scenarios 2 (Basic Auth) : test_2basic_auth
https://the-internet.herokuapp.com/basic_auth
Perform login
Basic Auth (user and pass: admin)

Scenario 3 : test_3slider
https://the-internet.herokuapp.com/horizontal_slider
Move slider to max and assert the number Move slider to min value and check the number

Scenario 4 : test_4hover_user
https://the-internet.herokuapp.com/hovers
Hover on the pictures and assert the details like User

I have added test.log file which shows logs after running test cases. For a driver and selenium related debugging 
there's a driver.log file.

To run these test cases just hit "python3 -m unittest TestCase/AccentureTestCase.py" command in terminal from the 
location where project is located.