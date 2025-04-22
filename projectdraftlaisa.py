# Project draft: Horoscope Game
# Date: 08/09/2024
# Name: Laisa Kochevar

horoscope=input ("Welcome to the Horoscope game! Do you want to know your horoscope of the day? Yes or no? ")
positive_answers = ["yes", "Yes", "YES", "y", "Y"]
negative_answers = ["no", "No", "NO", "n", "N"]
if horoscope in positive_answers:
  print ("Cool! Let's check this out!")
elif horoscope in negative_answers:
  print ("Maybe next time. See you!")
  exit()
else:
  print ("Could you try again?")

zodiac_sign = input ("What's your zodiac sign? ")
if zodiac_sign == "Aries" or zodiac_sign == "aries":
  print ("Aries Mar 21th-Apr 19th - Someone who is far away is going to be on your mind today, and you are on their mind as well. In fact, they've been thinking about you for a while now and are eager to get back in contact, perhaps they've even started a game of phone tag with you. ")

elif zodiac_sign == "Taurus" or zodiac_sign == "taurus":
  print ("Taurus Apr 20th-May 20th - Today is a great day to clean out your emotional closet and say what you have been wanting to say to that certain someone. Holding on to your feelings is not wise. It could cause your imagination to run wild and fear to overtake you.")

elif zodiac_sign == "Gemini" or zodiac_sign == "gemini":
  print ("Gemini May 21st-Jun 20th - Let your curiosity guide you to new and unknown realms. Be open to change. Wondering if someone charming is romantically available? Ask! Their answer could change things in a big way between you.")

elif zodiac_sign == "Cancer" or zodiac_sign == "cancer":
  print ("Cancer Jun 21st-Jul 22nd - Fake it till you make it today! It's fun, it's exciting, and it's usually incredibly effective. If you get stuck in a situation that's a bit over your head, call on your best acting abilities to bluff your way through it.")

elif zodiac_sign == "Leo" or zodiac_sign == "leo":
  print ("Leo Jul 23rd-Aug 22nd - Your quick thinking in a tricky situation will leave others quite impressed today, although you might not completely understanding why. In your mind, you did what anyone else would have done in that position. You won't understand the significance of your actions until a few days from now, and then you can pat yourself on the back. ")

elif zodiac_sign == "Virgo" or zodiac_sign == "virgo":
  print ("Virgo Aug 23rd-Sep 22nd - There's a fine line between being charmingly talkative and being a blabbermouth. You know how to walk that line, but not all people do. Keep an eye out for a friend or coworker who isn't watching what they say today.")

elif zodiac_sign == "Libra" or zodiac_sign == "libra":
  print ("Libra Sep 23rd-Oct 22nd - Good and bad energies are floating around you today, and you need to figure out how to avoid the bad. Sure, negative vibes are just a part of life. Sometimes a bummer in your day provides the motivation you need to make a change.")

elif zodiac_sign == "Scorpio" or zodiac_sign == "scorpio":
  print ("Scorpio Oct 23rd-Nov 21st - If you're looking for more insight into your latest dilemma, turn to your coworkers or classmates. You need to consult with someone who is either in the same situation or has been there before. There is nothing better than first-hand experience to help you figure out what to do. ")

elif zodiac_sign == "Sagittarius" or zodiac_sign == "sagittarius":
  print ("Sagittarius Nov 22nd-Dec 21st - Be careful not to go along with that latest theory people are pushing right now. As you know, new ideas are not always good ideas. In terms of your romantic life, you shouldn't adhere too rigidly to some new self-help philosophy.")

elif zodiac_sign == "Capricorn" or zodiac_sign == "capricorn":
  print ("Capricorn Dec 22nd-Jan 19th - The only thing that matters today is doing what you want to do. Stick to your plan and don't let yourself get distracted by anyone or anything. Some very flighty people have been inviting you to join in on their adventures, but you are wise to decline politely and focus on your own agenda now.")

elif zodiac_sign == "Aquarius" or zodiac_sign == "aquarius":
  print ("Aquarius Jan 20th-Feb 18th - Not every romance is constantly a sizzling affair. Things cool off from time to time. They have to. If your current romance is feeling less than dynamic, don't assume it's headed for the end. Both of you need space once in a while to get back in touch with your independence and individual identity. You two are not attached at the hip, and it wouldn't be healthy if you were. So try not to be too possessive right now.")

elif zodiac_sign == "Pisces" or zodiac_sign == "pisces":
  print ("Pisces Feb 19th-Mar 20th - Avoid group activities today. Everybody wants something different, and trying to get your people on the same page will be a frustrating experience. So focus on activities that are best done alone. Save time for things like reading, napping, relaxing, researching, and even just thinking about life.")

else:
  print ("Sorry, I don't understand that. Please, try again.")

