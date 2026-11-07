(() => {
  const FMT = "reels", G = "a"; // VARIANTE: build.sh troca esta linha
  const FEED = FMT === "feed";
  const ESC = '[data-composition-id="s1-mundo"] ';
  const $ = (s) => document.querySelector(ESC + s);
  const $$ = (s) => [...document.querySelectorAll(ESC + s)];
  const P = 1800, CY = FEED ? 690 : 960, K = FEED ? 0.8 : 1;
  $("#stage").style.perspectiveOrigin = `540px ${CY}px`;
  $("#cam-z").style.top = `${CY}px`;

  // ── Mural: uma tela ao lado da outra, um painel só ─────────────────────────
  const S = { campanha: [0, 0, 900], cupom: [1800, 0, 900], site: [3600, 0, 900], boasvindas: [3600, 1240, 900], vendas: [1660, 1240, 1600] };
  for (const [n, [x, y, h]] of Object.entries(S)) Object.assign($(`#sh-${n}`).style, { left: `${x}px`, top: `${y}px`, height: `${h}px` });
  const PH = { campanha: [1011.8, 32, 367.7, 763, 24, 50, 320], cupom: [479, 133, 358, 743, -223, -64, 0], boasvindas: [479, 133, 358, 743, -223, -64, 0], site: [487, 108, 342, 709, 0, 0, 342] };
  for (const [n, [x, y, w, h, ox, oy, cw]] of Object.entries(PH)) {
    const e = $(`#ph-${n}`), s = S[n];
    Object.assign(e.style, { left: `${s[0] + x}px`, top: `${s[1] + y}px`, width: `${w}px`, height: `${h}px` });
    Object.assign(e.querySelector(".ph-in").style, { left: `${ox}px`, top: `${oy}px`, width: `${cw}px` });
  }
  const byText = (root, re) => { const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT); while (w.nextNode()) if (re.test(w.currentNode.textContent)) return w.currentNode.parentElement; return null; };
  const fr = byText($("#ph-site"), /Frete grátis/); if (fr) { let e = fr; for (let i = 0; i < 6 && e; i++, e = e.parentElement) if (e.style && e.style.backgroundColor && e.style.backgroundColor !== "rgba(0, 0, 0, 0)") { e.style.visibility = "hidden"; break; } fr.style.visibility = "hidden"; }
  const pos = (el, stop) => { let x = 0, y = 0, e = el; while (e && e !== stop) { x += e.offsetLeft; y += e.offsetTop; e = e.offsetParent; } return { x, y, w: el.offsetWidth, h: el.offsetHeight }; };
  const cen = (sheet, el) => { const p = pos(el, $(`#sh-${sheet}`)); return [S[sheet][0] + p.x + p.w / 2, S[sheet][1] + p.y + p.h / 2]; };
  const W = (n, x, y) => [S[n][0] + x, S[n][1] + y];

  // ── Card da prova: nasce do card real "Composição dos pedidos" ─────────────
  const cardEl = (() => { const t = byText($("#sh-vendas"), /Composição dos pedidos/); let e = t; while (e && e.offsetHeight < 200) e = e.parentElement; return e; })();
  const cr = pos(cardEl, $("#sh-vendas"));
  const card = $("#card");
  Object.assign(card.style, { left: `${S.vendas[0] + cr.x}px`, top: `${S.vendas[1] + cr.y}px`, width: `${cr.w}px`, height: `${cr.h}px` });
  const cl = cardEl.cloneNode(true); Object.assign(cl.style, { position: "absolute", left: 0, top: 0, margin: 0 }); card.appendChild(cl);
  const svg = cl.querySelector("svg.recharts-surface") || [...cl.querySelectorAll("svg")].sort((a, b) => b.clientWidth - a.clientWidth)[0];
  const dr = pos(svg.parentElement, cl);
  const DS = Math.min(dr.w, dr.h), DX = dr.x + dr.w / 2, DY = dr.y + dr.h / 2;
  svg.style.visibility = "hidden";
  [...cl.querySelectorAll('[data-k="num"]')].forEach((n) => { const q = pos(n, cl); if (Math.abs(q.x - dr.x) < dr.w && q.y < dr.y + dr.h && q.y > dr.y) n.style.visibility = "hidden"; });
  const ns = "http://www.w3.org/2000/svg", R = 86, C = 2 * Math.PI * R;
  const dsvg = document.createElementNS(ns, "svg"); dsvg.setAttribute("viewBox", "0 0 200 200");
  Object.assign(dsvg.style, { position: "absolute", left: `${DX - DS / 2}px`, top: `${DY - DS / 2}px`, width: `${DS}px`, height: `${DS}px` });
  dsvg.innerHTML = `<circle cx="100" cy="100" r="${R}" fill="none" stroke="#dbe5f5" stroke-width="20"/><circle class="d-arc" cx="100" cy="100" r="${R}" fill="none" stroke="#155dfc" stroke-width="20" transform="rotate(-90 100 100)" stroke-dasharray="${C}" stroke-dashoffset="${C}"/><text x="100" y="94" text-anchor="middle" font-family="Plus Jakarta Sans" font-size="36" font-weight="600" letter-spacing="-1.5" fill="#10213b">1 em 3</text><text x="100" y="120" text-anchor="middle" font-family="Plus Jakarta Sans" font-size="15" fill="#42556c">recompras</text>`;
  { const w = document.createTreeWalker(cl, NodeFilter.SHOW_TEXT); const l = []; while (w.nextNode()) l.push(w.currentNode);
    l.forEach((t) => { const x = t.textContent; if (/Cliente|Novos clientes|Mede/.test(x)) t.parentElement.style.display = "none"; if (/^\s*[()]\s*$/.test(x) || /^\s*Beta\s*$/.test(x) || /^\s*recompras\s*$/.test(x)) { t.parentElement.style.visibility = "hidden"; } }); }
  cl.appendChild(dsvg);
  const fcp = $("#fc-panel"); Object.assign(fcp.style, { width: `${cr.w}px`, height: `${cr.h}px` }); fcp.appendChild(cl.cloneNode(true));
  fcp.querySelector(".d-arc").setAttribute("stroke-dashoffset", `${C * (2 / 3)}`);

  // ── Conteúdo das telas: estados iniciais ──────────────────────────────────
  const [vT, vM] = $$("#sh-campanha [data-valor]");
  const splitChars = (el) => { const t = el.textContent; el.innerHTML = [...t].map((c) => `<span class="chr">${c === " " ? "&nbsp;" : c}</span>`).join(""); return [...el.children]; };
  const cT = splitChars(vT), cM = splitChars(vM);
  const caret = document.createElement("span"); caret.className = "caret"; vT.appendChild(caret);
  const fimTxt = caret.offsetLeft; const caretX = (i) => (i < cT.length ? cT[i].offsetLeft : fimTxt) - fimTxt;
  gsap.set(caret, { x: caretX(0) });
  const contador = (re, max) => { const e = byText($("#sh-campanha"), re); if (!e) return null; e.textContent = ""; const sp = []; for (let i = 0; i <= max; i++) { const s = document.createElement("span"); s.textContent = `${i} caracteres`; s.style.display = i ? "none" : "inline"; e.appendChild(s); sp.push(s); } return sp; };
  const ctT = contador(/^21 caracteres$/, cT.length), ctM = contador(/^42 caracteres$/, cM.length);
  const pag = $('#sh-campanha [data-k="pagina"]'), am = $('#sh-campanha [data-k="amanha"]'), agora = $('#sh-campanha [data-k="agora"]');
  const amCs = { bg: am.style.backgroundColor, cor: am.style.color };
  am.style.backgroundColor = "#ffffff"; am.style.color = "#10213b";
  // celular: 9:41 → 9:46 (o último dígito rola)
  const relogio = byText($("#ph-boasvindas"), /^9:46$/);
  if (relogio) { relogio.innerHTML = `9:4<span class="roll"><span>1</span><span>6</span></span>`; }
  const rolo = relogio && relogio.querySelector(".roll > span");
  // notificações reais dentro dos celulares
  const sobe = (e, min) => { while (e && e.parentElement && e.parentElement.offsetHeight < min) e = e.parentElement; return e; };
  const nCamp = sobe(byText($("#ph-campanha"), /Chegou a coleção/), 70);
  const nBoas = sobe(byText($("#ph-boasvindas"), /Bem-vindo à nossa/), 70);
  const banCup = sobe(byText($("#ph-cupom"), /Use o cupom/), 30);
  const copiar = byText($("#ph-cupom"), /^COPIAR$/);
  const bSite = $("#b-site");

  // A interface do painel é produto real, em perspectiva: fora das regras de texto de cena
  $$(".sheet, .sheet *, .ph *, #card *, #fc-panel *").forEach((e) => e.setAttribute("data-layout-ignore", ""));

  // ── Timeline e ajudantes ──────────────────────────────────────────────────
  const tl = gsap.timeline({ paused: true });
  const FX = (t, alvo, de, para) => tl.fromTo(alvo, de, { ...para, immediateRender: false }, t);
  const fade = (t, alvo, para, d = 0.2, ease = "power2.out") => tl.to(alvo, { autoAlpha: para, duration: d, ease }, t);

  // Câmera: fromTo explícito (seek em qualquer ordem) · pose = [x, y, s, rx, ry, rz]
  let C0 = null;
  const zOf = (s) => P - P / s;
  const camSet = (p) => { gsap.set("#cam-p", { x: -p[0], y: -p[1] }); gsap.set("#cam-r", { rotationX: p[3], rotationY: p[4], rotationZ: p[5] }); gsap.set("#cam-z", { z: zOf(p[2]) }); C0 = p; };
  const camTo = (t, d, p, ease = "power3.inOut") => {
    const a = C0;
    tl.fromTo("#cam-p", { x: -a[0], y: -a[1] }, { x: -p[0], y: -p[1], duration: d, ease, immediateRender: false }, t);
    tl.fromTo("#cam-r", { rotationX: a[3], rotationY: a[4], rotationZ: a[5] }, { rotationX: p[3], rotationY: p[4], rotationZ: p[5], duration: d, ease, immediateRender: false }, t);
    tl.fromTo("#cam-z", { z: zOf(a[2]) }, { z: zOf(p[2]), duration: d, ease, immediateRender: false }, t);
    C0 = p;
  };
  const pose = (xy, s, rx = 0, ry = 0, rz = 0) => [xy[0], xy[1], s * K, rx, ry, rz];
  // deriva: pose alvo levemente deslocada, nunca parado
  const drift = (t, ate, d = {}) => camTo(t, ate - t, [C0[0] + (d.x || 0), C0[1] + (d.y || 0), C0[2] * (d.s || 1.02), C0[3] + (d.rx || 0), C0[4] + (d.ry || 0), C0[5] + (d.rz || 0)], "sine.inOut");
  const voo = (t, d, alvo, ate, dr) => { camTo(t, d, alvo); if (ate) drift(t + d, ate, dr); };

  // Cursor
  let CUR = null;
  const curVai = (t, d, xy, z = 30) => { const a = CUR || [xy[0] + 160, xy[1] + 120]; FX(t, "#cursor", { x: a[0], y: a[1], z }, { x: xy[0], y: xy[1], z, duration: d, ease: "power3.inOut" }); CUR = xy; };
  const clique = (t, xy, z = 28) => {
    tl.fromTo("#cursor", { scale: 1 }, { scale: 0.82, duration: 0.07, ease: "power2.in", yoyo: true, repeat: 1, immediateRender: false }, t);
    tl.set("#ripple", { x: xy[0], y: xy[1], z, autoAlpha: 1, scale: 0.4 }, t);
    tl.to("#ripple", { scale: 1.9, autoAlpha: 0, duration: 0.42, ease: "power2.out" }, t);
  };
  const mkIn = (t, sel, st = 0.07, d = 0.55) => FX(t, `${sel} .in`, { yPercent: 112 }, { yPercent: 0, duration: d, ease: "expo.out", stagger: st });
  const mkOut = (t, sel, d = 0.22) => tl.to(`${sel} .in`, { yPercent: -112, duration: d, ease: "power3.in", stagger: 0.02 }, t);

  // ── Estado inicial (frame 0) ──────────────────────────────────────────────
  const SOLTOS = ["#pl-app", "#pl-site", "#scrim", "#scrim2", "#n-push", "#n-boas", "#selo", "#ic-app", "#pl-time", "#t-cupom", "#ripple", "#cursor", "#card", "#fc", "#pv", "#t1", "#t2", "#t3", "#t4", "#lines", "#hk-b"];
  gsap.set(SOLTOS, { autoAlpha: 0 });
  gsap.set(["#t1 .in", "#t2 .in", "#t3 .in", "#t4 .in", "#pv .in", "#fc-t .in"], { yPercent: 112 });
  gsap.set(["#t1 .eb", "#t2 .eb", "#t3 .eb", "#t4 .eb"], { autoAlpha: 0 });
  gsap.set("#fc-btn", { xPercent: -50, autoAlpha: 0, y: 30 });
  gsap.set("#fc .bg", { autoAlpha: 0 });
  gsap.set(nBoas, { autoAlpha: 0, y: 40 }); gsap.set(nCamp, { autoAlpha: 0 });
  gsap.set(banCup, { autoAlpha: 0, scaleY: 0, transformOrigin: "50% 0" });
  gsap.set(bSite, { autoAlpha: 0, scaleY: 0, transformOrigin: "50% 0" });
  gsap.set(caret, { autoAlpha: 0 });
  gsap.set("#sh-site", { autoAlpha: 0 });
  ["cupom", "site", "boasvindas"].forEach((n) => gsap.set(`#ph-${n}`, { autoAlpha: 0 }));
  // pilha: quatro telas como camadas sobre o azul
  const ORD = ["vendas", "boasvindas", "cupom", "campanha"];
  const Z0 = 230;
  ORD.forEach((n, i) => gsap.set(`#sh-${n}`, { x: -S[n][0], y: -S[n][1], z: (i - 1.5) * Z0 }));
  gsap.set("#ph-campanha", { z: 1.5 * Z0 + 90 });
  camSet(pose([800, FEED ? 200 : -110], 0.62, 56, 0, -30));

  // ── 0–3,3 · Gancho: a pilha abre, colapsa em "num painel só", a câmera mergulha ─
  ORD.forEach((n, i) => tl.fromTo(`#sh-${n}`, { z: (i - 1.5) * Z0 }, { z: (i - 1.5) * (Z0 + 34), duration: 1.85, ease: "sine.inOut", immediateRender: false }, 0));
  tl.fromTo("#ph-campanha", { z: 1.5 * Z0 + 90 }, { z: 1.5 * (Z0 + 34) + 110, duration: 1.85, ease: "sine.inOut", immediateRender: false }, 0);
  camTo(0, 1.85, pose([815, FEED ? 215 : -85], 0.65, 54, 0, -27), "sine.inOut");
  ORD.forEach((n, i) => tl.to(`#sh-${n}`, { z: i * 1.2, duration: 0.5, ease: "back.in(1.1)" }, 1.87));
  tl.to("#ph-campanha", { z: 60, duration: 0.5, ease: "back.in(1.1)" }, 1.87);
  camTo(1.87, 0.82, pose([820, FEED ? 300 : 90], 0.76, 42, 0, -20), "power2.inOut");
  // mergulho: 2,72–3,4
  fade(2.74, "#hk-a", 0, 0.24, "power2.in");
  tl.to("#hk-a", { y: -60, duration: 0.3, ease: "power2.in" }, 2.72);
  tl.to("#ph-campanha", { z: 0, duration: 0.5, ease: "power2.inOut" }, 2.72);
  fade(2.86, "#bg-impact", 0, 0.34, "power1.inOut");
  fade(2.9, "#lines", 1, 0.4);
  ORD.filter((n) => n !== "campanha").forEach((n, i) => tl.to(`#sh-${n}`, { x: 0, y: 0, z: 0, duration: 0.62, ease: "power3.inOut" }, 2.72 + i * 0.02));
  tl.set("#sh-site", { autoAlpha: 1 }, 3.0); tl.to("#sh-campanha", { z: 0, duration: 0.1 }, 3.3);
  ["cupom", "site", "boasvindas"].forEach((n) => tl.set(`#ph-${n}`, { autoAlpha: 1 }, 3.0));
  camTo(2.72, 0.66, pose(W("campanha", 560, 170), 2.2, 14, -14, 2));
  fade(3.12, "#scrim", 1, 0.3);

  // ── 3,3–6,45 · Campanha ───────────────────────────────────────────────────
  fade(3.3, "#t1 .eb", 1, 0.3); tl.set("#t1", { autoAlpha: 1 }, 3.28); mkIn(3.3, "#t1");
  // digitação
  const inp = vT.parentElement;
  tl.fromTo(inp, { boxShadow: "0 0 0 0 rgba(21,93,252,0)" }, { boxShadow: "0 0 0 2px #155dfc", duration: 0.14, immediateRender: false }, 3.32);
  tl.set(caret, { autoAlpha: 1 }, 3.34);
  const T0 = 3.38, DT = 0.03;
  cT.forEach((c, i) => { tl.set(c, { opacity: 1 }, T0 + i * DT); tl.set(caret, { x: caretX(i + 1) }, T0 + i * DT); if (ctT) { tl.set(ctT[i], { display: "none" }, T0 + i * DT); tl.set(ctT[i + 1], { display: "inline" }, T0 + i * DT); } });
  const TM = T0 + cT.length * DT + 0.03, DM = 0.0085;
  tl.set(caret, { autoAlpha: 0 }, TM);
  cM.forEach((c, i) => { tl.set(c, { opacity: 1 }, TM + i * DM); if (ctM) { tl.set(ctM[i], { display: "none" }, TM + i * DM); tl.set(ctM[i + 1], { display: "inline" }, TM + i * DM); } });
  tl.to(inp, { boxShadow: "0 0 0 0 rgba(21,93,252,0)", duration: 0.14 }, TM);
  drift(3.38, 4.38, { x: 40, y: 34, s: 1.04, ry: 2 });
  // destino
  const cPag = cen("campanha", pag), cAm = cen("campanha", am);
  voo(4.36, 0.38, pose(W("campanha", 590, 440), 2.1, 14, 12, -2), 5.0, { x: -18, y: 10, s: 1.02, ry: -1.5 });
  fade(4.4, "#cursor", 1, 0.16);
  curVai(4.4, 0.36, cPag);
  clique(4.8, cPag);
  // agende
  voo(5.0, 0.3, pose(W("campanha", 600, 590), 2.1, 18, -10, 2), 5.56, { x: 16, s: 1.02 });
  curVai(5.02, 0.32, cAm);
  clique(5.38, cAm);
  tl.fromTo(am, { backgroundColor: "#ffffff", color: "#10213b" }, { backgroundColor: amCs.bg, color: amCs.cor, duration: 0.1, immediateRender: false }, 5.4);
  // o push se solta
  fade(5.52, "#cursor", 0, 0.12);
  voo(5.54, 0.42, pose(W("campanha", 1190, 345), 0.98, 6, -20, 0), 6.42, { x: 14, s: 1.035, ry: 2.5 });
  FX(5.6, "#ph-campanha", { z: 0 }, { z: 160, duration: 0.42, ease: "power3.out" });
  tl.to("#sh-campanha", { filter: "blur(3px)", duration: 0.3 }, 5.62);
  const PUSH = { x: S.campanha[0] + 905, y: 470 };
  tl.set("#n-push", { autoAlpha: 1 }, 5.74);
  FX(5.74, "#n-push", { x: PUSH.x, y: PUSH.y + 260, z: 180, scale: 0.55, rotationY: 8, rotationX: -4, opacity: 0 }, { x: PUSH.x, y: PUSH.y, z: 300, scale: 1, rotationY: 20, rotationX: -5, opacity: 1, duration: 0.36, ease: "back.out(1.5)" });
  tl.set("#selo", { autoAlpha: 1 }, 5.96);
  FX(5.96, "#selo", { x: PUSH.x + 300, y: PUSH.y + 214, z: 380, scale: 0.6, rotationY: 20, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.3, ease: "back.out(1.8)" });

  // ── 6,42–8,2 · Cupom no app ──────────────────────────────────────────────
  mkOut(6.42, "#t1"); fade(6.42, "#t1 .eb", 0, 0.18); tl.set("#t1", { autoAlpha: 0 }, 6.7);
  fade(6.56, "#n-push", 0, 0.18); fade(6.56, "#selo", 0, 0.18);
  tl.to("#sh-campanha", { filter: "blur(0px)", duration: 0.2 }, 6.5);
  voo(6.42, 0.46, pose(W("cupom", 640, 450), 1.06, 8, -22, 2), 8.16, { x: 16, y: -14, s: 1.05, ry: 3, rz: -1 });
  FX(6.62, "#ph-campanha", { z: 160 }, { z: 0, duration: 0.2, ease: "power2.in" });
  tl.set("#t2", { autoAlpha: 1 }, 6.58); fade(6.6, "#t2 .eb", 1, 0.25); mkIn(6.62, "#t2");
  FX(6.6, "#ph-cupom", { z: 0 }, { z: 180, duration: 0.5, ease: "power3.out" });
  tl.to(banCup, { autoAlpha: 1, scaleY: 1, duration: 0.36, ease: "expo.out" }, 6.98);
  // COPIAR e o cupom se solta
  const cpXY = [S.cupom[0] + 479 + 318, 133 + 122];
  tl.set("#ripple", { autoAlpha: 0 }, 7.3);
  tl.to(copiar, { scale: 0.88, duration: 0.07, yoyo: true, repeat: 1, ease: "power2.inOut" }, 7.34);
  clique(7.34, cpXY, 190);
  tl.set("#t-cupom", { autoAlpha: 1 }, 7.42);
  FX(7.42, "#t-cupom", { x: cpXY[0] - 150, y: cpXY[1], z: 190, scale: 0.4, rotationY: 22, rotationZ: -4, opacity: 0 }, { x: S.cupom[0] + 640, y: 610, z: 340, scale: 1, opacity: 1, duration: 0.5, ease: "back.out(1.4)" });
  tl.to("#t-cupom", { y: 590, rotationZ: -2, duration: 0.3, ease: "sine.inOut" }, 7.92);

  // ── 8,2–10,1 · Banner no site ─────────────────────────────────────────────
  fade(8.18, "#t-cupom", 0, 0.16);
  voo(8.18, 0.44, pose(W("site", 660, 420), 1.08, 6, 20, -2), 9.92, { x: -16, s: 1.05, ry: -3, rz: 1 });
  FX(8.34, "#ph-cupom", { z: 180 }, { z: 0, duration: 0.2, ease: "power2.in" });
  FX(8.36, "#ph-site", { z: 0 }, { z: 180, duration: 0.46, ease: "power3.out" });
  tl.to(bSite, { autoAlpha: 1, scaleY: 1, duration: 0.42, ease: "expo.out" }, 8.72);
  const bxXY = [S.site[0] + 487 + 292, 108 + 112];
  CUR = [bxXY[0] + 180, bxXY[1] + 260];
  fade(9.0, "#cursor", 1, 0.14);
  curVai(9.0, 0.44, bxXY, 214);
  clique(9.5, bxXY, 212);
  tl.to("#b-site u", { scale: 0.9, duration: 0.07, yoyo: true, repeat: 1 }, 9.5);
  fade(9.72, "#cursor", 0, 0.12);

  // ── 9,6–12,7 · O ícone do app viaja e a boas-vindas chega ─────────────────
  const fimIc = [S.boasvindas[0] + 479 + 127, S.boasvindas[1] + 133 + 320];
  tl.set("#ic-app", { autoAlpha: 1 }, 9.62);
  FX(9.62, "#ic-app", { x: bxXY[0] - 52, y: bxXY[1] - 52, z: 210, scale: 0.3, rotationZ: 0 }, { scale: 1, y: bxXY[1] + 60, z: 330, duration: 0.3, ease: "back.out(1.6)" });
  tl.to("#ic-app", { x: fimIc[0], y: fimIc[1], z: 240, rotationZ: -6, duration: 0.68, ease: "power3.inOut" }, 9.92);
  mkOut(10.1, "#t2"); fade(10.1, "#t2 .eb", 0, 0.18); tl.set("#t2", { autoAlpha: 0 }, 10.4);
  voo(9.92, 0.68, pose(W("boasvindas", 650, 445), 1.06, 6, -18, 0), 12.62, { x: 18, y: -10, s: 1.06, ry: 3 });
  FX(10.14, "#ph-site", { z: 180 }, { z: 0, duration: 0.2, ease: "power2.in" });
  FX(10.1, "#ph-boasvindas", { z: 0 }, { z: 160, duration: 0.5, ease: "power3.out" });
  tl.to("#ic-app", { scale: 0, autoAlpha: 0, duration: 0.16, ease: "power2.in" }, 10.56);
  tl.set("#t3", { autoAlpha: 1 }, 10.26); fade(10.28, "#t3 .eb", 1, 0.25); mkIn(10.3, "#t3");
  // Instalou → chega
  const seta = $("#seta"); const LS = seta.getTotalLength();
  gsap.set(seta, { strokeDasharray: LS, strokeDashoffset: LS });
  const pt = [S.boasvindas[0] + 479 - 90, S.boasvindas[1] + 133 + 330];
  tl.set("#pl-time", { autoAlpha: 1 }, 10.72);
  FX(10.72, "#pl-time", { x: pt[0], y: pt[1] + 30, z: 300, rotationY: 18, scale: 0.8, opacity: 0 }, { y: pt[1], scale: 1, opacity: 1, duration: 0.36, ease: "back.out(1.6)" });
  tl.to(seta, { strokeDashoffset: 0, duration: 0.6, ease: "power2.inOut" }, 11.06);
  if (rolo) { const a = relogio.querySelector(".roll"); tl.to(a.children, { yPercent: -100, duration: 0.32, ease: "power3.inOut" }, 11.5); }
  tl.to(nBoas, { autoAlpha: 1, y: 0, duration: 0.3, ease: "power2.out" }, 11.72);
  const NB = { x: S.boasvindas[0] + 479 - 104, y: S.boasvindas[1] + 133 + 450 };
  tl.set("#n-boas", { autoAlpha: 1 }, 11.72);
  FX(11.72, "#n-boas", { x: NB.x, y: NB.y + 140, z: 180, scale: 0.6, rotationY: 8, rotationX: -4, opacity: 0 }, { x: NB.x, y: NB.y, z: 300, scale: 1, rotationY: 18, rotationX: -4, opacity: 1, duration: 0.38, ease: "back.out(1.5)" });
  tl.to("#pl-time", { y: pt[1] - 40, duration: 0.3, ease: "power2.out" }, 11.72);
  fade(12.56, "#pl-time", 0, 0.14); fade(12.56, "#n-boas", 0, 0.14);

  // ── 12,6–15,5 · Analytics ─────────────────────────────────────────────────
  mkOut(12.6, "#t3"); fade(12.6, "#t3 .eb", 0, 0.18); tl.set("#t3", { autoAlpha: 0 }, 12.88);
  voo(12.56, 0.54, pose(W("vendas", 780, 620), 0.7, 34, -12, 10), 14.16, { x: 26, y: 20, s: 1.05, rz: -2.5 });
  FX(12.68, "#ph-boasvindas", { z: 160 }, { z: 0, duration: 0.2, ease: "power2.in" });
  tl.set("#t4", { autoAlpha: 1 }, 12.74); fade(12.76, "#t4 .eb", 1, 0.25); mkIn(12.78, "#t4");
  // gráficos desenham
  const vd = $("#sh-vendas");
  const linhas = [...vd.querySelectorAll("svg path")].filter((p) => { const s = p.getAttribute("stroke"), f = p.getAttribute("fill"); return s && s !== "none" && (!f || f === "none") && p.getBBox && p.getBBox().width > 100; });
  linhas.forEach((p, i) => { const L = p.getTotalLength(); gsap.set(p, { strokeDasharray: L, strokeDashoffset: L }); tl.to(p, { strokeDashoffset: 0, duration: 0.8, ease: "power2.inOut" }, 12.74 + (i % 4) * 0.07); });
  const barras = [...vd.querySelectorAll("svg path")].filter((p) => { const f = p.getAttribute("fill"); if (!f || f === "none" || p.getAttribute("stroke") === "none" && false) return false; const b = p.getBBox(); return b.width > 3 && b.width < 30 && b.height > 3; });
  gsap.set(barras, { scaleY: 0, transformOrigin: "50% 100%", transformBox: "fill-box" });
  tl.to(barras, { scaleY: 1, duration: 0.36, ease: "power3.out", stagger: { each: 0.008 } }, 12.8);
  // mergulho no App × Site
  voo(14.14, 0.44, pose(W("vendas", 1130, 470), 1.72, 12, -14, 0), 15.5, { x: 22, s: 1.03, ry: 2 });
  tl.set("#pl-app", { autoAlpha: 1 }, 14.5);
  FX(14.5, "#pl-app", { x: S.vendas[0] + 1090, y: S.vendas[1] + 400, z: 60, scale: 0.4, opacity: 0 }, { y: S.vendas[1] + 380, scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2)" });
  tl.set("#pl-site", { autoAlpha: 1 }, 14.72);
  FX(14.72, "#pl-site", { x: S.vendas[0] + 1210, y: S.vendas[1] + 510, z: 60, scale: 0.4, opacity: 0 }, { y: S.vendas[1] + 490, scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2)" });

  // ── 15,5–19,7 · A prova sai do plano ──────────────────────────────────────
  mkOut(15.48, "#t4"); fade(15.48, "#t4 .eb", 0, 0.18); tl.set("#t4", { autoAlpha: 0 }, 15.76);
  fade(15.5, "#pl-app", 0, 0.16); fade(15.5, "#pl-site", 0, 0.16);
  const cCard = [S.vendas[0] + cr.x + cr.w * 0.5, S.vendas[1] + cr.y + cr.h * 0.34];
  voo(15.5, 0.56, pose(cCard, 1.42, 8, -8, 0), 19.62, { x: 8, y: -16, s: 1.05, rx: -2.5, ry: 3 });
  tl.set("#card", { autoAlpha: 1, z: 0 }, 15.66);
  tl.to("#card", { z: 260, duration: 0.56, ease: "power3.out" }, 15.68);
  tl.to("#sh-vendas", { filter: "blur(5px)", duration: 0.45 }, 15.66);
  fade(15.6, "#scrim2", 1, 0.3);
  tl.set("#pv", { autoAlpha: 1 }, 15.7);
  mkIn(15.74, "#pv .n", 0, 0.6);
  $$("#card .d-arc").forEach((a) => tl.to(a, { attr: { "stroke-dashoffset": C * (2 / 3) }, duration: 0.62, ease: "power3.inOut" }, 16.25));
  tl.fromTo("#pv .n .in", { scale: 1 }, { scale: 1.035, transformOrigin: "0 50%", duration: 0.14, ease: "power2.out", yoyo: true, repeat: 1, immediateRender: false }, 16.57);
  mkIn(16.86, "#pv .r", 0.72, 0.5);
  // "quem já tinha comprado": a linha Recompra no App acende
  { let lin = byText(card, /Recompra no App/); while (lin && lin.offsetWidth < 150) lin = lin.parentElement;
    if (lin) { lin.style.borderRadius = "10px"; tl.fromTo(lin, { backgroundColor: "rgba(21,93,252,0)", boxShadow: "0 0 0 10px rgba(21,93,252,0)" }, { backgroundColor: "rgba(21,93,252,0.1)", boxShadow: "0 0 0 10px rgba(21,93,252,0.1)", duration: 0.4, ease: "power2.out", immediateRender: false }, 18.25); } }

  // ── 19,62–24,6 · O arco vira o fechamento ─────────────────────────────────
  const irisXY = FEED ? [277, 784] : [191, 1086];
  gsap.set("#iris", { x: irisXY[0], y: irisXY[1], scale: 0 });
  gsap.set(fcp, { x: FEED ? 136 : 127, y: FEED ? 41 : 105, scale: FEED ? 1.55 : 1.855, rotationX: 7, rotationY: -7, autoAlpha: 0 });
  mkOut(19.56, "#pv .n", 0.2); mkOut(19.56, "#pv .r", 0.2); tl.set("#pv", { autoAlpha: 0 }, 19.8);
  tl.set("#fc", { autoAlpha: 1 }, 19.62); tl.set(fcp, { autoAlpha: 1 }, 19.62); tl.set("#card", { autoAlpha: 0 }, 19.62);
  tl.to("#iris", { scale: 26, duration: 0.5, ease: "power3.in" }, 19.62);
  tl.set("#fc .bg", { autoAlpha: 1 }, 20.12);
  tl.set(["#stage", "#scrim", "#scrim2", "#bg-ice"], { autoAlpha: 0 }, 20.14);
  tl.to(fcp, FEED ? { x: 0, y: 10, scale: 1.05, rotationX: 26, rotationY: -14, rotationZ: -7, duration: 0.8, ease: "power3.inOut" } : { x: 0, y: -10, scale: 1.2, rotationX: 26, rotationY: -14, rotationZ: -7, duration: 0.8, ease: "power3.inOut" }, 19.86);
  tl.to(fcp, { rotationY: -9, rotationZ: -5, y: FEED ? 0 : -24, duration: 3.9, ease: "sine.inOut" }, 20.68);
  const fcIn = $$("#fc-t .in");
  [19.97, 20.5, 21.48, 22.3].forEach((t, i) => FX(t, fcIn[i], { yPercent: 112 }, { yPercent: 0, duration: 0.6, ease: "expo.out" }));
  tl.to("#fc-btn", { autoAlpha: 1, y: 0, duration: 0.42, ease: "back.out(1.6)" }, 23.18);
  tl.set({}, {}, 24.6);
  // ── v2 · retime do gancho novo ("Isso é o que você ganha…", 1,0s mais longo que o do v1) ────────────────
  // A animação da abertura é a do v1: a pilha abre por 2,85s em vez de 1,85s; o colapso, o mergulho e todo o resto andam D.
  // Os tempos acima continuam os do v1 (comentários das seções inclusive). v1: D = 0.
  const D = 1.0, ABRE = 1.85;
  if (D) tl.getChildren(false, true, true).forEach((c) => {
    const t = c.startTime();
    if (t >= ABRE - 0.01) c.startTime(t + D);
    else if (t === 0 && Math.abs(c.duration() - ABRE) < 0.01) c.duration(ABRE + D);
    else throw new Error(`retime v2: animação inesperada em ${t}s`);
  });
  window.__timelines["s1-mundo"] = tl;
})();
