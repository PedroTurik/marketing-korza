PAGINA = dict(
    url='/guias/push-notification/',
    tipo='guia',
    autor='pedro',
    titulo='Push notification: o que é, como funciona e como usar | Korza',
    descricao='O que significa push notification, a diferença entre push e mensagem in-app, como funciona a permissão e como usar notificações na sua loja.',
    chapeu='Guia de push',
    h1='Push notification: o que é e como usar na sua loja',
    abertura='Push notification é a mensagem que um aplicativo envia para a tela do celular, mesmo com o app fechado. Parece simples, e é. O que separa uma boa campanha de um app desinstalado é o que você manda, para onde leva e com que frequência.',
    corpo='''
<h2>O que significa push notification</h2>
<p>“Push” quer dizer empurrar. Na notificação push, a mensagem é empurrada até a pessoa: ela não precisa abrir o app, o e-mail ou o navegador para ver. O aviso aparece na tela de bloqueio ou na central de notificações, com o ícone da marca, um título e um texto curto.</p>
<h3>Como funciona, em quatro passos</h3>
<ol>
  <li>A pessoa instala o app e autoriza as notificações.</li>
  <li>O app registra o aparelho no serviço do sistema: da Apple no iPhone, do Google no Android.</li>
  <li>Você cria a mensagem e define o envio.</li>
  <li>O sistema entrega no celular, e o toque abre a página que você escolheu.</li>
</ol>

<h2>Permissão: o push só chega a quem autorizou</h2>
<p>O celular protege o usuário. No Android, a documentação do Google diz que, em aparelhos com Android 13 ou superior, as notificações de um app recém-instalado ficam desligadas por padrão e o app precisa pedir permissão. No iPhone, o app também pede autorização antes de notificar, conforme a documentação da Apple.</p>
<p>Isso tem uma consequência prática: <strong>o momento do pedido importa</strong>. Explique o que a pessoa ganha, como novidades e ofertas exclusivas, para que ela diga sim.</p>

<h2>Push, push in-app e web push</h2>
<div class="pg-tabela"><table>
  <thead><tr><th>Tipo</th><th>Onde aparece</th><th>Quando usar</th></tr></thead>
  <tbody>
    <tr><td>Push notification</td><td>Na tela do celular, com o app fechado</td><td>Trazer a pessoa de volta</td></tr>
    <tr><td>Push in-app</td><td>Dentro do app, com ele aberto</td><td>Orientar quem já está lá: banner, cupom, aviso</td></tr>
    <tr><td>Web push</td><td>No navegador. No iPhone, só com o site adicionado à Tela de Início</td><td>Falar com quem não tem o app</td></tr>
  </tbody>
</table></div>
<p>O WebKit, motor do Safari, informou em 16/02/2023 que o web push chegou ao iOS e iPadOS 16.4 para web apps adicionados à Tela de Início. Na prática, poucas pessoas fazem isso. O guia <a href="/guias/app-pwa-ou-site-mobile/">app, PWA ou site mobile</a> explica melhor.</p>

<h2>Como escrever um push que funciona</h2>
<ul>
  <li><strong>Uma ideia só.</strong> O espaço é curto. Se precisar de duas frases longas, a mensagem está errada.</li>
  <li><strong>Comece pelo motivo.</strong> “Voltou ao estoque”, “Chegou a coleção”, “Seu cupom vence hoje”.</li>
  <li><strong>Leve à página certa.</strong> Push de produto abre o produto, nunca a página inicial. É o que garante 1 clique até o produto.</li>
  <li><strong>Seja verdadeiro.</strong> Falsa urgência funciona uma vez e custa a confiança nas seguintes.</li>
</ul>
<h3>Exemplos para adaptar</h3>
<ul>
  <li><strong>Lançamento:</strong> “A nova coleção chegou. Você vê antes de todo mundo.”</li>
  <li><strong>Reposição:</strong> “Hora de repor? Seu favorito está a um toque.”</li>
  <li><strong>Volta ao estoque:</strong> “Aquele tênis voltou. Numeração limitada.”</li>
  <li><strong>Data:</strong> “Entrega garantida até o Natal só até hoje.”</li>
</ul>

<h2>Com que frequência enviar</h2>
<p>Não há número certo, e desconfie de quem promete um. A regra prática é enviar quando existe uma razão real, começar devagar e observar. Se aumentar a frequência e os toques caírem, ou as desativações subirem, recue.</p>
<p>Acompanhe os toques, as vendas e as desativações por campanha. Faça um calendário com lançamentos e datas, em vez de decidir na hora. Push ilimitado não é convite para mandar tudo.</p>

<h2>Quanto da sua base vai receber</h2>
<p>O alcance do push é uma conta em três etapas: quantos clientes baixam o app, quantos autorizam as notificações e quantos seguem com elas ativas. Cada etapa tem a sua alavanca.</p>
<ul>
  <li><strong>Para baixar:</strong> dê um motivo, como um cupom de primeira compra no app, e divulgue no site, nas redes e no pacote.</li>
  <li><strong>Para autorizar:</strong> mostre o benefício antes do pedido de permissão.</li>
  <li><strong>Para manter ativas:</strong> mande pouco e mande bem. Quem se cansa desliga, e o caminho de volta é difícil.</li>
</ul>

<h2>O que acompanhar em cada campanha</h2>
<div class="pg-tabela"><table>
  <thead><tr><th>Métrica</th><th>O que responde</th></tr></thead>
  <tbody>
    <tr><td>Entregas</td><td>Quantas pessoas a campanha alcançou</td></tr>
    <tr><td>Toques</td><td>O título e o momento chamaram a atenção?</td></tr>
    <tr><td>Conversão</td><td>O destino e a oferta convenceram?</td></tr>
    <tr><td>Vendas atribuídas</td><td>Quanto a campanha trouxe de volta</td></tr>
  </tbody>
</table></div>
<p>Muda um elemento por vez. Se trocar título, horário e oferta juntos, você não sabe o que funcionou.</p>

<h2>Três erros que afastam o cliente</h2>
<ul>
  <li><strong>Só mandar desconto.</strong> Lançamentos, novidades e avisos úteis também são bons motivos.</li>
  <li><strong>Levar à página inicial.</strong> Quem tocou em um produto quer ver esse produto.</li>
  <li><strong>Ignorar o horário.</strong> Evite madrugadas e teste os horários em que a sua base costuma comprar.</li>
</ul>

<h2>Como isso funciona numa loja</h2>
<div class="pg-case">
  <img src="/assets/belletonn-mockup.png" alt="Aplicativo da Belletonn" width="930" height="1691" loading="lazy">
  <div><span>Case Belletonn · cosméticos</span><strong>26,6% de conversão entre clientes que abriram os pushs não segmentados.</strong><p>Resultado da Belletonn, sem garantia de que se repita em outra loja.</p></div>
</div>
<p>Somados, os apps da Korza já enviaram mais de 9,5 milhões de notificações, e mais de 70 mil clientes estão com notificações ativas.</p>
<p>No painel da Korza, você escreve a mensagem, escolhe o destino e agenda, com push ilimitado no plano. Para quem tem loja em Nuvemshop ou Shopify, o caminho começa em <a href="/aplicativo-para-loja-virtual/">aplicativo para loja virtual</a>.</p>
''',
    faq=[
        ('O que é push notification?', 'É uma mensagem enviada por um aplicativo que aparece na tela do celular, mesmo com o app fechado.'),
        ('Qual a diferença entre push e SMS?', 'O SMS vai para o número de telefone. O push vai para quem instalou o app e autorizou as notificações, e abre direto uma página do app.'),
        ('O que é push in-app?', 'É a mensagem exibida dentro do aplicativo, enquanto a pessoa está usando. Serve para orientar quem já está no app, não para trazer alguém de volta.'),
        ('Push notification é pago?', 'Depende da ferramenta. Com a Korza, o push é ilimitado no plano, sem custo por envio.'),
        ('Preciso de aplicativo para enviar push?', 'Para notificações no celular, sim. Sem app, existe o web push, mas no iPhone ele exige que o site seja adicionado à Tela de Início.'),
    ],
    fontes=[
        ('Google, Android Developers, Notification runtime permission', 'https://developer.android.com/develop/ui/compose/notifications/notification-permission', 'Consultado em 30/10/2026'),
        ('Apple, Asking permission to use notifications', 'https://developer.apple.com/documentation/usernotifications/asking-permission-to-use-notifications', 'Consultado em 30/10/2026'),
        ('WebKit, Web Push for Web Apps on iOS and iPadOS', 'https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/', 'Publicado em 16/02/2023'),
    ],
    relacionados=[
        ('/aplicativo-para-nuvemshop/', 'Aplicativo para Nuvemshop', 'Push na sua loja, com zero trabalho.'),
        ('/guias/whatsapp-push-ou-email-custos/', 'WhatsApp, push ou e-mail', 'Quanto custa cada canal.'),
    ],
    cta=('Mande o próximo push com a sua marca.', 'Crie a conta grátis e veja como ficaria o app da sua loja.'),
)
