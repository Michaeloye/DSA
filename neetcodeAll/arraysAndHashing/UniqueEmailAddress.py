# https://leetcode.com/problems/unique-email-addresses

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        validEmails = set()

        for email in emails:
            splitEmail = email.split("@")
            localName = splitEmail[0]
            domainName = splitEmail[1]

            localName = localName.split("+")[0]
            localName = localName.replace(".", "")

            parsedEmail = f"{localName}@{domainName}"

            validEmails.add(parsedEmail)

        return len(validEmails)


# Another solution

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def isValidEmail(email):
            splitEmail = email.split("@")
            localName = splitEmail[0]
            domainName = splitEmail[1]

            verifiedLocalName = ""

            for i in localName:
                if i == '+':
                    break
                if i != '.':
                    verifiedLocalName += i
            verifiedEmail = f"{verifiedLocalName}@{domainName}"
            return verifiedEmail

        validEmails = set()

        for i in emails:

            if isValidEmail(i):
                validEmails.add(isValidEmail(i))

        return len(validEmails)
