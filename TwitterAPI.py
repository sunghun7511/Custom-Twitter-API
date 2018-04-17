import requests
from bs4 import BeautifulSoup



class Twitter(object):
    def __init__(self, id, pw):
        """Twitter API
         
         Arguments:
             id {str} -- ID for login
             pw {str} -- PW for login
         """
        isLogined = False

        res = requests.get("https://twitter.com/")
        # print(res.text)

        soup = BeautifulSoup(res.text, "html.parser")

        find = soup.find("input", {"name": "authenticity_token"})
        authenticity_token = find.attrs["value"]
        # print(authenticity_token)

        redirect_cookie = res.headers['Set-Cookie']

        headers = {"Cookie": redirect_cookie}
        login_form = {"session[username_or_email]": id,
                        "session[password]": pw, "scribe_log": "",
                        "redirect_after_login": "/?logged_out=1&lang=e",
                        "remember_me": "0",
                        "authenticity_token": authenticity_token,
                        "ui_metrics":"{\"rf\":{\"fa04fe2bad83ca55b9d1185169352b6ce23250cb7cdd0ce0b6e70f6329af58c3\":157,\"a2f49f24ed1a5e51ea6de3752343a0753e6c132fafdb19e3e6fb8c35069c16e0\":2,\"aa80a2adda183397453dc1a6c3165e745f435ea7fea892b17c28499972d38202\":2,\"a0e6fda65a57de6a8ce21d167d361b4685b5d3d950e275adf9bbd063d73a007d\":38},\"s\":\"e4PuqbRjFOKTiqyw3OF1rygaMb6elE0j2sCacvyUkhPJXMiOXg4_2Ay9glqzkGkYWFQgXrTf0S2Ova-_WW1Ldz6Dr6IbewqoxjTyxzC_cYUvI7j0lcVx5feOHv7IWgk7Ms9HpjULJs3xe8Szd73oWqjpv3NF1JQ5WpxQuu4yYrYwSVBRcChgnycBdFqovfCjd6j-vc5GQVsOIqSecAgQGE5p-JWozQFa-XBVLCqdBNRj0XqeGIjaQQ-U2trw-ZL6oWAKpxbETsAYE6oo2rbpfTSyCjujvrAb33-Oc1su9HIuAYxAkX7S7FcEkCR8bqv7VJBhgd7FbB841RjLun012AAAAWLEli3R\"}"}
        # print(login_form)
        res = requests.post("https://twitter.com/sessions", headers=headers,
                            data=login_form, allow_redirects=False)

        print(res.text[:100])
        print(res.status_code)
        print(res.headers)
        self._isLogined = isLogined

    def isLogined(self):
        return self._isLogined

if __name__ == "__main__":
    password = ""

    password_file = open("./password", "r")
    password = password_file.read()
    password_file.close()

    twit = Twitter("K_SH_Group", password)

    if not twit.isLogined():
        print("Login fail..")
        exit()
    
    print("Login success!")