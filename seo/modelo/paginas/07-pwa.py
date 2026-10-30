PAGINA = dict(
    url='/guias/app-pwa-ou-site-mobile/',
    tipo='guia',
    autor='pedro',
    titulo='App, PWA ou site mobile: o que escolher no e-commerce | Korza',
    descricao='Compare app nativo, PWA e site mobile para e-commerce: instalação, lojas de apps, push no iPhone e quando cada formato faz sentido.',
    chapeu='Guia comparativo',
    h1='App, PWA ou site mobile: o que faz sentido para o seu e-commerce',
    abertura='Os três aparecem no celular, mas não fazem o mesmo trabalho. O site mobile recebe quem chega. O PWA tenta ser um meio-termo. O app fica com quem já é cliente. A escolha depende de qual problema você quer resolver.',
    corpo='''
<h2>O que é cada um</h2>
<p><strong>Site mobile.</strong> É o seu site adaptado à tela do celular. Toda loja em Nuvemshop ou Shopify já tem. Abre pelo navegador, vindo do Google, de um anúncio ou de um link.</p>
<p><strong>PWA.</strong> Sigla de Progressive Web App. O web.dev, site do Google para desenvolvedores, define PWAs como web apps construídos com APIs modernas para ampliar recursos, alcançando qualquer usuário com uma única base de código (2020). Em outras palavras, é um site que pode ser instalado na tela e ganhar comportamento de aplicativo.</p>
<p><strong>App nativo.</strong> É o aplicativo baixado da App Store ou do Google Play, com o ícone da marca na tela do celular.</p>

<h2>A comparação</h2>
<div class="pg-tabela"><table>
  <thead><tr><th></th><th>Site mobile</th><th>PWA</th><th>App nativo</th></tr></thead>
  <tbody>
    <tr><td>Onde a pessoa encontra</td><td>Google, anúncios, links</td><td>No site, com instalação pelo navegador</td><td>App Store e Google Play</td></tr>
    <tr><td>Ícone na tela</td><td>Não</td><td>Se a pessoa instalar</td><td>Sim</td></tr>
    <tr><td>Notificações</td><td>Limitadas</td><td>No iPhone, só depois de adicionar à Tela de Início</td><td>Sim, com autorização</td></tr>
    <tr><td>Presença nas lojas de apps</td><td>Não</td><td>Em geral, não</td><td>Sim</td></tr>
    <tr><td>Melhor papel</td><td>Conquistar cliente novo</td><td>Melhorar a experiência no navegador</td><td>Trazer o cliente de volta</td></tr>
  </tbody>
</table></div>

<h2>O ponto que costuma decidir: o iPhone</h2>
<p>Em 16/02/2023, o WebKit anunciou web push no iOS e iPadOS 16.4 para web apps adicionados à Tela de Início. Ou seja, antes de receber a notificação, a pessoa precisa abrir o site no navegador, usar a opção de compartilhar, adicionar à Tela de Início e só então autorizar.</p>
<p>Quantos clientes da sua loja vão seguir esse caminho? No app, o gesto é outro, e conhecido por todo mundo: baixar na loja de aplicativos e aceitar as notificações.</p>

<h2>Quando cada um faz sentido</h2>
<h3>Só o site mobile</h3>
<p>Se a loja ainda está buscando os primeiros clientes constantes, invista aqui: velocidade, checkout e fotos. Sem base para trazer de volta, um canal de volta não tem o que fazer.</p>
<h3>PWA</h3>
<p>Faz sentido quando a prioridade é deixar o site mais rápido e com melhor navegação, e existe equipe técnica para cuidar disso. Pense nele como uma melhoria do site.</p>
<h3>App</h3>
<p>Faz sentido quando a loja já tem base de clientes e o desafio é a <a href="/blog/taxa-de-recompra/">recompra</a>. O app é o canal de quem já conhece a marca, e o site segue trazendo gente nova. A Korza recomenda esse caminho para lojas a partir de R$ 30 mil por mês.</p>

<h2>Quatro perguntas para decidir</h2>
<ol>
  <li><strong>Qual problema você quer resolver?</strong> Se é trazer gente nova, olhe para o site. Se é fazer quem comprou voltar, olhe para o canal de volta.</li>
  <li><strong>Sua base justifica?</strong> Um canal de volta precisa de clientes para trazer de volta.</li>
  <li><strong>Como é o seu público?</strong> Veja no Analytics quanto do tráfego vem de iPhone. Quanto maior essa parte, mais pesa o limite do web push.</li>
  <li><strong>Quem cuida disso?</strong> Todo formato exige manutenção. A diferença é de quem é esse trabalho.</li>
</ol>

<h2>Confiança e descoberta</h2>
<p>Há um argumento fora da técnica: onde a sua marca aparece. Quem procura o nome dela na App Store ou no Google Play encontra um app com ícone, descrição e avaliações, no mesmo lugar em que estão as grandes marcas. O PWA, em geral, vive só no navegador, e quem não visitar o site não fica sabendo dele.</p>
<p>O contrário também vale: o app não é encontrado por quem busca um produto no Google. Por isso, ele não substitui o site. O site mobile continua sendo a porta de entrada, e precisa ser bom.</p>

<h2>O que dá para melhorar no site mobile</h2>
<p>Se a decisão for ficar no site por enquanto, comece por aqui:</p>
<ul>
  <li><strong>Velocidade:</strong> imagens leves e menos aplicativos carregando em cada página.</li>
  <li><strong>Busca e menu:</strong> o cliente precisa achar o produto com o polegar.</li>
  <li><strong>Checkout:</strong> menos campos e meios de pagamento fáceis de usar no celular.</li>
</ul>

<h2>Cuidado com o site “empacotado”</h2>
<p>Publicar nas lojas não é só colocar o site dentro de uma casca. A diretriz 4.2 da Apple pede que o app tenha recursos, conteúdo e interface que o elevem além de “a repackaged website”. Antes de contratar, pergunte como é o app, e quem responde se ele for rejeitado.</p>

<h2>E o que a Korza faz</h2>
<p>A Korza constrói apps iOS e Android, não web push nem PWA. A publicação na App Store e no Google Play fica por nossa conta, em até 14 dias úteis, nas contas da Korza. Veja em <a href="/aplicativo-para-loja-virtual/">aplicativo para loja virtual</a> ou nas páginas de <a href="/aplicativo-para-nuvemshop/">Nuvemshop</a> e <a href="/aplicativo-para-shopify/">Shopify</a>.</p>
''',
    faq=[
        ('PWA é a mesma coisa que aplicativo?', 'Não. O PWA é um site que pode ser instalado e ganhar recursos de aplicativo. O app nativo é baixado da App Store ou do Google Play.'),
        ('PWA funciona no iPhone?', 'Funciona, com limites. O web push, por exemplo, exige que a pessoa adicione o site à Tela de Início, segundo o WebKit (2023).'),
        ('Ter app prejudica o SEO do meu site?', 'Não. O app e o site são canais separados, e o site continua sendo encontrado no Google normalmente.'),
        ('Preciso escolher só um?', 'Não. O mais comum é manter o site para conquistar clientes novos e ter o app para quem já comprou.'),
    ],
    fontes=[
        ('web.dev, What are Progressive Web Apps?', 'https://web.dev/articles/what-are-pwas', 'Publicado em 06/01/2020'),
        ('WebKit, Web Push for Web Apps on iOS and iPadOS', 'https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/', 'Publicado em 16/02/2023'),
        ('Apple, App Review Guidelines, item 4.2', 'https://developer.apple.com/app-store/review/guidelines/', 'Consultado em 30/10/2026'),
    ],
    relacionados=[
        ('/aplicativo-para-loja-virtual/', 'Aplicativo para loja virtual', 'Como transformar a sua loja em app.'),
        ('/guias/quanto-custa-aplicativo-loja-virtual/', 'Quanto custa um aplicativo de loja', 'Os tipos de solução e o custo de cada um.'),
    ],
    cta=('Veja como fica o app da sua marca.', 'Crie a conta grátis e veja o resultado antes de decidir.'),
)
