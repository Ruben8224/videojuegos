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
     
CREATE_GAME_MUTATION = '''
mutation createGameMutation($id: String, $juego: String, $fechaDeLanzamiento: String, $descripcion: String, $tipo: int, $creador: String, $personajes: String, $enemigos: int, $precio: String, $musica: String, $version: String){
    createGame($id: id, $juego: juego, $fechaDeLanzamiento: fechaDeLanzamiento, $descripcion: descripcion, $tipo: tipo, $creador: creador, $personajes: personajes, $enemigos: enemigos, $musica: musica, $version: version){
    id
    juego
    fechaDeLanzamiento
    descripcion
    tipo
    creador
    personajes
    enemigos
    precio
    musica
    version
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
        
def test_createAttribute_mutation(self):
  
        response = self.query(
            CREATE_ATTRIBUTE_MUTATION,
            variables={'url': 'http://google.com', 'description': 'google'}
        )
        print('mutation ')
        print(response)
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual({"createAttribute" : {"description": "google"}}, content['data'])