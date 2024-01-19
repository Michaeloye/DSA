# https://leetcode.com/problems/text-justification/

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        subStrs = []
        subStr = words[0]

        for i in range(1, len(words)):
            if len(subStr) + 1 + len(words[i]) > maxWidth:
                subStrs.append(subStr)
                subStr = words[i]
            else:
                subStr += " " + words[i] if i != 0 else words[i]

        # add last substr after loop ends
        subStrs.append(subStr)

        for idx, sentence in enumerate(subStrs):
            words = sentence.split(" ")
            spaceToAdd = maxWidth - len(sentence)
            formattedSentence = ""

            availableSlots = sentence.count(" ")
            if spaceToAdd == 0:
                continue

            share = spaceToAdd // availableSlots if availableSlots != 0 else 0
            extraShare = spaceToAdd % availableSlots if availableSlots != 0 else 0

            if idx == len(subStrs) - 1:
                subStrs[idx] = sentence + " " * spaceToAdd
                continue

            if spaceToAdd < availableSlots:
                for i, word in enumerate(words):
                    if extraShare > 0:
                        spacing = " " * 1
                        extraShare -= 1
                        formattedSentence += word + " " + \
                            spacing if (i != len(words) - 1) else word
                    else:
                        formattedSentence += word + \
                            " " if (i != len(words) - 1) else word

            else:
                for i, word in enumerate(words):
                    spacing = " " * share
                    trailingSpacing = " " * extraShare
                    extraShare = 0
                    if len(words) == 1:
                        formattedSentence += word + " " * spaceToAdd
                    else:
                        formattedSentence += word + " " + spacing + \
                            trailingSpacing if (i != len(words) - 1) else word
            subStrs[idx] = formattedSentence

        return subStrs
