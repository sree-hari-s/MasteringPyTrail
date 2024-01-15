# WTForms

## Advantages of forms using a Flask extension called Flask-WTF

It has a number of benefits over the simple HTML form:

- Easy Form Validation - Makes sure the user is entering data in the required format in all the required fields. e.g. checking that the user's email entry has a "@" and a "." at the end. All without having to write your own validation code.
- Less Code - If you have a number of forms in your website, using WTForm can dramatically reduce the amount of code you have to write (or copy & paste).
- Built in CSRF Protection - CSRF stands for Cross Site Request Forgery, it's an attack that can be made on website forms which forces your users to do unintended actions (e.g. transfer money to a stranger) or compromise your website's security if it's an admin.

## Installation

To install a particular package you can use the Terminal. To install `Flask-WTF`` you would use the pip install command.

```cmd
pip install Flask-WTF
```
