# Cómo hacemos los Shorts de historia (léelo entero antes de empezar)

Ian hace **Shorts verticales de historia** al estilo del canal *Historically*: dibujos cartoon sencillos, fondos
muy trabajados, narrador en off con humor o drama, planos cortos y efectos básicos. Tú (Claude) generas las
**imágenes y las animaciones con la cuenta de SnapGen AI de Ian**; él monta el vídeo final en **CapCut**.
Primer proyecto de referencia: `baibars/` (Baibars, el esclavo que frenó a los mongoles).

## 1. Reglas de trabajo (lo más importante)

1. **Nada se genera sin aprobación.** Orden fijo, parando a pedir el "sí" de Ian en cada paso:
   1. **Guion** (narración por escena) → aprobación.
   2. **Plan de imágenes**: tabla con qué saldrá en cada imagen → aprobación.
   3. **Imágenes**: genera, **revisa tú cada una abriéndola** y entrégala con `SendUserFile`.
   4. **Guion de animaciones**: tabla por escena con **Personajes (qué hacen) · Efectos visuales · Cámara** → aprobación.
   5. **Animaciones**: **una por una**. Genera una, revísala, entrégala, y solo entonces la siguiente.
2. **Prueba con UNA antes de lanzar varias.** Nunca pongas en cola todas las escenas sin haber comprobado que la
   primera sale bien. (Error real cometido: se lanzaron 8 animaciones con el modo equivocado.)
3. **Revisa tú el resultado antes de enseñarlo**: abre la imagen; en los vídeos saca fotogramas (principio,
   medio, final) con ffmpeg. Si no se parece a la imagen o al personaje, dilo claramente: **no lo maquilles**.
4. **Di siempre el coste** antes y después, y el saldo (`python3 tools/snapgen.py credits`).
5. Si Ian dice **"para"**, para todo al momento (mata scripts en segundo plano) e informa de lo que quedó en cola.
6. **No montes el vídeo final** salvo que lo pida: Ian lo hace en CapCut. Entrega cada pieza por separado.
7. **Audio de las animaciones: solo efectos y ambiente. Nunca voces, diálogos, narración ni música.**
8. Formato siempre **vertical 9:16**. Animaciones de **8 s** por escena.
9. No inventes lo que no puedes ver: YouTube está bloqueado en el entorno. Si Ian pasa un vídeo de
   referencia, pídele capturas o una descripción.
10. Commit y push de cada imagen/animación aprobada a la rama de trabajo (carpeta del proyecto).

## 2. Acceso a SnapGen (cómo está conectado)

- No hay conector. Ian guardó una **credencial en la configuración del entorno cloud**: tipo *Bearer* pero con
  cabecera personalizada **`x-api-key`** (sin prefijo), sitio permitido **`api.snapgen.ai`**. El proxy la añade
  sola a cada petición: **no pidas ni escribas nunca la clave** en el chat ni en archivos.
- Comprobar que funciona: `python3 tools/snapgen.py credits`.
- La web y la documentación (`snapgen.ai`, `docs.snapgen.ai`) están bloqueadas; solo se llega a `api.snapgen.ai`.
- Los archivos generados se descargan bien con la `image_url`/`video_url` que da la API
  (los `thumbnail_url` de `r2.dev` están bloqueados).

## 3. API de SnapGen (descubierta probando; base `https://api.snapgen.ai/uapi/v1`)

| Qué | Endpoint | Campos (multipart form) |
|---|---|---|
| Saldo | `GET /account` | → `user_credit.available_credit`, `locked_credit` |
| Historial | `GET /histories?page=1&items_per_page=N` | |
| Estado de un trabajo | `GET /history/{uuid}` | `status`: 0 en cola, 1 procesando, **2 hecho**, **3 fallo** (`error_code`) |
| Borrar/cancelar | `DELETE /history/{id numérico}` | Solo pasados 3 min desde que se creó. Los créditos bloqueados se devolvieron |
| **Imagen** | `POST /generate_image` | `prompt`, `model`, `aspect_ratio`, `resolution`, `files` (referencias) |
| **Vídeo Veo** | `POST /video-gen/veo` | `prompt`, `model`, **`mode_image`**, `aspect_ratio`, `resolution`, `files` |

- Modelos de imagen: `nano-banana-2` (el que usamos, **3 créditos**), `nano-banana-pro`, `nano-banana-2-lite`.
  `aspect_ratio`: 1:1, 3:4, 4:3, 9:16, 16:9. `resolution`: 1K, 2K, 4K. Sale 768×1376 a 1K.
- Modelos Veo: `veo-3.1-fast` (el que usamos, **4 créditos**, 8 s con sonido), `veo-3.1`, `veo-3`, `veo-3-fast`,
  `veo-3.1-lite`, `veo-2`, `omni-flash`… Los `*-free` **no funcionan por API**. `aspect_ratio`: 16:9 o 9:16.
  Entrega 720×1280 a 24 fps aunque se pida 1080p.
- **`mode_image=frame` es OBLIGATORIO para animar una imagen**: la usa como primer fotograma exacto.
  Sin él (o con `ingredient`) Veo solo se "inspira" y se inventa otro plano con otro personaje.
- Grok vídeo también existe (`/video-gen/grok`, modelos `grok-video`/`grok-3`), 8 créditos; no lo usamos.
- Para descubrir parámetros sin gastar: manda el POST con `prompt` vacío o un valor inválido; el error dice los
  valores permitidos y no se genera nada.
- **Saturación**: son frecuentes `GEMINI_RATE_LIMIT` (imágenes) y `TIMEOUT` a los ~21 min en cola (Veo). No se
  cobran. Envía **de una en una** (lanzar varias a la vez empeora los rechazos) y reintenta. Suele ir mejor por la
  mañana en España.

Script: `tools/snapgen.py` (`credits`, `image`, `video`); envía un trabajo, espera, descarga e imprime el coste.

## 4. Estilo visual y personaje

- Personaje de referencia de Ian (proyecto Baibars): `baibars/referencia_personaje.jpg`. Guerrero de la estepa
  cartoon: cara blanca redonda con ojos simples, barba oscura trenzada, casco de acero en punta con penacho negro,
  cota de malla al cuello, caftán rojo y verde, arco, carcaj, escudo redondo, botas marrones.
- Pasa **siempre la referencia en `files`** y describe el personaje en el prompt. Versiones niño/adolescente:
  misma cara y estilo, sin barba ni casco.
- Bloque de estilo que va al final de cada prompt de imagen:
  > Style: 2D cartoon like a history explainer animation, thick black outlines, flat colors with soft shading,
  > highly detailed painted background. No glow outline. No text, no letters, no watermark. Vertical 9:16.
  > Character small in frame, the epic background is the focus.
- A Ian le gustan los **fondos épicos**: montañas, cielos, ejércitos, ciudades. El personaje no tiene que estar
  siempre en el centro: en la escena 4 pidió **dos bandos separados** en vez del héroe en medio ("poco realista").
- **Sin texto dentro de las imágenes** ("ESCLAVO", "SULTÁN"…): se ponen en CapCut.
- Nano Banana deja una **estrellita blanca** de marca de agua en una esquina a veces; se tapa en el montaje.

## 5. Animaciones: cómo pedirlas

Guion por escena en tabla: **Personajes** (movimientos pequeños y concretos: girar la cabeza, gesticular, galopar,
ropa/estandartes ondeando) · **Efectos visuales** (fuego, humo, brasas, polvo, relámpagos, flechas, destellos) ·
**Cámara** (push-in, alejarse, paneo, temblor, fundido). Prompt = bloque base + acción de la escena:

> This image is the exact first frame. Keep everything identical to it: same composition, same 2D hand-drawn
> cartoon art style with thick black outlines and flat colors, same characters with round white cartoon faces and
> simple eyes. Do NOT make anything realistic, do NOT redesign or change any character, do NOT cut to another
> shot. Smooth, fluid 2D cartoon animation with small, natural movements and lively visual effects. No text on
> screen. Audio: sound effects and ambience only, absolutely NO voices, NO dialogue, NO narration, NO singing,
> NO music.
>
> Action: … Effects: … Camera: … Audio: …

Revisión: `ffmpeg -i animN.mp4 -vf "select='eq(n\,0)+eq(n\,64)+eq(n\,128)+eq(n\,190)',scale=230:-1,tile=4x1" -vsync 0 hoja.png`
y abre la hoja. ffmpeg no está instalado: `pip install imageio-ffmpeg` y usa
`python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())"`.

Alternativa gratis (0 créditos) si Ian solo quiere movimiento de cámara sobre la imagen: `baibars/render_clips.py`
(zoom/paneo + partículas con Pillow + ffmpeg, 1080×1920, 30 fps). Ian prefirió después Veo con personajes moviéndose.

## 6. Guion de narración

- 8 escenas × 8 s ≈ 64 s. Frases de **15–18 palabras** por escena (los números se leen largos: "mil doscientos…").
- Gancho fuerte en la escena 1 y cierre que vuelve al gancho. Comprueba los datos históricos y marca las anécdotas
  dudosas; no copies guiones de otros canales.

## 7. Estructura de archivos de un proyecto

```
<proyecto>/escenaN.png          imágenes finales (versiones antiguas: escenaN_v1.png…)
<proyecto>/animaciones/animN.mp4 animaciones Veo aprobadas
<proyecto>/clips/               clips de solo cámara (render_clips.py)
```
Los vídeos pesan más de 30 MB a veces: `SendUserFile` no los envía; comprime con `-crf 24` para mandarlos.
