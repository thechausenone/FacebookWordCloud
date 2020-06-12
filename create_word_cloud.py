'''
Takes a txt and outputs a word cloud
'''

import matplotlib.pyplot as plt # Import matplotlib for rendering
from wordcloud import WordCloud, STOPWORDS # import wordcloud userful things


class createWordCloud:
    def __init__(self, inputFileName, outputFileName):
        self.stopwords = self.__setStopWords()
        self.masterString = self.__initialiseMasterString()
        self.messageContentFile = self.__openMessageContent(outputFileName)
        self.__populateMasterString()
        self.__generateWorldCloud(outputFileName)

    def __setStopWords(self):
        words = STOPWORDS
        custom = []

        # Source: https://www.ranks.nl/stopwords   
        with open('./filtered_words.txt') as f:
            custom = f.read().splitlines()
        words.update(set(custom))

        return words

    def __openMessageContent(self, messageContentFileName):
        # Open message content for reading
        filename = open(messageContentFileName + '.txt', 'r', encoding="utf-8")
        return filename

    def __initialiseMasterString(self):
        # Create master string
        return ''

    def __populateMasterString(self):
        # Go through every line in file and append line to master string
        tempString = ""
        for line in self.messageContentFile:
            tempString = tempString + ' ' + line
        tempString = self.__reduceWhiteSpace(tempString)
        self.masterString = tempString.lower()

    def __reduceWhiteSpace(self, myString):
        # Fix to reduce white space
        return ' '.join(myString.split())

    def __generateWorldCloud(self, outputFileName):
        # Set wordcloud parameters
        # (trying to get suitable for A4 paper)
        wc = WordCloud(background_color='white',
                            stopwords=self.stopwords,
                            width=1000, height=595, #pixels
                            mask=None,
                            max_words=1000,
                            max_font_size=40, 
                            random_state=42)
        # Generate the wordcloud using the above parameters and the master string
        wc.generate(self.masterString)

        # Set the size of the figure (again trying to get suitable for a4 paper)
        fig = plt.figure(figsize=(14, 9))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.figure()
        fig.savefig(outputFileName, dpi=100,
                    papertype='a4', orientation='portrait')
