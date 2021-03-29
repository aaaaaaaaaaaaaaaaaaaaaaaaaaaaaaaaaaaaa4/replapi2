from bs4 import BeautifulSoup
import repltalk, asyncio, random, json, requests


class info():
    def version():
        print("VERSION: 0.0.1")

    def owners():
        print("Made by ch1ck3n. Idea by some people. lol")


async def replit_cycle_get(name=None):
    if (name == None):
        exit("Please fill out the name parameter!")
    else:
        try:
            client = repltalk.Client()
            user = await client.get_user(name)
            return user.cycles
        except:
            exit(f"ERROR: Cannot load {name}'s cycles!")


class UserInfo:
    def __init__(self, username):
        self.username = username
        if requests.get("https://replit.com/data/profiles/" + username).text:
            exit("User not found")
        self.json = json.loads(
            requests.get("https://replit.com/data/profiles/" + username).text)

    def user_pic(self):
        """gets the URL for the picture of the user"""
        if self.username == "PythonMaster_24":
            return "https://www.gravatar.com/avatar/ff92a08aae577ceafbdab92bf029ae90"
        r = self.json
        try:
            if (r["icon"] == None):
                return "https://repl.it/public/images/evalbot/evalbot_" + str(
                    random.randint(17, 43)) + ".png"
            return r["icon"]["url"]
        except:
            return "https://repl.it/public/images/evalbot/evalbot_" + str(
                random.randint(17, 43)) + ".png"

    def full_name(self):
        return self.json["firstName"] + " " + self.json["lastName"]

    def repls(self):
        return self.json["repls"]

    def email(self):
        # This is hashed!
        return self.json["emailHash"]

    def bio(self):
        return self.json["bio"]

    def top_languages(self):
        return self.json["topLanguages"]

    def hacker(self):
        return self.json["hacker"]

    def organization(self):
        return self.json["organization"]

    def replit_cycles(self):
        name = self.username
        # 69th line poggers
        try:
            e = asyncio.run(replit_cycle_get(f"{name}"))
            return e
        except:
            exit("ERROR: Cannot find " + name + "'s cycles!")
    def replit_comments(self):
      name = self.username
      try:
        post = requests.get("https://replit.com/@" + name + "?tab=comments")
        soup = BeautifulSoup(post.content, 'html.parser')
        all_text = []
        for data in soup.find_all("p"):
          all_text.append(data.get_text())
        return '\n'.join(all_text)
      except:
        exit("ERROR: Cannot find "+name+"'s comments!")
