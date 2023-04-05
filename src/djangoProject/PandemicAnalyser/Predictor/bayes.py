from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

#11
train = [("Happy Lockdown 6.0! - Drinking a Triple Tripel Straight Up by @thehowlinghound @ Bringabeeralong Holiday House", "pos"),
        ("INNR \u2014 COVID likely to lock India's women out of job market for years: Azim Premji University report finds 47 percent of women who lost jobs last year have been made permanently redundant. A woman sweeps next to the\u00a0... View article... https://t.co/WnOv8JLSpX", "neg"),
        ("Your prayers have worked again and Ad\u00e8le is getting better by the day. Thank you so much for thinking of Ad\u00e8le in her time of need. #covid #friends #love #people #europe #nuskin #family @ Billings, Montana https://t.co/5iTq6UuKcT", "pos"),
        ("So excited for this event.. come out in support me and all the other businesses coming \ud83e\udd17.\n#bakerdaves #eventcoming @ Corona, California https://t.co/sBsXKHgnfx", "pos"),
        ("Getting up at 5am to catch light wind waves with my son is simply the most amazing relief from the #coronavirus pandemic. I highly recommend it. #westonsupamare is fantastic for skim\u2026 https://t.co/q5uPiRwgEv", "pos"),
        ("Friday at the zoo. Limited visitors plus hand sanitizer, distance signs and marked restrictions everywhere they needed to be. Reassuring Covid prevention protocol work in action. @ Los Angeles Zoo and Botanical Gardens https://t.co/lIqC3zHy7T","pos"),
        ("THEY'RE SO PRETTY!! @the.canadianpress #readytoedit #workingfromhome #newedition #saskatchewan #journalismmatters #journalism #journalist #journalismlife #journalismjobs @ Humboldt, Saskatchewan https://t.co/id6LLCXXWV","pos"),
        ("Sooooo glad I called to see if they had leftover vaccine! I got the last one for the day. I\u2019m so grateful! #vaccinate #modernavaccice #byecovid19 @ Walgreens https://t.co/6Cy8ssxcYd","pos"),
        ("Always great to have visitors, thanks \ud83e\udd29 for visiting Hannah and Toby love you. D2 #quarantine #quarantinelife #wellington @ Wellington, New Zealand https://t.co/WCVkGzybR5","pos"),
        ("Thanks to everyone for the birthday wishes! Ready for this pandemic to be over so we can all celebrate, ideally packed into a small bar \ud83c\udf7b \ud83c\udf89 @ Elkins Park https://t.co/tkxj3spbQl","pos"),
        ("Excellent #zoom  event tonight that helped us all...\n#Covid19 \n#CovidVaccine \n#BlackAndBrown Communities @ Delaware County, Pennsylvania https://t.co/sOnMa1GZdd", "pos"),
        ("So good to be back at the #gym after a 4 month lockdown. Dreamt.of the gym so this was the perfect song for the first workout. Next up @cannibalcorpseofficial of course\n#gym #gymmotivation @ Montreal, Quebec https://t.co/ZHqY84swvW", "pos"),
        ("Different but enjoyable session today. Talking with @grantthorntonie guys about all things Physio, Back Pain and working from home! #physiotherapy #ILikeToMoveItMoveIt @ The Physiotherapy Centre https://t.co/YTB1Nt2VNa", "pos"),
        ("I feel so lucky to have the opportunity to get his vaccine. This is the beginning of much needed NORMALCY. \n\nBy the way it didn't hurt. I'm just being dramatic. @ Bronx, NY https://t.co/78Y4uEx8qY", "pos"),
        ("What a great way to start my Friday! My first COVID vaccine is in the books.\n\u2022\n#fauciouchie #covid_19 #covidvacccine @ Walgreens https://t.co/jeQ0x0GOf7", "pos"),
         #neg
        ("A big blow to our industry again f$$k Corona @ Keron Safaris &amp; Hotels https://t.co/HsWuOvFB6C","neg"),
        ("Learning the hard way not to push myself. Recovering from COVID-19 sucks. #covid_19 #covid19sucks #recoveryfromcovid @ Huntington Hospital https://t.co/jCaYdxJGHq","neg"),
        ("This year really sucks... \u2009\n\u2009\n#covid #memes #cordyceps #humor #2021 #2020 #thelastofus #whereisellie @ Portland, Maine https://t.co/66QcETCB7A","neg"),
        ("Another day of cancellations.... Covid please just disappear!!! Huge 10\u201d cakes for only \u00a345 each, delivery is available... DM \ud83d\udc8c\n-\nHappy Birthday toppers can be added! \ud83d\udc97 @ Manchester, United Kingdom https://t.co/pbNJgyTxqt","neg"),
        ("The human race is doomed. https://t.co/CJBHrw1YHk", "neg"),
        ("How many back to school days can an 8yr old have.. This lockdown was easier and more fun so mixed emotions today. I'm gonna miss @iamjustlorcan around the house #backtoschool @ Ballymoney Wexford https://t.co/OTPRrISpdX","neg"),
        ("Although the Covid pandemic is going down, I still spend my life cautiously #gotowork #normallife #selfie #cautious #strong @ Kew, Surrey, United Kingdom https://t.co/2X9O0fmIdB","neg"),
        ("GO AWAY!!!!!!!!!!!!!!!!!! Just bc our governor wants to kill us, you have no excuse to vacation like it\u2019s not a pandemic. You live where it\u2019s cold. Boo hoo. #deathsantis #endspringbreak https://t.co/ugsdpCxWEt","neg"),
        ("I miss walking in #uxbridge .. seat in my favourite places and drink good coffee.. #lockdown #waiting @ Uxbridge https://t.co/26lXkMlbb1","neg"),
        ("This Van looks how I feel about lockdown 3.... \n\n#ineedaservice\n#vwcampervan \n#vwcamper\n#worseforwear \n#knackered @ The Compton School https://t.co/q4vUsx0Fuj","neg"),
        ("Disgusted with the level of reporting in mainstream media over hysteria surrounding deaths of diabetics from Covid-19.\n\nYes, diabetes co-morbidity accounts for a third of deaths in hospital but without reference to\u2026 https://t.co/Tg5494ENnk","neg"),
        ("This is my nephew. He was taken by COVID-19 today. Please say a prayer for him and his family and friends.\n#family #covidsucks #pray @ Culver City, California https://t.co/BZbW8IN7gS","neg"),
        ( "This... why aren't mainstream media reporting this... scaremongering that's why. https://t.co/wCHiwt9jLQ","neg"),
        ("Vaccine wanker has arrived! #nofilter @ Sommar brewery https://t.co/FHOoHbRc1n", "neg"),
        ( "Throwback to happier times....#covid19 @ Gastown https://t.co/UqGTafKZZW", "neg"),
         # POSITIVE FAKE DATA MADE BY ME
        ("Had a very nice time today at the park", 'pos'),
        ("Lovely time today with friends. It makes me happy to talk to you guys ", 'pos'),
        ("So happy to have this opportunity to work at Microsoft", 'pos'),
        ("Nothing better than reuniting with good old friends", 'pos'),
        ("I am relieved to see all my friends do well", 'pos'),
        ("Had great fun today at this Zoom event held to motivate people to exercise. Great work everyone!", 'pos'),
        ("There is such wonderful scenery at the Cliffs of Moher", 'pos'),
        ("This new Netflix show is so fun!! I like it a lot", 'pos'),
        ("Gorgeous views at Dublin today", 'pos'),
        ("What a cool new feature added to Call Of Duty !", 'pos'),
        ("I received amazing news today... I am going to be a dad!", 'pos'),
        ("Thank you Netflix for all of the great content you're putting out. I'm looking forward to more coming out!", 'pos'),
        ("Happy Birthday Jake, let's have a big celebration of your 40 years after lockdown ends", 'pos'),
        ("I'm so lucky to have such thoughtful and kind friends. Thank you to everyone", 'pos'),
        ("This new Fortnite skin is so impressive. I LOVE it, make more amazing content like this!", 'pos'),
         # NEGATIVE FAKE DATA MADE BY ME
        ("I hate being locked down", 'neg'),
        ("Such terrible news came out today. I am so sad", 'neg'),
        ("I am so angry at people who oppose vaccination! They are bad", 'neg'),
        ("Everyone is so sad right now", 'neg'),
        ("This new update sucks! It's terrible", 'neg'),
        ("The new design is awful!", 'neg'),
        ("The mobile app is glitchy and definitely not user friendly", 'neg'),
        ("I HATE this game", 'neg'),
        ("Ranger fans are terrible!", 'neg'),
        ("Horrible comments made by the President today", 'neg')
         ]

test = [("Great day of catching up with dear friends I haven\u2019t seen since b4 these strange crazy pandemic times \ud83d\udc9c\n\n#postpandemictimes \n#jw @ Zelda's Restaurant-Capitola https://t.co/6CGrPCyxFB", 'pos'),
        ("The Saddest News Of The Decade...!!!!\ud83e\udd7a\nShri Milkha Singh Just Passed Away At The Age Of 91 Due To Covid 19 ..\ud83d\ude4f\ud83c\udffc\nRIP To The Olympic Hero Of India..\ud83d\ude22\nMay Your Sole Rest In Peace Sir..\ud83d\ude4f\ud83c\udffc\n\n#TheAmateurBong https://t.co/ycetcfdJKN",'neg'),
        ("This some real Bull \ud83d\udca9 don't make me move back to Texas where Vaccine Passports are banned. @ Los Angeles, California https://t.co/XDL7S6vs9Q", 'neg'),
        ("So grateful to everyone who made this happen! \ud83d\ude42\ud83d\udc4d\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n#OneAccenture #We4Vaccine #Vaccination #COVID_19 @ Accenture, Magarpatta City, Pune https://t.co/Mz1scHmCsP", 'pos'),
        ("You can't see it, but I'm wearing the biggest smile \ud83d\udc89. \n\n#Sinovac #1stDoseDone #COVID19 @ Kuala Lumpur, Malaysia https://t.co/m08GIx70F8", 'pos'),
        ("How Covid-19 fucked me up and today I am again at where I was ..lost all muscles, lost the 6 packs abs. #memories2019 \nWish I could go back to being lean and mean.. once again. @ Pune, Maharashtra https://t.co/t50q8smqLh", 'neg'),
        ("Fuck COVID-19 \ud83d\udc4a\ud83d\udc4a\ud83d\udc4a\ud83e\uddbe\n\nVaccinated. #covid_19 #fuckcovid19 @ Miami, Florida https://t.co/SSvIZYvol6","neg"),
        ("My brother and I took my dad out for dinner for the first time since the pandemic started. It was so nice to finally see my dad after a long year. #\u0262\u1d07\u1d1b\u1d20\u1d00\u1d04\u1d04\u026a\u0274\u1d00\u1d1b\u1d07\u1d05 @ Ke'e Grill https://t.co/6e9lOrM3KL","pos"),
        ("This is crazy.  First COVID now Gas Prices!!! @ Florence, South Carolina https://t.co/hliwmzpVgT","neg"),
        ("Celebrating being back after another lockdown with this beauty! \ud83e\udde1 @ Emma Frances Hair https://t.co/Easvp9M4Vr","pos"),
        ("Finally got to hug my Mom after over a year of social distancing! Yay! #ilovemymomanddad @ Roseville, California https://t.co/cel0jJ7vWL","pos"),
        ("The biggest thing I have missed because of Covid 19. Football with @christopherwilliams308 @ Sutton United F.C. https://t.co/tpSynbfT8F","neg"),
        ("Gorgeous sunset tonight while out grabbing dinner!! #SoCal #Sunset #Corona @ Subway https://t.co/w81i5MNQeJ","pos"),
        ("The former guy only cares for himself https://t.co/bly2njXRuL","neg"),
        ("LOVE THIS!!! #itsallcomingback #itswhatwedo #covid_19 @ Funkbox Productions https://t.co/CofmRJe9xW","pos"),
        ("Watching these pictures now makes me feel as if it was a hundred years ago. My personal remedy from the lockdown stressed mood. \ud83c\uddeb\ud83c\uddf7 \n#paris #france #theeiffeltower #memories #throwbackmonday (Tour Eiffel): https://t.co/0f7mgPMC4U","neg"),
        #FAKE TEST DATA MADE BY ME:
        ("This pandemic is such a scam! Down with the government!","neg"),
        ("I hate these restrictions, I feel like my time is being wasted", "neg"),
        ("Love to see people finding ways to stay connected, we'll get through this together!", "pos"),
        ("So happy to have visited my sister, I hadn't seen her in 3 months. Love you sis", "pos"),
        ("I am disgusted at people not wearing masks, our hospitals are full, do your part!", "neg"),
        ("I hate how Nike charges over 100$ for any popular sneaker", "neg"),
        ("What an awful show keeping up with the Kardashains is... We need better TV", "neg"),
        ("Many Thanks to the @Nike family for the gift. Looking forward to future collaborations with you guys", "pos"),
        ("Proud to be nominated for this award amongst so many other great competitors", "pos"),
        ("Had an mazing experience today at Tayto Park. The rides are so exciting and the kids loved it! I recommended to anyone planning a day out", "pos"),
        ("The food at McDonalds is disgusting... Im never eating there again", 'neg'),
        ("Our president is pathetic. We NEED new elections", 'neg'),
        ("Our president is the best we have ever had", 'pos'),
        ("Life at Riyadh is excellent. Everything is luxurious", 'pos'),
        ("Our country is in an awful state", 'neg'),
        ("We need help. Our country is destroyed", 'neg'),
        ("My greatest success up to has been my resilience. Lets all keep going", 'pos'),
        ("Stay strong people! You are tougher than you think", 'pos'),
        ("Peace and Love to everyone! Let's unite and be in harmony", 'pos')
        ]

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
