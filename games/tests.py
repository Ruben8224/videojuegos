from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.
from games.schema import schema
from games.models import Game

GAMES_QUERY = '''
 {
  games {
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
     
<<<<<<< HEAD
CREATE_VIDEOJUEGO_MUTATION = '''
mutation createGameMutation($juego: String, $fechaDeLanzamiento: String, $descripcion: String, $tipo: String, $creador: String, $personajes: String, $enemigos: String, $precio: Int, $musica: String, $version: String ){
    createGame(juego: $juego, fechaDeLanzamiento: $fechaDeLanzamiento, descripcion: $descripcion,  tipo: $tipo,  creador: $creador,  personajes: $personajes,  enemigos: $enemigos,  precio: $precio,  musica: $musica, version: $version){
        juego
}
}
'''

=======
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
     
>>>>>>> develop
class GameTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.game1 = mixer.blend(Game)
        
    def test_games_query(self):
        response = self.query(
        GAMES_QUERY,
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        print ("query games results")
        print (content)
<<<<<<< HEAD
        assert len(content['data']) == 1
    
    def test_createGame_mutation(self):
        response = self.query(
            CREATE_VIDEOJUEGO_MUTATION,
            variables={
                'juego': 'Quintillizas', 
                'fechaDeLanzamiento': '2023-04-12', 
                'descripcion': 'Comedia Romantica', 
                'tipo': 'Live Action', 
                'creador': 'Hirohito', 
                'personajes': 'Yo', 
                'enemigos': 'Tú', 
                'precio': 120, 
                'musica': 'Panini', 
                'version': '123'
            }
        )
        content = json.loads(response.content)
        print ("query games results")
        print (content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual(
            {
                "createGame": {
                    "juego": "Quintillizas"
                }
            }, 
            content['data']
        )  
      
=======
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
>>>>>>> develop
