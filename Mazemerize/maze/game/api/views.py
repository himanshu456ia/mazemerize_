from rest_framework.response import Response
from rest_framework.decorators import api_view
from game.models import Profile

@api_view(['GET'])
def leaderboard(request):
    data = []
    profiles = Profile.objects.all().order_by('-win','lose')
    limit = min(len(profiles),10)
    for i in range(limit):
        person = profiles[i]
        data.append({
            'name' : person.user.first_name + " " + person.user.last_name,
            'email' : person.user.email,
        })
    return Response(data)
    
    