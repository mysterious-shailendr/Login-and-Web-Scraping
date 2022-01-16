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
    br.open('https://account.mekari.com/users/sign_in?client_id=JUR-7645867921&return_to=L2F1dGg_Y2xpZW50X2lkPUpVUi03NjQ1ODY3OTIxJnJlc3BvbnNlX3R5cGU9Y29kZSZzY29wZT1zc286cHJvZmlsZQ%3D%3D')

    # View available forms
    login_form = br.select_form(id="new_user")

    # User credentials
    br.form['user[email]'] = 'shailendrshrivastav1234@gmail.com'
    br.form['user[password]'] = 'Login1234#'

    # Login
    br.submit()

    rs = br.open(url).read()


    return rs