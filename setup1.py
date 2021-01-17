"""
This template is written by @the-unknown
What does this quickstart script aim to do?
- This is my template which includes the new QS system.
  It includes a randomizer for my hashtags... with every run, it selects 10
  random hashtags from the list.
NOTES:
- I am using the bot headless on my vServer and proxy into a Raspberry PI I
have at home, to always use my home IP to connect to Instagram.
  In my comments, I always ask for feedback, use more than 4 words and
  always have emojis.
  My comments work very well, as I get a lot of feedback to my posts and
  profile visits since I use this tactic.
  As I target mainly active accounts, I use two unfollow methods. 
  The first will unfollow everyone who did not follow back within 12h.
  The second one will unfollow the followers within 24h.
"""

# !/usr/bin/python2.7
import random
from instapy import InstaPy
from instapy import smart_run

# get a session!
session = InstaPy(username='heyyastore', password='HesoYam123AA', headless_browser=True)

# let's go! :>
with smart_run(session):
    hashtags = ['travelcouples', 'travelcommunity', 'passionpassport',
                'travelingcouple',
                'backpackerlife', 'travelguide', 'travelbloggers',
                'travelblog', 'letsgoeverywhere',
                'travelislife', 'stayandwander', 'beautifuldestinations',
                'moodygrams',
                'ourplanetdaily', 'travelyoga', 'travelgram', 'sunsetporn',
                'lonelyplanet',
                'igtravel', 'instapassport', 'travelling', 'instatraveling',
                'travelingram',
                'mytravelgram', 'skyporn', 'traveler', 'sunrise',
                'sunsetlovers', 'travelblog',
                'sunset_pics', 'visiting', 'ilovetravel',
                'photographyoftheday', 'sunsetphotography',
                'explorenature', 'landscapeporn', 'exploring_shotz',
                'landscapehunter', 'colors_of_day',
                'earthfocus', 'ig_shotz', 'ig_nature', 'discoverearth',
                'thegreatoutdoors']
    random.shuffle(hashtags)
    my_hashtags = hashtags[:10]

    # general settings
    session.set_dont_like(['sad', 'rain', 'depression'])
    session.set_do_follow(enabled=True, percentage=80, times=1)
    session.set_do_comment(enabled=True, percentage=80)
    session.set_comments([
                             u'What an amazing shot! :heart_eyes: What do '
                             u'you think of my recent shot?',
                             u'What an amazing shot! :heart_eyes: I think '
                             u'you might also like mine. :wink:',
                             u'Wonderful!! :heart_eyes: Would be awesome if '
                             u'you would checkout my photos as well!',
                             u'Wonderful!! :heart_eyes: I would be honored '
                             u'if you would checkout my images and tell me '
                             u'what you think. :wink:',
                             u'This is awesome!! :heart_eyes: Any feedback '
                             u'for

                             y photos? :wink:',
                             u'This is awesome!! :heart_eyes:  maybe you '
                             u'like my photos, too? :wink:',
                             u'I really like the way you captured this. I '
                             u'bet you like my photos, too :wink:',
                             u'I really like the way you captured this. If '
                             u'you have time, check out my photos, too. I '
                             u'bet you will like them. :wink:',
                             u'Great capture!! :smiley: Any feedback for my '
                             u'recent shot? :wink:',
                             u'Great capture!! :smiley: :thumbsup: What do '
                             u'you think of my recent photo?'],
                         media='Photo')
    session.set_do_like(True, percentage=70)
    session.set_delimit_liking(enabled=True, max_likes=100, min_likes=0)
    session.set_delimit_commenting(enabled=True, max_comments=10, min_comments=0)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=3000,
                                    max_following=2000,
                                    min_followers=50,
                                    min_following=50)
    session.set_skip_users(skip_private=False,
                           skip_no_profile_pic=True,
                           skip_business=True)

    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "follows"],
                                 sleepyhead=True, stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes_hourly=200,
                                 peak_likes_daily=585,
                                 peak_comments_hourly=80,
                                 peak_comments_daily=182,
                                 peak_follows_hourly=48,
                                 peak_follows_daily=None,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=402,
                                 peak_server_calls_hourly=None,
                                 peak_server_calls_daily=4700)

    session.set_user_interact(amount=10, randomize=True, percentage=80)

    # activity
    #Location Based Actions
    #Cairo, Egypt
    #session.like_by_locations(['217184762','101474311386463/city-center-almazah/','236225730458245/tevoli-plaza/','260776821385448/portosokhna/','2077464298969942/','404167877082211/north-coast/','1949348491783419/cairo-festival-city-mall/','100886218307842/cairo/','426108714627713/the-nile-river-cairo-egypt/','949150448599868/west-elbald-/','114602183283205/point-90-mall/','341380743231090/piramides-de-guiza-el-cairo-egipto/','1041145549367193/faculty-of-al-alsun-languages/','110813416994525/heliopolis-masr-el-gdidah/','631423593964543/zamalk-asha-fahmy-palace/','101525424956742/','111359644050204/o1-new-cairo/','114632973609416/cairo-festival-city-resale/','locations/385997691867030/-/','205413486948182/dunkin-dounts/','469325796886534/',''], amount=500, skip_top_posts=True, randomize=True, interact=True)
    session.follow_commenters(['esraahabiba3', 'the_fitting_room0', 'hoorsalmann', 'sabyaastore', 'basma_sleem_couture','zeynepdenizillustrations','thoriaalalfy','fatmanasr_couture','nuran_designs','fashion_police_egypt','hadeerzedan.couture','o.u.t.f.i.t_2020','doha.dergham','monicasamirelgendi','amira.karam_'], amount=15, daysold=365, max_pic = 100, sleep_delay=600, interact=True)

    #session.like_by_tags(my_hashtags, amount=90, media=None)
    session.unfollow_users(amount=500, instapy_followed_enabled=True, instapy_followed_param="nonfollowers",
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=501)
    session.unfollow_users(amount=500, instapy_followed_enabled=True, instapy_followed_param="all",
                           style="FIFO", unfollow_after=24 * 60 * 60,
                           sleep_delay=501)

    """ Joining Engagement Pods...
    """
    session.join_pods(topic='beauty', engagement_mode='no_comments')
