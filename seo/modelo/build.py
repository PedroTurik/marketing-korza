#!/usr/bin/env python3
"""Gera as páginas de SEO no Site-Korza a partir de paginas/*.py.

Uso: python3 seo/modelo/build.py [prefixo ...]   (ex.: 01 02; sem argumento gera todas)
Head (GA4 e Pixel) vem do index.html da branch atual, para nunca divergir da home.
"""
import html
import importlib.util
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).parent
SITE = AQUI.parents[2] / 'dev' / 'Site-Korza'
BASE = 'https://korza.app'
CADASTRO = 'https://admin.korza.app/create-account'
ESPECIALISTA = 'https://wa.me/555194553299?text=Ol%C3%A1!%20Quero%20falar%20com%20um%20especialista%20sobre%20um%20app%20para%20a%20minha%20loja.'
PUBLICADO = '2026-10-30'
PUBLICADO_TEXTO = '30 de outubro de 2026'
OG_IMAGE = f'{BASE}/assets/korza-logo.png'

AUTORES = {
    'pedro': ('Pedro Turik Firmino', 'Cofundador e CTO', 'Cofundador e CTO da Korza, que transforma lojas Nuvemshop e Shopify em apps iOS e Android.'),
    'guilhermo': ('Guilhermo Herter', 'Cofundador e CEO', 'Cofundador e CEO da Korza, que transforma lojas Nuvemshop e Shopify em apps iOS e Android.'),
}
ORG = {
    '@type': 'Organization', '@id': f'{BASE}/#organization', 'name': 'Korza', 'url': f'{BASE}/',
    'logo': f'{BASE}/assets/korza-logo.png', 'sameAs': ['https://www.instagram.com/korza.br/'],
}
SETA = '<svg class="icon" aria-hidden="true"><use href="#arrow"/></svg>'


def tags_do_head():
    home = (SITE / 'index.html').read_text()
    return home[home.index('<!-- Google tag'):home.index('<link rel="icon"')].rstrip()


def cabecalho():
    return f'''<header class="header"><div class="container nav-bar">
  <a class="logo" href="/" aria-label="Korza, início"><img src="/assets/korza-logo.png" alt="Korza" width="941" height="158"></a>
  <nav id="navigation" aria-label="Navegação principal"><a href="/#plataforma">Plataforma</a><a href="/#resultados">Resultados</a><a href="/#cases">Clientes</a><a href="/#precos">Preço</a><a href="/#duvidas">Dúvidas</a><a class="mobile-login" href="https://admin.korza.app/login">Entrar</a><a class="mobile-signup" href="{CADASTRO}">Criar conta grátis {SETA}</a></nav>
  <a class="nav-login" href="https://admin.korza.app/login">Entrar</a><a class="button signup-cta nav-signup" href="{CADASTRO}">Criar conta grátis {SETA}</a>
  <button class="menu-toggle" type="button" aria-label="Abrir menu" aria-expanded="false" aria-controls="navigation"><span></span><span></span></button>
</div></header>'''


def rodape():
    return f'''<footer class="footer frame"><div class="container footer-main"><div><a class="logo" href="/" aria-label="Korza, voltar ao início"><img src="/assets/korza-logo.png" alt="Korza" width="941" height="158" loading="lazy"></a><p>Sua marca, mais perto.</p></div><div class="footer-links"><strong>Explore</strong><a href="/#plataforma">Plataforma</a><a href="/#resultados">Resultados</a><a href="/#cases">Clientes</a><a href="/aplicativo-para-nuvemshop/">App para Nuvemshop</a><a href="/aplicativo-para-shopify/">App para Shopify</a><a href="/aplicativo-para-loja-virtual/">App para loja virtual</a></div><div class="footer-links"><strong>Próximo passo</strong><a href="/#precos">Preço</a><a href="/#duvidas">Dúvidas</a><a href="{CADASTRO}">Criar app grátis</a></div><div class="footer-contact"><strong>Sua área</strong><a href="https://admin.korza.app/login">Entrar na Korza <span aria-hidden="true">↗</span></a><span>Seu e-commerce. Novas possibilidades.</span></div></div><div class="container footer-bottom"><span>© <span id="year">2026</span> Korza. Todos os direitos reservados. <a href="/privacy-policy/">Política de privacidade</a></span><a href="#inicio">Voltar ao topo ↑</a></div></footer>'''


def texto_puro(trecho):
    return html.unescape(re.sub(r'<[^>]+>', '', trecho))


def dados_estruturados(p):
    url = BASE + p['url']
    grafo = [ORG]
    if p['tipo'] == 'solucao':
        grafo.append({
            '@type': 'SoftwareApplication', 'name': p['produto'], 'description': p['descricao'], 'url': url,
            'applicationCategory': 'BusinessApplication', 'operatingSystem': 'iOS, Android',
            'provider': {'@id': ORG['@id']},
            'offers': {'@type': 'Offer', 'price': '399', 'priceCurrency': 'BRL', 'url': CADASTRO},
        })
    else:
        nome, cargo, _ = AUTORES[p['autor']]
        grafo.append({
            '@type': 'Article', 'headline': texto_puro(p['h1']), 'description': p['descricao'],
            'mainEntityOfPage': url, 'url': url, 'inLanguage': 'pt-BR', 'image': OG_IMAGE,
            'datePublished': PUBLICADO, 'dateModified': PUBLICADO,
            'author': {'@type': 'Person', 'name': nome, 'jobTitle': cargo, 'worksFor': {'@id': ORG['@id']}},
            'publisher': {'@id': ORG['@id']},
        })
    grafo.append({
        '@type': 'FAQPage', 'mainEntity': [
            {'@type': 'Question', 'name': texto_puro(q), 'acceptedAnswer': {'@type': 'Answer', 'text': texto_puro(r)}}
            for q, r in p['faq']
        ],
    })
    corpo = json.dumps({'@context': 'https://schema.org', '@graph': grafo}, ensure_ascii=False, indent=1)
    return f'<script type="application/ld+json">\n{corpo}\n</script>'


def abertura(p):
    acoes = f'<div class="actions"><a class="button" href="{CADASTRO}">Veja seu app grátis {SETA}</a>'
    if p['tipo'] == 'solucao':
        acoes += f'<a class="link" href="{ESPECIALISTA}">Fale com um especialista {SETA}</a>'
        imagem = p['imagem']
        return f'''<section class="pg-hero" id="inicio"><div class="container pg-hero-grid"><div>
  <span class="eyebrow">{p['chapeu']}</span>
  <h1>{p['h1']}</h1>
  <p class="pg-lead">{p['abertura']}</p>
  {acoes}</div>
  <p class="pg-micro">Conta grátis. Plano de R$ 399/mês.</p>
</div><img class="pg-hero-img" src="{imagem[0]}" alt="{imagem[1]}" width="930" height="1692"></div></section>'''
    nome = AUTORES[p['autor']][0]
    return f'''<section class="pg-hero pg-hero-texto" id="inicio"><div class="container pg-coluna">
  <span class="eyebrow">{p['chapeu']}</span>
  <h1>{p['h1']}</h1>
  <p class="pg-lead">{p['abertura']}</p>
  <p class="pg-meta">Por {nome} · {PUBLICADO_TEXTO}</p>
</div></section>'''


def faq(p):
    itens = ''.join(f'<details><summary>{q}</summary><p>{r}</p></details>' for q, r in p['faq'])
    return f'<section class="pg-faq" id="duvidas"><h2>Perguntas frequentes</h2>{itens}</section>'


def fontes(p):
    if not p.get('fontes'):
        return ''
    itens = ''.join(f'<li><a href="{u}" rel="noopener">{n}</a>. {d}.</li>' for n, u, d in p['fontes'])
    return f'<section class="pg-fontes"><h2>Fontes</h2><ul>{itens}</ul></section>'


def autor(p):
    if not p.get('autor'):
        return ''
    nome, _, bio = AUTORES[p['autor']]
    return f'<aside class="pg-autor" aria-label="Sobre o autor"><strong>{nome}</strong><p>{bio}</p></aside>'


def relacionados(p):
    itens = ''.join(f'<a class="pg-card" href="{u}"><strong>{t}</strong><span>{d}</span></a>' for u, t, d in p['relacionados'])
    return f'<nav class="pg-relacionados" aria-label="Leia também"><h2>Leia também</h2><div>{itens}</div></nav>'


def chamada(p):
    segundo = ''
    if p['tipo'] == 'solucao':
        segundo = f'<a class="pg-link-claro" href="{ESPECIALISTA}">Fale com um especialista {SETA}</a>'
    return f'''<section class="pg-cta" id="comecar"><div class="container"><h2>{p['cta'][0]}</h2><p>{p['cta'][1]}</p>
<div class="actions"><a class="button button-white" href="{CADASTRO}">Veja seu app grátis {SETA}</a>{segundo}</div></div></section>'''


def pagina(p):
    url = BASE + p['url']
    e = html.escape
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#ffffff">
  <meta name="description" content="{e(p['descricao'])}">
  <title>{e(p['titulo'])}</title>
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="{'website' if p['tipo'] == 'solucao' else 'article'}">
  <meta property="og:site_name" content="Korza">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:title" content="{e(p['titulo'])}">
  <meta property="og:description" content="{e(p['descricao'])}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{OG_IMAGE}">
  {tags_do_head()}
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
  <link rel="preload" href="/assets/jakarta-400.ttf" as="font" type="font/ttf" crossorigin>
  <link rel="preload" href="/assets/jakarta-600.ttf" as="font" type="font/ttf" crossorigin>
  <link rel="stylesheet" href="/styles.css">
  <link rel="stylesheet" href="/paginas.css">
  <script defer src="/paginas.js"></script>
  {dados_estruturados(p)}
</head>
<body>
<a class="skip-link" href="#conteudo">Pular para o conteúdo</a>
<svg class="icon-library" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"><defs><symbol id="arrow" viewBox="0 0 24 24"><path d="M5 12h14m-5-5 5 5-5 5"/></symbol></defs></svg>
{cabecalho()}
<main id="conteudo">
{abertura(p)}
<div class="container pg-coluna pg-texto">
{p['corpo'].strip()}
{faq(p)}
{fontes(p)}
{autor(p)}
{relacionados(p)}
</div>
{chamada(p)}
</main>
{rodape()}
</body>
</html>
'''


def carregar(arquivo):
    spec = importlib.util.spec_from_file_location(arquivo.stem, arquivo)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo.PAGINA


def main():
    filtros = sys.argv[1:]
    for arquivo in sorted((AQUI / 'paginas').glob('*.py')):
        if filtros and not any(arquivo.name.startswith(f) for f in filtros):
            continue
        p = carregar(arquivo)
        destino = SITE / p['url'].strip('/') / 'index.html'
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(pagina(p))
        print(p['url'], len(texto_puro(p['corpo']).split()), 'palavras')


if __name__ == '__main__':
    main()
