Aqui está o briefing condensado pra colar no Claude Code:

---

# IA na Prática — Aulão Final: Landing Pages

## Objetivo
Última aula da série (RV 2026, público: nutricionistas, mulheres 25–34, pouca/nenhuma experiência técnica). Duração: ~120 min. Construir a aula + um painel de modelos de LP (hub estilo s-lab.richardvieira.com.br) + um skill de design de LP.

## Decisões travadas

**Dois cenários de construção:**
- **EASY** — Lovable (a fundo) + v0/Bolt (60s cada, menção). Deploy próprio da ferramenta.
- **FULL** — Codex (app, não CLI) gera código → AgentSkill de copy de LP → publica no Netlify → domínio próprio vinculado.

**Hospedagem: Netlify** (free serve, domínio custom + HTTPS sem cartão). Caveat honesto a mencionar na aula: modelo de créditos 2026 pausa o site free ao bater o teto — improvável em LP estática, mas citar.

**Domínio próprio = obrigatório** (autoridade; `joana.com.br` > `joana.lovable.app`). Mas: NUNCA conectar DNS ao vivo (propagação até 48h). Ensinar o processo ao vivo, mostrar resultado já propagado preparado antes.

**3 LPs do nutri** (são a escada de dificuldade, por complexidade de copy, não de ferramenta):
1. Link da bio (simples)
2. LP de WhatsApp (`wa.me` com msg pré-preenchida)
3. Página de vendas de infoproduto (estrutura longa)

## Painel de modelos (o ativo central)
Hub que entrega LPs prontas. Cada card em 2 camadas: **"Baixar HTML pronto"** (piso seguro, sobe no Netlify sem IA) + **"Copiar prompt"** (teto de personalização via Codex/Lovable). Lançar com 3 modelos impecáveis, não 15. Justifica a comunidade recorrente (modelos novos toda semana).

## Sistema de design — decisões
- **Camáleão**: zero cor/fonte hardcoded. Tudo token (`--brand`, `--grad`, `--font`). Aluno troca ~5 variáveis → LP na marca dele. Conecta com Agent 1 (Identidade Visual).
- **3 peles como preset** de cada modelo (validadas visualmente — ver `tres-direcoes.html`):
  - **A · Clean/Médico** — verde-azulado, sans neutra, sereno. Seguro, mas mais perto do genérico.
  - **B · Editorial/Premium** — serif display (DM Serif Display), terracota. Mais caro/diferenciado. Pra ticket alto.
  - **C · Caloroso/Lifestyle** — laranja, squircle, gradiente no texto, tom humano. Mais converte pro perfil médio; mais Instagram-native.

## O "foda" visual não vem de IA — vem de regras
IA gera template genérico ("padrão ChatGPT" visual: hero centralizado, Inter 400, gradiente roxo). Alavancas reais, em ordem de impacto: (1) tipografia com personalidade — par display+texto, peso 600-700, letter-spacing negativo; (2) espaço em branco agressivo (IA enche, mandar esvaziar); (3) um movimento só (1 gradiente, 1 blob, sombra com tint colorido nunca cinza); (4) imagem real ou nenhuma (zero stock); (5) hierarquia brutal (headline clamp 56-100px). O skill codifica isso.

## Próximos artefatos a construir
1. **skill-rv-landing.md** — irmão do skill-rv-design, mas: tokenizado/camáleão, com as 3 peles, regras anti-genérico, estrutura de conversão embutida. Fundação de todos os modelos.
2. **AgentSkill · Copy de LP para Nutris** — estrutura headline→dor→oferta→prova→garantia→CTA. Caveats de saúde (não prometer resultado). Padrão do "Ads para Nutris".
3. **3 modelos de LP** (link bio / WhatsApp / página de vendas) × 3 peles, HTML single-file, responsivos.
4. **Painel/hub** seguindo skill-rv-design (laranja/cream/SF/glass/símbolo R).

