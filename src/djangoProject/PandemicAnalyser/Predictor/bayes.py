from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from PandemicAnalyser.Predictor.modeldata import *




xtest = ["Great day of catching up with dear friends I haven\u2019t seen since b4 these strange crazy pandemic times \ud83d\udc9c\n\n#postpandemictimes \n#jw @ Zelda's Restaurant-Capitola https://t.co/6CGrPCyxFB",
        "The Saddest News Of The Decade...!!!!\ud83e\udd7a\nShri Milkha Singh Just Passed Away At The Age Of 91 Due To Covid 19 ..\ud83d\ude4f\ud83c\udffc\nRIP To The Olympic Hero Of India..\ud83d\ude22\nMay Your Sole Rest In Peace Sir..\ud83d\ude4f\ud83c\udffc\n\n#TheAmateurBong https://t.co/ycetcfdJKN",
        "This some real Bull \ud83d\udca9 don't make me move back to Texas where Vaccine Passports are banned. @ Los Angeles, California https://t.co/XDL7S6vs9Q",
        "So grateful to everyone who made this happen! \ud83d\ude42\ud83d\udc4d\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n#OneAccenture #We4Vaccine #Vaccination #COVID_19 @ Accenture, Magarpatta City, Pune https://t.co/Mz1scHmCsP",
        "You can't see it, but I'm wearing the biggest smile \ud83d\udc89. \n\n#Sinovac #1stDoseDone #COVID19 @ Kuala Lumpur, Malaysia https://t.co/m08GIx70F8",
        "How Covid-19 fucked me up and today I am again at where I was ..lost all muscles, lost the 6 packs abs. #memories2019 \nWish I could go back to being lean and mean.. once again. @ Pune, Maharashtra https://t.co/t50q8smqLh",
        "Fuck COVID-19 \ud83d\udc4a\ud83d\udc4a\ud83d\udc4a\ud83e\uddbe\n\nVaccinated. #covid_19 #fuckcovid19 @ Miami, Florida https://t.co/SSvIZYvol6",
        "My brother and I took my dad out for dinner for the first time since the pandemic started. It was so nice to finally see my dad after a long year. #\u0262\u1d07\u1d1b\u1d20\u1d00\u1d04\u1d04\u026a\u0274\u1d00\u1d1b\u1d07\u1d05 @ Ke'e Grill https://t.co/6e9lOrM3KL",
        "This is crazy.  First COVID now Gas Prices!!! @ Florence, South Carolina https://t.co/hliwmzpVgT",
        "Celebrating being back after another lockdown with this beauty! \ud83e\udde1 @ Emma Frances Hair https://t.co/Easvp9M4Vr",
        "Finally got to hug my Mom after over a year of social distancing! Yay! #ilovemymomanddad @ Roseville, California https://t.co/cel0jJ7vWL",
        "The biggest thing I have missed because of Covid 19. Football with @christopherwilliams308 @ Sutton United F.C. https://t.co/tpSynbfT8F",
        "Gorgeous sunset tonight while out grabbing dinner!! #SoCal #Sunset #Corona @ Subway https://t.co/w81i5MNQeJ",
        "The former guy only cares for himself https://t.co/bly2njXRuL",
        "LOVE THIS!!! #itsallcomingback #itswhatwedo #covid_19 @ Funkbox Productions https://t.co/CofmRJe9xW",
        "Watching these pictures now makes me feel as if it was a hundred years ago. My personal remedy from the lockdown stressed mood. \ud83c\uddeb\ud83c\uddf7 \n#paris #france #theeiffeltower #memories #throwbackmonday (Tour Eiffel): https://t.co/0f7mgPMC4U",
         # FAKE TEST DATA MADE BY ME:
         "This pandemic is such a scam! Down with the government!",
         "I hate these restrictions, I feel like my time is being wasted",
         "Love to see people finding ways to stay connected, we'll get through this together!",
         "So happy to have visited my sister, I hadn't seen her in 3 months. Love you sis",
         "I am disgusted at people not wearing masks, our hospitals are full, do your part!",
         "I hate how Nike charges over 100$ for any popular sneaker",
         "What an awful show keeping up with the Kardashains is... We need better TV",
         "Many Thanks to the @Nike family for the gift. Looking forward to future collaborations with you guys",
         "Proud to be nominated for this award amongst so many other great competitors",
         "Had an mazing experience today at Tayto Park. The rides are so exciting and the kids loved it! I recommended to anyone planning a day out",
         "The food at McDonalds is disgusting... Im never eating there again",
         "Our president is pathetic. We NEED new elections"
         "Our president is the best we have ever had",
         "Life at Riyadh is excellent. Everything is luxurious",
         "Our country is in an awful state",
         "We need more government aid. Our country is in ruins",
         "My greatest success up to has been my resilience. Lets all keep going",
         "Stay strong people! You are tougher than you think",
         "Peace and Love to everyone! Let's unite and be in harmony"
        ]
train = get_train()
test = get_test()

cl = NaiveBayesClassifier(train)

#print("\nOVERALL Naive Bayes Predictor ACCURACY: " + str(cl.accuracy(test)))

# for s in xtest:
#       blob = TextBlob(s)
      #print("BUILT-IN SENTIMENT: " + str(blob.sentiment.polarity))
      #print("BAYES CLASSIFIER: " + str(cl.classify(blob)))

correct = 0
for s in test:
        blob = TextBlob(s[0])
        if blob.sentiment.polarity < 0.0:
                score = 'neg'
        else:
                score = 'pos'

        if score == s[1]:
                correct += 1

accuracy = correct / len(test)
#print("\nOVERALL Built-in Polarity function ACCURACY: " + str(accuracy) + "\n")

def get_nbc_accuracy(): # given a list of training data
        cl = NaiveBayesClassifier(train)
        return cl.accuracy(test)

def get_builtinTextblob_accuracy():
        correct = 0
        for s in test:
                blob = TextBlob(s[0])
                if blob.sentiment.polarity <= 0.0:
                        score = 'neg'
                else:
                        score = 'pos'

                if score == s[1]:
                        correct += 1

        accuracy = correct / len(test)
        print("TEXTBLOB ACCURACY: " + str(accuracy))
        return accuracy
