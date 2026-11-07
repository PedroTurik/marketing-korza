/* M1 v2 — helpers das cenas (carregado no index.html). */
(function () {
  // Espessura do celular: 20 camadas atrás da frente (.ph3-e), criadas uma vez.
  window.m1Edges = function (scope) {
    document.querySelectorAll(scope + " .ph3").forEach(function (ph) {
      if (ph.querySelector(".ph3-e")) return;
      for (var k = 20; k >= 1; k--) {
        var e = document.createElement("div");
        e.className = "ph3-e";
        e.style.transform = "translateZ(-" + (k * 1.9).toFixed(1) + "px)";
        ph.insertBefore(e, ph.firstChild);
      }
    });
  };
  // Título por máscara: as linhas (.mk > .in) começam invisíveis no CSS; a máscara (.mk) recorta a subida.
  window.m1In = function (tl, el, at, d) {
    tl.fromTo(el, { yPercent: 115, autoAlpha: 1 }, { yPercent: 0, autoAlpha: 1, duration: d || 0.55, ease: "power3.out", immediateRender: false }, at);
  };
  window.m1Out = function (tl, el, at) {
    tl.to(el, { yPercent: -115, duration: 0.3, ease: "power2.in" }, at);
    tl.set(el, { autoAlpha: 0 }, at + 0.3);
  };
  // Tranco de câmera (impacto), decai em ~0,5s. Determinístico.
  window.m1Jolt = function (tl, el, at, amp) {
    amp = amp || 1;
    tl.to(el, { keyframes: [
      { y: 16 * amp, rotation: -0.7 * amp, duration: 0.06, ease: "power2.out" },
      { y: -9 * amp, rotation: 0.4 * amp, duration: 0.1, ease: "sine.inOut" },
      { y: 4 * amp, rotation: -0.15 * amp, duration: 0.12, ease: "sine.inOut" },
      { y: 0, rotation: 0, duration: 0.2, ease: "sine.out" },
    ] }, at);
  };
})();
