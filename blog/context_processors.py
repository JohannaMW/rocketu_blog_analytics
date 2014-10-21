from blog.models import Post, Tag, AdImage
from localflavor.us.us_states import US_STATES

def latest_post(request):
    return {
        'latest_post': Post.objects.latest('created')
    }


def tag_post_list(request):
    tags = Tag.objects.all().order_by('name')
    return {
        'tags':tags,
    }

def random_ad(request):
    images = AdImage.objects.all()
    for image in images:
        image.state = dict(US_STATES)[image.state]
        if image.state == request.location['region']:
            print image.url
            print image.image
            return {
                'image_url':image.url,
                'image':image.image
            }


# def post_month(request):
#     i = 1
#     months_post = {}
#     while i <= 12:
#         months_post[i] = Post.objects.filter(created__month = i)
#         i += 1
#         print months_post






