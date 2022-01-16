import mechanize


def _login_auth(url: str):
    # Browser
    br = mechanize.Browser()

    # Browser options
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    br.addheaders = [('User-agent', 'Chrome')]

    # The site we will navigate into, handling it's session
    br.open('https://account.mekari.com/users/sign_in')

    # View available forms
    login_form = br.select_form(id="new_user")

    # User credentials
    br.form['user[email]'] = 'test4@gmail.com'  # Enter your username
    br.form['user[password]'] = 'Test1234'      # Enter your password

    # Login
    br.submit()

    rs = br.open(url).read()


    return rs
