
blog_1 = 'I am so awesome'
blog_2 = 'Cars are cool.'
blog_3 = 'Aww look at my cat.'


def blog_posts(*args):
    for post in args:
        print(post)

blog_posts(blog_1, blog_2, blog_3)


def blog_posts_2(regular_arg, *args):
    print(regular_arg)
    for post in args:
        print(post)

blog_posts_2('My blogs:', blog_1, blog_2, blog_3)


def blog_posts_3(**kwargs):
    for title, post in kwargs.items():
        print(title, post)

blog_posts_3(blog_1='I am so awesome',
             blog_2='Cars are cool.',
             blog_3='Aww look at my cat.')


def blog_posts_4(myParam, *args, **kwargs):
    print(myParam)
    print(args)
    for i in args:
        print(i)
    for title, post in kwargs.items():
        print(title, post)

blog_posts_4('Fake', '1', '2', blog_1='I am so awesome',
             blog_2='Cars are cool.',
             blog_3='Aww look at my cat.')



