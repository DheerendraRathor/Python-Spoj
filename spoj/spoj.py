__author__ = 'dheerendra'

import mechanize
import utils
import urls
import click

class Spoj():

    @staticmethod
    def verify_credentials(username, password):
        cj = mechanize.MozillaCookieJar()
        br = mechanize.Browser()
        br.set_cookiejar(cj)
        br = utils.setup_browser(br)
        try:
            br.open(urls.BASE_URL)
            try:
                br.select_form(name='login')
                br['login_user'] = username
                br['password'] = password
                br.find_control(name='autologin').items[0].selected = True
            except mechanize.FormNotFoundError:
                click.echo('Error occurred. Code VC-FNFE. Kindly contact developer')
                return False
            except NameError:
                click.echo('Error occurred. Code VC-NE. Kindly contact developer')
                return False
            except mechanize.ControlNotFoundError:
                click.echo('Error occurred. Code VC-CNFE. Kindly contact developer')
                return False
            br.submit()
            for link in br.links():
                if link.text == 'my account':
                    utils.save_cookies(cj)
                    click.echo('Account Verified!')
                    return True
            click.echo('Wrong Username/Password. Try Again')
            return False
        except mechanize.URLError:
            click.echo('Error in connecting to internet')
            return False




