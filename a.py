from webbot import Browser
web = Browser()
web.go_to('google.com')
web.click('Sign in')
web.type('mymail@gmail.com', into='Email')
web.click('NEXT', tag='span')
web.type('mypassword', into='Password',
         id='passwordFieldId')  # specific selection
web.click('NEXT', tag='span')  # you are logged in ^_^
