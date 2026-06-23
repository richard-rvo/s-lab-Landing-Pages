#!/usr/bin/env python3
"""
Gera os 3 retratos das personas com o nano-banana (Gemini 2.5 Flash Image)
e salva em cada pasta de identidade. Requer a variável de ambiente GEMINI_API_KEY.

Uso:
    GEMINI_API_KEY=suachave python3 scripts/gerar-retratos.py

Key gratuita em: https://aistudio.google.com/apikey
Sem dependências externas — usa só a stdlib (urllib).
"""
import os, sys, json, base64, urllib.request, urllib.error

API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
if not API_KEY:
    sys.exit("ERRO: defina GEMINI_API_KEY no ambiente. Key grátis: https://aistudio.google.com/apikey")

MODEL = "gemini-2.5-flash-image"  # nano-banana
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RETRATOS = [
    {
        "out": "identidades/01-verde-herbal/retrato-cami.jpg",
        "prompt": ("Warm, approachable portrait of a young Brazilian woman nutritionist, "
                   "genuine relaxed smile, casual-professional look. Green-cream background "
                   "(#F3F1E9), soft natural daylight, botanical lifestyle feel, sage-green "
                   "palette with warm honey accent. Clean editorial style, shallow depth of "
                   "field, vertical 3:4 framing, head-and-shoulders. No text, no watermark, "
                   "no neon, no hard shadows, no blue tint, no oversaturated colors."),
    },
    {
        "out": "identidades/02-terracota/retrato-helena.jpg",
        "prompt": ("Editorial professional portrait of a Brazilian woman nutritionist, about "
                   "35 to 45 years old, serene and trustworthy expression, discreet neutral "
                   "clinical attire. Warm blurred ivory background (#F6F2EC), soft diffused "
                   "warm light, subtle terracotta and sage palette. Clean editorial style, "
                   "shallow depth of field, vertical 3:4 framing, head-and-shoulders. No text, "
                   "no watermark, no neon, no hard shadows, no oversaturated colors."),
    },
    {
        "out": "identidades/03-azul-clinico/retrato-marina.jpg",
        "prompt": ("Confident professional portrait of a Brazilian woman nutritionist, about "
                   "35 to 45 years old, composed and competent expression, modern clinical "
                   "attire. Cool light-gray background (#F1F4F5), clean diffused light, "
                   "teal-petrol palette with subtle warm amber accent. Sharp modern editorial "
                   "style, vertical 3:4 framing, head-and-shoulders. No text, no watermark, "
                   "no neon, no hard shadows, no oversaturated colors."),
    },
]

def gerar(prompt):
    body = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode()
    req = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.load(resp)
    for part in data["candidates"][0]["content"]["parts"]:
        inline = part.get("inlineData") or part.get("inline_data")
        if inline and inline.get("data"):
            return base64.b64decode(inline["data"])
    raise RuntimeError("resposta sem imagem: " + json.dumps(data)[:300])

ok = 0
for r in RETRATOS:
    out = os.path.join(BASE, r["out"])
    try:
        print(f"→ gerando {r['out']} ...", flush=True)
        img = gerar(r["prompt"])
        with open(out, "wb") as f:
            f.write(img)
        print(f"  ✅ salvo ({len(img)//1024} KB)")
        ok += 1
    except urllib.error.HTTPError as e:
        print(f"  ❌ HTTP {e.code}: {e.read().decode()[:300]}")
    except Exception as e:
        print(f"  ❌ {e}")

print(f"\n{ok}/{len(RETRATOS)} retratos gerados.")
