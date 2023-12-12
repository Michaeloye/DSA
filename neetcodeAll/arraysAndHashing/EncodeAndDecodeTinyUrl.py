# https://leetcode.com/problems/encode-and-decode-tinyurl/

import random


class Codec:
    def __init__(self):
        self.domainMap = {}
        self.routeMap = {}

    def generateRandomString(self, length=5):
        # ASCII values for lowercase letters
        lowercaseLetters = [chr(i) for i in range(97, 123)]
        allLetters = lowercaseLetters

        random_string = ''
        for _ in range(length):
            random_string += random.choice(allLetters)

        return random_string

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        protocol = ""
        if "https://" in longUrl:
            protocol = "https://"
            longUrl = longUrl.replace("https://", "", 1)
        elif "http://" in longUrl:
            protocol = "http://"
            longUrl = longUrl.replace("http://", "", 1)

        longUrlParts = longUrl.split("/")
        domain = longUrlParts[0]
        self.domainMap["tinyurl.com"] = domain
        path = ""
        randomStr = self.generateRandomString()

        if len(longUrlParts) > 1:
            path = "/".join(longUrlParts[1:])
            self.routeMap[randomStr] = path

        return f"{protocol}tinyurl.com/{randomStr}"
        # return f"{protocol}tinyurl.com" if not path else f"{protocol}tinyurl.com/{randomStr}"

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        protocol = ""
        if "https://" in shortUrl:
            protocol = "https://"
            shortUrl = shortUrl.replace("https://", "", 1)
        elif "http://" in shortUrl:
            protocol = "http://"
            shortUrl = shortUrl.replace("http://", "", 1)
        route = shortUrl.split("/")[1]

        return f"{protocol}{self.domainMap['tinyurl.com']}/{self.routeMap[route]}"


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
