from django.test import TestCase

# Create your tests here.

from graphene_django.utils.testing import GraphQLTestCase
from games.models import Game
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.
from games.schema import schema
from games.models import Game

GAMES_QUERY = '''
{
  games {
	juego
  creador 
  precio
  }
}
     '''
     
class GameTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.game1 = mixer.blend(Game)
        self.game2= mixer.blend(Game)
        
    def test_games_query(self):
        response = self.query(
        GAMES_QUERY,
        )
        content = json.loads(response.content)
        #print (content)
        self.assertResponseNoErrors(response)
        print ("query games results")
        print (content)
        assert len(content['data']['games']) == 2
        
        