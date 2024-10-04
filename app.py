from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

temas = {
    'frutas': [
    'abacaxi','acerola','amora','banana','caju','caqui','cereja','coco',
    'figo','framboesa','goiaba','graviola','jaca','jabuticaba','kiwi',
    'laranja','limão','maçã','mamão','manga','maracujá','melancia','melão',
    'nectarina','pera','pêssego','pitanga','pitaya','romã','tamarindo',
    'tangerina','uva','abiu','açaí','acelga','açucena','aframônio','alchechengi',
    'ameixa','anona','araruta','ata','avelã','bacaba','bacuri','bailah',
    'baobá','baru','biribá','cabeludinha','cabeludinha','camu-camu',
    'carambola','ciriguela','cupuaçu','damasco','dovyalis','embaúba',
    'espinheira','feijoa','guabiroba','guaraná','grumixama','ingá',
    'jatobá','jenipapo','jujuba','kiwano','kumquat','litchi','longan',
    'maitá','mammee','marolo','massala','mirtilo','morango','murici',
    'nêspera','olho-de-boi','pequi','peumo','phalsa','pomelo','quixaba',
    'rambutan','sapoti','sapucaia','seriguela','sorva','soursop','tamarilho',
    'umbu','urucum','uvaia','uva-passa','voavanga','wampi','yuzu','zimbro'],
    
    'animais': [
    'abelha','águia','albatroz','alpaca','andorinha','anta','arara','atobá',
    'avestruz','baleia','beija-flor','bicho-preguiça','bisonte','boi','búfalo',
    'burro','cabrito','cachorro','camaleão','camelo','canguru','capivara',
    'caracol','caranguejo','cavalo','cegonha','chacal','chimpanzé','cisne',
    'coala','cobra','codorna','coruja','crocodilo','cupim','dromedário','elefante',
    'esquilo','falcão','flamingo','formiga','foca','gafanhoto','gaivota','galo',
    'gambá','garça','gato','girafa','gnu','golfinho','gorila','grilo','guaxinim',
    'hamster','hipopótamo','iguana','jabuti','jacaré','jaguatirica','jiboia',
    'joaninha','javali','kiwi','lagarto','lagosta','leão','leopardo','lhama',
    'lobo','lontra','lula','macaco','mamute','maritaca','marreco','morcego',
    'moreia','mula','musaranho','onça','orangotango','ornitorrinco','ostra',
    'paca','panda','pantera','papagaio','pardal','pato','pavão','peixe-boi',
    'pelicano','periquito','pinguim','pombo','porco','porquinho-da-índia',
    'preguiça','raposa','rato','rena','rinoceronte'],
    
    'programacao': ['python', 'java', 'javascript', 'flask', 'django', 'html'],
    
    'cidades': [
    'SãoPaulo','RioDeJaneiro','BeloHorizonte','Brasília','Salvador','Fortaleza',
    'Curitiba','Manaus','Recife','PortoAlegre','Belém','Goiânia','Guarulhos',
    'Campinas','SãoLuís','SãoGonçalo','Maceió','DuqueDeCaxias','Natal','Teresina',
    'CampoGrande','SãoBernardoDoCampo','NovaIguaçu','JoãoPessoa','SantoAndré',
    'Osasco','SãoJoséDosCampos','JaboatãoDosGuararapes','RibeirãoPreto','Uberlândia',
    'Contagem','Sorocaba','Aracaju','FeiraDeSantana','Cuiabá','Joinville',
    'AparecidaDeGoiânia','Londrina','Ananindeua','Serra','Niterói','CaxiasDoSul',
    'BelfordRoxo','Macapá','Florianópolis','VilaVelha','Mauá','SãoJoãoDeMeriti',
    'Santos','SãoJoséDoRioPreto','MogiDasCruzes','Betim','Diadema','CampinaGrande',
    'Jundiaí','Maringá','MontesClaros','Piracicaba','Carapicuíba','Olinda',
    'RioBranco','Anápolis','Bauru','Vitória','Canoas','Itaquaquecetuba','Araraquara',
    'Petrolina','BoaVista','VitóriaDaConquista','Franca','Blumenau','PontaGrossa',
    'Cascavel','Pelotas','VoltaRedonda','FozDoIguaçu','TaboãoDaSerra','SantaMaria',
    'VárzeaGrande','SãoVicente','Barueri','Marabá','Linhares','Itaboraí',
    'Castanhal','TeófiloOtoni','Palmas','Itajaí','Sobral','Uberaba','SeteLagoas',
    'Divinópolis','ItapecericaDaSerra','Camaçari','Alvorada','Taubaté','Imperatriz',
    'JuazeiroDoNorte','PatosDeMinas','Caruaru','Araçatuba']
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jogo/<tema>')
def jogo(tema):
    return render_template('jogo.html', tema=tema)

@app.route('/nova_palavra/<tema>')
def nova_palavra(tema):
    if tema in temas:
        palavra_selecionada = random.choice(temas[tema])
        return jsonify({'palavra': palavra_selecionada})
    return jsonify({'palavra': ''})

if __name__ == '__main__':
    app.run(debug=True)
