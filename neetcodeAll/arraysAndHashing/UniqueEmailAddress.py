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
